BELTS = {
    "white": {
        "name": "White Belt",
        "tagline": "Understand the language of improvement.",
        "description": "A practical introduction for anyone who participates in process improvement work.",
        "modules": [
            ("01", "What is Six Sigma?", "Why do organizations care about variation, defects, and process performance?", ["Six Sigma is a disciplined approach to reducing process variation and improving outcomes.", "The goal is not statistics for its own sake; it is better customer and business performance.", "Improvement work starts by defining the problem rather than jumping to a solution."], "Explain Six Sigma to a colleague who thinks it is just a statistics program."),
            ("02", "Process Thinking", "Where does a business result actually come from?", ["A process converts inputs into outputs for a customer or stakeholder.", "Most operational problems are created by a system, not one isolated employee.", "Process thinking makes handoffs, rework, bottlenecks, and variation visible."], "Teach me how you would explain a process to someone new to operations."),
            ("03", "Lean Mindset", "What is the customer actually willing to pay for?", ["Lean focuses on customer value and removing activities that do not create value.", "Common waste categories include defects, waiting, overprocessing, and unnecessary motion.", "Lean and Six Sigma are complementary: Lean improves flow; Six Sigma reduces variation."], "Give me a simple example of waste in an office process."),
            ("04", "DMAIC Overview", "Why would we define a problem before trying to fix it?", ["DMAIC stands for Define, Measure, Analyze, Improve, and Control.", "Each phase answers a different question about the problem.", "The discipline is what prevents teams from confusing symptoms with causes."], "Walk me through DMAIC without using the acronym."),
        ],
    },
    "yellow": {
        "name": "Yellow Belt",
        "tagline": "Participate effectively in improvement projects.",
        "description": "Build the practical skills to map processes, identify waste, support data collection, and contribute to DMAIC projects.",
        "modules": [
            ("01", "Your Role in Six Sigma", "Where do Yellow Belts create value on a project team?", ["Yellow Belts often support process mapping, data collection, problem identification, and implementation.", "They need enough methodology to challenge assumptions and contribute credible evidence.", "Strong team members understand the business context as well as the technical task."], "Teach me how a Yellow Belt adds value without trying to become the project leader."),
            ("02", "SIPOC and Process Mapping", "How do you see a process before measuring it?", ["SIPOC gives a high-level view of suppliers, inputs, process, outputs, and customers.", "A detailed process map exposes decisions, handoffs, queues, rework, and failure points.", "Mapping is a shared understanding exercise, not just documentation."], "Teach me when you would use SIPOC versus a detailed process map."),
            ("03", "VOC and CTQ", "How do you know what 'good' means?", ["Voice of the Customer translates customer needs into measurable requirements.", "Critical-to-Quality characteristics turn broad needs into specific performance measures.", "A process can be internally efficient and still fail the customer."], "Give me an example of turning a vague customer complaint into a CTQ."),
            ("04", "Basic Data and Pareto", "Which problems deserve attention first?", ["Start with a clear operational definition and consistent data collection.", "Pareto analysis helps prioritize categories that contribute materially to a problem.", "A Pareto chart is a prioritization tool, not proof of root cause."], "Explain why a Pareto chart does not tell you what caused the problem."),
            ("05", "Team Dynamics", "What happens when the team agrees on the solution too early?", ["Improvement teams move through predictable stages of formation and conflict.", "RACI clarifies accountability, but it does not remove politics or incentives.", "Good facilitation creates space for evidence and dissent."], "How would you respond when a senior stakeholder shuts down an alternative view?"),
        ],
    },
    "green": {
        "name": "Green Belt",
        "tagline": "Lead structured improvement projects.",
        "description": "Apply DMAIC, Lean, measurement, analysis, improvement, and control methods to real operational problems.",
        "modules": [
            ("01", "Six Sigma and Organizational Goals", "Why should an improvement project exist in the first place?", ["A project should connect a measurable operational problem to a meaningful business or customer outcome.", "Project selection requires trade-offs across impact, urgency, feasibility, and organizational capacity.", "The strongest projects have a sponsor, clear scope, and credible measures."], "Teach me how you would test whether a project is worth doing."),
            ("02", "Define", "What exactly are we trying to improve?", ["Define frames the problem, customer, scope, goal, and business case.", "VOC, CTQ, COPQ, project charters, and stakeholder analysis create alignment.", "A good problem statement describes a gap without embedding an assumed cause."], "Create a problem statement for a process with rising customer complaints."),
            ("03", "Measure", "How do you know the problem is real and how large it is?", ["Measurement establishes the baseline and tests whether the metric itself is trustworthy.", "Key tools include data collection plans, distributions, MSA, and process capability.", "A bad measurement system can make a good analysis useless."], "Explain why you would assess the measurement system before trusting a capability result."),
            ("04", "Analyze", "What evidence would convince you that you found a root cause?", ["Analyze separates plausible explanations from evidence-supported causes.", "Exploratory analysis and hypothesis testing help determine whether differences are meaningful.", "Correlation can be useful for investigation, but it is not automatically causal evidence."], "Defend the difference between a symptom, a correlation, and a root cause."),
            ("05", "Improve", "Which change should the organization actually implement?", ["Improve converts analysis into tested changes rather than intuition-driven fixes.", "DOE, root cause analysis, Lean tools, and solution evaluation help compare alternatives.", "Implementation must account for operational constraints, stakeholder incentives, and risk."], "Explain how you would select between two technically valid solutions."),
            ("06", "Control", "How do you stop the process from returning to its old behavior?", ["Control creates ownership, monitoring, response rules, and standardized work.", "SPC distinguishes normal process variation from signals that deserve investigation.", "A control plan must fit how the process is actually operated."], "Teach me how a control plan creates accountability after a project closes."),
        ],
    },
    "black": {
        "name": "Black Belt",
        "tagline": "Lead complex, cross-functional improvement.",
        "description": "Handle higher-complexity analysis, project portfolios, advanced statistics, and organizational change.",
        "modules": [
            ("01", "Six Sigma Strategy", "How should an organization choose where improvement effort goes?", ["Black Belts connect enterprise goals with a portfolio of measurable improvement opportunities.", "VOC, VOB, and VOE capture different perspectives that can conflict.", "Project economics, sponsor capacity, and strategic fit matter alongside technical feasibility."], "Teach me how you would rank three potential projects with different types of value."),
            ("02", "Project Economics", "How do you know an improvement will create economic value?", ["COPQ, expected benefits, NPV, and benefits capture connect operational changes to finance.", "Benefits need an owner, a baseline, and a credible mechanism for realization.", "A theoretically positive project can still be a poor investment if implementation risk is high."], "Explain how you would challenge an optimistic benefits estimate."),
            ("03", "Advanced Analyze", "What happens when the obvious explanation is wrong?", ["Black Belt analysis may require non-normal distributions, multiple hypotheses, and more sophisticated modelling.", "The analyst must understand assumptions before trusting a test or model.", "Statistical significance is not the same as practical significance."], "Teach me how you would investigate a result that is statistically significant but operationally trivial."),
            ("04", "Regression and DOE", "How can we learn which inputs actually influence an outcome?", ["Regression models relationships between variables; DOE deliberately varies factors to learn about effects.", "Factorial experiments help explore interactions among factors.", "Experimental design is often more informative than observing uncontrolled historical data."], "Explain when you would prefer DOE over regression on existing data."),
            ("05", "Organizational Change", "Why do technically correct improvements fail?", ["Process changes redistribute effort, risk, control, and status.", "Stakeholder incentives and informal power can undermine a technically sound solution.", "Black Belt leadership requires facilitation, negotiation, escalation, and coalition building."], "Give me a plan for implementing a process change opposed by the frontline team."),
            ("06", "Control at Scale", "How do you make improvement durable across a portfolio?", ["Control systems need governance, ownership, metrics, escalation paths, and periodic review.", "SPC and control plans operate at process level; portfolio governance operates at management level.", "Sustained improvement requires both technical control and organizational reinforcement."], "Teach me how process control and management control are different."),
        ],
    },
}

