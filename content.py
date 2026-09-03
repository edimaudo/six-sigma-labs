BELT_ORDER = ["white", "yellow", "green", "black"]


def lesson(code, title, question, concepts, terms=None, math=None, teach_back="Teach the approach back to me in your own words.", builds_on=None):
    return {
        "code": code,
        "title": title,
        "opening_question": question,
        "concepts": concepts,
        "terms": terms or [],
        "math": math or [],
        "teach_back": teach_back,
        # Codes of lessons (any belt) this lesson assumes as prerequisite knowledge.
        # A lesson should NOT re-explain a concept already owned by a builds_on target;
        # it should extend it. Used by validate_hierarchy() below to catch drift.
        "builds_on": builds_on or [],
    }


def validate_hierarchy(belts):
    """Fails loudly if a lesson's builds_on references a lesson that doesn't
    exist, or references a lesson from a LATER belt (forward dependency)."""
    order = {b: i for i, b in enumerate(BELT_ORDER)}
    code_to_belt = {}
    for belt_key, belt in belts.items():
        for l in belt["modules"]:
            code_to_belt[l["code"]] = belt_key
    errors = []
    for belt_key, belt in belts.items():
        for l in belt["modules"]:
            for dep in l["builds_on"]:
                if dep not in code_to_belt:
                    errors.append(f"{l['code']} builds_on unknown code {dep!r}")
                elif order[code_to_belt[dep]] > order[belt_key]:
                    errors.append(f"{l['code']} ({belt_key}) builds_on {dep} which is a LATER belt ({code_to_belt[dep]})")
    if errors:
        raise ValueError("Hierarchy validation failed:\n" + "\n".join(errors))
    return True


