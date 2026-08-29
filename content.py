BELT_ORDER = ["white", "yellow", "green", "black"]


def lesson(code, title, question, concepts, terms=None, math=None, teach_back="Teach the approach back to me in your own words."):
    return {
        "code": code,
        "title": title,
        "opening_question": question,
        "concepts": concepts,
        "terms": terms or [],
        "math": math or [],
        "teach_back": teach_back,
    }


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
            lesson("G01", "Introduction to Six Sigma and Organizational Goals", "Why should an improvement project exist in the first place?", [
                "Six Sigma is an improvement system that connects process performance to business and customer outcomes.",
                "An improvement project should exist because a measurable gap matters to the organization or customer.",
                "Project selection balances impact, urgency, feasibility, and organizational capacity.",
            ], ["business goal", "project selection", "gap"], [], "Explain how an improvement project connects to an organizational goal."),
            lesson("G02", "Six Sigma and Organizational Goals", "How do you prove that a project matters beyond the process metric?", [
                "Translate process measures into business outcomes such as service, cost, risk, revenue, quality, or capacity.",
                "A strong project has a sponsor, clear scope, measurable goals, and a defined benefits mechanism.",
                "Executive urgency should not replace evidence about the actual process problem.",
            ], ["VOB", "business case", "benefits"], [], "Teach me how you would test whether a proposed project is strategically meaningful."),
            lesson("G03", "Lean Principles in the Organization", "Where is work consuming effort without creating customer value?", [
                "Lean emphasizes customer value, flow, pull, respect for people, and continuous improvement.",
                "Use waste categories to identify opportunities for flow and effort reduction.",
                "Lean changes work design and flow; Six Sigma adds disciplined variation reduction and evidence.",
            ], ["Lean", "flow", "pull", "waste", "5S", "TIMWOODS", "DOWNTIME"], [], "Explain how Lean and Six Sigma complement one another."),
            lesson("G04", "Design for Six Sigma (DFSS) Methodologies", "When should quality be designed into a process rather than improved after launch?", [
                "DFSS applies structured quality thinking to new products and processes rather than relying on post-launch correction.",
                "DMADV, also known as IDOV, is an explicit DFSS method for new development: Define, Measure, Analyze, Design, Verify (or Identify, Design, Optimize, Verify).",
                "Use DMADV/IDOV when an existing process cannot be improved adequately through DMAIC because the product or process must be designed or substantially redesigned to meet customer requirements.",
                "Design choices influence downstream variation, failure modes, and customer experience.",
            ], ["DFSS", "DMADV", "IDOV", "design quality"], [], "Teach me when you would choose DFSS instead of DMAIC, and walk me through DMADV/IDOV."),
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
            lesson("B01", "Introduction to Black Belt", "What changes when you move from leading a project to leading improvement capability?", [
                "Black Belts connect project work to enterprise strategy, coaching, governance, and complex problem solving.",
                "The role requires technical depth and the ability to influence across organizational boundaries.",
            ], ["Black Belt", "Master Black Belt", "portfolio", "governance"], [], "Teach me what distinguishes Black Belt work from Green Belt work."),
            lesson("B02", "1.01 Introduction to Define Phase", "Why does advanced improvement still begin with problem framing?", [
                "Complexity increases the need for disciplined problem definition rather than reducing it.",
            ], ["Define", "problem framing"], [], "Explain why Define becomes more important as the problem becomes more complex."),
            lesson("B03", "1.02 Learning Objectives", "How should a Black Belt know what capability a lesson or project is meant to build?", [
                "Learning objectives should be observable and linked to decisions the learner must make in practice.",
            ], ["learning objective", "competency"], [], "Teach me how you would write a useful project competency."),
            lesson("B04", "1.03 Six Sigma", "What is the management problem that Six Sigma is solving?", [
                "Six Sigma creates a disciplined system for reducing variation and improving process outcomes using evidence.",
            ], ["Six Sigma", "variation", "DMAIC"], [], "Teach Six Sigma to an executive in one minute."),
            lesson("B05", "1.04 Lean", "Where does Lean change the operating model rather than just the process map?", [
                "Lean reshapes flow, pull, waste, visibility, and frontline problem solving.",
            ], ["Lean", "flow", "pull", "waste"], [], "Teach me the organizational implication of Lean."),
            lesson("B06", "1.05 Sigma Shift", "What does the sigma shift assumption mean when converting defect data into a sigma level?", [
                "Traditional Six Sigma teaching sometimes uses a long-term 1.5 sigma shift convention when translating short-term performance to a long-term sigma estimate.",
                "The convention is a modelling assumption and should not be treated as a physical law.",
            ], ["sigma level", "1.5 sigma shift", "DPMO"], ["DPMO = defects / (units × opportunities per unit) × 1,000,000."], "Explain the 1.5 sigma shift and why it is an assumption."),
            lesson("B07", "1.06 Yield", "How should yield change the way an executive sees process performance?", [
                "Yield expresses the proportion of units that meet the relevant requirement under the chosen definition.",
                "First-pass yield and rolled throughput yield answer different questions.",
            ], ["yield", "FPY", "RTY"], ["Yield = good units / total units × 100%."], "Explain the difference between first-pass yield and rolled throughput yield."),
            lesson("B08", "1.07 Continuous Improvement Process Evolution", "Why did modern improvement methods evolve beyond inspection?", [
                "Quality thinking progressed from inspection toward statistical control, process improvement, Lean flow, and design for quality.",
            ], ["inspection", "TQM", "continuous improvement"], [], "Tell the story of how improvement methods evolved."),
            lesson("B09", "1.08 Six Sigma Deliverables", "What evidence should exist at the end of a Six Sigma project?", [
                "Deliverables include validated problem definition, baseline, analysis evidence, improvement results, controls, and benefits capture.",
            ], ["deliverable", "baseline", "benefits", "control"], [], "Teach me what makes a project deliverable decision-useful."),
            lesson("B10", "1.09 Problem Solving Strategy", "How do you choose the right level of analysis for a complex problem?", [
                "Start with the decision, then determine the evidence, method, and precision needed.",
                "More sophisticated analysis is not automatically better analysis.",
            ], ["problem solving", "evidence", "method selection"], [], "Explain how you choose between simple and advanced analysis."),
            lesson("B11", "1.10 VOC Campaign", "What would you learn from customers that internal metrics cannot tell you?", [
                "A VOC campaign systematically gathers customer needs, expectations, friction, and priorities across relevant segments.",
            ], ["VOC campaign", "segment", "customer journey"], [], "Teach me how you would design a VOC campaign."),
            lesson("B12", "1.11 VOC Tools", "Which VOC tool would give you the strongest evidence for a CTQ?", [
                "Interviews, surveys, complaint analysis, observation, journey mapping, and Kano can be combined depending on the decision.",
            ], ["VOC tools", "Kano", "journey map", "survey"], [], "Choose two VOC tools and explain why."),
            lesson("B13", "1.12 VOB", "What does the business need that the customer may not articulate?", [
                "Voice of the Business captures strategic, economic, operational, and risk requirements.",
            ], ["VOB", "strategy", "economics"], [], "Teach me how VOB can conflict with VOC."),
            lesson("B14", "1.13 VOE", "Why should employee experience be part of process improvement?", [
                "Voice of the Employee surfaces workarounds, friction, capability constraints, and adoption barriers.",
            ], ["VOE", "frontline", "adoption"], [], "Explain why VOE matters to improvement results."),
            lesson("B15", "1.14 KANO Analysis", "Which customer needs create dissatisfaction when missing versus delight when exceeded?", [
                "Kano distinguishes basic, performance, and attractive qualities, helping prioritize customer requirements.",
            ], ["Kano", "must-be", "performance", "attractive"], [], "Teach me how Kano can change feature priorities."),
            lesson("B16", "1.15 Six Sigma Roles and Responsibilities", "Who owns the project when the project team crosses organizational boundaries?", [
                "Roles clarify sponsorship, leadership, analysis, process ownership, subject matter expertise, and change support.",
            ], ["Champion", "Master Black Belt", "Black Belt", "Green Belt", "Yellow Belt"], [], "Explain how roles prevent ownership ambiguity."),
            lesson("B17", "1.16 Project Champion and Master Black Belt", "What should leaders do that analysts cannot do alone?", [
                "Champions align strategy, remove barriers, provide sponsorship, and ensure benefits are realized.",
                "Master Black Belts provide coaching, methods, governance, and capability building across projects.",
            ], ["Champion", "Master Black Belt", "governance", "escalation"], [], "Teach me the difference between a Champion and a Master Black Belt."),
            lesson("B18", "1.17 Black Belt and Yellow Belt", "How should responsibility change across belt levels?", [
                "Yellow Belts contribute to project execution; Black Belts lead more complex analysis and cross-functional improvement.",
            ], ["Yellow Belt", "Green Belt", "Black Belt"], [], "Explain how you would delegate project work across belt levels."),
            lesson("B19", "1.18 Drivers of Six Sigma", "What organizational forces make Six Sigma succeed or fail?", [
                "Strategy, leadership, customer pressure, economics, capability, data quality, culture, and governance all drive adoption.",
            ], ["drivers", "culture", "leadership", "governance"], [], "Teach me the strongest organizational drivers of Six Sigma."),
            lesson("B20", "1.19 Key Takeaways", "What principles from Define should govern the rest of the project?", [
                "A Black Belt should be able to connect customer, business, employee, technical, and financial perspectives before committing resources.",
            ], ["Define", "VOC", "VOB", "VOE", "charter"], [], "Summarize the Define principles you would carry into Measure."),
            lesson("B21", "2.01 Learning Objectives", "What should a Black Belt be able to do with the fundamentals?", ["Fundamentals should produce practical decisions, not passive recall."], ["competency"], [], "Teach me how you would assess mastery of fundamentals."),
            lesson("B22", "2.02 Process", "What exactly is the system that creates the result?", ["A process has inputs, activities, decisions, outputs, controls, customers, and variation."], ["process", "input", "output", "control"], [], "Teach me how to describe a process as a system."),
            lesson("B23", "2.03 Project Charter", "What commitments must be made before analysis begins?", ["A charter defines the problem, goal, scope, team, milestones, and business case."], ["charter", "scope", "goal"], [], "Teach me what a complete charter needs."),
            lesson("B24", "2.04 Critical to Quality (CTQ)", "How do you turn customer language into measurable requirements?", ["CTQs are measurable characteristics linked to customer requirements."], ["CTQ", "VOC", "specification"], [], "Teach me how to derive a CTQ from VOC."),
            lesson("B25", "2.05 Cost of Poor Quality (COPQ)", "What does poor quality actually cost the organization?", ["COPQ includes costs associated with defects, rework, inspection, failures, complaints, and related losses depending on the business context."], ["COPQ", "internal failure", "external failure"], [], "Teach me how COPQ changes project prioritization."),
            lesson("B26", "2.06 Calculating COPQ", "Which costs would you include and which would you challenge?", ["Build a traceable cost model with units, frequency, unit cost, and a mechanism for realization."], ["COPQ", "cost driver", "benefits"], ["Basic COPQ = frequency × cost per occurrence; extend for labor, material, customer impact, and other relevant components."], "Walk me through a defensible COPQ calculation."),
            lesson("B27", "2.07 Pareto Analysis (80-20 rule)", "How does Pareto thinking help you allocate improvement effort?", ["Pareto prioritizes categories by contribution and helps focus investigation."], ["Pareto", "vital few", "trivial many"], ["Cumulative percentage is the running sum of category percentage contributions."], "Teach me why Pareto is not a causal analysis."),
            lesson("B28", "2.08 Basic Six Sigma Metrics", "Which metric would best represent the problem you are managing?", ["Metrics can include DPU, DPO, DPMO, yield, sigma level, cycle time, capability, and defect rates depending on the process."], ["DPU", "DPO", "DPMO", "yield", "sigma"], ["DPU = defects / units.", "DPO = defects / (units × opportunities).", "DPMO = DPO × 1,000,000."], "Teach me how you would choose a Six Sigma metric."),
            lesson("B29", "2.09 Key Takeaways", "What should a business-ready Six Sigma fundamental always connect back to?", ["Every metric should support a decision, a baseline, or a measurable outcome."], ["metrics", "business case"], [], "Teach me the core fundamentals to a project sponsor."),
            lesson("B30", "3.01 Learning Objectives", "What should project-selection capability enable you to decide?", ["The learner should be able to compare opportunities and select projects with credible strategic and economic value."], ["project selection"], [], "Teach me the project-selection competency."),
            lesson("B31", "3.02 Selecting Lean Six Sigma Projects", "Which candidate problem deserves a project?", ["Screen projects for strategic alignment, impact, urgency, feasibility, controllability, and sponsor readiness."], ["project selection", "screening"], [], "Teach me a project-selection framework."),
            lesson("B32", "3.03 Project Selection Roadmap", "How can an organization standardize project selection without creating bureaucracy?", ["Use a staged funnel from opportunity identification through business case, feasibility, sponsorship, and approval."], ["roadmap", "portfolio", "funnel"], [], "Teach me a lightweight selection roadmap."),
            lesson("B33", "3.04 Project Charter: Elements", "What information must every project charter contain?", ["Core elements include business case, problem, goal, scope, team, milestones, measures, risks, and benefits."], ["charter", "scope", "milestones"], [], "Teach me the minimum viable charter."),
            lesson("B34", "3.05 Project Charter: Business Case", "Why should anyone spend scarce resources on this problem?", ["The business case explains consequences, value at stake, urgency, and expected return or risk reduction."], ["business case", "value"], [], "Teach me how to make a business case evidence based."),
            lesson("B35", "3.06 Project Charter: Problem Statement", "What does a good problem statement exclude?", ["A problem statement should exclude assumed causes, preferred solutions, and blame."], ["problem statement", "cause", "scope"], [], "Give me a strong problem statement and explain why it works."),
            lesson("B36", "3.07 Project Charter: Goal Statement", "How precise should a project goal be?", ["A goal should be specific, measurable, time-bound, and linked to the baseline and customer or business requirement."], ["goal", "baseline", "target"], ["Improvement % = (baseline − new value) / baseline × 100% when lower is better."], "Teach me how to write a measurable goal."),
            lesson("B37", "3.08 Project Charter: Scope", "What should be kept out of the project?", ["Scope defines boundaries so the project remains solvable and ownership remains clear."], ["scope", "in-scope", "out-of-scope"], [], "Teach me how scope protects a project."),
            lesson("B38", "3.09 Project Charter: Key Milestones", "Which milestones prove that the project is learning something important?", ["Milestones should correspond to decisions, validated deliverables, and phase exits."], ["milestone", "phase gate"], [], "Teach me how to build evidence-based milestones."),
            lesson("B39", "3.10 Project Charter: Team Selection", "Who must be on the team because they own information, decisions, or implementation?", ["Select people based on process knowledge, analysis skills, authority, customer perspective, and implementation responsibility."], ["team selection", "SME", "process owner"], [], "Teach me how you would select a cross-functional team."),
            lesson("B40", "3.11 Tuckman's Stages of Team Formation", "How should a Black Belt respond when a team enters conflict?", ["Forming, storming, norming, and performing describe common team-development dynamics."], ["Tuckman", "storming", "performing"], [], "Teach me how you would lead a team through storming."),
            lesson("B41", "3.12 The RACI and RASIC Matrix", "Where does accountability become ambiguous on a cross-functional project?", ["RACI/RASIC clarifies who performs, owns, supports, is consulted, and is informed."], ["RACI", "RASIC", "accountability"], [], "Teach me how RACI resolves an ownership conflict."),
            lesson("B42", "3.13 Expected Financial Benefits", "What makes a financial benefit credible?", ["A credible benefit has a baseline, causal mechanism, calculation, owner, timing, and capture method."], ["benefits", "baseline", "capture"], [], "Teach me how to challenge an optimistic benefit estimate."),
            lesson("B43", "3.14 Developing Project Metrics", "Which measures prove the project is improving the problem without creating perverse incentives?", ["Use outcome, process, and balancing measures where necessary."], ["CTQ", "KPI", "balancing measure"], [], "Teach me how to design a useful metric set."),
            lesson("B44", "3.15 Key Performance Indicator KPI", "When does a KPI help management and when does it distort behavior?", ["A KPI should align with the desired outcome, be controllable enough to manage, and resist gaming."], ["KPI", "leading indicator", "lagging indicator"], [], "Teach me how a KPI can create unintended behavior."),
            lesson("B45", "3.16 Financial Evaluation and Benefits Capture", "How do you distinguish projected benefits from realized benefits?", ["Benefits capture requires operational change, financial validation, ownership, and evidence that the result persisted."], ["benefits capture", "realization", "finance"], [], "Teach me how you would govern benefits capture."),
            lesson("B46", "3.17 Net Present Value NPV", "Why can two projects with the same nominal benefit have different economic value?", ["NPV accounts for the timing of cash flows and the required return."], ["NPV", "discount rate", "cash flow"], ["NPV = Σ CF_t/(1+r)^t − initial investment."], "Teach me NPV without assuming a finance audience already understands it."),
            lesson("B47", "3.18 Key Takeaways", "What makes a project financially and operationally credible?", ["Strong projects connect strategy, customer need, problem definition, measurement, economics, and ownership."], ["charter", "business case", "NPV"], [], "Summarize the project-leadership fundamentals."),
            lesson("B48", "4.01 Learning Objectives", "What should enterprise Lean capability allow leaders to see and change?", ["The learner should recognize waste, flow constraints, and organizational mechanisms that sustain performance."], ["Lean"], [], "Teach me the Lean leadership competency."),
            lesson("B49", "4.02 Lean", "What is Lean trying to optimize from the customer's perspective?", ["Lean seeks to maximize customer value while minimizing delay, effort, and waste."], ["Lean", "value"], [], "Teach me Lean in operational terms."),
            lesson("B50", "4.03 Principles of Lean", "How do value, flow, pull, and perfection change process decisions?", ["The Lean principles guide teams from customer value to smooth flow, demand-driven work, and continuous improvement."], ["value", "flow", "pull", "perfection"], [], "Teach me the four core Lean principles."),
            lesson("B51", "4.04 Lean Methodology", "How does a Lean improvement cycle differ from a purely analytical project?", ["Lean emphasizes observation, flow, visual management, standard work, rapid experimentation, and frontline involvement."], ["Lean methodology", "Kaizen", "standard work"], [], "Teach me what a Lean improvement cycle looks like."),
            lesson("B52", "4.05 Lean and Six Sigma", "When does a problem require Lean, Six Sigma, or both?", ["Use Lean for flow and waste problems, Six Sigma for variation and defect problems, and both when the mechanisms interact."], ["Lean Six Sigma", "flow", "variation"], [], "Teach me how you would choose between Lean and Six Sigma."),
            lesson("B53", "4.06 3Ms of Lean", "What do Muda, Mura, and Muri reveal that one waste checklist cannot?", ["Muda is waste, Mura is unevenness, and Muri is overburden. Together they explain unstable flow and excess effort."], ["Muda", "Mura", "Muri"], [], "Teach me the 3Ms using one operations example."),
            lesson("B54", "4.07 Categories of Waste TIMWOODS", "Which wastes are hidden inside apparently productive work?", ["TIMWOODS covers Transportation, Inventory, Motion, Waiting, Overproduction, Overprocessing, Defects, and Skills/non-used talent."], ["TIMWOODS"], [], "Teach me TIMWOODS using a service process."),
            lesson("B55", "4.08 Category of Waste DOWNTIME", "Why are multiple waste mnemonics useful if they name the same underlying ideas?", ["DOWNTIME is another mnemonic for common Lean wastes: defects, overproduction, waiting, non-utilized talent, transportation, inventory, motion, extra processing."], ["DOWNTIME"], [], "Compare TIMWOODS and DOWNTIME."),
            lesson("B56", "4.09 5S", "How can workplace organization change process performance?", ["5S creates visible standards for sort, set in order, shine, standardize, and sustain."], ["5S"], [], "Teach me why 5S is a control mechanism, not just housekeeping."),
            lesson("B57", "4.10 Steps in 5S: Part One", "What should be removed or organized before a team attempts standardization?", ["Sort, set in order, and shine create a stable baseline for the work environment."], ["sort", "set in order", "shine"], [], "Teach me the first three 5S steps."),
            lesson("B58", "4.11 Steps in 5S: Part Two", "How do standards become daily behavior?", ["Standardize and sustain turn the first three steps into routines, visual controls, and management discipline."], ["standardize", "sustain"], [], "Teach me how to sustain 5S after the initial event."),
            lesson("B59", "4.12 Key Takeaways", "What does Lean reveal about the design of work?", ["Lean makes value, flow, waste, unevenness, and overburden explicit."], ["Lean", "3Ms", "5S"], [], "Summarize the Lean enterprise principles."),
            lesson("B60", "4.13 Activity", "Where would you look for waste before changing the process?", ["Observe the work, compare demand with flow, identify queues, defects, rework, and unnecessary movement."], ["Gemba", "waste", "flow"], [], "Teach me how you would run a Lean observation."),
            lesson("B61", "4.14 Solution", "What would a strong Lean solution change about the work itself?", ["Solutions should remove the mechanism of waste and make the preferred flow easier to execute and sustain."], ["countermeasure", "standard work", "flow"], [], "Defend a Lean countermeasure against a skeptical operator."),
            # Measure
            lesson("B62", "Measure 01: Process Definition", "Which process boundaries must be fixed before you can measure performance?", ["Define start/end points, units, customer, failure definition, and segmentation before collecting data."], ["process definition", "CTQ", "operational definition"], [], "Teach me how you would establish a measurable process boundary."),
            lesson("B63", "Measure 02: Six Sigma Statistics", "Which statistics are enough to answer the operational question?", ["Use descriptive statistics to summarize center, spread, shape, and variation; inferential methods answer population questions."], ["mean", "variance", "standard deviation", "confidence interval"], ["Variance = Σ(x−x̄)^2/(n−1) for a sample.", "Standard error of the mean = s/√n."], "Teach me the statistics you actually need for Measure."),
            lesson("B64", "Measure 03: Measurement System Analysis", "How much of what you see is the process and how much is measurement?", ["Evaluate repeatability, reproducibility, bias, stability, and resolution where appropriate."], ["MSA", "Gauge R&R", "bias"], [], "Teach me when a Gauge R&R is useful."),
            lesson("B65", "Measure 04: Process Capability", "Can the current process consistently meet the customer's specifications?", ["Capability compares process spread and centering to specification limits after confirming stability and appropriate assumptions."], ["Cp", "Cpk", "Pp", "Ppk"], ["Cp=(USL−LSL)/(6σ).", "Cpk=min[(USL−μ)/(3σ),(μ−LSL)/(3σ)]."], "Teach me when Ppk and Cpk answer different questions."),
            # Analyze
            lesson("B66", "Analyze 01: Classes of Distribution", "How does distribution class influence your analytical choice?", ["Distribution type affects assumptions, visual diagnostics, and which test or model is appropriate."], ["normal", "binomial", "Poisson", "Weibull"], [], "Teach me why distribution choice matters."),
            lesson("B67", "Analyze 02: Inferential Statistics", "How can a sample support a conclusion about a larger process?", ["Inferential statistics uses sample evidence to estimate or test population parameters under stated assumptions."], ["estimator", "confidence interval", "inference"], ["A 95% confidence interval is typically estimate ± critical value × standard error."], "Teach me what a confidence interval means in business language."),
            lesson("B68", "Analyze 03: Hypothesis Testing", "What claim are you actually testing?", ["State H0 and H1, choose alpha, select an appropriate test, assess assumptions, and interpret practical importance."], ["H0", "H1", "alpha", "power", "p-value"], ["Type I error = rejecting a true H0; Type II error = failing to reject a false H0."], "Teach me the logic of hypothesis testing step by step."),
            lesson("B69", "Analyze 04: Hypothesis Testing with Normal Data", "How does normality support common parametric tests?", ["When assumptions are reasonable, tests based on normal or t distributions can be efficient and interpretable."], ["t-test", "z-test", "ANOVA", "normality"], ["One-sample t statistic: t=(x̄−μ0)/(s/√n)."], "Teach me when you would use a t-test."),
            lesson("B70", "Analyze 05: Hypothesis Testing with Non Normal Data", "What should you do when your data does not meet normal assumptions?", ["Consider transformation, nonparametric tests, appropriate count models, or robust methods based on the process question."], ["nonparametric", "Mann-Whitney", "Kruskal-Wallis", "transformation"], [], "Teach me how you would respond to non-normal data without forcing a normal model."),
            # Improve
            lesson("B71", "Improve 01: Simple Linear Regression", "How can one input help explain variation in an outcome?", ["Simple regression estimates the relationship between one predictor and a continuous response, while checking assumptions and practical usefulness."], ["regression", "slope", "intercept", "R²"], ["Simple regression: Y=β0+β1X+ε.", "R² is the proportion of response variation explained by the fitted model in the sample."], "Teach me what the slope means operationally."),
            lesson("B72", "Improve 02: Multiple Regression Analysis", "What changes when several process inputs influence the outcome at the same time?", ["Multiple regression estimates adjusted relationships while considering other included predictors and potential interactions."], ["multiple regression", "coefficient", "multicollinearity", "residual"], ["Multiple regression: Y=β0+β1X1+...+βkXk+ε."], "Teach me why correlation among predictors can make interpretation difficult."),
            lesson("B73", "Improve 03: Designed Experiments", "How can you learn causality rather than only observe association?", ["Designed experiments manipulate factors under a planned structure to estimate effects and interactions."], ["DOE", "factor", "level", "response"], ["A treatment effect is the estimated change in response associated with changing a factor under the experimental design."], "Teach me the difference between observational regression and DOE."),
            lesson("B74", "Improve 04: Factorial Experiments", "Why would you vary factors together instead of one at a time?", ["Factorial designs estimate main effects and interactions efficiently across combinations of factor levels."], ["factorial", "main effect", "interaction"], ["For two factors, interaction means the effect of one factor depends on the level of the other."], "Teach me what an interaction means in an operations setting."),
            lesson("B75", "Improve 05: Improve Implementation Tools and Techniques", "What makes an improvement survive contact with the real organization?", ["Implementation uses pilots, change plans, stakeholder alignment, training, standard work, risk controls, and benefits tracking."], ["implementation", "change management", "pilot", "adoption"], [], "Teach me how you would move from statistical improvement to operational adoption."),
            # Control
            lesson("B76", "Control 01: Lean Controls", "How can Lean controls make the improved process easier to sustain?", ["Standard work, visual management, daily management, mistake proofing, and 5S can embed expected behavior."], ["Lean controls", "standard work", "visual management", "poka-yoke"], [], "Teach me how Lean controls support sustainability."),
            lesson("B77", "Control 02: Statistical Process Control", "How do you know when a process signal deserves intervention?", ["SPC uses time-ordered data and control rules to distinguish routine variation from special-cause signals."], ["SPC", "control limits", "special cause", "Western Electric rules"], ["Three-sigma control limits are designed around the expected distribution of a monitored statistic under stable conditions."], "Teach me how control charts support management decisions."),
            lesson("B78", "Control 03: Six Sigma Control Plans", "How should technical control and management governance reinforce one another?", ["Control plans specify measures, ownership, thresholds, reactions, documentation, and review mechanisms."], ["control plan", "governance", "reaction plan", "audit"], [], "Teach me how you would design a control plan for a critical CTQ."),
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
    {
        "name": "Mean",
        "formula": "x̄ = Σx / n",
        "explanation": "The arithmetic average of the observed values. It is sensitive to unusually large or small observations.",
        "variables": [
            "x = an individual observed value",
            "x̄ = the sample mean",
            "n = the number of observations in the sample",
            "Σ = sum across all observations"
        ],
    },
    {
        "name": "Median",
        "formula": "Middle ordered value",
        "explanation": "The middle value after observations are sorted. With an even number of observations, it is the average of the two middle values.",
        "variables": ["No algebraic variables are required for this definition."]
    },
    {
        "name": "Sample variance",
        "formula": "s² = Σ(x − x̄)² / (n − 1)",
        "explanation": "Measures the squared dispersion of sample observations around their sample mean.",
        "variables": [
            "s² = sample variance",
            "x = an individual observed value",
            "x̄ = the sample mean",
            "n = the number of observations in the sample",
            "Σ = sum across all observations"
        ],
    },
    {
        "name": "Sample standard deviation",
        "formula": "s = √s²",
        "explanation": "The square root of sample variance; it expresses spread in the original units of measurement.",
        "variables": [
            "s = sample standard deviation",
            "s² = sample variance",
            "√ = square-root operation"
        ],
    },
    {
        "name": "Z-score",
        "formula": "z = (x − μ) / σ",
        "explanation": "Expresses how far an observation is from the population mean in standard-deviation units.",
        "variables": [
            "z = standardized score",
            "x = observed value",
            "μ = population mean",
            "σ = population standard deviation"
        ],
    },
    {
        "name": "Standard error of the mean",
        "formula": "SE = s / √n",
        "explanation": "Estimates the sampling variability of a sample mean.",
        "variables": [
            "SE = standard error of the sample mean",
            "s = sample standard deviation",
            "n = sample size",
            "√ = square-root operation"
        ],
    },
    {
        "name": "95% confidence interval",
        "formula": "estimate ± critical value × SE",
        "explanation": "Builds an interval around a sample estimate using a critical value appropriate to the chosen confidence level and statistical method.",
        "variables": [
            "estimate = the sample estimate of the population quantity of interest",
            "critical value = value determined by the confidence level and statistical distribution",
            "SE = standard error of the estimate",
            "± = add and subtract the margin from the estimate"
        ],
    },
    {
        "name": "Binomial probability",
        "formula": "P(X = k) = C(n,k)pᵏ(1 − p)ⁿ⁻ᵏ",
        "explanation": "Models the probability of exactly k successes in n independent trials when each trial has the same success probability p.",
        "variables": [
            "P(X = k) = probability of exactly k successes",
            "X = number of successes across the trials",
            "k = target number of successes",
            "n = total number of independent trials",
            "p = probability of success on each trial",
            "C(n,k) = number of ways to choose k successes from n trials",
            "1 − p = probability of failure on each trial"
        ],
    },
    {
        "name": "Poisson probability",
        "formula": "P(X = k) = e⁻λ λᵏ / k!",
        "explanation": "Models the probability of observing exactly k events in a fixed interval when the Poisson assumptions are appropriate.",
        "variables": [
            "P(X = k) = probability of exactly k events",
            "X = event count in the interval",
            "k = observed event count of interest",
            "λ = expected number of events in the interval",
            "e = Euler's number, approximately 2.71828",
            "k! = factorial of k"
        ],
    },
    {
        "name": "Defects per opportunity",
        "formula": "DPO = defects / (units × opportunities per unit)",
        "explanation": "Normalizes defects by the number of opportunities for a defect to occur.",
        "variables": [
            "DPO = defects per opportunity",
            "defects = total counted defects",
            "units = total units processed",
            "opportunities per unit = number of potential defect opportunities on each unit"
        ],
    },
    {
        "name": "Defects per million opportunities",
        "formula": "DPMO = DPO × 1,000,000",
        "explanation": "Expresses defects per opportunity on a one-million-opportunity scale.",
        "variables": [
            "DPMO = defects per million opportunities",
            "DPO = defects per opportunity",
            "1,000,000 = scaling factor to one million opportunities"
        ],
    },
    {
        "name": "Yield",
        "formula": "Yield = good units / total units × 100%",
        "explanation": "The percentage of units that meet the defined acceptance rule.",
        "variables": [
            "Yield = percentage of units that pass the defined acceptance rule",
            "good units = units meeting the defined acceptance rule",
            "total units = all units considered",
            "100% = converts the proportion to a percentage"
        ],
    },
    {
        "name": "Cp",
        "formula": "Cp = (USL − LSL) / (6σ)",
        "explanation": "Measures potential process capability by comparing specification width with estimated process spread, without accounting for process centering.",
        "variables": [
            "Cp = potential process capability index",
            "USL = upper specification limit",
            "LSL = lower specification limit",
            "σ = process standard deviation",
            "6σ = six standard deviations representing the process spread convention used in the index"
        ],
    },
    {
        "name": "Cpk",
        "formula": "Cpk = min[(USL − μ)/(3σ), (μ − LSL)/(3σ)]",
        "explanation": "Measures capability while accounting for the distance between the process mean and the nearest specification limit.",
        "variables": [
            "Cpk = centered process capability index",
            "USL = upper specification limit",
            "LSL = lower specification limit",
            "μ = process mean",
            "σ = process standard deviation",
            "min = select the smaller of the two capability ratios"
        ],
    },
    {
        "name": "Simple regression",
        "formula": "Y = β₀ + β₁X + ε",
        "explanation": "Represents a linear model relating one predictor to a response.",
        "variables": [
            "Y = response variable being modeled",
            "X = predictor or explanatory variable",
            "β₀ = estimated intercept of the fitted line",
            "β₁ = estimated slope for X",
            "ε = model error or unexplained residual component"
        ],
    },
    {
        "name": "Multiple regression",
        "formula": "Y = β₀ + β₁X₁ + … + βₖXₖ + ε",
        "explanation": "Models a response using multiple predictors while estimating a coefficient for each predictor.",
        "variables": [
            "Y = response variable",
            "β₀ = intercept",
            "βⱼ = estimated coefficient for predictor j",
            "Xⱼ = value of predictor j",
            "k = total number of predictors",
            "ε = model error or unexplained residual component",
            "j = index identifying a predictor from 1 through k"
        ],
    },
    {
        "name": "CUSUM",
        "formula": "Cₜ = max(0, Cₜ₋₁ + xₜ − target − k)",
        "explanation": "Accumulates deviations from a target to make persistent shifts in a process easier to detect. Exact CUSUM forms vary by chart design.",
        "variables": [
            "Cₜ = current cumulative-sum statistic",
            "Cₜ₋₁ = previous cumulative-sum statistic",
            "xₜ = current observed process value",
            "target = target or reference process value",
            "k = reference or allowance constant used by the selected CUSUM design",
            "t = time or observation index",
            "max(0, …) = resets the one-sided statistic at zero when the accumulated evidence becomes negative"
        ],
    },
    {
        "name": "EWMA",
        "formula": "Zₜ = λXₜ + (1 − λ)Zₜ₋₁",
        "explanation": "Weights the current observation and the prior smoothed value to detect gradual shifts.",
        "variables": [
            "Zₜ = current EWMA statistic",
            "Xₜ = current observed process value",
            "Zₜ₋₁ = prior EWMA statistic",
            "λ = smoothing constant between 0 and 1; larger values give more weight to the latest observation",
            "t = time or observation index"
        ],
    },
    {
        "name": "Correlation",
        "formula": "r = cov(X,Y) / (sₓsᵧ)",
        "explanation": "Measures standardized linear association between two variables. It does not establish causation.",
        "variables": [
            "r = correlation coefficient",
            "X = first variable",
            "Y = second variable",
            "cov(X,Y) = sample covariance between X and Y",
            "sₓ = sample standard deviation of X",
            "sᵧ = sample standard deviation of Y"
        ],
    },
    {
        "name": "R-squared",
        "formula": "R² = 1 − SSE / SST",
        "explanation": "Describes the proportion of sample response variation represented by the fitted regression model.",
        "variables": [
            "R² = coefficient of determination",
            "SSE = sum of squared residual errors from the fitted model",
            "SST = total sum of squares measuring total response variation"
        ],
    },
    {
        "name": "Two-level factorial combinations",
        "formula": "2ᵏ",
        "explanation": "Counts the treatment combinations in a full factorial experiment with two levels for each factor.",
        "variables": [
            "k = number of factors",
            "2 = number of levels for each factor"
        ],
    },
    {
        "name": "PCA variance share",
        "formula": "variance shareⱼ = eigenvalueⱼ / Σ eigenvalues",
        "explanation": "Shows the share of total scaled variance represented by principal component j.",
        "variables": [
            "variance shareⱼ = proportion of total represented variance for component j",
            "eigenvalueⱼ = eigenvalue associated with principal component j",
            "j = index identifying the principal component",
            "Σ eigenvalues = sum of the eigenvalues retained or considered"
        ],
    },
    {
        "name": "Net present value",
        "formula": "NPV = Σ[CFₜ / (1 + r)ᵗ] − initial investment",
        "explanation": "Measures the present value of future cash flows after discounting them and subtracting the initial investment.",
        "variables": [
            "NPV = net present value",
            "CFₜ = net cash flow received in period t",
            "t = period number",
            "r = discount rate per period",
            "initial investment = cash outflow at the start of the project",
            "Σ = sum across the project periods"
        ],
    },
]