DIAGNOSTIC = [
    {"id": 1, "belt": "white", "question": "A team says a process is 'broken.' What should happen first?", "options": ["Buy a new system", "Define the problem and desired outcome", "Run a t-test", "Train the employees"], "answer": 1},
    {"id": 2, "belt": "yellow", "question": "What does SIPOC provide?", "options": ["A detailed regression model", "A high-level view of a process and its boundaries", "A control chart", "A financial forecast"], "answer": 1},
    {"id": 3, "belt": "yellow", "question": "A Pareto chart primarily helps you do what?", "options": ["Prove causation", "Prioritize categories contributing to a problem", "Calculate NPV", "Replace measurement"], "answer": 1},
    {"id": 4, "belt": "green", "question": "Why assess a measurement system?", "options": ["To make a dashboard look better", "To establish whether the data can be trusted for decisions", "To eliminate variation", "To avoid defining the problem"], "answer": 1},
    {"id": 5, "belt": "green", "question": "Which sequence best represents DMAIC?", "options": ["Define, Measure, Analyze, Improve, Control", "Design, Measure, Automate, Implement, Close", "Define, Model, Approve, Improve, Control", "Discover, Analyze, Measure, Implement, Check"], "answer": 0},
    {"id": 6, "belt": "green", "question": "Which is the strongest evidence of a root cause?", "options": ["A manager's opinion", "A plausible story", "Evidence showing the factor is linked to the outcome and responds predictably when changed", "A Pareto chart alone"], "answer": 2},
    {"id": 7, "belt": "black", "question": "What is a key advantage of designed experiments?", "options": ["They avoid all data", "They deliberately vary factors to learn about effects", "They guarantee a profitable outcome", "They eliminate stakeholder management"], "answer": 1},
    {"id": 8, "belt": "black", "question": "A statistically significant improvement is tiny and operationally irrelevant. What should you conclude?", "options": ["It is automatically a success", "Statistical significance and practical significance are different", "The data must be wrong", "The project should skip Control"], "answer": 1},
]