BELTS = {
    "white": {
        "name": "White Belt",
        "tagline": "Understand the language of improvement.",
        "description": "Learn the core language, mindset, process thinking, and DMAIC logic used in Six Sigma work.",
        "modules": [
            lesson("W01", "What is Six Sigma?", "Why do organizations care about variation, defects, and process performance?", [
                "Six Sigma is a disciplined approach to reducing process variation and improving customer and business outcomes.",
                "The goal is not statistics for its own sake. The goal is a better, more predictable process.",
                "Improvement starts by defining the problem and desired outcome before selecting a solution.",
            ], ["Six Sigma", "variation", "defect", "process"], ["Variation is the spread of observed process outcomes around a central tendency.", "A defect is a failure to meet a defined customer or process requirement."], "Explain Six Sigma to a colleague who thinks it is just a statistics program."),
            lesson("W02", "Process Thinking", "Where does a business result actually come from?", [
                "A process converts inputs into outputs for a customer or stakeholder.",
                "Process maps make handoffs, queues, rework, decisions, and failure points visible.",
                "Most operational problems are produced by systems and process design, not one isolated employee.",
            ], ["process map", "handoff", "rework", "cycle time"], ["Cycle time is elapsed time from a defined start to a defined end of a process."], "Teach me how you would explain a process to someone new to operations."),
            lesson("W03", "Lean Mindset", "What is the customer actually willing to pay for?", [
                "Lean focuses on customer value and removal of activities that consume resources without creating value.",
                "Common waste categories include defects, overproduction, waiting, non-used talent, transportation, inventory, motion, and extra-processing.",
                "Lean improves flow; Six Sigma reduces variation. They are complementary, not competing methods.",
            ], ["Lean", "value", "TIMWOODS", "waste"], ["A value-adding activity changes the product or service in a way the customer needs and is willing to pay for."], "Give me a simple example of waste in an office process."),
            lesson("W04", "DMAIC Overview", "Why define a problem before trying to fix it?", [
                "DMAIC means Define, Measure, Analyze, Improve, and Control.",
                "Each phase answers a different question and creates evidence for the next phase.",
                "The discipline prevents teams from confusing symptoms with causes and solutions with proof.",
            ], ["DMAIC", "Define", "Measure", "Analyze", "Improve", "Control"], [], "Walk me through DMAIC without relying on the acronym alone."),
        ],
    },
    "yellow": {
        "name": "Yellow Belt",
        "tagline": "Participate effectively in improvement projects.",
        "description": "Build the practical skills to map processes, support data collection, use basic tools, and contribute to DMAIC teams.",
        "modules": [
            lesson("Y01", "Your Role in Six Sigma", "Where does a Yellow Belt create value on a project team?", [
                "Yellow Belts commonly support process mapping, data collection, problem identification, and implementation.",
                "They need enough methodology to challenge assumptions and contribute credible evidence.",
                "Effective project contributors understand the business context as well as the technical task.",
            ], ["Yellow Belt", "project team", "sponsor", "process owner"], [], "Teach me how a Yellow Belt adds value without becoming the project leader."),
            lesson("Y02", "SIPOC and Process Mapping", "How do you see a process before measuring it?", [
                "SIPOC gives a high-level view of Suppliers, Inputs, Process, Outputs, and Customers.",
                "Detailed process maps expose decisions, handoffs, queues, rework, and failure points.",
                "Mapping is also a stakeholder alignment exercise because different groups often describe the same process differently.",
            ], ["SIPOC", "supplier", "input", "output", "customer", "process map"], [], "Teach me when you would use SIPOC versus a detailed process map."),
            lesson("Y03", "Voice of the Customer", "How do you know what 'good' means?", [
                "Voice of the Customer converts customer needs and pain points into measurable requirements.",
                "Critical-to-Quality characteristics make broad needs operationally testable.",
                "A process can be internally efficient and still fail the customer.",
            ], ["VOC", "CTQ", "customer requirement", "specification"], ["A specification defines the acceptable range for a measurable characteristic."], "Turn a vague customer complaint into a measurable CTQ."),
            lesson("Y04", "Basic Data and Pareto", "Which problems deserve attention first?", [
                "Define what will be counted and use consistent operational definitions before collecting data.",
                "Pareto analysis helps prioritize categories that contribute materially to the observed problem.",
                "A Pareto chart is a prioritization tool, not proof of causation.",
            ], ["Pareto", "frequency", "operational definition"], ["Pareto percentage = category frequency / total frequency × 100."], "Explain why a Pareto chart does not tell you what caused the problem."),
            lesson("Y05", "Team Dynamics", "What happens when a team agrees on the solution too early?", [
                "Improvement teams experience forming, storming, norming, and performing dynamics.",
                "RACI clarifies accountability, but it does not remove politics, power, or incentives.",
                "Good facilitation creates space for evidence and dissent before the team converges.",
            ], ["RACI", "Tuckman", "facilitation", "stakeholder"], [], "How would you respond when a senior stakeholder shuts down an alternative view?"),
        ],
    },
    "green": {
        "name": "Green Belt",
        "tagline": "Lead structured improvement projects.",
        "description": "Develop the DMAIC, Lean, measurement, analysis, improvement, and control skills required to lead improvement work.",
        "modules": [
            # Six Sigma and organizational context
            # NOTE: W01 (White) already owns "what is Six Sigma" and W04 owns "what is DMAIC."
            # G01/G02 must NOT re-derive those definitions — they extend into project
            # selection and business-case territory that White Belt never covers.
            lesson("G01", "Introduction to Six Sigma and Organizational Goals", "Why should an improvement project exist in the first place?", [
                "An improvement project should exist because a measurable gap matters to the organization or customer — not because a tool or technique is available.",
                "Project selection balances impact, urgency, feasibility, and organizational capacity; strong candidates trace back to a strategic goal leadership already tracks.",
                "A project disconnected from any goal leadership recognizes will struggle for funding, staffing, and follow-through, however sound the analysis.",
            ], ["business goal", "project selection", "gap"], [], "Explain how an improvement project connects to an organizational goal.", builds_on=["W01", "W04"]),
            lesson("G02", "Six Sigma and Organizational Goals", "How do you prove that a project matters beyond the process metric?", [
                "Translate process measures into business outcomes such as service, cost, risk, revenue, quality, or capacity — goal cascading turns a strategic objective into a measurable project target.",
                "A strong project has an engaged sponsor (not just a nominal one), clear scope, measurable goals, and a defined benefits mechanism validated with Finance.",
                "Executive urgency should not replace evidence about the actual process problem; a loud stakeholder is not the same thing as a strategically aligned project.",
            ], ["VOB", "business case", "benefits", "goal cascading"], [], "Teach me how you would test whether a proposed project is strategically meaningful.", builds_on=["G01"]),
            lesson("G03", "Lean Principles in the Organization", "Where is work consuming effort without creating customer value across a whole organization, not just one workstation?", [
                "At an organizational level, waste often hides in handoffs BETWEEN functions (approvals, reviews, queues between departments) more than within any single team's visible work.",
                "Use waste categories to identify opportunities for flow and effort reduction, then confirm with data before acting — a visible waste can be a symptom of a different upstream root cause (e.g. a queue caused by upstream overproduction, not the queue step itself).",
                "Lean changes work design and flow; Six Sigma adds disciplined variation reduction and evidence. They are complementary, applied together on most real projects.",
            ], ["cross-functional waste", "flow", "pull", "value stream"], [], "Explain how Lean and Six Sigma complement one another at an organizational, cross-team level.", builds_on=["W03"]),
            # G04 is the SINGLE canonical owner of DFSS/DMADV/IDOV in this curriculum.
            # Every other DMADV-related lesson (Green or Black) must builds_on=["G04"]
            # and add new depth rather than re-explaining what DMADV/IDOV stands for.
            lesson("G04", "Design for Six Sigma (DFSS) Methodologies", "When should quality be designed into a process rather than improved after launch?", [
                "DFSS applies structured quality thinking to new products and processes rather than relying on post-launch correction.",
                "DMADV, also known as IDOV, is an explicit DFSS method for new development: Define, Measure, Analyze, Design, Verify (or Identify, Design, Optimize, Verify) — it shares DMAIC's first three letters but replaces Improve/Control with Design/Verify, because there is no existing process to improve, only something new to build correctly from the start.",
                "Use DMADV/IDOV when an existing process cannot be improved adequately through DMAIC because the product or process must be designed or substantially redesigned to meet customer requirements.",
                "Design choices influence downstream variation, failure modes, and customer experience.",
            ], ["DFSS", "DMADV", "IDOV", "design quality"], [], "Teach me when you would choose DFSS instead of DMAIC, and walk me through DMADV/IDOV.", builds_on=["W04"]),
            # Define
            lesson("G05", "Define Phase: Introduction", "What exactly are we trying to improve?", [
                "Define establishes the problem, customer, scope, goal, sponsor, and business case.",
                "A strong problem statement describes a gap without embedding an assumed cause.",
                "The Define phase creates alignment before data collection and analysis begin.",
            ], ["problem statement", "goal statement", "scope", "charter"], [], "Write and explain a problem statement that avoids assuming the cause."),
            lesson("G06", "Project Identification", "How do you decide which problem is worth a formal Six Sigma project?", [
                "Project candidates can come from strategy, customer pain, COPQ, risk, operational performance, or recurring failure.",
                "Use impact, urgency, feasibility, controllability, and sponsor commitment to screen candidates.",
                "Not every problem needs a DMAIC project; some need routine management or rapid improvement instead.",
            ], ["project selection", "COPQ", "feasibility"], [], "Teach me a practical project-selection screen."),
            lesson("G07", "Voice of the Customer", "What does the customer experience that the internal dashboard may not show?", [
                "VOC gathers explicit and implicit customer needs using complaints, interviews, surveys, observations, and usage data.",
                "Translate customer language into measurable requirements.",
                "Different customer segments may have different priorities.",
            ], ["VOC", "CTQ", "Kano"], [], "Explain how VOC changes the project definition."),
            lesson("G08", "Project Management Basics", "How do you keep an improvement project moving without confusing activity with progress?", [
                "Project management creates milestones, dependencies, ownership, decisions, risks, and escalation paths.",
                "A project plan should make missing decisions visible early.",
                "Progress is measured by validated learning and deliverables, not meeting count.",
            ], ["milestone", "risk", "dependency", "RACI"], [], "Teach me how you would distinguish project activity from actual progress."),
            lesson("G09", "Management and Planning Tools", "Which management tool would make the next project decision easier?", [
                "Common tools include SIPOC, process maps, stakeholder analysis, RACI/RASIC, action logs, risk logs, and prioritization matrices.",
                "Choose tools because they improve a decision, not because they are required paperwork.",
                "Management tools should make ownership and trade-offs explicit.",
            ], ["RACI", "RASIC", "risk log", "prioritization matrix"], [], "Pick two planning tools and explain the decision each enables."),
            lesson("G10", "Business Results for Projects", "How will you know the project created a real business result?", [
                "Define the baseline, target, measurement period, owner, and benefits mechanism before declaring success.",
                "Separate operational improvement from accounting realization.",
                "Validate that benefits persist after implementation.",
            ], ["benefits capture", "baseline", "target", "realization"], [], "Teach me what evidence you would require before calling an improvement a business benefit."),
            lesson("G11", "Team Dynamics and Performance", "How should a project leader respond when the team starts defending positions instead of investigating the process?", [
                "Use facilitation to surface assumptions, evidence, competing incentives, and unresolved disagreements.",
                "Team effectiveness depends on clarity of roles and psychological permission to challenge the current story.",
                "Seniority should not determine which hypothesis survives.",
            ], ["team dynamics", "facilitation", "stakeholder", "conflict"], [], "Teach me how you would reset a project team that has stopped challenging assumptions."),
            lesson("G12", "Define Case Study", "What would you investigate before approving a project charter?", [
                "A Define case should reveal the difference between the initial business story and the evidence you still need.",
                "The learner should identify customer impact, baseline, scope, stakeholder interests, and a defensible goal.",
            ], ["case study", "charter", "VOC", "scope"], [], "Defend the Define decisions you would make in the case."),
            # Measure
            lesson("G13", "Measure Phase", "How do you know the problem is real and how large it is?", [
                "Measure establishes a trustworthy operational definition, baseline, data collection plan, and process performance view.",
                "A baseline is the reference point against which improvement is evaluated.",
            ], ["baseline", "operational definition", "data collection plan"], ["Mean = sum of observations / number of observations.", "Standard deviation describes the spread of observations around the mean."], "Explain why the Measure phase comes before root-cause claims."),
            lesson("G14", "Process Analysis and Documentation", "What does the process actually do rather than what the procedure says it does?", [
                "Map the current state using actual work, handoffs, decisions, queues, and rework.",
                "Compare documented procedure with observed process behavior to identify gaps.",
            ], ["SIPOC", "process map", "swimlane", "value stream"], [], "Teach me how you would validate a process map with frontline employees."),
            lesson("G15", "Probability and Statistics", "What can probability tell you that a single observed outcome cannot?", [
                "Probability quantifies uncertainty and provides a language for expected variation and risk.",
                "Statistics summarizes samples and helps infer what may be true about a broader process or population.",
            ], ["probability", "population", "sample", "random variable"], ["P(A) is the probability of event A.", "Expected value for a discrete variable: E(X) = Σ x·P(X=x)."], "Explain why a sample statistic is not automatically the population truth."),
            lesson("G16", "Collecting and Summarizing Data", "How should data be collected so that the analysis answers the actual process question?", [
                "Define variables, units, sampling method, timing, inclusion rules, and data ownership.",
                "Summaries should show center, spread, shape, and segmentation where relevant.",
                "Poor sampling can create a false picture of the process.",
            ], ["sampling", "mean", "median", "range", "IQR"], ["IQR = Q3 − Q1.", "Coefficient of variation = standard deviation / mean, when the ratio is meaningful."], "Explain how your sampling plan could bias a process study."),
            lesson("G17", "Statistical Distributions", "Why does the shape of the data matter?", [
                "Distributions describe how observations are spread and provide assumptions for many analytical methods.",
                "Normal, binomial, and Poisson distributions model different types of process behavior.",
                "Do not force a distributional assumption when the data does not support it.",
            ], ["normal", "binomial", "Poisson", "distribution", "skew"], ["Normal density: f(x)=1/(σ√(2π))·e^{-(x−μ)^2/(2σ²)}.", "Binomial probability: P(X=k)=C(n,k)p^k(1-p)^{n-k}."], "Teach me how you decide whether a distribution assumption is reasonable."),
            lesson("G18", "Measurement System Analysis", "How can you improve a process if the measurement itself is unstable?", [
                "MSA evaluates whether the measurement system is adequate for the decision being made.",
                "Common concepts include repeatability, reproducibility, bias, stability, and resolution.",
            ], ["MSA", "repeatability", "reproducibility", "bias", "stability"], ["Gauge R&R separates measurement variation from process variation for suitable measurement contexts."], "Explain why measurement-system quality is a prerequisite for trustworthy capability analysis."),
            lesson("G19", "Process and Performance Capability", "How do you know whether a stable process can consistently meet requirements?", [
                "Capability compares process variation with specification limits under appropriate conditions.",
                "Cp reflects potential capability; Cpk considers process centering relative to the specification limits.",
                "Capability indices should not be interpreted blindly when the process is unstable or assumptions are violated.",
            ], ["Cp", "Cpk", "Pp", "Ppk", "specification limit"], ["Cp = (USL−LSL)/(6σ).", "Cpk = min[(USL−μ)/(3σ),(μ−LSL)/(3σ)]."], "Teach me the difference between Cp and Cpk."),
            lesson("G20", "Measure Case Study", "What evidence from the baseline would determine what you analyze next?", [
                "A Measure case should connect data quality, process behavior, segmentation, and performance to the next hypothesis.",
            ], ["baseline", "variation", "capability", "MSA"], ["Z-score = (x−μ)/σ."], "Defend your Measure findings and the analysis questions they create."),
            # Analyze
            lesson("G21", "Introduction to Analyze Phase", "What evidence would convince you that you found a root cause?", [
                "Analyze evaluates competing explanations using data, process knowledge, and structured reasoning.",
                "Separate symptoms, correlations, plausible causes, and validated causal mechanisms.",
            ], ["root cause", "hypothesis", "correlation", "causation"], [], "Explain the difference between a symptom, correlation, and root cause."),
            lesson("G22", "Hypothesis Testing", "How do you decide whether an observed difference is more than random variation?", [
                "Hypothesis testing compares observed evidence with a null model under specified assumptions.",
                "A p-value measures how unusual the observed result would be if the null hypothesis were true.",
                "Statistical significance does not automatically mean operational significance.",
            ], ["null hypothesis", "alternative hypothesis", "p-value", "alpha", "power"], ["Two-sided z statistic: z=(x̄−μ0)/(σ/√n).", "Approximate two-sided 95% CI: estimate ± 1.96×standard error."], "Teach me what a p-value does and does not tell a project team."),
            lesson("G23", "Exploratory Data Analysis", "What patterns should you look for before running a formal test?", [
                "EDA uses plots and summaries to detect distribution shape, outliers, clusters, trends, and relationships.",
                "Segment by meaningful process factors when a pooled view can hide different mechanisms.",
            ], ["EDA", "scatterplot", "box plot", "histogram", "segmentation"], [], "Teach me how EDA can change the hypothesis you test."),
            lesson("G24", "Analyze Case Study", "What would you conclude if the data contradicts the initial stakeholder story?", [
                "A strong Analyze conclusion explains the evidence, uncertainty, alternative explanations, and operational implication.",
            ], ["evidence", "root cause", "alternative hypothesis"], [], "Defend the root-cause conclusion against a skeptical sponsor."),
            # Improve
            lesson("G25", "Introduction to Improve Phase", "How do you move from a validated cause to a defensible intervention?", [
                "Improve turns validated causes into changes that can be tested, compared, and implemented.",
                "Solution selection should consider impact, feasibility, risk, control, cost, and stakeholder adoption.",
            ], ["improvement", "solution selection", "pilot", "impact"], [], "Teach me why selecting a solution is a decision problem, not just a brainstorming exercise."),
            lesson("G26", "Design of Experiments", "How can you learn which factors influence an outcome efficiently?", [
                "DOE deliberately varies factors to estimate effects and interactions while controlling the experimental design.",
                "Factor selection, randomization, replication, and blocking influence the quality of conclusions.",
            ], ["DOE", "factor", "response", "interaction", "randomization"], ["A simple factorial model can be written Y = β0 + β1X1 + β2X2 + β12X1X2 + ε."], "Explain why DOE can reveal interactions that one-factor-at-a-time testing can miss."),
            lesson("G27", "Root Cause Analysis", "How do you stop a root-cause exercise from becoming a list of guesses?", [
                "Use structured methods such as 5 Whys, fishbone analysis, fault trees, and causal verification.",
                "Every proposed cause should lead to a testable prediction or evidence requirement.",
            ], ["5 Whys", "fishbone", "fault tree", "cause verification"], [], "Teach me how you would verify a root cause instead of merely naming one."),
            lesson("G28", "Lean Tools", "Which Lean intervention would change the flow rather than just speed up one step?", [
                "Common tools include 5S, visual management, standard work, error proofing, pull systems, and setup reduction.",
                "Use the tool that fits the failure mechanism instead of applying Lean tools mechanically.",
            ], ["5S", "standard work", "visual management", "poka-yoke", "SMED"], [], "Choose one Lean tool and explain the problem it is designed to address."),
            lesson("G29", "Selecting a Solution", "How should you choose between two technically valid solutions?", [
                "Compare expected effect, implementation effort, risk, reversibility, cost, customer impact, and control requirements.",
                "Pilot where uncertainty is material and the downside is manageable.",
            ], ["prioritization", "pilot", "risk", "decision matrix"], [], "Teach me a defensible way to select between competing solutions."),
            lesson("G30", "Improve Case Study", "What would you test before scaling the selected improvement?", [
                "The Improve case should force trade-offs among effect size, feasibility, political support, risk, and testability.",
            ], ["pilot", "DOE", "implementation", "risk"], [], "Defend the improvement decision to an executive sponsor."),
            # Control
            lesson("G31", "Introduction to Control Phase", "How do you stop the process from returning to its old behavior?", [
                "Control creates ownership, monitoring, response rules, standard work, and escalation paths.",
                "A control plan must match how work is actually performed.",
            ], ["control plan", "standard work", "owner", "response plan"], [], "Teach me how a control plan creates accountability after a project closes."),
            lesson("G32", "Statistical Process Control", "How can you tell common-cause variation from a meaningful process signal?", [
                "SPC monitors process behavior over time and distinguishes routine variation from signals that deserve investigation.",
                "Chart choice depends on data type, sampling structure, and the process question.",
            ], ["SPC", "control chart", "UCL", "LCL", "special cause"], ["For an individuals chart, limits are typically center line ± 3×estimated process standard deviation, with chart-specific constants used in practice."], "Explain why a control limit is not the same thing as a specification limit."),
            lesson("G33", "Control Plan", "What decisions must happen when the process starts drifting?", [
                "A control plan defines the critical characteristic, measure, owner, frequency, limit, reaction, and escalation.",
                "Controls should be embedded in normal work rather than dependent on memory.",
            ], ["control plan", "reaction plan", "escalation", "owner"], [], "Teach me what a useful reaction plan looks like."),
            lesson("G34", "Lean Tools for Process Control", "Which Lean mechanisms make the improved process easier to sustain?", [
                "Visual management, standard work, mistake proofing, daily management, and 5S can make expected behavior visible.",
                "Sustainability depends on both technical controls and management routines.",
            ], ["visual management", "standard work", "poka-yoke", "daily management"], [], "Explain how a Lean control can reinforce an SPC signal."),
            lesson("G35", "Control Case Study", "What would you monitor, who would act, and what happens when performance breaks the rule?", [
                "The Control case should force the learner to specify a metric, trigger, owner, reaction, and governance mechanism.",
            ], ["SPC", "control plan", "governance", "reaction plan"], [], "Defend the control system you would leave behind."),
        ],
    },
    "black": {
        "name": "Black Belt",
        "tagline": "Lead complex, cross-functional improvement.",
        "description": "Extend Green Belt capability into strategy, economics, advanced analysis, experimental design, and organizational change.",
        "modules": [
            # NOTE ON STRUCTURE: the source curriculum numbers sub-points (1.01-1.19, 2.01-2.09, etc.)
            # under FOUR named lessons. Earlier content mechanically exploded every sub-point into
            # its own lesson() call (61 entries for what the outline actually calls 4 lessons), which
            # also caused "1.03 Six Sigma" / "1.04 Lean" to silently re-teach concepts W01/W03/W04
            # already own. Fixed: one lesson() per NAMED outline lesson, each builds_on its real
            # prerequisites, and none of them re-derive a definition owned by an earlier belt.
            lesson("B01", "Introduction to Black Belt", "What changes when you move from leading a project to leading improvement capability?", [
                "Black Belts connect project work to enterprise strategy, coaching, governance, and complex problem solving.",
                "The role requires technical depth and the ability to influence across organizational boundaries.",
            ], ["Black Belt", "Master Black Belt", "portfolio", "governance"], [], "Teach me what distinguishes Black Belt work from Green Belt work."),
            lesson("B02", "Lesson 1: The Basics of Six Sigma", "You already know what Six Sigma and DMAIC are. What does a Black Belt need to understand about how quality thinking evolved, and how projects actually get resourced, that a Green Belt doesn't need to know?", [
                "Quality thinking evolved through Shewhart (statistical control) -> Deming (PDCA, systemic causes) -> Juran (cost of quality, vital few) -> Crosby (zero defects) -> TQM -> Six Sigma -> Lean Six Sigma; place any tool in this lineage, not just use it.",
                "Sigma shift (commonly 1.5-sigma) converts a short-term capability estimate into a more realistic long-term defect estimate; treat it as a modelling convention, not a physical law.",
                "First Pass Yield (FPY) measures one step; Rolled Throughput Yield (RTY) multiplies FPY across every step, exposing hidden failure a single-step view hides -- a five-step process at 95% FPY per step has an RTY near 77%, not 95%.",
                "Six Sigma deliverables at project close: signed charter, VOC-derived CTQ tree, current-state maps, data collection plan, validated root cause, tested improvement, control plan, and a Finance-validated benefit statement.",
                "Structured problem solving (DMAIC/PDCA) is chosen deliberately over unstructured trial-and-error, because unstructured fixes tend to treat symptoms and don't survive the next crisis.",
                "A VOC campaign is planned and multi-method (interviews, surveys, complaint/warranty data), not a single survey; VOB captures business/strategic/risk constraints and VOE captures frontline reality -- the three voices don't always agree, and a Black Belt reconciles them rather than picking one.",
                "Kano analysis sorts requirements into Basic/Must-be, Performance, and Delighters, helping decide which CTQs are worth over-delivering on versus simply table stakes.",
                "Role hierarchy: White (awareness) -> Yellow (part-time contributor) -> Green (project co-lead, still has a day job) -> Black Belt (leads complex, cross-functional projects, mentors Green Belts) -> Master Black Belt (coach/trainer across many projects, not owner of one) -> Project Champion (secures resources, resolves cross-functional obstacles).",
                "What actually drives Six Sigma adoption or failure is rarely the tools -- it's leadership sponsorship, incentive alignment, data availability, and whether the culture treats a surfaced problem as an opportunity or a blame target.",
            ], ["Sigma Shift", "FPY", "RTY", "VOC campaign", "VOB", "VOE", "Kano", "Master Black Belt", "Project Champion"],
               ["DPMO = defects / (units x opportunities per unit) x 1,000,000.", "RTY = FPY_1 x FPY_2 x ... x FPY_n across process steps."],
               "A Green Belt on your team says 'we already covered what Six Sigma is, why does Black Belt training spend a whole lesson on this again?' Explain what's actually new here.",
               builds_on=["W01", "W04", "G01"]),
            lesson("B03", "Lesson 2: The Fundamentals of Six Sigma", "A process, a charter, and a CTQ tree all sound like Green Belt vocabulary you already know. What does a Black Belt need to add to 'process,' 'CTQ,' and 'Pareto' that a Green Belt's version doesn't cover?", [
                "Describe a process as a full system -- inputs, activities, decisions, outputs, controls, customers, and variation -- not just the SIPOC-level boundary a Green Belt draws; identify where control mechanisms are missing, not just where the process starts and ends.",
                "A CTQ tree translates a VOC statement into a measurable requirement (as introduced in Green Belt's VOC lesson); at Black Belt depth, prioritize CTQs using Kano classification and check them against VOB constraints, since not every CTQ can be maximized simultaneously.",
                "Cost of Poor Quality (COPQ) organizes quality-related spending into the PAF model: Prevention, Appraisal, Internal Failure, External Failure. Organizations reliably under-track Prevention (scattered across HR/training budgets) and under-track External Failure (customers who leave without filing a complaint never generate a data point) -- a first COPQ estimate should be presented as a floor, not a ceiling.",
                "Calculating COPQ requires a traceable cost model: units x frequency x unit cost, extended for labor, material, and customer impact, with an explicit mechanism for how the estimate will be validated with Finance later.",
                "Pareto analysis (the 80/20 rule) identifies the vital few causes worth attacking first; at Black Belt depth, use it to allocate a limited DOE or root-cause investigation budget, not just to make a chart.",
                "Basic Six Sigma metrics -- DPU, DPO, DPMO -- build toward a sigma-level conversion; choosing the right metric for a given decision matters more than calculating any one of them correctly.",
            ], ["process system", "CTQ tree", "Kano", "COPQ", "PAF model", "Pareto", "DPU", "DPO", "DPMO"],
               ["Basic COPQ = frequency x cost per occurrence, extended for labor, material, and customer impact.", "DPU = defects / units.", "DPO = defects / (units x opportunities per unit).", "DPMO = DPO x 1,000,000."],
               "Walk a skeptical plant manager through why the scrap cost he already tracks is very likely a fraction of the real Cost of Poor Quality.",
               builds_on=["G05", "G07", "B02"]),
            lesson("B04", "Lesson 3: Lean Six Sigma Projects", "Green Belt training already covered project selection, charters, teams, and financial benefits. What does a Black Belt need to know about running this at a scale where the project spans multiple departments, multiple sponsors, and real political friction?", [
                "A project selection roadmap is a staged funnel -- opportunity identification through business case, feasibility, sponsorship, approval -- that exists specifically to stop technically interesting but low-value problems from consuming a Black Belt's time.",
                "A complete charter's elements each protect against a specific failure mode: a vague problem statement invites scope disputes later; a goal statement without a baseline and target can't prove success; unexplained scope exclusions resurface as mid-project disputes.",
                "Tuckman's stages (forming, storming, norming, performing) describe normal team development -- reading early 'storming' conflict as a normal, temporary phase is far more productive than treating it as a sign the team is failing.",
                "RACI/RASIC clarifies who is Responsible, Accountable, Consulted, and Informed for each concrete task -- ambiguous ownership is a common, avoidable cause of project delay, not a rare edge case.",
                "A credible financial benefit has a baseline, a causal mechanism, a calculation method, an owner, a timing, and a capture method; distinguish 'hard' savings (verifiable, bottom-line) from 'soft' savings (real but less directly verifiable) when reporting to Finance.",
                "Net Present Value (NPV) accounts for the timing of cash flows: a smaller, faster-payoff project can have a higher NPV than a larger, more distant one, which is why 'biggest projected savings' is not by itself the right selection criterion.",
            ], ["project selection roadmap", "charter elements", "Tuckman", "RACI", "RASIC", "hard savings", "soft savings", "NPV"],
               ["NPV = sum CF_t/(1+r)^t - initial investment.", "Improvement % = (baseline - new value) / baseline x 100% when lower is better."],
               "A sponsor asks why you'd recommend a $200K project with a 3-month payback over a $600K project with a 3-year payback. Defend the recommendation using NPV.",
               builds_on=["G06", "G08", "G10", "G11", "B03"]),
            lesson("B05", "Lesson 4: The Lean Enterprise", "You already know Lean targets waste and customer value from White and Green Belt. What's the enterprise-level mechanism that causes waste to keep reappearing even after a team removes it once?", [
                "The 3Ms -- Muda (waste), Mura (unevenness), Muri (overburden) -- describe a causal chain, not three independent categories: uneven demand (Mura) often forces overburden during spikes (Muri), and overburden produces waste (Muda) through rushed work, defects, and breakdowns. Removing visible Muda without addressing its Mura/Muri root cause is why waste tends to reappear.",
                "TIMWOODS and DOWNTIME are two common mnemonics for the identical eight categories of waste -- different organizations adopted different acronyms for the same underlying list.",
                "5S (Sort, Set in Order, Shine, Standardize, Sustain) is sequential -- Shine functions as a first-line inspection, and Sustain is where most 5S initiatives actually fail, since it requires ongoing habit rather than a single visible event.",
                "An enterprise Lean transformation succeeds or fails based on whether Sustain-type discipline (visual controls, audits, accountability) gets built into daily management -- not on how impressive the initial kaizen event looked.",
            ], ["Muda", "Mura", "Muri", "TIMWOODS", "DOWNTIME", "5S", "Sustain"], [],
               "Explain to a plant manager why a 5S event that looked great on day one but has quietly reverted by month three is a Sustain failure, not a Sort failure.",
               builds_on=["W03", "G03", "B04"]),
            # Measure
            lesson("B62", "Measure 01: Process Definition", "Green Belt's Measure Phase lesson already covered establishing a baseline. What decisions about process boundaries have real financial or legal consequences at Black Belt scale — spanning multiple sites or systems — that a single-site Green Belt project never has to resolve?", ["Define start/end points, units, customer, failure definition, and segmentation before collecting data — at multi-site scale, an inconsistent failure definition between sites silently invalidates any cross-site comparison later.", "Segmentation strategy (by site, shift, product family, customer tier) should be decided before data collection, not discovered afterward by slicing the data until a pattern appears."], ["process definition", "CTQ", "operational definition", "segmentation"], [], "Teach me how you would establish a measurable process boundary across three sites with different legacy definitions of 'defect.'", builds_on=["G13", "G14"]),
            lesson("B63", "Measure 02: Six Sigma Statistics", "Green Belt's Probability and Statistics and Statistical Distributions lessons already cover descriptive statistics and distribution shape. What's the Black Belt-level judgment call those lessons don't teach?", ["Use descriptive statistics to summarize center, spread, shape, and variation; inferential methods answer population questions the descriptive numbers alone cannot.", "The Black Belt judgment isn't computing a mean or a confidence interval correctly — it's choosing which statistic actually answers the business decision at hand, and being explicit about what assumption that choice depends on."], ["mean", "variance", "standard deviation", "confidence interval"], ["Variance = Σ(x−x̄)^2/(n−1) for a sample.", "Standard error of the mean = s/√n."], "Teach me the statistics you actually need for Measure — and which ones you'd deliberately leave out of an executive readout.", builds_on=["G15", "G16", "G17"]),
            lesson("B64", "Measure 03: Measurement System Analysis", "Green Belt's MSA lesson already covers repeatability and reproducibility conceptually. What does a Black Belt need to be able to DO with MSA data that a Green Belt-level understanding doesn't equip you for?", ["Run and interpret an ANOVA-based Gauge R&R: decompose total measurement variation into part-to-part, repeatability (equipment), and reproducibility (appraiser) variance components, not just judge repeatability/reproducibility qualitatively.", "%Study Variation and %Contribution from Gauge R&R determine whether a measurement system is acceptable (commonly under 10%), marginal, or unacceptable (over 30%) for the decision being made — the threshold depends on the decision's stakes, not a single universal cutoff.", "For attribute (pass/fail) data, use attribute agreement analysis instead of a variables Gauge R&R — a fundamentally different method, not a simplified version of the same one."], ["MSA", "Gauge R&R", "bias", "%Study Variation", "attribute agreement analysis", "variance components"], ["%Study Variation = (measurement system standard deviation / total observed standard deviation) × 100%."], "Teach me when a Gauge R&R result of 18% Study Variation should block a capability study versus when it's tolerable.", builds_on=["G18"]),
            lesson("B65", "Measure 04: Process Capability", "Green Belt's Process and Performance Capability lesson already covers Cp and Cpk. What does 'Pp' and 'Ppk' in your terms list actually add, and why does a Black Belt need both pairs?", ["Capability compares process spread and centering to specification limits after confirming stability and appropriate assumptions.", "Cp/Cpk use WITHIN-subgroup sigma (short-term, common-cause variation only); Pp/Ppk use the OVERALL sigma calculated from all the data (long-term, including any between-subgroup drift) — a large gap between Cpk and Ppk is itself diagnostic evidence that the process isn't as stable as a control chart alone might suggest.", "When data is meaningfully non-normal, Cp/Cpk/Pp/Ppk built on a normal-distribution assumption are misleading; use a transformation or a distribution-appropriate capability method instead of reporting a standard index against the wrong assumption."], ["Cp", "Cpk", "Pp", "Ppk", "within-subgroup sigma", "overall sigma"], ["Cp=(USL−LSL)/(6σ_within).", "Cpk=min[(USL−μ)/(3σ_within),(μ−LSL)/(3σ_within)].", "Pp=(USL−LSL)/(6σ_overall).", "Ppk=min[(USL−μ)/(3σ_overall),(μ−LSL)/(3σ_overall)]."], "Teach me why a process can show a healthy Cpk but a poor Ppk, and what that gap tells you about the process.", builds_on=["G19"]),
            # Analyze
            lesson("B66", "Analyze 01: Classes of Distribution", "How does distribution class influence your analytical choice?", ["Distribution type affects assumptions, visual diagnostics, and which test or model is appropriate."], ["normal", "binomial", "Poisson", "Weibull"], [], "Teach me why distribution choice matters.", builds_on=["G17"]),
            lesson("B67", "Analyze 02: Inferential Statistics", "How can a sample support a conclusion about a larger process?", ["Inferential statistics uses sample evidence to estimate or test population parameters under stated assumptions."], ["estimator", "confidence interval", "inference"], ["A 95% confidence interval is typically estimate ± critical value × standard error."], "Teach me what a confidence interval means in business language.", builds_on=["G21"]),
            lesson("B68", "Analyze 03: Hypothesis Testing", "What claim are you actually testing?", ["State H0 and H1, choose alpha, select an appropriate test, assess assumptions, and interpret practical importance."], ["H0", "H1", "alpha", "power", "p-value"], ["Type I error = rejecting a true H0; Type II error = failing to reject a false H0."], "Teach me the logic of hypothesis testing step by step.", builds_on=["G22"]),
            lesson("B69", "Analyze 04: Hypothesis Testing with Normal Data", "How does normality support common parametric tests?", ["When assumptions are reasonable, tests based on normal or t distributions can be efficient and interpretable."], ["t-test", "z-test", "ANOVA", "normality"], ["One-sample t statistic: t=(x̄−μ0)/(s/√n)."], "Teach me when you would use a t-test.", builds_on=["B68"]),
            lesson("B70", "Analyze 05: Hypothesis Testing with Non Normal Data", "What should you do when your data does not meet normal assumptions?", ["Consider transformation, nonparametric tests, appropriate count models, or robust methods based on the process question."], ["nonparametric", "Mann-Whitney", "Kruskal-Wallis", "transformation"], [], "Teach me how you would respond to non-normal data without forcing a normal model.", builds_on=["B68"]),
            # Improve
            lesson("B71", "Improve 01: Simple Linear Regression", "How can one input help explain variation in an outcome?", ["Simple regression estimates the relationship between one predictor and a continuous response, while checking assumptions and practical usefulness."], ["regression", "slope", "intercept", "R²"], ["Simple regression: Y=β0+β1X+ε.", "R² is the proportion of response variation explained by the fitted model in the sample."], "Teach me what the slope means operationally.", builds_on=["G26"]),
            lesson("B72", "Improve 02: Multiple Regression Analysis", "What changes when several process inputs influence the outcome at the same time?", ["Multiple regression estimates adjusted relationships while considering other included predictors and potential interactions."], ["multiple regression", "coefficient", "multicollinearity", "residual"], ["Multiple regression: Y=β0+β1X1+...+βkXk+ε."], "Teach me why correlation among predictors can make interpretation difficult.", builds_on=["B71"]),
            lesson("B73", "Improve 03: Designed Experiments", "How can you learn causality rather than only observe association?", ["Designed experiments manipulate factors under a planned structure to estimate effects and interactions."], ["DOE", "factor", "level", "response"], ["A treatment effect is the estimated change in response associated with changing a factor under the experimental design."], "Teach me the difference between observational regression and DOE.", builds_on=["G26"]),
            lesson("B74", "Improve 04: Factorial Experiments", "Green Belt's DOE lesson already introduced the idea of interaction. What can a full factorial calculation tell you that Green Belt's conceptual introduction doesn't?", ["Factorial designs estimate main effects and interactions efficiently across combinations of factor levels, rather than testing one factor at a time.", "A main effect is calculated as the average response at a factor's high level minus the average response at its low level, across all other factor combinations — this number, not just the concept of 'interaction,' is what tells you where to focus tightest process control."], ["factorial", "main effect", "interaction", "2^k design"], ["Main effect of Factor A = mean(response at A-high) − mean(response at A-low), averaged across all levels of other factors."], "Teach me what an interaction means in an operations setting, then walk me through calculating a main effect from a small 2×2 dataset.", builds_on=["B73"]),
            lesson("B75", "Improve 05: Improve Implementation Tools and Techniques", "What makes an improvement survive contact with the real organization?", ["Implementation uses pilots, change plans, stakeholder alignment, training, standard work, risk controls, and benefits tracking."], ["implementation", "change management", "pilot", "adoption"], [], "Teach me how you would move from statistical improvement to operational adoption.", builds_on=["G29"]),
            # DMADV in practice — builds on G04 (the sole owner of "what DMADV/IDOV is").
            # This lesson does NOT redefine the framework; it applies the regression,
            # DOE, and hypothesis-testing tools from this same Improve section to a
            # DMADV Measure/Analyze/Design/Verify sequence, which is the genuinely new
            # thing a Black Belt adds beyond Green Belt's conceptual DFSS introduction.
            lesson("B75B", "DMADV in Practice: Applying Regression, DOE, and Hypothesis Testing to New Design", "Green Belt's DFSS lesson told you DMADV exists and when to use it. Given the regression, factorial design, and hypothesis-testing tools you already have from this Improve section, what does a Black Belt actually DO differently across DMADV's five phases compared to a Green Belt running the same framework conceptually?", [
                "In DMADV's Measure phase, set CTQ targets from real customer data with a stated confidence interval (not a single point estimate) — a target set at a confidence interval's conservative bound is more defensible than one set at the raw sample proportion.",
                "In DMADV's Analyze phase, use a factorial experiment (not one-factor-at-a-time testing) to compare design concepts across multiple factors simultaneously, and rank factors by calculated main effect size, the same calculation from Improve 04, applied here to concept selection rather than an existing process.",
                "In DMADV's Design phase, fit a regression model to predict a CTQ from a controllable input variable, and solve the fitted equation for the input value needed to hit the CTQ target — this converts a qualitative design choice into a specific formulation or process specification.",
                "In DMADV's Verify phase, a promising small-batch or single-site result is not sufficient; a formal hypothesis test (e.g., ANOVA across multiple sites or pilot batches) is needed to confirm performance holds before full launch — a p-value above the significance threshold means insufficient evidence of a problem, not proof that none exists.",
            ], ["DMADV Measure", "DMADV Analyze", "DMADV Design", "DMADV Verify", "confidence interval", "factorial design", "regression", "ANOVA"],
               ["One-sided capability at a minimum spec: (mean − minimum) / (3 × σ)."],
               "A Green Belt asks why DMADV needs a Black Belt at all if the five phases are the same letters they already learned. Explain what statistical tools you're adding at each phase and why that changes the outcome.",
               builds_on=["G04", "B71", "B73", "B74", "B68"]),
            # Control
            lesson("B76", "Control 01: Lean Controls", "How can Lean controls make the improved process easier to sustain?", ["Standard work, visual management, daily management, mistake proofing, and 5S can embed expected behavior."], ["Lean controls", "standard work", "visual management", "poka-yoke"], [], "Teach me how Lean controls support sustainability.", builds_on=["G34", "B05"]),
            lesson("B77", "Control 02: Statistical Process Control", "Green Belt's SPC lesson already covers common-cause versus special-cause variation. What specific, checkable rules does a Black Belt use to actually DECIDE a signal is special-cause, rather than judging a chart by eye?", ["SPC uses time-ordered data and control rules to distinguish routine variation from special-cause signals.", "The Western Electric rules give specific, checkable triggers beyond 'a point outside 3-sigma': e.g. 2 of 3 consecutive points beyond 2-sigma on the same side, 4 of 5 beyond 1-sigma on the same side, or 8 consecutive points on the same side of the centerline — each rule catches a different pattern of drift, not just a single outlier.", "Shewhart charts (using these rules) are tuned to catch large, sudden shifts; CUSUM and EWMA charts are built specifically to detect small, sustained shifts a Shewhart chart's rules would miss for many periods — choose based on the size of shift that actually matters operationally."], ["SPC", "control limits", "special cause", "Western Electric rules", "CUSUM", "EWMA"], ["Three-sigma control limits are designed around the expected distribution of a monitored statistic under stable conditions."], "Teach me how control charts support management decisions, then explain why you'd add a CUSUM chart alongside a standard Shewhart chart for one specific CTQ.", builds_on=["G32"]),
            lesson("B78", "Control 03: Six Sigma Control Plans", "Green Belt's Control Plan lesson already covers measures, owners, and reactions. What does 'governance' and 'audit' in your terms list add that a Green Belt-level control plan doesn't need?", ["Control plans specify measures, ownership, thresholds, reactions, documentation, and review mechanisms.", "At Black Belt / enterprise scale, a control plan also needs a governance layer: who audits whether the control plan is actually being followed (not just whether the process is in control), on what cadence, and what triggers an escalation above the process owner when a reaction plan itself repeatedly fails to hold the gain.", "A control plan without a defined audit cadence tends to quietly stop being followed within months of the project closing — the same failure mode as an unsustained 5S initiative, for the same underlying reason: no one is checking."], ["control plan", "governance", "reaction plan", "audit", "escalation"], [], "Teach me how you would design a control plan for a critical CTQ, including who audits it and how often.", builds_on=["G33"]),
        ],
    },
}