# Every lesson-level math entry is normalized to the same structure used by the glossary.
# The mapping is deliberately exact so a displayed equation always has a visible variable glossary.
MATH_VARIABLES_BY_FORMULA = {
    "Variation is the spread of observed process outcomes around a central tendency.": ["No algebraic variables are used; this is a conceptual definition."],
    "A defect is a failure to meet a defined customer or process requirement.": ["No algebraic variables are used; this is a conceptual definition."],
    "Cycle time is elapsed time from a defined start to a defined end of a process.": ["No algebraic variables are used; this is a conceptual definition."],
    "A value-adding activity changes the product or service in a way the customer needs and is willing to pay for.": ["No algebraic variables are used; this is a conceptual definition."],
    "Pareto percentage = category frequency / total frequency × 100.": ["category frequency = count in the selected category", "total frequency = total count across all categories", "100 = percentage conversion factor"],
    "Mean = sum of observations / number of observations.": ["sum of observations = total of all observed values", "number of observations = sample size"],
    "Standard deviation describes the spread of observations around the mean.": ["No algebraic variables are used; this is a conceptual definition."],
    "P(A) is the probability of event A.": ["P(A) = probability that event A occurs", "A = the event whose probability is being evaluated"],
    "Expected value for a discrete variable: E(X) = Σ x·P(X=x).": ["E(X) = expected value of random variable X", "X = discrete random variable", "x = a possible value of X", "P(X=x) = probability that X equals x", "Σ = sum across all possible values of X"],
    "IQR = Q3 − Q1.": ["IQR = interquartile range", "Q3 = third quartile, the 75th percentile", "Q1 = first quartile, the 25th percentile"],
    "Coefficient of variation = standard deviation / mean, when the ratio is meaningful.": ["coefficient of variation = standardized measure of relative spread", "standard deviation = measure of spread in the original units", "mean = arithmetic average"],
    "Normal density: f(x)=1/(σ√(2π))·e^{-(x−μ)^2/(2σ²)}.": ["f(x) = normal probability density at x", "x = observed value", "μ = population mean", "σ = population standard deviation", "π = mathematical constant pi", "e = Euler's number, approximately 2.71828"],
    "Binomial probability: P(X=k)=C(n,k)p^k(1-p)^{n-k}.": ["P(X=k) = probability of exactly k successes", "X = number of successes", "k = target number of successes", "n = number of trials", "p = probability of success on each trial", "C(n,k) = number of combinations of k successes among n trials"],
    "Gauge R&R separates measurement variation from process variation for suitable measurement contexts.": ["No algebraic variables are used; this is a conceptual statement about measurement-system analysis."],
    "Cp = (USL−LSL)/(6σ).": ["Cp = potential capability index", "USL = upper specification limit", "LSL = lower specification limit", "σ = process standard deviation"],
    "Cpk = min[(USL−μ)/(3σ),(μ−LSL)/(3σ)].": ["Cpk = centered capability index", "USL = upper specification limit", "LSL = lower specification limit", "μ = process mean", "σ = process standard deviation", "min = the smaller of the two capability ratios"],
    "Z-score = (x−μ)/σ.": ["Z-score = standardized distance from the mean", "x = observed value", "μ = population mean", "σ = population standard deviation"],
    "Two-sided z statistic: z=(x̄−μ0)/(σ/√n).": ["z = standardized test statistic", "x̄ = sample mean", "μ₀ = hypothesized population mean under the null hypothesis", "σ = population standard deviation or known standard deviation used by the test", "n = sample size"],
    "Approximate two-sided 95% CI: estimate ± 1.96×standard error.": ["estimate = sample estimate of the population quantity", "1.96 = approximate 97.5th percentile of the standard normal distribution for a two-sided 95% interval", "standard error = estimated sampling variability of the estimate"],
    "A simple factorial model can be written Y = β0 + β1X1 + β2X2 + β12X1X2 + ε.": ["Y = response variable", "β₀ = intercept", "β₁ = coefficient for factor X₁", "β₂ = coefficient for factor X₂", "β₁₂ = interaction coefficient for X₁ and X₂", "X₁ = first factor level encoded numerically", "X₂ = second factor level encoded numerically", "ε = experimental error"],
    "For an individuals chart, limits are typically center line ± 3×estimated process standard deviation, with chart-specific constants used in practice.": ["center line = estimated process center or mean", "3 = conventional three-sigma multiplier", "estimated process standard deviation = estimated within-process spread", "limits = control limits calculated for the selected chart method"],
    "DPMO = defects / (units × opportunities per unit) × 1,000,000.": ["DPMO = defects per million opportunities", "defects = total counted defects", "units = total units processed", "opportunities per unit = potential defect opportunities on each unit", "1,000,000 = scaling factor"],
    "Yield = good units / total units × 100%.": ["Yield = percentage of acceptable units", "good units = units meeting the acceptance rule", "total units = all units considered", "100% = percentage conversion factor"],
    "Basic COPQ = frequency × cost per occurrence; extend for labor, material, customer impact, and other relevant components.": ["frequency = number of occurrences", "cost per occurrence = estimated cost of each occurrence", "COPQ = cost of poor quality under the defined scope"],
    "Cumulative percentage is the running sum of category percentage contributions.": ["cumulative percentage = running total of category percentages", "category percentage = category contribution divided by total contribution × 100%"],
    "DPU = defects / units.": ["DPU = defects per unit", "defects = total counted defects", "units = total units processed"],
    "DPO = defects / (units × opportunities).": ["DPO = defects per opportunity", "defects = total counted defects", "units = total units processed", "opportunities = defect opportunities per unit"],
    "DPMO = DPO × 1,000,000.": ["DPMO = defects per million opportunities", "DPO = defects per opportunity", "1,000,000 = scaling factor"],
    "Improvement % = (baseline − new value) / baseline × 100% when lower is better.": ["Improvement % = percentage improvement", "baseline = starting performance level", "new value = performance after improvement", "100% = percentage conversion factor"],
    "NPV = Σ CF_t/(1+r)^t − initial investment.": ["NPV = net present value", "CF_t = net cash flow in period t", "t = period number", "r = discount rate per period", "initial investment = starting cash outflow", "Σ = sum across periods"],
    "Variance = Σ(x−x̄)^2/(n−1) for a sample.": ["Variance = sample variance", "x = observed value", "x̄ = sample mean", "n = sample size", "Σ = sum across observations"],
    "Standard error of the mean = s/√n.": ["standard error of the mean = estimated sampling variability of the mean", "s = sample standard deviation", "n = sample size"],
    "A 95% confidence interval is typically estimate ± critical value × standard error.": ["estimate = sample estimate", "critical value = value determined by confidence level and statistical distribution", "standard error = estimated sampling variability of the estimate"],
    "Type I error = rejecting a true H0; Type II error = failing to reject a false H0.": ["H₀ = null hypothesis", "Type I error = rejecting H₀ when H₀ is true", "Type II error = failing to reject H₀ when H₀ is false"],
    "One-sample t statistic: t=(x̄−μ0)/(s/√n).": ["t = one-sample t test statistic", "x̄ = sample mean", "μ₀ = hypothesized population mean under H₀", "s = sample standard deviation", "n = sample size"],
    "Simple regression: Y=β0+β1X+ε.": ["Y = response variable", "β₀ = intercept", "β₁ = slope coefficient", "X = predictor variable", "ε = model error or residual"],
    "R² is the proportion of response variation explained by the fitted model in the sample.": ["R² = coefficient of determination", "response variation = variation in the observed response values", "fitted model = estimated regression relationship"],
    "Multiple regression: Y=β0+β1X1+...+βkXk+ε.": ["Y = response variable", "β₀ = intercept", "βⱼ = coefficient for predictor j", "Xⱼ = predictor j", "k = number of predictors", "ε = model error or residual", "j = predictor index"],
    "A treatment effect is the estimated change in response associated with changing a factor under the experimental design.": ["treatment effect = estimated change in the response attributable to a factor change under the design", "response = measured outcome", "factor = experimental input being changed"],
    "For two factors, interaction means the effect of one factor depends on the level of the other.": ["factor 1 = first experimental input", "factor 2 = second experimental input", "interaction = dependence of one factor's effect on the level of the other factor"],
    "Three-sigma control limits are designed around the expected distribution of a monitored statistic under stable conditions.": ["three-sigma = three estimated standard deviations from the center under the selected chart assumptions", "control limits = statistical boundaries for identifying unusual process behavior", "monitored statistic = value plotted on the control chart"],
}

