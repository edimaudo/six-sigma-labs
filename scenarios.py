SCENARIO_DETAIL = {
    "loan-onboarding": {
        "phases": ["define", "measure", "analyze", "improve", "control"],
        "stakeholders": {
            "VP, Commercial Banking": {
                "role": "Executive sponsor",
                "opening": "The VP tells you the headline is simple: commercial loan onboarding is taking too long, and competitors are moving faster.",
                "clues": [
                    "The executive target is a 20% faster cycle time this year.",
                    "The VP is already discussing a digital transformation program with the board.",
                ],
                "incentive": "Wants visible improvement quickly and prefers a narrative that supports the transformation agenda.",
            },
            "Branch Manager": {
                "role": "Sales leader",
                "opening": "The Branch Manager says customers are frustrated, but adds that branches are being measured on applications submitted rather than applications completed correctly.",
                "clues": [
                    "Branches have a volume incentive that can encourage incomplete applications.",
                    "Managers worry that slower submissions will hurt sales reporting.",
                ],
                "incentive": "Protect branch volume and sales performance.",
            },
            "Underwriter": {
                "role": "Frontline process owner",
                "opening": "The Underwriter says applications frequently arrive missing information and that rework is the real source of delay.",
                "clues": [
                    "A recurring set of missing-document issues creates repeat handoffs.",
                    "Underwriters do not control the quality of upstream submissions.",
                ],
                "incentive": "Reduce rework without being blamed for the overall service problem.",
            },
            "Operations Manager": {
                "role": "Process owner",
                "opening": "The Operations Manager shows you a process map. It has seven handoffs, two queues, and a manual status update step.",
                "clues": [
                    "Queue time appears to account for more of the elapsed cycle than touch time.",
                    "The status update step exists partly because teams lack a shared workflow view.",
                ],
                "incentive": "Improve service while avoiding uncontrolled operational risk.",
            },
            "Customer": {
                "role": "Voice of the customer",
                "opening": "The customer says speed matters, but uncertainty matters almost as much. They do not know who owns the application after submission.",
                "clues": [
                    "Customers value predictable communication, not simply the minimum possible cycle time.",
                    "Customers experience internal handoffs as one combined process.",
                ],
                "incentive": "Receive a fast, predictable, low-effort experience.",
            },
            "Compliance Lead": {
                "role": "Control function",
                "opening": "Compliance warns that some proposed shortcuts could create documentation and audit risk.",
                "clues": [
                    "Certain controls are mandatory; others are legacy practices that may be redesigned.",
                    "Compliance wants evidence that any change preserves the control objective.",
                ],
                "incentive": "Protect regulatory obligations and auditability.",
            },
        },
        "branch_questions": [
            {"id": "problem", "prompt": "What is the business problem you would define first?", "requires": ["baseline", "customer"], "feedback": "A good definition separates the customer problem from the assumed internal cause."},
            {"id": "measure", "prompt": "Which measure would you establish before changing the process?", "requires": ["baseline", "process"], "feedback": "You need a stable operational definition and baseline before claiming improvement."},
            {"id": "cause", "prompt": "What evidence would you seek to distinguish rework from queueing as the primary driver?", "requires": ["rework", "queue"], "feedback": "Treat rework and queueing as competing hypotheses until the data supports one or both."},
        ],
        "decision_options": [
            {"id": "automation", "label": "Automate status updates first", "signal": "fast", "effect": "May remove manual effort but does not directly address incomplete upstream submissions."},
            {"id": "submission-quality", "label": "Improve application quality at the branch", "signal": "system", "effect": "Could reduce rework but may conflict with branch volume incentives."},
            {"id": "flow", "label": "Redesign the handoffs and queues", "signal": "flow", "effect": "Targets elapsed time directly but requires coordination across teams and controls."},
        ],
    },
    "claims": {
        "phases": ["define", "measure", "analyze", "improve", "control"],
        "stakeholders": {
            "Claims Director": {"role": "Executive sponsor", "opening": "The Claims Director says cycle time is missing the service target and wants automation considered immediately.", "clues": ["The service target is important for customer retention.", "Leadership is under pressure to show productivity gains."], "incentive": "Visible service and productivity improvement."},
            "Adjuster": {"role": "Process expert", "opening": "The Adjuster says upstream intake quality is creating repeat work and interruptions.", "clues": ["Missing information causes cases to be reopened.", "Adjusters spend time chasing information rather than evaluating claims."], "incentive": "Reduce avoidable rework and interruptions."},
            "Customer": {"role": "Customer", "opening": "The Customer says the biggest frustration is not knowing when the claim will be resolved.", "clues": ["Predictability matters alongside speed.", "Repeated requests for the same information undermine trust."], "incentive": "Fast, predictable resolution."},
            "Technology Lead": {"role": "Technology", "opening": "The Technology Lead says automation is possible, but only after the process and decision rules are clarified.", "clues": ["Automation can amplify a poorly designed process.", "Some manual checks exist for legitimate risk reasons."], "incentive": "Deliver sustainable technology changes rather than automate chaos."},
            "Quality Manager": {"role": "Quality", "opening": "Quality says the team should first distinguish normal variation from special causes.", "clues": ["Not all long claims share the same cause.", "A small number of claim types may account for a large share of misses."], "incentive": "Prevent recurrence with evidence-based controls."},
            "Finance Partner": {"role": "Finance", "opening": "Finance wants a quantified business case and a credible benefits mechanism.", "clues": ["Reduced handling time is only a benefit if capacity can be redeployed.", "Avoided cost and released capacity are not automatically cash savings."], "incentive": "Credible benefits capture."},
        },
        "branch_questions": [
            {"id": "problem", "prompt": "What performance gap should define the problem?", "requires": ["baseline", "customer"], "feedback": "Anchor the project in a measurable service gap and a clear customer outcome."},
            {"id": "variation", "prompt": "Which claim segments would you compare before assuming one root cause?", "requires": ["segment", "variation"], "feedback": "Segmentation can reveal different mechanisms hidden inside one headline metric."},
            {"id": "benefits", "prompt": "How would you test whether productivity improvement becomes a real financial benefit?", "requires": ["capacity", "finance"], "feedback": "Benefits need a mechanism, an owner, and a way to capture them."},
        ],
        "decision_options": [
            {"id": "automation", "label": "Automate intake immediately", "signal": "fast", "effect": "Can improve speed but may encode current intake defects into the new workflow."},
            {"id": "segment", "label": "Segment the claims and target the dominant failure mode", "signal": "data", "effect": "Builds an evidence path before selecting a solution."},
            {"id": "capacity", "label": "Redesign work allocation and controls", "signal": "system", "effect": "May create durable capacity benefits but requires cross-functional alignment."},
        ],
    },
    "service-desk": {
        "phases": ["define", "measure", "analyze", "improve", "control"],
        "stakeholders": {
            "CIO": {"role": "Executive sponsor", "opening": "The CIO says high-priority tickets are aging and wants a visible improvement in service reliability.", "clues": ["Executive reporting focuses heavily on aging and SLA misses.", "The CIO expects measurable improvement within one quarter."], "incentive": "Service reliability and executive confidence."},
            "Service Desk Manager": {"role": "Process owner", "opening": "The Service Desk Manager says the team is understaffed and classification is inconsistent.", "clues": ["Ticket categories are assigned differently by different agents.", "Staffing is being used as the default explanation for backlog growth."], "incentive": "Protect service capacity and team performance."},
            "Engineer": {"role": "Downstream resolver", "opening": "The Engineer says many escalated tickets are not actually engineering problems and arrive with poor context.", "clues": ["Unclear escalation criteria create avoidable handoffs.", "Engineers lose time clarifying ticket information."], "incentive": "Protect specialist capacity."},
            "Business User": {"role": "Customer", "opening": "The Business User says ticket updates are hard to interpret and that the same issue can generate multiple tickets.", "clues": ["Users value resolution certainty, not just response speed.", "Duplicate tickets distort the backlog signal."], "incentive": "Fast, understandable service."},
            "Vendor Manager": {"role": "External partner", "opening": "The Vendor Manager says some ticket classes are tied to third-party SLAs.", "clues": ["External SLA categories may have different economics and constraints.", "Vendor performance data is not aligned cleanly with internal ticket categories."], "incentive": "Clear accountability across partner boundaries."},
            "Risk Partner": {"role": "Risk and controls", "opening": "Risk wants priority definitions and escalation rules to be explicit and auditable.", "clues": ["Priority is currently interpreted differently by teams.", "Controls can be simplified if decision criteria are made explicit."], "incentive": "Consistent, auditable service controls."},
        },
        "branch_questions": [
            {"id": "problem", "prompt": "What exactly is the service problem: backlog size, aging, SLA performance, or something else?", "requires": ["baseline", "customer"], "feedback": "A strong Define phase distinguishes the headline metric from the customer outcome behind it."},
            {"id": "classification", "prompt": "How would you test whether classification inconsistency is materially contributing to aging?", "requires": ["classification", "data"], "feedback": "You need a measurable linkage between classification quality and downstream delay."},
            {"id": "handoffs", "prompt": "What would make you investigate unnecessary escalations as a root cause?", "requires": ["handoff", "evidence"], "feedback": "Trace where tickets wait or change ownership; specialist capacity may be consumed by avoidable flow problems."},
        ],
        "decision_options": [
            {"id": "staffing", "label": "Add service desk staff", "signal": "capacity", "effect": "May relieve pressure without addressing the reasons tickets age or escalate."},
            {"id": "classification", "label": "Redesign classification and escalation rules", "signal": "flow", "effect": "Targets handoff quality and can improve the signal used for workload management."},
            {"id": "priority", "label": "Simplify priority and control rules", "signal": "control", "effect": "Can improve consistency but should be tested against customer outcomes and risk requirements."},
        ],
    },
}