# Cross-cutting process/data curriculum inspired by the structure of LearnChe's
# "Process Improvement using Data" resource. These are original summaries,
# not copied source text.
DATA_PROCESS_CURRICULUM = [
    {
        "code": "PD01", "title": "Visualizing Process Data",
        "question": "What can a chart reveal that a summary number hides?",
        "concepts": [
            "Use time-series plots to see change over time, bar charts for category comparison, histograms for distribution shape, box plots for spread, and scatter plots for relationships.",
            "A useful visualization preserves context: unit of analysis, time period, segmentation, specification, and operational definition.",
        ], "tools": ["time-series plots", "bar plots", "histograms", "box plots", "scatter plots"],
    },
    {
        "code": "PD02", "title": "Understanding Variability",
        "question": "What does the spread of the data tell you about the process?",
        "concepts": [
            "Separate center from spread and distinguish routine variation from meaningful shifts in the process.",
            "Use appropriate distributions and summaries rather than assuming every process is normal.",
        ], "tools": ["variability", "probability distributions", "Bernoulli", "uniform", "normal", "t-distribution", "Poisson"],
    },
    {
        "code": "PD03", "title": "Process Monitoring",
        "question": "How can you tell whether a process has actually changed?",
        "concepts": [
            "Monitor time-ordered observations and distinguish common-cause behavior from special-cause signals.",
            "Match the control chart to the data and use capability only when the process is suitably stable and specifications are defined.",
        ], "tools": ["Shewhart charts", "CUSUM", "EWMA", "control limits", "process capability"],
    },
    {
        "code": "PD04", "title": "Least Squares and Regression",
        "question": "When does a relationship in the data become useful for improving a process?",
        "concepts": [
            "Regression estimates relationships between predictors and responses while making assumptions explicit.",
            "Check residuals, leverage, outliers, influential observations, and practical significance rather than relying on a single fit statistic.",
        ], "tools": ["covariance", "correlation", "simple regression", "multiple regression", "residual analysis", "outliers"],
    },
    {
        "code": "PD05", "title": "Design and Analysis of Experiments",
        "question": "How can you learn what actually causes a change instead of only observing a relationship?",
        "concepts": [
            "Designed experiments manipulate factors under a planned structure to estimate effects and interactions.",
            "Compare one-factor-at-a-time approaches with factorial designs, and understand blocking, replication, and randomization.",
        ], "tools": ["factorial designs", "main effects", "interactions", "blocking", "replication", "randomization"],
    },
    {
        "code": "PD06", "title": "Multivariate Process Thinking",
        "question": "What do you do when many correlated variables describe the same system?",
        "concepts": [
            "Multivariate methods can compress correlated information and reveal latent structure that univariate analysis can miss.",
            "Principal Component Analysis and Projection to Latent Structures are advanced tools for exploration, modelling, and monitoring.",
        ], "tools": ["PCA", "PLS", "latent variables", "scores", "loadings", "multivariate monitoring"],
    },
    {
        "code": "PD07", "title": "Applying Data to Process Improvement",
        "question": "How do you turn analysis into an operational decision?",
        "concepts": [
            "Data analysis can support process understanding, troubleshooting, monitoring, product development, and product improvement.",
            "A statistical result matters when it changes a decision, control, design, or operating condition.",
        ], "tools": ["process understanding", "troubleshooting", "multivariate monitoring", "product development", "process improvement"],
    },
]


