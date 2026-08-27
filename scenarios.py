SCENARIO_DETAIL = {
    "loan-onboarding": {
        "phases": ["define", "measure", "analyze", "improve", "control"],
        "stakeholders": {
            "VP, Commercial Banking": {"role": "Executive sponsor", "opening": "The VP wants visible improvement quickly and believes incomplete submissions are the main issue.", "clues": ["The executive target is a 20% faster cycle time this year.", "The VP is already discussing a digital transformation program with the board."], "incentive": "Visible improvement and a narrative that supports transformation."},
            "Branch Manager": {"role": "Sales leader", "opening": "The Branch Manager says customers are frustrated, but branches are measured on applications submitted.", "clues": ["Branches have a volume incentive that can encourage incomplete applications.", "Managers worry that slower submissions will hurt sales reporting."], "incentive": "Protect branch volume and sales performance."},
            "Underwriter": {"role": "Frontline process owner", "opening": "The Underwriter says missing information creates repeated rework and handoffs.", "clues": ["A recurring set of missing-document issues creates repeat handoffs.", "Underwriters do not control the quality of upstream submissions."], "incentive": "Reduce rework without being blamed for the overall service problem."},
            "Operations Manager": {"role": "Process owner", "opening": "The Operations Manager shows a process with seven handoffs, two queues, and a manual status update.", "clues": ["Queue time accounts for more elapsed cycle time than touch time.", "The status update step exists partly because teams lack a shared workflow view."], "incentive": "Improve service while avoiding uncontrolled operational risk."},
            "Customer": {"role": "Voice of the customer", "opening": "The customer says speed matters, but uncertainty matters almost as much.", "clues": ["Customers value predictable communication, not simply minimum cycle time.", "Customers experience internal handoffs as one combined process."], "incentive": "Receive a fast, predictable, low-effort experience."},
            "Compliance Lead": {"role": "Control function", "opening": "Compliance warns that shortcuts could create documentation and audit risk.", "clues": ["Some controls are mandatory; others are legacy practices that may be redesigned.", "Compliance wants evidence that changes preserve the control objective."], "incentive": "Protect regulatory obligations and auditability."},
        },
        "branch_questions": [
            {"id": "problem", "prompt": "What is the business problem you would define first?", "requires": ["baseline", "customer"], "feedback": "A strong definition separates the customer problem from the assumed internal cause."},
            {"id": "measure", "prompt": "Which measure would you establish before changing the process?", "requires": ["baseline", "process"], "feedback": "You need a stable operational definition and baseline before claiming improvement."},
            {"id": "cause", "prompt": "What evidence would you seek to distinguish rework from queueing as the primary driver?", "requires": ["rework", "queue"], "feedback": "Treat rework and queueing as competing hypotheses until data supports one or both."},
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
            "Technology Lead": {"role": "Technology", "opening": "The Technology Lead says automation is possible only after decision rules are clarified.", "clues": ["Automation can amplify a poorly designed process.", "Some manual checks exist for legitimate risk reasons."], "incentive": "Deliver sustainable technology changes rather than automate chaos."},
            "Quality Manager": {"role": "Quality", "opening": "Quality says the team should distinguish normal variation from special causes.", "clues": ["Not all long claims share the same cause.", "A small number of claim types may account for a large share of misses."], "incentive": "Prevent recurrence with evidence-based controls."},
            "Finance Partner": {"role": "Finance", "opening": "Finance wants a quantified business case and credible benefits mechanism.", "clues": ["Reduced handling time is only a benefit if capacity can be redeployed.", "Avoided cost and released capacity are not automatically cash savings."], "incentive": "Credible benefits capture."},
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
            "CIO": {"role": "Executive sponsor", "opening": "The CIO says high-priority tickets are aging and wants visible improvement in service reliability.", "clues": ["Executive reporting focuses heavily on aging and SLA misses.", "The CIO expects measurable improvement within one quarter."], "incentive": "Service reliability and executive confidence."},
            "Service Desk Manager": {"role": "Process owner", "opening": "The Service Desk Manager says the team is understaffed and classification is inconsistent.", "clues": ["Ticket categories are assigned differently by different agents.", "Staffing is being used as the default explanation for backlog growth."], "incentive": "Protect service capacity and team performance."},
            "Engineer": {"role": "Downstream resolver", "opening": "The Engineer says many escalated tickets are not actually engineering problems and arrive with poor context.", "clues": ["Unclear escalation criteria create avoidable handoffs.", "Engineers lose time clarifying ticket information."], "incentive": "Protect specialist capacity."},
            "Business User": {"role": "Customer", "opening": "The Business User says updates are hard to interpret and the same issue can create multiple tickets.", "clues": ["Users value resolution certainty, not just response speed.", "Duplicate tickets distort the backlog signal."], "incentive": "Fast, understandable service."},
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
    "hospital-discharge": {
        "phases": ["define", "measure", "analyze", "improve", "control"],
        "stakeholders": {
            "Chief Operating Officer": {"role": "Executive sponsor", "opening": "The COO wants shorter discharge delays and believes bed availability is the main issue.", "clues": ["The hospital is under pressure to improve patient flow without increasing staffed beds.", "Executive dashboards emphasize length of stay and bed occupancy."], "incentive": "Patient flow, capacity, and executive commitments."},
            "Nurse Manager": {"role": "Frontline leader", "opening": "The Nurse Manager says patients are often clinically ready, but discharge tasks arrive unpredictably.", "clues": ["Medication reconciliation and paperwork timing create uneven workload.", "Nurses experience discharge work as interruption-heavy."], "incentive": "Safe discharge and manageable frontline workload."},
            "Pharmacist": {"role": "Specialist process owner", "opening": "The Pharmacist says late medication requests create a queue near the end of the process.", "clues": ["Some prescriptions arrive too late for efficient batching.", "The pharmacy queue varies substantially by day and time."], "incentive": "Safe medication release without avoidable expedite work."},
            "Transport Lead": {"role": "Support process owner", "opening": "Transport says demand is clustered and priority rules are not always clear.", "clues": ["Transport requests are not evenly distributed across the day.", "Incomplete readiness signals create wasted trips."], "incentive": "Reliable transport and efficient resource use."},
            "Patient": {"role": "Voice of the patient", "opening": "The patient says the hardest part is waiting without knowing what is happening next.", "clues": ["Predictability matters almost as much as speed.", "Patients experience medication, paperwork, and transport as one combined journey."], "incentive": "Safe, predictable discharge."},
            "Bed Manager": {"role": "Flow coordinator", "opening": "The Bed Manager says delayed discharges make bed assignment harder and create downstream congestion.", "clues": ["A small number of long delays create outsized flow pressure.", "Bed availability is affected by several upstream queues."], "incentive": "Smooth system-wide patient flow."},
            "Physician": {"role": "Clinical decision maker", "opening": "The physician says discharge timing depends on clinical decisions and communication with multiple services.", "clues": ["Late rounds can shift discharge timing.", "Some discharge dependencies are predictable but not visible in a shared workflow."], "incentive": "Clinical safety and efficient care transitions."},
            "Finance Partner": {"role": "Finance", "opening": "Finance wants the benefit translated into capacity, avoided overtime, or other measurable outcomes.", "clues": ["Releasing capacity is economically valuable even if staffed headcount does not immediately fall.", "Benefits need a mechanism and owner."], "incentive": "Credible economic value."},
        },
        "branch_questions": [
            {"id": "problem", "prompt": "How would you define the discharge-delay problem without assuming the cause?", "requires": ["baseline", "patient"], "feedback": "Separate the patient experience and measured delay from the hypothesis about bed capacity."},
            {"id": "queue", "prompt": "Which queues would you measure across the discharge process?", "requires": ["queue", "process"], "feedback": "Map elapsed time into touch, wait, rework, and handoff components."},
            {"id": "variation", "prompt": "What would you segment before changing staffing or scheduling?", "requires": ["variation", "segment"], "feedback": "Time of day, service line, medication requirements, and discharge type may expose different mechanisms."},
        ],
        "decision_options": [
            {"id": "beds", "label": "Add discharge-related bed capacity", "signal": "capacity", "effect": "May improve flow but could treat a downstream symptom rather than the upstream queues."},
            {"id": "workflow", "label": "Redesign the discharge readiness workflow", "signal": "flow", "effect": "Targets visibility, handoffs, and late-stage queueing across services."},
            {"id": "scheduling", "label": "Standardize earlier-day discharge preparation", "signal": "variation", "effect": "Could reduce timing variation but requires clinical and frontline alignment."},
        ],
    },
}
