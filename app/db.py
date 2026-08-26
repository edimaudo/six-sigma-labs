from pathlib import Path
import hashlib
import json
import os
import secrets
import sqlite3

DB_PATH = Path(__file__).resolve().parent.parent / "sixsigma.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _hash_password(password: str, salt: str | None = None) -> str:
    salt = salt or secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 120_000).hex()
    return f"pbkdf2_sha256$120000${salt}${digest}"


def verify_password(password: str, encoded: str) -> bool:
    try:
        _, iterations, salt, digest = encoded.split("$", 3)
        check = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), int(iterations)).hex()
        return secrets.compare_digest(check, digest)
    except (ValueError, TypeError):
        return False


def init_db():
    conn = get_conn()
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            name TEXT DEFAULT '',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS learner_profiles (
            user_id INTEGER PRIMARY KEY,
            business_area TEXT DEFAULT '',
            belt TEXT DEFAULT 'white',
            diagnostic_score INTEGER DEFAULT 0,
            diagnostic_total INTEGER DEFAULT 0,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );
        CREATE TABLE IF NOT EXISTS journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            reflection TEXT NOT NULL,
            scenario_id TEXT DEFAULT '',
            lesson_id TEXT DEFAULT '',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            activity_type TEXT NOT NULL,
            activity_id TEXT DEFAULT '',
            response TEXT NOT NULL,
            feedback TEXT NOT NULL,
            score INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS scenario_sessions (
            id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            scenario_id TEXT NOT NULL,
            phase TEXT DEFAULT 'define',
            visited_stakeholders TEXT DEFAULT '[]',
            discovered_clues TEXT DEFAULT '[]',
            decisions TEXT DEFAULT '[]',
            conversation TEXT DEFAULT '[]',
            reasoning_score INTEGER DEFAULT 0,
            evidence_score INTEGER DEFAULT 0,
            stakeholder_score INTEGER DEFAULT 0,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """
    )
    conn.commit()

    # Provide a single local demo account so the prototype remains usable without signup.
    existing = conn.execute("SELECT id FROM users ORDER BY id LIMIT 1").fetchone()
    if not existing:
        password = os.getenv("SSOL_DEMO_PASSWORD", "demo-only")
        cur = conn.execute(
            "INSERT INTO users (email, password_hash, name) VALUES (?, ?, ?)",
            ("demo@sixsigma.local", _hash_password(password), "Demo Learner"),
        )
        user_id = cur.lastrowid
        conn.execute("INSERT INTO learner_profiles (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()


def create_user(email: str, password: str, name: str = ""):
    conn = get_conn()
    try:
        cur = conn.execute(
            "INSERT INTO users (email, password_hash, name) VALUES (?, ?, ?)",
            (email.strip().lower(), _hash_password(password), name.strip()),
        )
        user_id = cur.lastrowid
        conn.execute("INSERT INTO learner_profiles (user_id) VALUES (?)", (user_id,))
        conn.commit()
        return user_id
    except sqlite3.IntegrityError:
        return None
    finally:
        conn.close()


def authenticate(email: str, password: str):
    conn = get_conn()
    row = conn.execute("SELECT * FROM users WHERE email=?", (email.strip().lower(),)).fetchone()
    conn.close()
    if row and verify_password(password, row["password_hash"]):
        return dict(row)
    return None


def get_user(user_id: int):
    conn = get_conn()
    row = conn.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def learner(user_id: int):
    conn = get_conn()
    row = conn.execute(
        """
        SELECT u.id AS user_id, u.email, u.name, p.business_area, p.belt,
               p.diagnostic_score, p.diagnostic_total, p.updated_at
        FROM users u JOIN learner_profiles p ON p.user_id=u.id
        WHERE u.id=?
        """,
        (user_id,),
    ).fetchone()
    conn.close()
    return dict(row) if row else None


def update_learner(user_id: int, **values):
    allowed = {"business_area", "belt", "diagnostic_score", "diagnostic_total"}
    values = {k: v for k, v in values.items() if k in allowed}
    if not values:
        return
    sets = []
    params = []
    for key, value in values.items():
        sets.append(f"{key} = ?")
        params.append(value)
    sets.append("updated_at = CURRENT_TIMESTAMP")
    conn = get_conn()
    conn.execute(f"UPDATE learner_profiles SET {', '.join(sets)} WHERE user_id=?", params + [user_id])
    conn.commit()
    conn.close()


def add_journal(user_id, reflection, scenario_id="", lesson_id=""):
    conn = get_conn()
    conn.execute(
        "INSERT INTO journal (user_id, reflection, scenario_id, lesson_id) VALUES (?, ?, ?, ?)",
        (user_id, reflection.strip(), scenario_id, lesson_id),
    )
    conn.commit()
    conn.close()


def list_journal(user_id, limit=20):
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM journal WHERE user_id=? ORDER BY id DESC LIMIT ?", (user_id, limit)
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def add_attempt(user_id, activity_type, activity_id, response, feedback, score=0):
    conn = get_conn()
    conn.execute(
        "INSERT INTO attempts (user_id, activity_type, activity_id, response, feedback, score) VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, activity_type, activity_id, response, feedback, score),
    )
    conn.commit()
    conn.close()


def list_attempts(user_id, limit=20):
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM attempts WHERE user_id=? ORDER BY id DESC LIMIT ?", (user_id, limit)
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def create_scenario_session(session_id, user_id, scenario_id):
    conn = get_conn()
    conn.execute(
        "INSERT OR IGNORE INTO scenario_sessions (id, user_id, scenario_id) VALUES (?, ?, ?)",
        (session_id, user_id, scenario_id),
    )
    conn.commit()
    conn.close()


def get_scenario_session(session_id, user_id):
    conn = get_conn()
    row = conn.execute(
        "SELECT * FROM scenario_sessions WHERE id=? AND user_id=?", (session_id, user_id)
    ).fetchone()
    conn.close()
    if not row:
        return None
    data = dict(row)
    for key in ("visited_stakeholders", "discovered_clues", "decisions", "conversation"):
        try:
            data[key] = json.loads(data[key] or "[]")
        except json.JSONDecodeError:
            data[key] = []
    return data


def update_scenario_session(session_id, user_id, **values):
    allowed = {
        "phase", "visited_stakeholders", "discovered_clues", "decisions", "conversation",
        "reasoning_score", "evidence_score", "stakeholder_score"
    }
    sets = []
    params = []
    for key, value in values.items():
        if key not in allowed:
            continue
        if key in {"visited_stakeholders", "discovered_clues", "decisions", "conversation"}:
            value = json.dumps(value)
        sets.append(f"{key}=?")
        params.append(value)
    if not sets:
        return
    sets.append("updated_at=CURRENT_TIMESTAMP")
    params.extend([session_id, user_id])
    conn = get_conn()
    conn.execute(f"UPDATE scenario_sessions SET {', '.join(sets)} WHERE id=? AND user_id=?", params)
    conn.commit()
    conn.close()