# Process/data material is integrated into the belt lessons rather than taught as a separate track.
# Matching is intentionally lightweight and content-driven so new lessons inherit relevant analytical material.
_DATA_KEYWORDS = {
    "PD01": ["visual", "chart", "process map", "collecting", "summariz", "exploratory", "pareto", "data"],
    "PD02": ["probability", "distribution", "variability", "statistics", "measurement", "capability", "summariz", "normal", "non-normal"],
    "PD03": ["control", "spc", "statistical process", "monitor", "capability", "stability", "control chart"],
    "PD04": ["regression", "correlation", "residual", "exploratory", "eda", "relationship"],
    "PD05": ["design of experiments", "factorial", "doe", "experiment", "factor", "interaction", "randomization"],
    "PD06": ["multivariate", "pca", "pls", "latent", "principal component"],
    "PD07": ["improve", "troubleshoot", "business results", "financial", "decision", "application", "process improvement", "project"],
}
_DATA_BY_CODE = {item["code"]: item for item in DATA_PROCESS_CURRICULUM}

for _belt in BELTS.values():
    for _module in _belt["modules"]:
        _haystack = " ".join([
            _module.get("title", ""),
            _module.get("opening_question", ""),
            " ".join(_module.get("concepts", [])),
            " ".join(_module.get("terms", [])),
        ]).lower()
        _scores = []
        for _code, _keywords in _DATA_KEYWORDS.items():
            _score = sum(1 for _kw in _keywords if _kw in _haystack)
            if _score:
                _scores.append((_score, _code))
        _scores.sort(key=lambda x: (-x[0], x[1]))
        _module["process_data"] = [_DATA_BY_CODE[code] for _, code in _scores[:2]]


