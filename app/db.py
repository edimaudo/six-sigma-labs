from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).resolve().parent.parent / "sixsigma.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS learner (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            name TEXT DEFAULT '',
            business_area TEXT DEFAULT '',
            belt TEXT DEFAULT 'white',
            diagnostic_score INTEGER DEFAULT 0,
            diagnostic_total INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reflection TEXT NOT NULL,
            scenario_id TEXT DEFAULT '',
            lesson_id TEXT DEFAULT '',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            activity_type TEXT NOT NULL,
            activity_id TEXT DEFAULT '',
            response TEXT NOT NULL,
            feedback TEXT NOT NULL,
            score INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        INSERT OR IGNORE INTO learner (id) VALUES (1);
        """
    )
    conn.commit()
    conn.close()


def learner():
    conn = get_conn()
    row = conn.execute("SELECT * FROM learner WHERE id=1").fetchone()
    conn.close()
    return dict(row)


def update_learner(**values):
    allowed = {"name", "business_area", "belt", "diagnostic_score", "diagnostic_total"}
    values = {k: v for k, v in values.items() if k in allowed}
    if not values:
        return
    values["updated_at"] = "CURRENT_TIMESTAMP"
    sets = []
    params = []
    for key, value in values.items():
        if key == "updated_at":
            sets.append("updated_at = CURRENT_TIMESTAMP")
        else:
            sets.append(f"{key} = ?")
            params.append(value)
    conn = get_conn()
    conn.execute(f"UPDATE learner SET {', '.join(sets)} WHERE id=1", params)
    conn.commit()
    conn.close()


def add_journal(reflection, scenario_id="", lesson_id=""):
    conn = get_conn()
    conn.execute(
        "INSERT INTO journal (reflection, scenario_id, lesson_id) VALUES (?, ?, ?)",
        (reflection.strip(), scenario_id, lesson_id),
    )
    conn.commit()
    conn.close()


def list_journal(limit=20):
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM journal ORDER BY id DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def add_attempt(activity_type, activity_id, response, feedback, score=0):
    conn = get_conn()
    conn.execute(
        "INSERT INTO attempts (activity_type, activity_id, response, feedback, score) VALUES (?, ?, ?, ?, ?)",
        (activity_type, activity_id, response, feedback, score),
    )
    conn.commit()
    conn.close()
    

def list_attempts(limit=20):
    conn = get_conn()
    rows = conn.execute("SELECT * FROM attempts ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
    conn.close()
    return [dict(row) for row in rows]