def _math_item(formula):
    for item in MATH_REFERENCE:
        if item["formula"] == formula:
            return dict(item)
    return {
        "name": formula,
        "formula": formula,
        "explanation": "See the glossary for the method-specific explanation.",
        "variables": MATH_VARIABLES_BY_FORMULA.get(formula, ["No variables are used in this statement."]),
    }

for _belt in BELTS.values():
    for _module in _belt["modules"]:
        _normalized_math = []
        for _formula in _module.get("math", []):
            _item = _math_item(_formula)
            if _formula in MATH_VARIABLES_BY_FORMULA:
                _item["variables"] = MATH_VARIABLES_BY_FORMULA[_formula]
            _normalized_math.append(_item)
        _module["math"] = _normalized_math


# Belt-level assessment: 10 questions. It is a starting-point check, not a certification exam.
DIAGNOSTIC = [
    {"id": 1, "belt": "white", "question": "A team says a process is broken. What should happen first?", "options": ["Buy a new system", "Define the problem and desired outcome", "Run a hypothesis test", "Train employees"], "answer": 1},
    {"id": 2, "belt": "white", "question": "Which statement best describes process thinking?", "options": ["Problems are usually caused by one person", "A process transforms inputs into outputs for a customer or stakeholder", "Every process problem requires advanced statistics", "A written procedure is always the same as the actual process"], "answer": 1},
    {"id": 3, "belt": "yellow", "question": "What does SIPOC provide?", "options": ["A regression model", "A high-level view of process boundaries, inputs and outputs", "A control chart", "A project financial forecast"], "answer": 1},
    {"id": 4, "belt": "yellow", "question": "A Pareto chart primarily helps a team do what?", "options": ["Prove causation", "Prioritize categories contributing to the observed problem", "Calculate process capability", "Replace measurement"], "answer": 1},
    {"id": 5, "belt": "green", "question": "Why assess a measurement system before analyzing process data?", "options": ["To make dashboards look better", "To establish whether the measurement can be trusted for the decision", "To eliminate process variation", "To avoid defining the problem"], "answer": 1},
    {"id": 6, "belt": "green", "question": "Which statement about process capability is correct?", "options": ["Capability ignores specification limits", "Capability compares a stable process with defined specifications", "Capability is the same as a control limit", "Capability proves root cause"], "answer": 1},
    {"id": 7, "belt": "green", "question": "What is the strongest evidence for a root cause?", "options": ["A manager's opinion", "A plausible story", "Evidence showing a repeatable relationship and response when the factor changes", "A Pareto chart alone"], "answer": 2},
    {"id": 8, "belt": "black", "question": "What is a key advantage of a designed experiment?", "options": ["It avoids the need for a response variable", "It deliberately varies factors to learn about effects and interactions", "It guarantees a positive business result", "It eliminates stakeholder management"], "answer": 1},
    {"id": 9, "belt": "black", "question": "Why can a statistically significant result still be a poor business decision?", "options": ["Statistical analysis is never useful", "Statistical significance and practical significance are different", "A p-value guarantees implementation success", "Control is unnecessary after significance"], "answer": 1},
    {"id": 10, "belt": "black", "question": "When is DMADV/IDOV more appropriate than DMAIC?", "options": ["When an existing process only needs routine monitoring", "When a new product or process must be designed or substantially redesigned", "When a control chart has a special-cause signal", "When the team wants to avoid customer requirements"], "answer": 1},
]


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




# Keep glossary presentation deterministic and alphabetical.
GLOSSARY = dict(sorted(GLOSSARY.items(), key=lambda item: item[0].lower()))