# Terms are intentionally reusable across lessons so the glossary can be a real reference system.
GLOSSARY = {'5S': {'definition': 'Sort, Set in Order, Shine, Standardize, Sustain: a Lean workplace organization and control method.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'Common Cause': {'definition': 'Routine variation arising from a stable process system.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'Confidence Interval': {'definition': 'An interval estimation procedure that quantifies uncertainty around a population parameter under a specified confidence level and method.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'Control Limit': {'definition': 'A statistically derived boundary used to identify unusual process behavior on a control chart.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'COPQ': {'definition': 'Cost of Poor Quality: costs attributable to failures, defects, rework, complaints, inspection, and related quality losses.', 'why_it_matters': 'COPQ makes the economic consequence of poor performance visible through prevention, appraisal, internal failure and external failure costs.', 'use_when': 'Use it to build the business case and compare improvement options.', 'watch_out': 'Counting only visible rework or complaint costs can understate the true economic impact.'}, 'Cp': {'definition': 'Potential capability index based on specification width relative to six standard deviations of process variation.', 'why_it_matters': 'Cp compares specification width with six standard deviations and describes potential capability when centeredness is ignored.', 'use_when': 'Use it alongside Cpk to separate spread problems from centering problems.', 'watch_out': 'High Cp does not prove that the process is centered or currently meeting specifications.'}, 'Cpk': {'definition': 'Capability index that also accounts for how centered the process is within the specification limits.', 'why_it_matters': 'Cpk combines process spread with distance from the nearest specification limit.', 'use_when': 'Use it to assess practical capability when both variation and centering matter.', 'watch_out': 'Cpk can fall even when variation is acceptable if the process mean drifts toward a specification limit.'}, 'CTQ': {'definition': 'Critical to Quality: a measurable characteristic that represents an important customer requirement.', 'why_it_matters': 'A CTQ converts an important requirement into a measurable characteristic with an operational definition.', 'use_when': 'Use it to translate VOC into metrics and acceptance criteria.', 'watch_out': 'A vague “quality” goal is not a CTQ until it has a measurable definition and threshold.'}, 'CUSUM': {'definition': 'Cumulative Sum control chart: a monitoring method designed to detect small or persistent shifts in a process mean.', 'why_it_matters': 'CUSUM accumulates deviations from a target to make small persistent shifts easier to detect than with some traditional charts.', 'use_when': 'Use it when small mean shifts matter and rapid detection is valuable.', 'watch_out': 'Chart settings and target values should reflect the actual process and decision risk.'}, 'Defect': {'definition': 'A failure to meet a defined customer, specification, or process requirement.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'DFSS': {'definition': 'Design for Six Sigma: structured methods for designing products and processes to meet requirements from the outset.', 'why_it_matters': 'DFSS applies Six Sigma thinking during design so customer and business requirements are built into a new product, service or process.', 'use_when': 'Use it when creating something new or making a redesign substantial enough that an existing-process improvement cycle is not sufficient.', 'watch_out': 'A DFSS project still requires explicit requirements, verification and stakeholder alignment.'}, 'DMADV': {'definition': 'Define, Measure, Analyze, Design, Verify: a DFSS method used for new development or substantial redesign when DMAIC is not sufficient.', 'why_it_matters': 'DMADV is the Define, Measure, Analyze, Design and Verify framework used within Design for Six Sigma for new development.', 'use_when': 'Use it when the desired future process or product does not yet exist, or when redesign requires a new architecture.', 'watch_out': 'Do not assume it is interchangeable with DMAIC: the object of improvement and the evidence available are different.'}, 'DMAIC': {'definition': 'Define, Measure, Analyze, Improve, Control: the core cycle for improving an existing process.', 'why_it_matters': 'It is designed for improving an existing process whose problem and performance can be characterized.', 'use_when': 'Use it when the process exists and the team needs disciplined problem definition, measurement, causal analysis, improvement and control.', 'watch_out': 'Do not use DMAIC as a substitute for choosing the right problem or understanding the operating context.'}, 'DOE': {'definition': 'Design of Experiments: planned manipulation of factors to learn about their effects on a response.', 'why_it_matters': 'DOE changes multiple factors in a planned way so their effects and interactions can be estimated efficiently.', 'use_when': 'Use it when controlled experimentation is feasible and the team needs evidence about causal factors.', 'watch_out': 'Poor factor selection, uncontrolled noise and an ambiguous response measure weaken the experiment.'}, 'DPMO': {'definition': 'Defects per million opportunities: DPO multiplied by one million.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'DPO': {'definition': 'Defects per opportunity: defects divided by units times opportunities per unit.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'DPU': {'definition': 'Defects per unit: total defects divided by total units.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'EWMA': {'definition': 'Exponentially Weighted Moving Average control chart: a monitoring method that weights recent observations more heavily to detect gradual shifts.', 'why_it_matters': 'EWMA gives greater weight to recent observations while retaining information from earlier data.', 'use_when': 'Use it to detect gradual or sustained shifts when a moving average view is useful.', 'watch_out': 'Smoothing can delay or obscure individual large signals if used without understanding the process.'}, 'Hypothesis Test': {'definition': 'A statistical procedure for evaluating evidence against a null hypothesis under stated assumptions.', 'why_it_matters': 'A hypothesis test compares observed evidence with what would be expected under a null model and its assumptions.', 'use_when': 'Use it when a decision requires formal evidence about a difference, relationship or effect.', 'watch_out': 'A p-value is not the probability that the null hypothesis is true, nor is statistical significance the same as business importance.'}, 'IDOV': {'definition': 'Identify, Design, Optimize, Verify: a DFSS framework commonly used as an alternative naming convention to DMADV for new development.', 'why_it_matters': 'IDOV—Identify, Design, Optimize and Verify—is a DFSS framework closely related to DMADV and often used for new development.', 'use_when': 'Use it as an alternative design-oriented roadmap when the organization uses IDOV terminology.', 'watch_out': 'The names differ by organization; the underlying logic remains requirements, design, optimization and verification.'}, 'Interaction': {'definition': 'A situation where the effect of one factor depends on the level of another factor.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'Kano': {'definition': 'A framework for classifying customer requirements into categories such as basic, performance, and attractive needs.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'Lean': {'definition': 'An approach focused on customer value, flow, waste reduction, and continuous improvement.', 'why_it_matters': 'Lean focuses on creating customer value with less unnecessary work, delay, inventory, motion and complexity.', 'use_when': 'Use it to understand flow and remove waste before or alongside statistical analysis.', 'watch_out': 'Waste elimination without understanding demand, variation or quality can simply move problems downstream.'}, 'MSA': {'definition': 'Measurement System Analysis: evaluation of whether a measurement system is adequate for its intended decision.', 'why_it_matters': 'Measurement System Analysis determines whether the measurement process is precise and stable enough for the decisions being made.', 'use_when': 'Use it before trusting process data for capability, comparison or root-cause decisions.', 'watch_out': 'A sophisticated analysis cannot rescue a measurement system that cannot reliably distinguish meaningful differences.'}, 'NPV': {'definition': 'Net Present Value: the discounted value of future cash flows less the initial investment.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'p-value': {'definition': 'The probability, under the null hypothesis, of observing a result at least as extreme as the one obtained, according to the chosen test statistic.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'Pareto': {'definition': 'A prioritization method that ranks categories by contribution, often illustrated with bars and a cumulative line.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'PCA': {'definition': 'Principal Component Analysis: a dimension-reduction method that represents correlated variables through orthogonal components.', 'why_it_matters': 'PCA reduces many correlated variables into a smaller set of components that capture major patterns of variation.', 'use_when': 'Use it for exploratory analysis and dimensionality reduction when many variables move together.', 'watch_out': 'Components are mathematical constructs and should not automatically be treated as causal factors.'}, 'PLS': {'definition': 'Projection to Latent Structures: a multivariate modelling method that extracts latent predictors while considering the response.', 'why_it_matters': 'PLS models relationships between predictors and responses through latent structures, especially when predictors are numerous or correlated.', 'use_when': 'Use it when the goal is prediction or explanation with strongly correlated process variables.', 'watch_out': 'Validation and overfitting checks are essential before using a PLS model operationally.'}, 'Practical Significance': {'definition': 'The real-world magnitude and consequence of an effect, distinct from statistical significance.', 'why_it_matters': 'Practical significance asks whether the size of an effect is meaningful for customers, operations, cost or risk.', 'use_when': 'Use it alongside statistical significance when deciding whether to act.', 'watch_out': 'A statistically significant effect can still be too small to justify a process change.'}, 'Process': {'definition': 'A set of related activities that transforms inputs into outputs for a customer or stakeholder.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'Process Capability': {'definition': 'The ability of a stable process to meet specification requirements, often summarized with indices such as Cp and Cpk.', 'why_it_matters': 'Capability compares the spread and location of a stable process with specification limits.', 'use_when': 'Use it after verifying process stability and an appropriate measurement system.', 'watch_out': 'Capability indices are not meaningful when the process is unstable or the specification is poorly defined.'}, 'RACI': {'definition': 'Responsible, Accountable, Consulted, Informed: a responsibility-assignment framework.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'Regression': {'definition': 'A modelling approach used to estimate relationships between predictors and a response variable.', 'why_it_matters': 'Regression estimates relationships between predictor variables and a response while making assumptions explicit.', 'use_when': 'Use it to quantify associations, build predictions and support causal investigation when paired with sound design and domain knowledge.', 'watch_out': 'Association in a regression model does not by itself establish causation.'}, 'Repeatability': {'definition': 'Variation when the same operator measures the same item using the same method and equipment.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'Reproducibility': {'definition': 'Variation attributable to differences among operators or appraisers using the measurement system.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'Root Cause': {'definition': 'A validated causal mechanism whose removal or control prevents recurrence of the problem under the relevant conditions.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'Sigma Shift': {'definition': 'A convention often used in Six Sigma teaching to translate short-term process performance into an assumed long-term performance estimate.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'SIPOC': {'definition': 'Suppliers, Inputs, Process, Outputs, Customers: a high-level view of process boundaries.', 'why_it_matters': 'SIPOC sets process boundaries by identifying suppliers, inputs, high-level process steps, outputs and customers.', 'use_when': 'Use it early in Define to align stakeholders on scope before detailed mapping.', 'watch_out': 'A SIPOC is intentionally high level; it should not become a detailed process map.'}, 'Six Sigma': {'definition': 'A disciplined approach to improving process performance by reducing defects and variation using data and structured problem solving.', 'why_it_matters': 'It is a management system as much as a set of analytical tools: the objective is predictable process performance and better decisions.', 'use_when': 'Use it to frame improvement around customer requirements, variation, evidence and measurable business outcomes.', 'watch_out': 'Do not reduce Six Sigma to a sigma-level calculation or a statistics exercise.'}, 'SPC': {'definition': 'Statistical Process Control: monitoring process behavior over time to distinguish common-cause from special-cause variation.', 'why_it_matters': 'SPC monitors process behavior over time to distinguish routine variation from signals that warrant investigation.', 'use_when': 'Use it when a process needs ongoing control after improvement or when stability is itself in question.', 'watch_out': 'Control limits are not specification limits; a process can be stable but incapable.'}, 'Special Cause': {'definition': 'An identifiable source of unusual variation that produces a non-routine signal.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'Specification Limit': {'definition': 'A customer, engineering, regulatory, or business requirement defining acceptable output values.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'Variation': {'definition': 'The degree to which process outcomes differ from one another.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}, 'VOB': {'definition': 'Voice of the Business: business, strategic, economic, operational, and risk requirements.', 'why_it_matters': 'VOB captures the organization’s economic, strategic, operational and risk requirements.', 'use_when': 'Use it to connect improvement work to value, capacity, revenue, cost, resilience or risk outcomes.', 'watch_out': 'Business metrics can conflict with customer or employee needs; the trade-off should be made explicit.'}, 'VOC': {'definition': 'Voice of the Customer: structured understanding of customer needs, expectations, pain, and requirements.', 'why_it_matters': 'VOC translates customer experience and expectations into requirements that can be measured and acted upon.', 'use_when': 'Use it at project definition and whenever a proposed solution risks optimizing an internal metric at the expense of customer value.', 'watch_out': 'A complaint is evidence, not automatically the complete customer requirement.'}, 'VOE': {'definition': 'Voice of the Employee: frontline experience, friction, capability constraints, and adoption concerns.', 'why_it_matters': 'VOE captures the experience of employees who operate, support or are affected by the process.', 'use_when': 'Use it to identify workarounds, hidden rework, capability constraints, incentives and adoption barriers.', 'watch_out': 'Employee feedback is not merely sentiment; it can reveal process conditions that transaction data misses.'}, 'Yield': {'definition': 'The proportion of output that meets the relevant requirement under a defined yield convention.', 'why_it_matters': 'It provides a shared language for analyzing, improving or controlling process performance.', 'use_when': 'Use it when the lesson or case study requires this concept to make a decision or interpret evidence.', 'watch_out': 'Keep the definition, assumptions and business context aligned before applying the term.'}}


MATH_REFERENCE = [
    ("Mean", "x̄ = Σx / n", "Average of observed values; sensitive to extreme values."),
    ("Median", "Middle ordered value", "Robust measure of center when data is skewed."),
    ("Sample variance", "s² = Σ(x−x̄)² / (n−1)", "Measures squared dispersion around the sample mean."),
    ("Sample standard deviation", "s = √s²", "Expresses process spread in the original measurement units."),
    ("Z-score", "z = (x−μ) / σ", "Number of standard deviations an observation is from the mean."),
    ("Standard error of mean", "SE = s / √n", "Sampling variability of the sample mean."),
    ("95% confidence interval", "estimate ± critical value × SE", "Quantifies uncertainty around a population estimate."),
    ("Binomial probability", "P(X=k)=C(n,k)p^k(1-p)^(n-k)", "Models counts of successes across fixed independent trials under assumptions."),
    ("Poisson probability", "P(X=k)=e^(−λ) λ^k / k!", "Models counts over a fixed interval under Poisson assumptions."),
    ("DPO", "defects / (units × opportunities)", "Normalizes defects by the number of defect opportunities."),
    ("DPMO", "DPO × 1,000,000", "DPO expressed per one million opportunities."),
    ("Yield", "good units / total units", "Share of units meeting the defined acceptance rule."),
    ("Cp", "(USL−LSL)/(6σ)", "Potential capability assuming a stable, centered-enough process and suitable assumptions."),
    ("Cpk", "min[(USL−μ)/(3σ),(μ−LSL)/(3σ)]", "Capability adjusted for process centering."),
    ("Simple regression", "Y = β0 + β1X + ε", "Models a linear relationship between one predictor and a response."),
    ("Multiple regression", "Y = β0 + ΣβjXj + ε", "Models a response using several predictors."),
    ("CUSUM", "C_t = max(0, C_{t−1} + x_t − target − k)", "Cumulative evidence for a sustained process shift; exact form depends on the chart design."),
    ("EWMA", "Z_t = λX_t + (1−λ)Z_{t−1}", "Exponentially weighted monitoring statistic; λ controls responsiveness to recent observations."),
    ("Correlation", "r = cov(X,Y)/(s_X s_Y)", "Standardized linear association; correlation alone does not establish causation."),
    ("R-squared", "R² = 1 − SSE/SST", "Proportion of sample response variation explained by the fitted regression model."),
    ("Factorial combinations", "2^k", "Number of treatment combinations for a two-level full factorial with k factors."),
    ("PCA variance share", "eigenvalue_j / Σ eigenvalues", "Share of total scaled variance represented by a principal component."),
    ("NPV", "Σ CFt/(1+r)^t − initial investment", "Discounted economic value of a project."),
]


# Belt-level assessment: 20-question adaptive bank.
# The session presents 4 anchors first, then routes to a 6-question branch.
DIAGNOSTIC_BANK = [
    {"id": "W1", "belt": "white", "tier": 1, "anchor": True, "topic": "Six Sigma & Org",
     "question": "What is the primary goal of Six Sigma as a business methodology?",
     "options": [
         "To eliminate all variation and defects in a process, improving customer satisfaction and reducing costs",
         "To increase the number of employees trained in statistics",
         "To guarantee zero customer complaints within one year",
         "To replace all manual processes with automation",
     ], "answer": 0,
     "rationale": "Six Sigma centers on reducing variation and defects to improve quality and business performance — it is not a training quota or a guarantee.",
     "socratic": "If a process has very little variation but still produces defects, has Six Sigma succeeded?"},
    {"id": "W2", "belt": "white", "tier": 1, "topic": "Lean Principles",
     "question": "In simple terms, what does waste mean in a Lean environment?",
     "options": [
         "Any activity that consumes resources but adds no value from the customer's perspective",
         "Any material left over after production",
         "Only physical scrap or damaged product",
         "Time employees spend on breaks",
     ], "answer": 0,
     "rationale": "Lean defines waste (muda) broadly as non-value-adding activity — much wider than physical scrap alone.",
     "socratic": "Can you think of an activity in your own work that feels necessary but might not add value to the customer?"},
    {"id": "W3", "belt": "white", "tier": 1, "topic": "Voice of the Customer",
     "question": "Which of the following best describes Voice of the Customer (VOC)?",
     "options": [
         "Feedback and requirements gathered directly or indirectly from customers about their needs and expectations",
         "A survey sent only to unhappy customers",
         "The company's internal quality standards",
         "A single customer's opinion used to set project priorities",
     ], "answer": 0,
     "rationale": "VOC is a structured, ongoing process of capturing needs and expectations — not a complaints inbox or one person's opinion.",
     "socratic": "How might the voice of an internal customer differ from an external one?"},
    {"id": "W4", "belt": "white", "tier": 1, "topic": "Six Sigma & Org",
     "question": "What is a defect in Six Sigma terms?",
     "options": [
         "Any output that fails to meet a specified customer requirement or specification",
         "Any product returned by a customer",
         "A cosmetic flaw only",
         "An error made by an employee",
     ], "answer": 0,
     "rationale": "A defect is defined against specification, regardless of whether it results in a return or is visually obvious.",
     "socratic": "If a product meets specification but the customer is still unhappy, is that a defect?"},
    {"id": "W5", "belt": "white", "tier": 1, "topic": "Team Dynamics",
     "question": "Why is teamwork important in continuous improvement efforts?",
     "options": [
         "Diverse perspectives and cross-functional knowledge lead to better root-cause identification and more sustainable solutions",
         "It ensures management approval is not required",
         "It reduces the total time spent on paperwork",
         "It is mainly to distribute blame if the project fails",
     ], "answer": 0,
     "rationale": "Cross-functional input surfaces causes and constraints a single person would likely miss.",
     "socratic": "What might go wrong on an improvement project run by just one person working alone?"},

    {"id": "Y1", "belt": "yellow", "tier": 2, "anchor": True, "topic": "Define Phase / DMAIC",
     "question": "What does the acronym DMAIC stand for?",
     "options": [
         "Define, Measure, Analyze, Improve, Control",
         "Design, Manage, Analyze, Implement, Check",
         "Define, Model, Assess, Improve, Confirm",
         "Determine, Measure, Act, Investigate, Correct",
     ], "answer": 0,
     "rationale": "DMAIC is the standard Six Sigma project structure.",
     "socratic": "Why do you think Define comes before Measure rather than the other way around?"},
    {"id": "Y2", "belt": "yellow", "tier": 2, "topic": "Analyze — Root Cause Tools",
     "question": "What tool would you use to identify the vital few causes contributing to most of a problem (the 80/20 rule)?",
     "options": ["Pareto Chart", "Control Chart", "Scatter Diagram", "Histogram"], "answer": 0,
     "rationale": "The Pareto chart is specifically built to visualize the 80/20 relationship between causes and effect.",
     "socratic": "If your Pareto chart shows one cause responsible for 90% of defects, how should that change your project's priorities?"},
    {"id": "Y3", "belt": "yellow", "tier": 2, "topic": "Root Cause Analysis",
     "question": "What is the purpose of a fishbone (Ishikawa) diagram?",
     "options": [
         "To organize potential causes of a problem into categories to explore root causes systematically",
         "To rank causes by financial impact only",
         "To track defects over time",
         "To calculate process capability",
     ], "answer": 0,
     "rationale": "It is a brainstorming and organizing tool for causes, not a statistical or financial calculation.",
     "socratic": "Why might grouping causes into categories like Method, Machine, or People help a team brainstorm more completely?"},
    {"id": "Y4", "belt": "yellow", "tier": 2, "topic": "Lean Tools — 5S",
     "question": "In 5S, what does the Sort step involve?",
     "options": [
         "Removing unnecessary items from the workspace, keeping only what is needed",
         "Cleaning the workspace daily",
         "Labelling all items alphabetically",
         "Creating a maintenance schedule",
     ], "answer": 0,
     "rationale": "Sort (Seiri) is specifically about removing what is not needed, before organizing what remains.",
     "socratic": "What is a risk of skipping the Sort step and going straight to organizing everything neatly?"},
    {"id": "Y5", "belt": "yellow", "tier": 2, "topic": "Six Sigma Roles",
     "question": "What is the role of a Yellow Belt on a Six Sigma project team?",
     "options": [
         "Supports projects as a team member, providing local process knowledge and helping with data collection",
         "Leads complex, cross-functional projects independently",
         "Trains Black Belts on advanced statistics",
         "Approves project charters and allocates budget",
     ], "answer": 0,
     "rationale": "Yellow Belts are typically subject-matter contributors, not project leads or approvers.",
     "socratic": "How does a Yellow Belt's role differ from a Green Belt's role on the same project?"},

    {"id": "G1", "belt": "green", "tier": 3, "anchor": True, "topic": "Measure — MSA",
     "question": "What is the purpose of a Measurement System Analysis (MSA)?",
     "options": [
         "To determine how much of the observed variation in data comes from the measurement system itself versus the actual process",
         "To calculate the financial return of a project",
         "To identify which employees need more training",
         "To set the specification limits for a process",
     ], "answer": 0,
     "rationale": "MSA isolates measurement-system variation from true process variation — a prerequisite for trusting any data collected afterward.",
     "socratic": "If your measurement system contributes 40% of the variation you are seeing, can you trust your process data?"},
    {"id": "G2", "belt": "green", "tier": 3, "topic": "Measure — Process Capability",
     "question": "Which statistical concept describes the spread of a process relative to its specification limits?",
     "options": ["Process Capability (e.g., Cp/Cpk)", "Correlation coefficient", "Standard deviation alone", "Sample size"], "answer": 0,
     "rationale": "Cp/Cpk specifically relate process spread to the specification width, unlike standard deviation on its own.",
     "socratic": "What does it mean if a process has a Cpk below 1.0?"},
    {"id": "G3", "belt": "green", "tier": 3, "topic": "Analyze — Hypothesis Testing",
     "question": "What does a p-value in hypothesis testing help you determine?",
     "options": [
         "The probability of observing your data (or something more extreme) if the null hypothesis is true",
         "The probability that your hypothesis is correct",
         "The percentage of defects in your sample",
         "The confidence level you should report to stakeholders",
     ], "answer": 0,
     "rationale": "This is the precise statistical definition — a very common point of confusion worth reinforcing.",
     "socratic": "If a p-value is 0.03, and your significance level is 0.05, what conclusion would you draw about the null hypothesis?"},
    {"id": "G4", "belt": "green", "tier": 3, "topic": "Control — Control Plan",
     "question": "What is the primary purpose of a Control Plan in the Control phase?",
     "options": [
         "To document how key process variables will be monitored and controlled so improvements are sustained after the project ends",
         "To list every employee assigned to the process",
         "To calculate the project's return on investment",
         "To replace the need for standard operating procedures",
     ], "answer": 0,
     "rationale": "The Control Plan exists specifically to sustain gains after the project team disbands.",
     "socratic": "What might happen to your project's gains six months after closure if there is no control plan in place?"},
    {"id": "G5", "belt": "green", "tier": 3, "topic": "Define — Project Management",
     "question": "Which tool is used in the Define phase to establish project scope, goals, and business case?",
     "options": ["Project Charter", "Fishbone Diagram", "Control Chart", "DOE Matrix"], "answer": 0,
     "rationale": "The charter is the foundational Define-phase document; the other tools belong to later phases.",
     "socratic": "Why is a clearly defined problem statement in the charter important before a team starts collecting data?"},

    {"id": "B1", "belt": "black", "tier": 4, "anchor": True, "topic": "Improve — Factorial Experiments",
     "question": "In Design of Experiments (DOE), what is a factorial experiment used for?",
     "options": [
         "To study the effects of multiple input factors and their interactions on an output simultaneously",
         "To test one variable at a time for simplicity",
         "To replace the need for hypothesis testing",
         "To measure only the main effect of a single factor",
     ], "answer": 0,
     "rationale": "Factorial designs are specifically valued for detecting interaction effects that one-factor-at-a-time testing would miss.",
     "socratic": "Why might testing one factor at a time miss an important interaction effect between two variables?"},
    {"id": "B2", "belt": "black", "tier": 4, "topic": "Define — Sigma Shift",
     "question": "What does the 1.5 sigma shift account for in long-term Six Sigma calculations?",
     "options": [
         "It accounts for the fact that process means tend to drift over the long term, so short-term capability studies are adjusted to better estimate long-term defect rates",
         "It corrects for measurement error only",
         "It is a rounding convention used only in reporting",
         "It applies only to attribute (discrete) data, never continuous data",
     ], "answer": 0,
     "rationale": "The shift bridges short-term and long-term process performance estimates.",
     "socratic": "Why might a process that looks capable in a short-term study still produce more defects than expected over a year?"},
    {"id": "B3", "belt": "black", "tier": 4, "topic": "Analyze — Hypothesis Testing with Non-Normal Data",
     "question": "When should you use a non-parametric (non-normal) hypothesis test instead of a standard t-test?",
     "options": [
         "When the data significantly violates the assumption of normality and sample sizes are small, or the data is ordinal/ranked rather than continuous",
         "Whenever you have more than 30 data points",
         "Only when analyzing attribute data",
         "Non-parametric tests should never be used in Six Sigma",
     ], "answer": 0,
     "rationale": "Non-parametric tests exist precisely for cases where normality assumptions do not hold.",
     "socratic": "If a Shapiro-Wilk test shows your data is non-normal and you cannot transform it, what does that mean for choosing between a t-test and a Mann-Whitney test?"},
    {"id": "B4", "belt": "black", "tier": 4, "topic": "Improve — Multiple Regression",
     "question": "In multiple regression analysis, what does a high VIF (variance inflation factor) indicate?",
     "options": [
         "High multicollinearity among predictor variables, meaning they are highly correlated with each other, making individual coefficient estimates unreliable",
         "That the regression model has a very high R-squared and is highly accurate",
         "That the sample size is too large for the model",
         "That the residuals are normally distributed",
     ], "answer": 0,
     "rationale": "VIF flags multicollinearity specifically — a common source of misleading coefficient estimates.",
     "socratic": "If two of your predictors are highly correlated, how would you decide which one to keep in the model?"},
    {"id": "B5", "belt": "black", "tier": 4, "topic": "Define — COPQ Calculation",
     "question": "How is Cost of Poor Quality (COPQ) typically calculated?",
     "options": [
         "By summing costs of prevention, appraisal, and internal/external failure related to poor quality",
         "By dividing total revenue by number of defects",
         "By calculating only the cost of scrapped material",
         "By multiplying headcount by average salary",
     ], "answer": 0,
     "rationale": "This is the standard prevention-appraisal-failure model used to calculate COPQ.",
     "socratic": "Which of the four COPQ cost categories do you think is most often underestimated by organizations, and why?"},
]

# Randomize answer order deterministically per question so answer position is not a cue.
# The question bank supplied all correct answers as option A; the order below preserves
# the correct answer while removing positional bias.
import random as _diagnostic_random
for _q in DIAGNOSTIC_BANK:
    _correct_text = _q["options"][_q["answer"]]
    _options = list(_q["options"])
    _diagnostic_random.Random(_q["id"]).shuffle(_options)
    _q["options"] = _options
    _q["answer"] = _options.index(_correct_text)

DIAGNOSTIC = DIAGNOSTIC_BANK


SCENARIOS = [{'area': 'Retail',
  'belt': 'white',
  'difficulty': 'White Belt',
  'id': 'w-process-map',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'Returns are piling up between store intake and warehouse receiving. The organization cannot agree where '
            'the process actually starts and ends.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Retail returns handoff',
  'method': 'DMAIC'},
 {'area': 'Professional Services',
  'belt': 'white',
  'difficulty': 'White Belt',
  'id': 'w-customer-email',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'A shared inbox is creating delays. Teams disagree about what counts as urgent and who owns the first '
            'response.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Customer email triage',
  'method': 'DMAIC'},
 {'area': 'Manufacturing',
  'belt': 'white',
  'difficulty': 'White Belt',
  'id': 'w-invoice-correction',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'A new invoicing workflow is being designed. Finance wants fewer corrections, while operations wants a '
            'simple process that people will actually follow.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Designing an error-proof invoice correction workflow',
  'method': 'DMADV / IDOV'},
 {'area': 'Healthcare',
  'belt': 'white',
  'difficulty': 'White Belt',
  'id': 'w-appointment-scheduling',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'A healthcare team is designing a new scheduling process. Patients want clarity and speed while staff need '
            'a workable process across different appointment types.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Designing a better appointment scheduling flow',
  'method': 'DMADV / IDOV'},
 {'area': 'Technology',
  'belt': 'white',
  'difficulty': 'White Belt',
  'id': 'w-password-reset',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'Password and access requests are generating frustration. Managers want faster service while security '
            'wants consistent controls.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Employee access requests',
  'method': 'DMAIC'},
 {'area': 'Retail',
  'belt': 'yellow',
  'difficulty': 'Yellow Belt',
  'id': 'y-order-fulfillment',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'Orders miss the promised ship date. Picking, packing, and customer service each report a different cause.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Order fulfillment handoffs',
  'method': 'DMAIC'},
 {'area': 'Insurance',
  'belt': 'yellow',
  'difficulty': 'Yellow Belt',
  'id': 'y-policy-intake',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'New policy applications are being returned for missing information. Frontline teams want simpler '
            'requirements.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Insurance policy intake',
  'method': 'DMAIC'},
 {'area': 'Government',
  'belt': 'yellow',
  'difficulty': 'Yellow Belt',
  'id': 'y-purchase-orders',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'A company is replacing its purchase approval process. Procurement wants control, managers want speed, and '
            'finance needs reliable spend visibility.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Designing a new purchase approval workflow',
  'method': 'DMADV / IDOV'},
 {'area': 'Banking',
  'belt': 'yellow',
  'difficulty': 'Yellow Belt',
  'id': 'y-contact-centre',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'Agents spend substantial time completing after-call work. The team suspects too many mandatory fields.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Contact centre after-call work',
  'method': 'DMAIC'},
 {'area': 'Manufacturing',
  'belt': 'yellow',
  'difficulty': 'Yellow Belt',
  'id': 'y-maintenance-request',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'A plant is designing a new maintenance request process. Operators need fast response while maintenance '
            'needs enough information to prioritize work safely.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Designing a new maintenance request process',
  'method': 'DMADV / IDOV'},
 {'area': 'Banking',
  'belt': 'green',
  'difficulty': 'Green Belt',
  'id': 'g-loan-underwriting',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'Mortgage applications are missing the service target. Sales, underwriting, and risk each have a different '
            'explanation.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Mortgage underwriting cycle time',
  'method': 'DMAIC'},
 {'area': 'Healthcare',
  'belt': 'green',
  'difficulty': 'Green Belt',
  'id': 'g-hospital-pharmacy',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'An outpatient pharmacy is designing a new intake process to reduce waiting without compromising '
            'medication safety or staff workload.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Designing a safer outpatient pharmacy intake process',
  'method': 'DMADV / IDOV'},
 {'area': 'Insurance',
  'belt': 'green',
  'difficulty': 'Green Belt',
  'id': 'g-insurance-claims',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'Claims are repeatedly reopened. Leadership wants automation, while adjusters say upstream information '
            'quality is the real issue.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Claims rework',
  'method': 'DMAIC'},
 {'area': 'Telecommunications',
  'belt': 'green',
  'difficulty': 'Green Belt',
  'id': 'g-call-resolution',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'Customers call back after supposedly resolved cases. Operations wants a higher first-call resolution rate '
            'without increasing average handle time.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Contact centre first-call resolution',
  'method': 'DMAIC'},
 {'area': 'Manufacturing',
  'belt': 'green',
  'difficulty': 'Green Belt',
  'id': 'g-factory-changeover',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'A factory is designing a new changeover standard for a high-mix production line. The design must reduce '
            'setup time while protecting quality.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Designing a faster changeover standard',
  'method': 'DMADV / IDOV'},
 {'area': 'Banking',
  'belt': 'black',
  'difficulty': 'Black Belt',
  'id': 'b-digital-onboarding',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'A bank is designing a new digital account-opening experience. The design must balance customer '
            'conversion, fraud controls, compliance and operating cost.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Designing a new digital onboarding experience',
  'method': 'DMADV / IDOV'},
 {'area': 'Retail',
  'belt': 'black',
  'difficulty': 'Black Belt',
  'id': 'b-supply-planning',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'Forecast error is creating both excess inventory and stockouts. Different teams optimize different '
            'metrics.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Supply planning forecast error',
  'method': 'DMAIC'},
 {'area': 'Healthcare',
  'belt': 'black',
  'difficulty': 'Black Belt',
  'id': 'b-medication-administration',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'A healthcare organization is redesigning medication administration. The new process must improve '
            'reliability while fitting real clinical work.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Designing a safer medication administration workflow',
  'method': 'DMADV / IDOV'},
 {'area': 'Manufacturing',
  'belt': 'black',
  'difficulty': 'Black Belt',
  'id': 'b-product-defects',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'A manufacturer is launching a new product and needs a design-to-launch process that prevents defects from '
            'escaping into production and customers.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Designing a defect-resistant new product launch process',
  'method': 'DMAIC'},
 {'area': 'Financial Services',
  'belt': 'black',
  'difficulty': 'Black Belt',
  'id': 'b-customer-verification',
  'metrics': {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [8, 10, 9, 13, 12, 15, 16, 14, 18, 20]},
  'prompt': 'A financial institution is designing a new customer verification process that balances conversion, fraud '
            'risk, compliance obligations and frontline usability.',
  'stakeholders': ['Executive Sponsor',
                   'Process Owner',
                   'Frontline Representative',
                   'Customer Representative',
                   'Risk & Controls',
                   'Finance Partner'],
  'title': 'Designing a new customer verification process',
  'method': 'DMAIC'}]




# Source-based case studies added in the expanded case library.
ADDITIONAL_CASE_STUDIES = [{'id': 'cs-praxie-production-waste', 'belt': 'yellow', 'difficulty': 'Yellow Belt', 'area': 'Manufacturing', 'method': 'DMAIC', 'title': 'Production scrap reduction', 'prompt': 'A manufacturing line is producing more scrap than expected. The team suspects machine settings, material handling and operator practices, but the baseline is not yet clear.', 'source_url': 'https://praxie.com/dmaic-project-examples-in-manufacturing/', 'source_title': 'DMAIC Project Success Stories & Cases in Manufacturing'}, {'id': 'cs-praxie-product-quality', 'belt': 'green', 'difficulty': 'Green Belt', 'area': 'Manufacturing', 'method': 'DMAIC', 'title': 'Product defect reduction', 'prompt': 'Final-product defects are above target. Supplier material quality and inspection practices are both being blamed, but the team needs evidence to distinguish the causes.', 'source_url': 'https://praxie.com/dmaic-project-examples-in-manufacturing/', 'source_title': 'DMAIC Project Success Stories & Cases in Manufacturing'}, {'id': 'cs-praxie-supply-chain', 'belt': 'green', 'difficulty': 'Green Belt', 'area': 'Manufacturing', 'method': 'DMAIC', 'title': 'Supply-chain lead-time reduction', 'prompt': 'Production is being delayed by long supply-chain lead times. Inventory practices and vendor communication are both potential drivers, and the team needs to establish where delay accumulates.', 'source_url': 'https://praxie.com/dmaic-project-examples-in-manufacturing/', 'source_title': 'DMAIC Project Success Stories & Cases in Manufacturing'}, {'id': 'cs-praxie-equipment-efficiency', 'belt': 'green', 'difficulty': 'Green Belt', 'area': 'Manufacturing', 'method': 'DMAIC', 'title': 'Equipment efficiency and downtime', 'prompt': 'A plant is operating below its expected equipment efficiency, with recurring downtime. Maintenance schedules and aging parts are competing explanations.', 'source_url': 'https://praxie.com/dmaic-project-examples-in-manufacturing/', 'source_title': 'DMAIC Project Success Stories & Cases in Manufacturing'}, {'id': 'cs-pump-ovality', 'belt': 'green', 'difficulty': 'Green Belt', 'area': 'Manufacturing', 'method': 'DMAIC', 'title': 'Pump stage-casing ovality', 'prompt': 'A submersible-pump manufacturer is seeing ovality in a stage-casing component. The team must separate casting, machining and process-setting effects before selecting a solution.', 'source_url': 'https://www.researchgate.net/publication/264819873_Six_Sigma_implementation_through_DMAIC_a_case_study', 'source_title': 'Six Sigma implementation through DMAIC: a case study'}, {'id': 'cs-hospital-admin', 'belt': 'white', 'difficulty': 'White Belt', 'area': 'Healthcare', 'method': 'DMAIC', 'title': 'On-time completion of resident administrative tasks', 'prompt': 'A hospital wants more resident administrative tasks completed on time. Leaders see a performance problem, but the process, workload and incentives have not been defined clearly.', 'source_url': 'https://www.isixsigma.com/case-studies/case-study-dmaic-project-improves-hospitals-on-time-completion-of-administrative-tasks/', 'source_title': "DMAIC Project Improves Hospital's On-time Completion of Administrative Tasks"}, {'id': 'cs-cricket-batting', 'belt': 'green', 'difficulty': 'Green Belt', 'area': 'Sports', 'method': 'DMAIC', 'title': 'Batting consistency and performance', 'prompt': 'A cricket team wants to improve a key batter’s consistency. The team has performance data by pitch, bowling style and batting position, but they disagree about which factors matter most.', 'source_url': 'https://www.slideshare.net/slideshow/six-sigma-dmaic-case-study/27088799', 'source_title': 'Six Sigma DMAIC Case Study'}, {'id': 'cs-router-config', 'belt': 'white', 'difficulty': 'White Belt', 'area': 'Telecommunications', 'method': 'DMAIC', 'title': 'Incorrect router configurations', 'prompt': 'Field installations are being delayed because routers arrive with configuration errors. Engineering, provisioning and field teams each see a different point of failure.', 'source_url': 'https://goleansixsigma.com/reducing-incorrect-router-installations-call-one/', 'source_title': 'Call One Reduced Router Configuration Time By 55%'}, {'id': 'cs-software-bug', 'belt': 'green', 'difficulty': 'Green Belt', 'area': 'Technology', 'method': 'DMAIC', 'title': 'Software bug-fix lead time', 'prompt': 'Bug fixes take too long to reach the official branch. The team must distinguish productive engineering work from queue time, extra reviews and handoffs.', 'source_url': 'https://goleansixsigma.com/project-storyboard-reducing-software-bug-fix-lead-time-from-25-to-15-days/', 'source_title': 'Telecommunications Company Reduced Software Bug Fix Lead Time By 40%'}, {'id': 'cs-offshore-inspection', 'belt': 'green', 'difficulty': 'Green Belt', 'area': 'Oil & Gas', 'method': 'DMAIC', 'title': 'Critical-equipment inspection and risk monitoring', 'prompt': 'An offshore operator has inconsistent monitoring of critical equipment failures. The improvement team must clarify indicators, acceptance criteria and the connection between inspection data and operational risk.', 'source_url': 'https://jpt.spe.org/twa/analysis-method-and-continuous-improvement-of-the-critical-equipment-inspection-process-in-the-offshore-sector', 'source_title': 'Analysis Method and Continuous Improvement of the Critical Equipment Inspection Process in the Offshore Sector'}, {'id': 'cs-drillbit-inventory', 'belt': 'green', 'difficulty': 'Green Belt', 'area': 'Oil & Gas', 'method': 'DMAIC', 'title': 'Drill-bit inventory and lease management', 'prompt': 'Drill-bit inventory is spread across warehouses, field locations and clients. Poor visibility and manual records are creating waste, errors and underutilization.', 'source_url': 'https://jpt.spe.org/twa/lean-six-sigma-applications-in-the-oil-and-gas-industry-drill-bit-inventory-and-lease-management', 'source_title': 'Lean Six Sigma Applications in the Oil and Gas Industry: Drill-Bit Inventory and Lease Management'}, {'id': 'cs-underwriting-resubmits', 'belt': 'green', 'difficulty': 'Green Belt', 'area': 'Financial Services', 'method': 'DMAIC', 'title': 'Commercial-loan underwriting resubmits', 'prompt': 'More than half of commercial-loan packages are being resubmitted. Bankers and analysts disagree on why, and early hypotheses do not yet explain the rework.', 'source_url': 'https://goleansixsigma.com/project-storyboard-reducing-underwriting-resubmits-by-over-20/', 'source_title': 'Reducing Underwriting Resubmits by Over 20%'}, {'id': 'cs-la-county-filing', 'belt': 'yellow', 'difficulty': 'Yellow Belt', 'area': 'Government', 'method': 'DMAIC', 'title': 'Business filing rejection rates', 'prompt': 'A county registrar wants fewer business filings rejected and shorter customer waits. Frontline teams have ideas for removing unnecessary steps, but ownership crosses bureau boundaries.', 'source_url': 'https://goleansixsigma.com/a-call-to-change-pioneering-lean-six-sigma-in-los-angeles-county/', 'source_title': 'LA County Reduced Business Filing Rejection Rates By 30%'}, {'id': 'cs-kern-helpdesk', 'belt': 'yellow', 'difficulty': 'Yellow Belt', 'area': 'Government', 'method': 'DMAIC', 'title': 'Government IT help-desk resolution time', 'prompt': 'IT help-desk requests take far longer to resolve than the actual work time suggests. Multiple handoffs and unclear intake requirements are suspected contributors.', 'source_url': 'https://goleansixsigma.com/project-example-lean-six-sigma-delivers-64-improvement-in-government-help-desk-resolution-time/', 'source_title': 'Kern County Improved Government Help Desk Resolution Time By 64%'}, {'id': 'cs-san-antonio-payments', 'belt': 'green', 'difficulty': 'Green Belt', 'area': 'Government', 'method': 'DMAIC', 'title': 'Street-maintenance payment processing', 'prompt': 'Contractors report long delays before street-maintenance invoices are paid. Rejected quantities, documentation and approval handoffs are competing explanations.', 'source_url': 'https://goleansixsigma.com/black-belt-project-storyboard-example-task-order-invoicing-process-timing-city-san-antonio/', 'source_title': 'City of San Antonio Improved Street Maintenance Payments By 20%'}, {'id': 'cs-stlouis-bid-tab', 'belt': 'yellow', 'difficulty': 'Yellow Belt', 'area': 'Government', 'method': 'DMAIC', 'title': 'Bid-tabulation cycle time', 'prompt': 'Procurement bid tabs take longer than customers expect, especially for complex bids. Buyers hesitate to escalate roadblocks because of hierarchy and concerns about involving management.', 'source_url': 'https://goleansixsigma.com/project-storyboard-reducing-bid-tab-creation-cycle-time-by-22/', 'source_title': 'City of St. Louis Reduced Bid Tab Creation Cycle Time By 22%'}, {'id': 'cs-fema-disaster', 'belt': 'green', 'difficulty': 'Green Belt', 'area': 'Emergency Response', 'method': 'DMAIC', 'title': 'Natural-disaster response cycle time', 'prompt': 'Emergency-response work is slowed by bottlenecks at distribution centres and relief sites. Staffing shortages and weak coordination across agencies compound the delay.', 'source_url': 'https://goleansixsigma.com/project-storyboard-reducing-cycle-time-for-natural-disaster-response-by-50/', 'source_title': 'Reducing Cycle Time for Natural Disaster Response by 50%'}, {'id': 'cs-food-pantry', 'belt': 'white', 'difficulty': 'White Belt', 'area': 'Nonprofit', 'method': 'DMAIC', 'title': 'Food-box packing flow', 'prompt': 'A food pantry wants to assemble boxes faster without creating congestion. Volunteers, food locations and changing box contents are all affecting flow.', 'source_url': 'https://goleansixsigma.com/lean-six-sigma-helps-feed-people-in-need-45-faster/', 'source_title': 'Lean Six Sigma Helps Feed People In Need 45% Faster'}, {'id': 'cs-first-run-parts', 'belt': 'yellow', 'difficulty': 'Yellow Belt', 'area': 'Manufacturing', 'method': 'DMAIC', 'title': 'First-run parts yield', 'prompt': 'Only 60% of new parts are right the first time. Operators report confusing steps and disorganization, but the business case depends on identifying where the process actually fails.', 'source_url': 'https://goleansixsigma.com/increasing-first-run-parts-60-90/', 'source_title': 'Manufacturer Increased First Run Parts By 30%'}, {'id': 'cs-bsd-scrap', 'belt': 'black', 'difficulty': 'Black Belt', 'area': 'Manufacturing', 'method': 'DMAIC', 'title': 'Bent, scratched and damaged material scrap', 'prompt': 'A material-handling operation is facing rising scrap cost. The team must use defect data, layout analysis and control methods to determine which interventions will change the economics of the process.', 'source_url': 'https://goleansixsigma.com/single-black-belt-project-jump-starts-successful-lean-six-sigma-effort/', 'source_title': 'Manufacturer Reduced Scrap Money Costs By 76%'}, {'id': 'cs-replacement-parts', 'belt': 'white', 'difficulty': 'White Belt', 'area': 'Healthcare', 'method': 'DMAIC', 'title': 'Customer replacement-part lead time', 'prompt': 'Customers are waiting too long for replacement parts. Inventory availability, workload balance and non-value-added checks are all possible sources of delay.', 'source_url': 'https://goleansixsigma.com/reducing-lead-time-customer-replacement-part-orders-41/', 'source_title': 'Reducing Lead Time in Customer Replacement Part Orders By 41%'}, {'id': 'cs-temp-learning', 'belt': 'yellow', 'difficulty': 'Yellow Belt', 'area': 'Manufacturing', 'method': 'DMAIC', 'title': 'Temporary-worker learning curve', 'prompt': 'New temporary workers take too long to reach the expected productivity level. Training, workstation design and follow-up support may all shape the learning curve.', 'source_url': 'https://goleansixsigma.com/reducing-learning-curve-ramp-for-temp-employees-by-2-weeks/', 'source_title': 'Reducing Learning Curve Ramp for Temp Employees by 2 Weeks'}, {'id': 'cs-stuff-sack', 'belt': 'yellow', 'difficulty': 'Yellow Belt', 'area': 'Nonprofit / Manufacturing', 'method': 'DMAIC', 'title': 'Capacity in a parallel production process', 'prompt': 'A mission-driven production operation must increase output while several work streams run in parallel. The challenge is to expose capacity constraints without disrupting the social mission.', 'source_url': 'https://goleansixsigma.com/herding-cats-using-lean-six-sigma-plan-manage-chaos-parallel-processes/', 'source_title': 'Herding Cats Using Lean Six Sigma: How to Plan for and Manage the Chaos of Parallel Processes'}, {'id': 'cs-meat-production', 'belt': 'white', 'difficulty': 'White Belt', 'area': 'Food Processing', 'method': 'DMAIC', 'title': 'Daily meat-production throughput', 'prompt': 'A food-processing plant wants more daily output without losing control of quality or creating unsafe working conditions. The team needs to see the process rather than jump straight to capacity fixes.', 'source_url': 'https://goleansixsigma.com/lean-six-sigma-increases-daily-meat-production-25/', 'source_title': 'Lean Six Sigma Increases Daily Meat Production by 25%'}, {'id': 'cs-miami-housing', 'belt': 'black', 'difficulty': 'Black Belt', 'area': 'Construction / Education', 'method': 'DMADV / IDOV', 'title': 'Designing new student housing', 'prompt': 'A university is designing a new residential concept rather than improving an existing facility. Customer requirements, design choices, cost and verification must be balanced from the outset.', 'source_url': 'https://asq.org/quality-resources/articles/case-studies/designing-new-housing-at-the-university-of-miami-a-six-sigmac-dmadvdfss-case-study', 'source_title': 'Designing New Housing at the University of Miami: A Six Sigma DMADV/DFSS Case Study'}, {'id': 'cs-fishery-procurement', 'belt': 'black', 'difficulty': 'Black Belt', 'area': 'Fisheries / Supply Chain', 'method': 'DMADV / IDOV', 'title': 'Designing a procurement-management tool', 'prompt': 'A fishery company needs a new procurement-management capability that improves material visibility and reliability. The challenge is to define requirements, design the tool and verify it in operations.', 'source_url': 'https://www.researchgate.net/publication/377499925_A_Design_of_Procurement_Managing_Tool_Based_on_the_Lean_Six_Sigma-DMADV_A_Case_Study_of_an_Indonesian_Fishery_Company', 'source_title': 'A Design of Procurement Managing Tool Based on Lean Six Sigma-DMADV'}, {'id': 'cs-hospital-surgical-dmadv', 'belt': 'black', 'difficulty': 'Black Belt', 'area': 'Healthcare', 'method': 'DMADV / IDOV', 'title': 'Designing surgical-instrument picking and staffing', 'prompt': 'A hospital has redesigned surgical-instrument picking and transport and now needs to determine the right human-resource allocation. Process time, workload, staffing and quality must be considered together.', 'source_url': 'https://pubmed.ncbi.nlm.nih.gov/40781857/', 'source_title': 'Improving Hospital Surgical Instrument Picking Processes Through Six Sigma DMADV'}, {'id': 'cs-performance-system-dmadv', 'belt': 'black', 'difficulty': 'Black Belt', 'area': 'Financial Services', 'method': 'DMADV / IDOV', 'title': 'Redesigning performance management', 'prompt': 'A financial-services department cannot achieve its goals with incremental tweaks to the existing performance-management system. The team must redesign the system around stakeholder needs and organizational alignment.', 'source_url': 'https://www.isixsigma.com/case-studies/dmadv-case-study-performance-management-system-redesign/', 'source_title': 'DMADV Case Study: Performance Management System Redesign'}, {'id': 'cs-aerospace-dmadv', 'belt': 'black', 'difficulty': 'Black Belt', 'area': 'Aerospace Manufacturing', 'method': 'DMADV / IDOV', 'title': 'Deploying DMADV in aerospace manufacturing', 'prompt': 'An aerospace manufacturer is introducing a new operating approach and must design for performance, digital integration, sustainability and compliance rather than optimize an established process.', 'source_url': 'https://flevy.com/topic/dmadv/case-dmadv-deployment-leading-aerospace-firms-manufacturing-operations', 'source_title': "DMADV Deployment in a Leading Aerospace Firm's Manufacturing Operations"}]
SCENARIOS.extend(ADDITIONAL_CASE_STUDIES)
# Illustrative chart series used by the interactive case view; these are not source-study measurements.
for _case in ADDITIONAL_CASE_STUDIES:
    _case.setdefault('metrics', {'x': list(range(1, 11)), 'y': [10, 11, 9, 12, 13, 11, 14, 13, 15, 14]})


# Keep glossary presentation deterministic and alphabetical.
GLOSSARY = dict(sorted(GLOSSARY.items(), key=lambda item: item[0].lower()))