SCENARIOS = [
    {
        "id": "loan-onboarding",
        "title": "Commercial loan onboarding",
        "area": "Banking",
        "prompt": "Customer onboarding is taking too long. The VP believes branch staff submit incomplete applications, while underwriters blame unclear requirements.",
        "metrics": {"x": [1,2,3,4,5,6,7,8,9,10], "y": [9,11,12,14,16,15,18,20,23,25]},
        "stakeholders": ["VP, Commercial Banking", "Branch Manager", "Underwriter", "Operations Manager", "Customer", "Compliance Lead"],
    },
    {
        "id": "claims",
        "title": "Insurance claims cycle time",
        "area": "Insurance",
        "prompt": "Claims are missing a service target. Operations wants more automation; adjusters say rework is being created upstream.",
        "metrics": {"x": [1,2,3,4,5,6,7,8,9,10], "y": [6,7,9,8,12,11,15,14,17,20]},
        "stakeholders": ["Claims Director", "Adjuster", "Customer", "Technology Lead", "Quality Manager", "Finance Partner"],
    },
    {
        "id": "service-desk",
        "title": "Technology service desk backlog",
        "area": "Technology",
        "prompt": "High-priority tickets are aging. The service desk wants more staff; engineering says ticket classification is creating unnecessary escalation.",
        "metrics": {"x": [1,2,3,4,5,6,7,8,9,10], "y": [42,39,44,48,47,55,61,58,66,70]},
        "stakeholders": ["CIO", "Service Desk Manager", "Engineer", "Business User", "Vendor Manager", "Risk Partner"],
    },
]
