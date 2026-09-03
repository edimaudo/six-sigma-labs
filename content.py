BELT_ORDER = ["white", "yellow", "green", "black"]

MATH_REFERENCE = [
    {"name":"Mean","formula":"x̄ = Σx / n","explanation":"Average of observed values; sensitive to extreme values.","variables":"x = each observed value; n = number of observations; Σ = sum of all observed values; x̄ = sample mean."},
    {"name":"Median","formula":"Median = middle value of ordered observations","explanation":"Robust measure of center when data is skewed.","variables":"n = number of observations; observations are ordered from smallest to largest. For even n, the median is the average of the two middle observations."},
    {"name":"Sample variance","formula":"s² = Σ(x − x̄)² / (n − 1)","explanation":"Measures squared dispersion around the sample mean.","variables":"x = each observed value; x̄ = sample mean; n = number of observations; Σ = sum across observations; s² = sample variance."},
    {"name":"Sample standard deviation","formula":"s = √s²","explanation":"Expresses process spread in the original measurement units.","variables":"s = sample standard deviation; s² = sample variance; √ = square-root operation."},
    {"name":"Z-score","formula":"z = (x − μ) / σ","explanation":"Number of standard deviations an observation is from the population mean.","variables":"z = standardized score; x = observed value; μ = population mean; σ = population standard deviation."},
    {"name":"Standard error of mean","formula":"SE = s / √n","explanation":"Estimates the sampling variability of the sample mean.","variables":"SE = standard error of the sample mean; s = sample standard deviation; n = sample size."},
    {"name":"95% confidence interval","formula":"estimate ± critical value × SE","explanation":"Quantifies uncertainty around a population estimate under the specified confidence level and statistical method.","variables":"estimate = sample-based point estimate; critical value = value from the relevant reference distribution; SE = standard error; ± = lower and upper interval bounds."},
    {"name":"Binomial probability","formula":"P(X = k) = C(n, k) p^k (1 − p)^(n − k)","explanation":"Models the probability of exactly k successes across n fixed independent trials with constant success probability.","variables":"X = number of successes; k = specified successes; n = number of trials; p = probability of success; C(n,k) = combinations of n items taken k at a time; 1 − p = probability of failure."},
    {"name":"Poisson probability","formula":"P(X = k) = e^(−λ) λ^k / k!","explanation":"Models counts occurring over a fixed interval when a Poisson process is an appropriate assumption.","variables":"X = event count; k = specified count; λ = expected event count in the interval; e = Euler's number; k! = factorial of k."},
    {"name":"DPO","formula":"DPO = defects / (units × opportunities)","explanation":"Normalizes defects by the number of defect opportunities.","variables":"DPO = defects per opportunity; defects = number of defects; units = units processed; opportunities = defect opportunities per unit."},
    {"name":"DPMO","formula":"DPMO = DPO × 1,000,000","explanation":"Expresses defects per opportunity on a one-million-opportunity basis.","variables":"DPMO = defects per million opportunities; DPO = defects per opportunity; 1,000,000 = one million opportunities."},
    {"name":"Yield","formula":"Yield = good units / total units","explanation":"Share of units meeting the defined acceptance rule.","variables":"Yield = proportion of acceptable units; good units = units meeting the acceptance requirement; total units = all units evaluated."},
    {"name":"Cp","formula":"Cp = (USL − LSL) / (6σ)","explanation":"Potential process capability based on specification width relative to process variation, without accounting for centering.","variables":"Cp = potential capability index; USL = upper specification limit; LSL = lower specification limit; σ = process standard deviation."},
    {"name":"Cpk","formula":"Cpk = min[(USL − μ)/(3σ), (μ − LSL)/(3σ)]","explanation":"Capability index that accounts for both process spread and process centering.","variables":"Cpk = centered capability index; USL = upper specification limit; LSL = lower specification limit; μ = process mean; σ = process standard deviation; min = smaller of the two one-sided capability values."},
    {"name":"Simple regression","formula":"Y = β₀ + β₁X + ε","explanation":"Models a linear relationship between one predictor and a response.","variables":"Y = response variable; β₀ = intercept; β₁ = slope coefficient; X = predictor variable; ε = random error term."},
    {"name":"Multiple regression","formula":"Y = β₀ + ΣβⱼXⱼ + ε","explanation":"Models a response using multiple predictors.","variables":"Y = response; β₀ = intercept; βⱼ = coefficient for predictor j; Xⱼ = predictor j; ε = random error; Σ = sum across predictors."},
    {"name":"CUSUM","formula":"Cₜ = max(0, Cₜ₋₁ + xₜ − target − k)","explanation":"Cumulative evidence for a sustained process shift; exact form depends on the chart design.","variables":"Cₜ = current cumulative sum; Cₜ₋₁ = previous cumulative sum; xₜ = current observation or subgroup statistic; target = process target; k = reference/allowance value."},
    {"name":"EWMA","formula":"Zₜ = λXₜ + (1 − λ)Zₜ₋₁","explanation":"Exponentially weighted monitoring statistic that gives more weight to recent observations.","variables":"Zₜ = current EWMA statistic; λ = smoothing constant between 0 and 1; Xₜ = current observation; Zₜ₋₁ = previous EWMA value."},
    {"name":"Correlation","formula":"r = cov(X, Y) / (sₓ sᵧ)","explanation":"Standardized measure of linear association; correlation alone does not establish causation.","variables":"r = correlation coefficient; cov(X,Y) = covariance between X and Y; sₓ = sample standard deviation of X; sᵧ = sample standard deviation of Y."},
    {"name":"R-squared","formula":"R² = 1 − SSE / SST","explanation":"Proportion of sample response variation explained by the fitted regression model.","variables":"R² = coefficient of determination; SSE = sum of squared errors; SST = total sum of squares."},
    {"name":"Factorial combinations","formula":"Number of combinations = 2^k","explanation":"Number of treatment combinations in a two-level full factorial experiment with k factors.","variables":"k = number of factors; 2 = number of levels per factor; 2^k = total treatment combinations."},
    {"name":"PCA variance share","formula":"Variance shareⱼ = eigenvalueⱼ / Σ eigenvalues","explanation":"Share of total scaled variance represented by principal component j.","variables":"Variance shareⱼ = proportion represented by component j; eigenvalueⱼ = eigenvalue for component j; Σ eigenvalues = sum of all included eigenvalues."},
    {"name":"NPV","formula":"NPV = Σ[CFₜ / (1 + r)^t] − initial investment","explanation":"Discounted economic value of a project based on the timing of cash flows.","variables":"NPV = net present value; CFₜ = cash flow in period t; r = discount rate per period; t = time period; initial investment = upfront cash outflow; Σ = sum across periods."},
]

def lesson(code, title, question, concepts, terms=None, math=None, teach_back="Teach the approach back to me in your own words."):
    resolved_math = []
    if math:
        for math_name in math:
            for ref in MATH_REFERENCE:
                if ref["name"] == math_name:
                    resolved_math.append(ref)
                    break

    return {
        "code": code,
        "title": title,
        "opening_question": question,
        "concepts": concepts,
        "terms": terms or [],
        "math": resolved_math,
        "teach_back": teach_back,
    }

BELTS = {'white': {'name': 'White Belt',
           'tagline': 'Understand the language of improvement.',
           'description': 'Learn the core language, mindset, process thinking, and DMAIC logic used in Six Sigma work.',
           'modules': [{'code': 'W01',
                        'title': 'What Is Six Sigma, and Why Does It Matter?',
                        'opening_question': 'Think of the last time you got frustrated with a product or service that '
                                            "didn't work the way it was supposed to. Why do you think that happened?",
                        'concepts': ['**Six Sigma** is a structured way of finding the real cause of a mistake and '
                                     "fixing it so it doesn't keep happening.",
                                     "A **defect** is simply anything that doesn't meet what the customer expects — it "
                                     "doesn't have to be dramatic to count.",
                                     "Quality isn't an accident. It comes from understanding how work actually gets "
                                     'done, not just hoping people are careful.',
                                     '**Socratic prompt:** If a mistake happens once, is it bad luck? What if it '
                                     'happens the same way, over and over?',
                                     "You don't need a technical title to notice a problem — everyone doing the work "
                                     'sees things that "experts" often miss.'],
                        'terms': ['Six Sigma', 'Defect', 'Quality'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain, in plain language, what Six Sigma is trying to achieve',
                                                'Describe why organizations care about reducing mistakes and '
                                                'inconsistency',
                                                'Recognize that Six Sigma is a way of thinking about work, not just a '
                                                'toolkit for specialists'],
                        'full_explanation': 'Most people have a story like the one in the opening question — an order '
                                            'that came out wrong, a form that had to be resubmitted three times, a '
                                            "delivery that showed up late without warning. These aren't random bad "
                                            'luck. Somewhere in the process that produced that outcome, something '
                                            "happened consistently enough to cause the problem — a step that's "
                                            'confusing, a handoff that loses information, a machine that drifts out of '
                                            'adjustment. Six Sigma exists because most quality problems are not '
                                            "one-off accidents; they're the predictable output of how a process is "
                                            'actually built and run.\n'
                                            '\n'
                                            'The name "Six Sigma" comes from a statistical idea — you don\'t need the '
                                            'math to get the point — that says: the more consistent a process is, the '
                                            "fewer defects it produces. A company committed to Six Sigma isn't just "
                                            "hoping employees try harder. It's committing to actually study its "
                                            'processes, find out where and why things go wrong, and fix the real cause '
                                            'instead of just apologizing and moving on.\n'
                                            '\n'
                                            'This matters to you even if you never run a project yourself. A workplace '
                                            'that takes this seriously is one where your frustrations with a broken '
                                            'process are treated as useful information, not something to just '
                                            "tolerate. And you're often the person best positioned to notice the "
                                            "problem in the first place, because you're the one actually doing the "
                                            'work — not reading about it in a report.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What is a "defect" in Six Sigma terms?',
                                             'options': [{'key': 'a',
                                                          'text': "Anything that doesn't meet what the customer "
                                                                  'expects, big or small',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'Only a serious safety failure',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Only something a customer complains about in '
                                                                  'writing',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Only a mistake made by a new employee',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 2,
                                             'question': 'Why does Six Sigma treat repeated mistakes as more than "bad '
                                                         'luck"?',
                                             'options': [{'key': 'a',
                                                          'text': 'Because a repeated problem usually points to a '
                                                                  'consistent, fixable cause in how the work is done',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'Because repeated mistakes are always caused by one '
                                                                  'careless employee',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "Because bad luck can't be measured",
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Because repeated mistakes only happen in factories',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 3,
                                             'question': 'Why might someone doing the day-to-day work notice a problem '
                                                         'before a manager or expert does?',
                                             'options': [{'key': 'a',
                                                          'text': "Because they're the ones actually experiencing the "
                                                                  'process firsthand',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'Because managers are never allowed to see the '
                                                                  'process',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Because Six Sigma only applies to frontline work',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Because experts don't care about quality",
                                                          'correct': False}],
                                             'answer': 'a'}],
                        'summary': ['Six Sigma is a structured way to find and fix the real cause of mistakes.',
                                    'A defect is anything that fails to meet customer expectations — not just dramatic '
                                    'failures.',
                                    'Quality comes from understanding the process, not just asking people to try '
                                    'harder.',
                                    'Anyone doing the work can spot a real problem, whether or not they lead the fix.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Module 1: Six Sigma Foundations'},
                       {'code': 'W02',
                        'title': 'What Is Lean? Waste and Value in Everyday Work',
                        'opening_question': 'Have you ever spent more time looking for something — a tool, a form, an '
                                            'email — than you actually spent using it once you found it? What did that '
                                            'feel like?',
                        'concepts': ['**Value** is anything the customer actually wants and would be willing to pay '
                                     'for (directly or indirectly).',
                                     "**Waste** is everything else — time, effort, or motion that doesn't move the "
                                     'work forward.',
                                     'Common everyday waste: waiting for something, searching for something, redoing '
                                     'something that was done wrong, and doing more than what was actually needed.',
                                     '**Socratic prompt:** Is being busy the same thing as being productive?'],
                        'terms': ['Value', 'Waste'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Define "value" and "waste" in plain, everyday terms',
                                                'Recognize common examples of waste in your own work',
                                                'Explain why removing waste benefits both customers and employees'],
                        'full_explanation': '"Lean" is a way of looking at work and asking one simple question: does '
                                            'this step actually help the customer, or is it just something we do '
                                            "because that's how it's always been done? Anything that doesn't help the "
                                            'customer is waste — even if it looks like effort, and even if everyone '
                                            'involved is genuinely busy doing it.\n'
                                            '\n'
                                            'You\'ve probably experienced this without calling it "Lean." Searching '
                                            "for a misplaced tool or file is waste — the customer doesn't care that "
                                            'you had to search, they just want the result. Waiting for an approval, a '
                                            'delivery, or someone else to finish their part is waste — nothing is '
                                            'being added to the product or service during that wait. Redoing something '
                                            'because it was done incorrectly the first time is waste — the customer is '
                                            'paying (in time, cost, or trust) for the same work twice. And doing more '
                                            'than what was actually asked for — extra steps, extra approvals, extra '
                                            'polish nobody requested — is waste too, even though it can feel like '
                                            '"going above and beyond."\n'
                                            '\n'
                                            "Here's the key mindset shift: removing waste isn't about making people "
                                            "work harder or faster. It's usually about making the work itself simpler "
                                            '— fewer unnecessary steps, less searching, fewer redos — which tends to '
                                            'make the job less frustrating for the person doing it, not more '
                                            'demanding. A calmer, simpler process that removes waste is often better '
                                            'for the employee and the customer at the same time, which is part of why '
                                            'Lean thinking tends to stick once people actually try it.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Which of the following best describes "waste" in Lean '
                                                         'thinking?',
                                             'options': [{'key': 'a',
                                                          'text': "Any time or effort spent on something that doesn't "
                                                                  'actually help the customer',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'Only physical scrap thrown away',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Any task that takes more than five minutes',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Only mistakes made by new employees',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 2,
                                             'question': 'Why is "searching for a misplaced tool or file" considered '
                                                         'waste, even though it takes effort?',
                                             'options': [{'key': 'a',
                                                          'text': 'Because the customer only cares about the result, '
                                                                  'not the time spent searching for it',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': "Because searching is always the employee's fault",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "Because it doesn't count unless it happens every "
                                                                  'day',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Because Lean only applies to factory work',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 3,
                                             'question': 'Why might removing waste actually make a job feel *less* '
                                                         'stressful, not more demanding?',
                                             'options': [{'key': 'a',
                                                          'text': 'Because it usually means fewer unnecessary steps '
                                                                  'and less searching or redoing work, not working '
                                                                  'harder',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'Because it means doing the same work faster with no '
                                                                  'other changes',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Because it removes all quality checks',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Because it eliminates the need for teamwork',
                                                          'correct': False}],
                                             'answer': 'a'}],
                        'summary': ['Value is what the customer actually wants; waste is everything else.',
                                    'Everyday waste includes waiting, searching, redoing work, and doing more than '
                                    'needed.',
                                    "Removing waste usually simplifies the work itself — it's not about working "
                                    'harder.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Module 1: Six Sigma Foundations'},
                       {'code': 'W03',
                        'title': 'Understanding the Voice of the Customer',
                        'opening_question': 'If your manager asked you to improve a process, but never asked the '
                                            'people actually using it what they wanted, what might go wrong?',
                        'concepts': ['A **customer** is anyone receiving the result of your work — this can be an '
                                     'external, paying customer, or an **internal customer** (the next person or '
                                     'department in line).',
                                     '**Voice of the Customer (VOC)** means finding out what people actually need, '
                                     'instead of assuming you already know.',
                                     'Simple ways VOC gets collected: asking directly, listening to complaints, '
                                     "observing how something is actually used, or reviewing feedback that's already "
                                     'been recorded.',
                                     '**Socratic prompt:** If you never see the end buyer of the product, who is your '
                                     'customer?'],
                        'terms': ['Customer', 'Internal Customer', 'Voice of the Customer (VOC)'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain what "Voice of the Customer" means at a basic level',
                                                'Recognize why listening to customers — internal or external — matters '
                                                'before making changes',
                                                'Identify a few simple ways an organization gathers the Voice of the '
                                                'Customer'],
                        'full_explanation': "It's easy to assume you already know what the people relying on your work "
                                            "actually want — especially if you've done the job for a while. But "
                                            'assumptions are exactly what "Voice of the Customer" is designed to '
                                            'replace with real information.\n'
                                            '\n'
                                            "A customer doesn't have to be an outside buyer. If you hand off paperwork "
                                            'to another department, that department is your **internal customer** — '
                                            'and if what you hand them is incomplete or hard to use, they experience '
                                            'that the same way an external customer experiences a bad product. Six '
                                            'Sigma treats both kinds of customers seriously, because a process can '
                                            'fail its internal customers long before it ever reaches the person paying '
                                            'for the final result.\n'
                                            '\n'
                                            "Gathering VOC doesn't require a formal research department. It can be as "
                                            "simple as asking someone directly what's frustrating about a process, "
                                            'paying attention to recurring complaints instead of dismissing them as '
                                            'one-offs, watching how a form or tool is actually used (which is often '
                                            'different from how it was designed to be used), or reviewing feedback '
                                            "that's already been written down somewhere — a returns log, a help-desk "
                                            "ticket queue, a suggestion box. The point isn't the sophistication of the "
                                            "method; it's making sure changes are based on what people actually need, "
                                            'rather than what seems reasonable from a distance.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What is an "internal customer"?',
                                             'options': [{'key': 'a',
                                                          'text': 'The next person or department that receives the '
                                                                  "result of your work, even if they're not the end "
                                                                  'buyer',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'Someone who works in the same building as you',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'A customer who only exists in manufacturing',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'A customer who has complained more than once',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 2,
                                             'question': 'Why does Six Sigma emphasize actually gathering VOC instead '
                                                         'of assuming you already know what people need?',
                                             'options': [{'key': 'a',
                                                          'text': 'Because assumptions can be wrong, and acting on a '
                                                                  'wrong assumption can make a process worse, not '
                                                                  'better',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'Because VOC is only useful for external customers',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Because assumptions are always illegal to use',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Because gathering VOC replaces the need for any '
                                                                  'other data',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 3,
                                             'question': 'Which of these is a simple, everyday way to gather VOC?',
                                             'options': [{'key': 'a',
                                                          'text': 'Reviewing a help-desk ticket queue for recurring '
                                                                  'complaints',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'Only reading a formal market research report',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Guessing based on what worked at a different '
                                                                  'company',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Skipping it if the process seems fine on the '
                                                                  'surface',
                                                          'correct': False}],
                                             'answer': 'a'}],
                        'summary': ['A customer can be external or internal — anyone receiving the result of your '
                                    'work.',
                                    'VOC means finding out real needs instead of assuming you already know them.',
                                    'Simple, everyday methods (asking, listening, observing, reviewing existing '
                                    'feedback) are enough to start gathering VOC.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Module 1: Six Sigma Foundations'},
                       {'code': 'W04',
                        'title': 'A Quick Look at DMAIC',
                        'opening_question': 'If you wanted to improve something at home — say, your morning routine — '
                                            'would you just guess at a fix, or would you first figure out exactly '
                                            "what's slowing you down?",
                        'concepts': ['**Define** — what exactly is the problem, and why does it matter?',
                                     '**Measure** — how big is the problem, really, and how do we know?',
                                     '**Analyze** — why is this actually happening?',
                                     '**Improve** — what change will fix the real cause?',
                                     '**Control** — how do we make sure the fix sticks?',
                                     '**Socratic prompt:** Why might jumping straight to "Improve" — skipping Define, '
                                     "Measure, and Analyze — lead to a fix that doesn't actually work?"],
                        'terms': ['DMAIC', 'Define', 'Measure', 'Analyze', 'Improve', 'Control'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Name the five phases of DMAIC, in order',
                                                'Describe, in one sentence, what each phase is trying to accomplish',
                                                'Understand DMAIC as a structured way to solve problems, without '
                                                'needing statistics at this level'],
                        'full_explanation': 'Imagine you decide your morning routine is too rushed and you want to fix '
                                            'it. If you skip straight to a "fix" — say, waking up 20 minutes earlier — '
                                            'you might solve nothing, because you never actually figured out *why* '
                                            'mornings feel rushed in the first place. Maybe the real problem is that '
                                            'you spend 15 minutes every morning looking for your keys. DMAIC is a '
                                            'structured way to avoid that kind of guessing.\n'
                                            '\n'
                                            '**Define** means getting specific about the problem before doing anything '
                                            'else — not "mornings are stressful," but "I\'m consistently 10 minutes '
                                            'late leaving the house on weekdays." **Measure** means confirming how big '
                                            'the problem actually is with real information, not just a feeling — '
                                            'tracking your actual departure time for two weeks, for example. '
                                            "**Analyze** means digging into *why* it's happening — maybe every late "
                                            "day involves searching for keys, and every on-time day doesn't. "
                                            '**Improve** means making a change aimed at that specific cause — putting '
                                            'a hook by the door for your keys, rather than a generic "try harder" fix. '
                                            '**Control** means making sure the fix actually holds up over time — '
                                            "checking in a month later to confirm you're still using the hook, not "
                                            'slipping back into old habits.\n'
                                            '\n'
                                            "You'll notice each phase builds on the one before it. Skipping ahead — "
                                            'especially jumping straight to "Improve" without Define, Measure, and '
                                            'Analyze — is exactly how organizations end up implementing fixes that '
                                            "don't actually address the real cause, and the original problem quietly "
                                            'comes back a few months later.',
                        'knowledge_check': [{'number': 1,
                                             'question': "What is the correct order of DMAIC's five phases?",
                                             'options': [{'key': 'a',
                                                          'text': 'Define, Measure, Analyze, Improve, Control',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'Measure, Define, Analyze, Control, Improve',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Define, Analyze, Measure, Control, Improve',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Analyze, Define, Measure, Improve, Control',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 2,
                                             'question': 'What is the main purpose of the "Analyze" phase?',
                                             'options': [{'key': 'a',
                                                          'text': 'To figure out why the problem is actually happening',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'To decide who is at fault',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'To implement the fix immediately',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'To skip ahead to Control',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 3,
                                             'question': 'Why is jumping straight to "Improve" without the earlier '
                                                         'phases risky?',
                                             'options': [{'key': 'a',
                                                          'text': 'The fix might not address the real cause, so the '
                                                                  'problem is likely to come back later',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': "It's always faster and just as effective",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'It removes the need for a Control phase',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It only works for very small problems',
                                                          'correct': False}],
                                             'answer': 'a'}],
                        'summary': ['DMAIC: Define, Measure, Analyze, Improve, Control — in that order.',
                                    'Each phase builds on the one before it; skipping ahead risks fixing the wrong '
                                    'thing.',
                                    "You don't need statistics to understand the logic of DMAIC at this level — just "
                                    'the discipline of defining and confirming before fixing.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Module 1: Six Sigma Foundations'},
                       {'code': 'W05',
                        'title': 'Your Role as a White Belt',
                        'opening_question': "You don't run projects as a White Belt — so why would an organization "
                                            'still want you trained in these basics?',
                        'concepts': ['A **White Belt** provides broad organizational awareness — not project '
                                     'leadership.',
                                     'Concrete contributions: reporting problems you notice, participating honestly in '
                                     'VOC interviews or surveys, following new standard work created by an improvement '
                                     "team, and supporting a Green or Black Belt's data collection when asked.",
                                     'The **belt hierarchy**, from broadest awareness to deepest expertise: White → '
                                     'Yellow → Green → Black Belt → Master Black Belt, with a Champion sponsoring '
                                     'projects from a leadership seat.',
                                     '**Socratic prompt:** If a company trained only a handful of Black Belts and '
                                     'nobody else understood basic Six Sigma vocabulary, what might go wrong when '
                                     'those projects try to roll out changes?'],
                        'terms': ['White Belt', 'Belt Hierarchy', 'Champion'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ["Describe the White Belt's role in supporting Six Sigma efforts",
                                                'Identify concrete ways a White Belt can contribute, even without '
                                                'leading a project',
                                                'Explain, at a basic level, where White Belt fits in the overall belt '
                                                'hierarchy'],
                        'full_explanation': "It might seem like White Belt training is only useful if you're going to "
                                            'lead a project — but the opposite is usually true. Six Sigma projects '
                                            'succeed or fail based on whether the rest of the organization actually '
                                            "understands and supports the change, not just on whether the Black Belt's "
                                            'statistics were correct.\n'
                                            '\n'
                                            'Think about what happens when a project team finishes a fix and rolls it '
                                            'out to the wider team. If nobody outside the project team understands '
                                            'basic terms like "root cause" or "standard work," the new process can '
                                            'feel like an arbitrary rule imposed from above, rather than something '
                                            "people understand the reason for — and it's much easier to quietly "
                                            "abandon a rule you don't understand than one you do. This is exactly the "
                                            'gap White Belt training closes: broad, shared vocabulary and awareness '
                                            'across the organization, so improvements actually stick once the project '
                                            'team moves on.\n'
                                            '\n'
                                            'Concretely, being a White Belt means you can meaningfully contribute '
                                            'without ever running a project yourself: reporting a recurring problem '
                                            'instead of just working around it quietly, giving honest answers when '
                                            'someone gathers VOC or VOE input (rather than telling them what you think '
                                            'they want to hear), actually following new standard work instead of '
                                            'reverting to the old way out of habit, and helping a Green or Black Belt '
                                            'collect accurate data when they ask — because inaccurate data from an '
                                            "uninterested frontline contributor can quietly derail an entire project's "
                                            'analysis.\n'
                                            '\n'
                                            'In the belt hierarchy, White sits at the base — broadest reach, lightest '
                                            'depth — building up through Yellow (part-time team member), Green '
                                            '(project co-lead), Black (project lead), and Master Black Belt (expert '
                                            'coach across many projects), with a Champion sponsoring projects from a '
                                            "leadership position. You're not expected to master statistics or run a "
                                            "charter. You're expected to understand enough to be a genuine partner in "
                                            'the process, instead of an obstacle to it.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why does an organization benefit from training White Belts, '
                                                         "even though they don't lead projects?",
                                             'options': [{'key': 'a',
                                                          'text': 'Broad shared awareness makes it more likely '
                                                                  'improvements actually stick after a project team '
                                                                  'moves on',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'White Belts are required to approve every project '
                                                                  'charter',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'White Belt training replaces the need for a Black '
                                                                  'Belt',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It has no real benefit beyond a certificate',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 2,
                                             'question': 'Which of the following is a concrete way a White Belt can '
                                                         'contribute to a Six Sigma effort?',
                                             'options': [{'key': 'a',
                                                          'text': 'Giving honest input during a VOC interview and '
                                                                  'following new standard work',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'Independently designing a hypothesis test',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "Approving a project's financial benefits",
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Selecting which projects the organization should '
                                                                  'fund',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 3,
                                             'question': 'In the belt hierarchy, where does White Belt sit?',
                                             'options': [{'key': 'a',
                                                          'text': 'At the base — broadest awareness, lightest depth, '
                                                                  'no project leadership expectation',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'At the top, above Master Black Belt',
                                                          'correct': False},
                                                         {'key': 'c', 'text': 'Equal to a Champion', 'correct': False},
                                                         {'key': 'd',
                                                          'text': "It isn't part of the hierarchy at all",
                                                          'correct': False}],
                                             'answer': 'a'}],
                        'summary': ['White Belt provides broad awareness, not project leadership — and that awareness '
                                    'is exactly what helps improvements survive after a project ends.',
                                    'Concrete contributions: reporting problems, honest VOC/VOE input, following new '
                                    'standard work, supporting data collection.',
                                    'Belt hierarchy: White → Yellow → Green → Black Belt → Master Black Belt, with a '
                                    'Champion sponsoring from leadership.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Module 1: Six Sigma Foundations'},
                       {'code': 'W06',
                        'title': "When You're Building Something New: A First Look at DMADV",
                        'opening_question': "You've learned DMAIC — a way to fix something that already exists, like a "
                                            'rushed morning routine. But imagine you just moved into a brand new '
                                            'apartment and have no morning routine at all yet, because nothing has '
                                            'ever been established there. Would DMAIC even apply here — can you '
                                            '"improve" something that doesn\'t exist yet?',
                        'concepts': ["**DMADV**: Define, Measure, Analyze, Design, Verify — used when there's no "
                                     'existing process or product to improve, only something new to build.',
                                     "**Socratic prompt:** If you're building a morning routine from scratch in a new "
                                     'apartment, does it make sense to talk about "improving" it before it\'s ever '
                                     'existed once?',
                                     'The first three letters (Define, Measure, Analyze) are similar in spirit to '
                                     'DMAIC — the last two change, because there\'s nothing existing yet to "Improve" '
                                     'or "Control."'],
                        'terms': ['DMADV', 'Design', 'Verify'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain the basic difference between fixing something that exists '
                                                '(DMAIC) and designing something brand new (DMADV)',
                                                'Name the five letters of DMADV, in order',
                                                'Recognize, at a basic level, when a workplace situation calls for '
                                                'DMADV instead of DMAIC'],
                        'full_explanation': 'DMAIC assumes something is already happening, just not well enough — a '
                                            "rushed morning routine, a delivery that's often late. DMADV assumes the "
                                            "opposite: there's nothing there yet at all. Moving into a brand new "
                                            'apartment with no established routine is a genuinely different situation '
                                            'than a routine that already exists but runs late every day.\n'
                                            '\n'
                                            'DMADV keeps the same first three letters as DMAIC for good reason: you '
                                            'still need to **Define** what you actually want (a smooth, on-time '
                                            'morning in the new place), **Measure** what "smooth and on-time" would '
                                            'look like in real numbers (leaving by a specific time, with specific '
                                            'tasks done), and **Analyze** what options exist for getting there '
                                            '(different orders of getting ready, different routes to a new commute). '
                                            'But instead of **Improve** and **Control** — which assume something '
                                            'already running that just needs adjustment — DMADV shifts to **Design** '
                                            '(actually building the new routine, step by step) and **Verify** (trying '
                                            'it for real and confirming it actually works, before treating it as your '
                                            'new normal).\n'
                                            '\n'
                                            'In a workplace, this same distinction shows up whenever a company '
                                            'launches something brand new — a new product, a new service, a new '
                                            'location — rather than fixing something that already exists. The letters '
                                            'change because the starting point is fundamentally different: nothing to '
                                            'improve, only something to build correctly from the start.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What is the key difference between the situations DMAIC and '
                                                         'DMADV are each designed for?',
                                             'options': [{'key': 'a',
                                                          'text': 'DMAIC improves something that already exists; DMADV '
                                                                  "designs something brand new that doesn't exist yet "
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'DMAIC is only for factories, DMADV is only for '
                                                                  'offices *(the distinction is existing vs. new, not '
                                                                  'industry type)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'DMADV is a shorter version of DMAIC *(both have '
                                                                  'five phases)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'DMAIC and DMADV are two names for the exact same '
                                                                  'thing *(they share some phases but diverge to fit '
                                                                  'different situations)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Which two letters differ between DMAIC and DMADV, and why?',
                                             'options': [{'key': 'a',
                                                          'text': 'Improve/Control become Design/Verify, because '
                                                                  "there's nothing existing yet to improve or control "
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Define/Measure become Design/Verify *(the first two '
                                                                  'letters are shared between both)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Analyze is replaced entirely in DMADV *(Analyze is '
                                                                  'common to both frameworks)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'DMADV shares no letters with DMAIC at all *(the '
                                                                  'first three letters are shared)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why do DMAIC and DMADV share the same first three letters?',
                                             'options': [{'key': 'a',
                                                          'text': 'Both situations still require clearly defining the '
                                                                  'goal, measuring what "good" looks like, and '
                                                                  'analyzing options — whether something already '
                                                                  'exists or not *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "It's a coincidence with no real reason *(this "
                                                                  'shared logic applies in both fixing and building '
                                                                  'situations)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'DMADV was created before DMAIC *(DMAIC is the '
                                                                  'original, more widely used framework)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'These phases require no real work in either '
                                                                  'framework *(both require substantive work here)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['DMAIC fixes something that already exists; DMADV designs something brand new.',
                                    'DMADV: Define, Measure, Analyze, Design, Verify — sharing its first three letters '
                                    'with DMAIC, replacing Improve/Control with Design/Verify.',
                                    'Workplaces use DMADV when launching something new rather than fixing something '
                                    'old.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Module 2: DMAIC and DMADV'}]},
 'yellow': {'name': 'Yellow Belt',
            'tagline': 'Participate effectively in improvement projects.',
            'description': 'Build the practical skills to map processes, support data collection, use basic tools, and '
                           'contribute to DMAIC teams.',
            'modules': [{'code': 'Y01',
                         'title': "DMAIC in Practice: A Team Member's View",
                         'opening_question': "As a Yellow Belt, you won't write the project charter or run the "
                                             'statistics — so why do you still need to understand what happens in all '
                                             'five DMAIC phases?',
                         'concepts': ["**Define**: the Green/Black Belt writes the charter, but a Yellow Belt's local "
                                      'knowledge often helps scope the problem correctly.',
                                      '**Measure**: Yellow Belts are frequently the ones actually collecting the data, '
                                      "since they're closest to the process.",
                                      '**Analyze**: Yellow Belts contribute firsthand observations about suspected '
                                      'causes.',
                                      "**Improve**: Yellow Belts often pilot the new method on the floor before it's "
                                      'rolled out further.',
                                      '**Control**: Yellow Belts frequently become the ones monitoring the new '
                                      'standard work day to day, long after the project team disbands.',
                                      '**Socratic prompt:** If nobody who actually performs the process is asked '
                                      "what's happening during the Measure phase, how reliable is the resulting data "
                                      'likely to be?'],
                         'terms': ['DMAIC (recap)', 'Team Member Contribution'],
                         'math': [],
                         'teach_back': 'Teach the approach back to me in your own words.',
                         'learning_objectives': ['Describe what actually happens in each DMAIC phase, in more detail '
                                                 'than a White Belt overview',
                                                 'Explain what a Yellow Belt is typically asked to do during each '
                                                 'phase',
                                                 'Recognize the kinds of data and observations a team member is '
                                                 'uniquely positioned to contribute'],
                         'full_explanation': 'It\'s tempting to think DMAIC is "the project leader\'s job" and a team '
                                             "member just needs to show up when asked. In practice, a Yellow Belt's "
                                             'contribution shapes the *quality* of every phase, even without owning '
                                             'any of them.\n'
                                             '\n'
                                             'During **Define**, the charter gets written by whoever leads the project '
                                             "— but a Yellow Belt who's actually done the job for years can catch a "
                                             'problem statement that\'s subtly wrong (e.g., "orders are late" when the '
                                             'real pattern is "orders are late only on Mondays") before the team '
                                             'wastes weeks measuring the wrong thing. During **Measure**, someone has '
                                             'to physically record data — timestamps, defect counts, wait times — and '
                                             "that's very often a Yellow Belt's responsibility; sloppy or inconsistent "
                                             "data collection here can quietly derail the entire project's analysis "
                                             'later. During **Analyze**, a Yellow Belt\'s honest answer to "what do '
                                             'you think is actually causing this?" is frequently more accurate than an '
                                             "outside analyst's best guess, because the Yellow Belt has watched the "
                                             'failure happen repeatedly. During **Improve**, new solutions are often '
                                             'piloted with a small group before a full rollout — and Yellow Belts are '
                                             'typically the ones actually running the pilot and reporting back whether '
                                             'it worked in real conditions, not just on paper. During **Control**, '
                                             "once the project team moves on to other work, it's frequently the Yellow "
                                             'Belts who keep the new standard work alive day to day, and who notice '
                                             'first if the process starts drifting back to old habits.\n'
                                             '\n'
                                             "The throughline: a Yellow Belt doesn't need to run statistics to "
                                             'meaningfully shape whether a project succeeds. Accurate data, honest '
                                             'observations, and genuine follow-through on new standard work are just '
                                             "as critical to a project's outcome as the analysis itself.",
                         'knowledge_check': [{'number': 1,
                                              'question': "Why is a Yellow Belt's input often valuable during the "
                                                          "Define phase, even though they don't write the charter?",
                                              'options': [{'key': 'a',
                                                           'text': 'Their firsthand knowledge can catch an inaccurate '
                                                                   'problem statement before the team wastes time '
                                                                   'measuring the wrong thing',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'They are legally required to approve every charter',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'They replace the need for a project champion',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': "Define phase doesn't involve Yellow Belts at all",
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 2,
                                              'question': 'Why does data collection accuracy during Measure matter so '
                                                          'much, even for someone not "running" the project?',
                                              'options': [{'key': 'a',
                                                           'text': 'Inconsistent or careless data collection can '
                                                                   "derail the entire project's later analysis",
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'Measure phase data is discarded after the project '
                                                                   'starts',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'Only Black Belts are allowed to collect data',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'Measure phase has no connection to Analyze',
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 3,
                                              'question': 'Who typically keeps new standard work alive during the '
                                                          'Control phase, after the project team has moved on?',
                                              'options': [{'key': 'a',
                                                           'text': 'The Yellow Belts and other frontline staff who do '
                                                                   'the work daily',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'Only the Master Black Belt',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'Nobody — Control phase ends the moment the charter '
                                                                   'closes',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'Only external auditors',
                                                           'correct': False}],
                                              'answer': 'a'}],
                         'summary': ["Yellow Belts shape DMAIC's success through accurate data, honest input, and "
                                     'follow-through — not by owning the analysis.',
                                     'Define benefits from local knowledge that catches scoping errors early.',
                                     'Control frequently depends on Yellow Belts sustaining the new standard work '
                                     'long-term.'],
                         'hands_on_activity': '',
                         'worked_solution': '',
                         'module_title': 'Module 1: Team Member Toolkit'},
                        {'code': 'Y02',
                         'title': 'Understanding a Process: Process Mapping Basics',
                         'opening_question': 'Before you can improve a process, can you draw out — step by step — '
                                             'exactly what happens today? Try it in your head for a task you do daily. '
                                             'Is it harder than you expected?',
                         'concepts': ['A **process map** is a visual, step-by-step picture of how work actually flows, '
                                      "not how it's supposed to flow on paper.",
                                      'Basic symbols: an **oval** for start/end points, a **rectangle** for a process '
                                      'step, and a **diamond** for a decision point (where the path branches based on '
                                      'a yes/no or condition).',
                                      'An **"as-is" map** documents the process as it actually runs today; a **"to-be" '
                                      'map** documents the proposed future state after improvement.',
                                      '**Socratic prompt:** Why might two people who both "do the same job" draw '
                                      'slightly different process maps of it?'],
                         'terms': ['Process Map', 'As-Is Map', 'To-Be Map'],
                         'math': [],
                         'teach_back': 'Teach the approach back to me in your own words.',
                         'learning_objectives': ['Explain the purpose of a process map (flowchart)',
                                                 'Identify the basic symbols used in a process map: start/end, process '
                                                 'step, and decision point',
                                                 'Explain why an "as-is" map often reveals surprises, even to people '
                                                 'who perform the process daily'],
                         'full_explanation': 'Most people assume they already know exactly how their own process works '
                                             "— until they're asked to draw it out step by step, in order, including "
                                             'every decision point and handoff. This exercise is deceptively '
                                             'difficult, and that difficulty is exactly the point: a written procedure '
                                             'often describes an idealized version of the process, while a **process '
                                             'map** captures what actually happens, including the workarounds, '
                                             'exceptions, and shortcuts that develop over time.\n'
                                             '\n'
                                             'The basic symbols are simple by design. An **oval** marks where the '
                                             'process begins and ends. A **rectangle** represents a single step or '
                                             'action. A **diamond** represents a decision point — a place where the '
                                             'process branches depending on a condition (e.g., "Is the form complete? '
                                             'Yes → continue. No → return to sender"). Connecting these with arrows in '
                                             "the correct order produces a map anyone can follow, even someone who's "
                                             'never done the job.\n'
                                             '\n'
                                             'This is why building an **"as-is" map** (the process as it genuinely '
                                             'runs today, warts and all) is usually the first real step of process '
                                             "improvement — you can't fix a process you haven't honestly mapped. It's "
                                             'common, and useful, for this exercise to surface disagreement: two '
                                             'experienced employees doing "the same job" often turn out to handle a '
                                             'particular exception differently, or skip a step the written procedure '
                                             "says is mandatory. That disagreement isn't a failure of the exercise — "
                                             "it's exactly the kind of hidden inconsistency Six Sigma is looking for. "
                                             'Only after the as-is map is honestly captured does a team move on to '
                                             'designing a **"to-be" map** — the proposed future version, once the '
                                             'inconsistencies and unnecessary steps have been addressed.',
                         'knowledge_check': [{'number': 1,
                                              'question': 'What does an "as-is" process map represent?',
                                              'options': [{'key': 'a',
                                                           'text': 'The process exactly as it actually runs today, '
                                                                   'including workarounds and exceptions',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'Only the officially written procedure, regardless '
                                                                   'of practice',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'The proposed future state after improvement',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'A map that never needs updating',
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 2,
                                              'question': 'What does a diamond symbol represent in a process map?',
                                              'options': [{'key': 'a',
                                                           'text': 'A decision point where the process branches based '
                                                                   'on a condition',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'The start or end of the process',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'A single action or task',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'A data collection point only',
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 3,
                                              'question': 'Why might two experienced employees draw slightly different '
                                                          'process maps of "the same" job?',
                                              'options': [{'key': 'a',
                                                           'text': 'They may handle exceptions or edge cases '
                                                                   'differently, even if the core steps are similar',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'Only one of them actually knows the job',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'Process maps are always identical for the same job',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'One of them is lying',
                                                           'correct': False}],
                                              'answer': 'a'}],
                         'summary': ['A process map visually documents how work actually flows, using ovals, '
                                     'rectangles, and diamonds.',
                                     '"As-is" maps capture current reality; "to-be" maps capture the proposed future '
                                     'state.',
                                     "Mapping honestly often reveals inconsistencies even experienced staff didn't "
                                     'realize existed.'],
                         'hands_on_activity': '',
                         'worked_solution': '',
                         'module_title': 'Module 1: Team Member Toolkit'},
                        {'code': 'Y03',
                         'title': 'Finding Root Causes: Fishbone Diagrams and the 5 Whys',
                         'opening_question': 'If you ask "why" about a problem only once, do you usually land on the '
                                             'real root cause — or just the first convenient excuse?',
                         'concepts': ['A **fishbone (Ishikawa) diagram** organizes potential causes of a problem into '
                                      'categories, commonly: Method, Machine, Material, Manpower (People), '
                                      'Measurement, and Environment (the "6 Ms").',
                                      'The **5 Whys** technique asks "why" repeatedly (typically about five times) to '
                                      'move past the first, surface-level answer and reach a deeper cause.',
                                      'A **symptom** is what you initially observe; a **root cause** is the underlying '
                                      'reason the symptom keeps occurring.',
                                      '**Socratic prompt:** If your first answer to "why did this happen" is "the '
                                      'employee made a mistake," is that a root cause, or just a place most root-cause '
                                      'digging incorrectly stops?'],
                         'terms': ['Fishbone (Ishikawa) Diagram', '5 Whys', 'Root Cause vs. Symptom'],
                         'math': [],
                         'teach_back': 'Teach the approach back to me in your own words.',
                         'learning_objectives': ['Build a basic fishbone (Ishikawa) diagram using common cause '
                                                 'categories',
                                                 'Apply the 5 Whys technique to drill down from a symptom to a root '
                                                 'cause',
                                                 'Distinguish a symptom from a genuine root cause'],
                         'full_explanation': 'When a problem happens, the fastest explanation is often the shallowest '
                                             'one — "the machine broke," "someone forgot a step," "the part was '
                                             'defective." These are usually **symptoms**, not root causes, and '
                                             "stopping there tends to produce a fix that doesn't actually prevent the "
                                             'problem from recurring.\n'
                                             '\n'
                                             'The **fishbone diagram** helps a team brainstorm more completely by '
                                             'organizing possible causes into categories before jumping to '
                                             'conclusions. The "6 Ms" are a common starting set: **Method** (the way '
                                             'the work is performed), **Machine** (equipment or tools involved), '
                                             '**Material** (inputs used), **Manpower/People** (training, staffing, '
                                             'fatigue), **Measurement** (how the problem is detected or gauged), and '
                                             '**Environment** (temperature, lighting, layout, noise). Sketched as a '
                                             'fish skeleton with the problem at the "head" and each category as a '
                                             '"bone," this structure prevents a team from fixating on the first '
                                             'plausible cause someone mentions and ignoring the other five categories '
                                             'entirely.\n'
                                             '\n'
                                             'The **5 Whys** technique works alongside this by pushing past the first '
                                             'answer. For example: *Why did the shipment go out late?* Because the '
                                             "order wasn't packed on time. *Why wasn't it packed on time?* Because the "
                                             'packing station was short-staffed that day. *Why was it short-staffed?* '
                                             'Because two people called in sick with no backup plan. *Why was there no '
                                             'backup plan?* Because cross-training was never set up for that station. '
                                             "*Why wasn't cross-training set up?* Because it was never flagged as a "
                                             'priority during onboarding. Notice how the first answer ("wasn\'t packed '
                                             'on time") is a symptom, while the fifth answer (a gap in onboarding '
                                             'priorities) is something you can actually fix in a way that prevents the '
                                             'problem from recurring — not just patches this one instance of it.\n'
                                             '\n'
                                             'Fishbone diagrams and 5 Whys work well together: the fishbone widens the '
                                             'search across categories so nothing gets overlooked, and the 5 Whys '
                                             'deepens the search within whichever branch looks most promising, so the '
                                             "team doesn't stop at the first convenient explanation.",
                         'knowledge_check': [{'number': 1,
                                              'question': 'What is the purpose of organizing causes into fishbone '
                                                          'categories (the "6 Ms")?',
                                              'options': [{'key': 'a',
                                                           'text': 'To make sure a team brainstorms broadly, rather '
                                                                   'than fixating on the first cause mentioned',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'To assign blame to a specific department',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'To calculate the financial cost of the defect',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'To replace the need for any further analysis',
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 2,
                                              'question': 'In the 5 Whys example above, what was the actual root cause '
                                                          'identified?',
                                              'options': [{'key': 'a',
                                                           'text': 'A gap in onboarding priorities that meant '
                                                                   'cross-training was never set up',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': "The shipment wasn't packed on time",
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'Two people called in sick',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'The packing station was short-staffed',
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 3,
                                              'question': 'Why is "the employee made a mistake" usually a poor place '
                                                          'to stop root-cause analysis?',
                                              'options': [{'key': 'a',
                                                           'text': "It's typically a symptom, and stopping there "
                                                                   'misses the deeper, fixable reason the mistake was '
                                                                   'possible in the first place',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'Employees are never actually responsible for '
                                                                   'defects',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': "It's always factually incorrect",
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'It skips the Measure phase entirely',
                                                           'correct': False}],
                                              'answer': 'a'}],
                         'summary': ['Fishbone diagrams organize causes into categories (commonly the "6 Ms") to widen '
                                     "a team's search.",
                                     'The 5 Whys pushes past the first, surface-level explanation to find a genuine '
                                     'root cause.',
                                     'A symptom is what you observe; a root cause is the underlying, fixable reason it '
                                     'keeps happening.'],
                         'hands_on_activity': '',
                         'worked_solution': '',
                         'module_title': 'Module 1: Team Member Toolkit'},
                        {'code': 'Y04',
                         'title': 'Prioritizing Problems: Pareto Charts and the 80/20 Rule',
                         'opening_question': 'If you have ten different problems you could work on, but limited time, '
                                             'how do you decide where to actually start?',
                         'concepts': ['A **Pareto chart** sorts causes by frequency (or cost) from largest to '
                                      'smallest, usually with a cumulative percentage line overlaid.',
                                      'The **80/20 rule** observes that, in most defect data, roughly 80% of the '
                                      'problem traces back to roughly 20% of the causes — the "vital few."',
                                      'The remaining causes are sometimes called the "trivial many" — not because they '
                                      "don't matter at all, but because they matter far less than the top few.",
                                      '**Socratic prompt:** If 80% of your defects trace back to just 15% of your '
                                      'causes, why would spreading improvement effort evenly across *all* causes be a '
                                      'poor use of limited time?'],
                         'terms': ['Pareto Chart', '80/20 Rule', 'Vital Few / Trivial Many'],
                         'math': [],
                         'teach_back': 'Teach the approach back to me in your own words.',
                         'learning_objectives': ['Read and interpret a basic Pareto chart',
                                                 'Apply the 80/20 rule to prioritize which problems to tackle first',
                                                 'Explain why attacking the "vital few" causes is usually smarter than '
                                                 'spreading effort evenly across every cause'],
                         'full_explanation': "When a process has many possible causes of failure, it's tempting to try "
                                             'to fix everything at once. In practice, most defect data follows a '
                                             'predictable pattern: a small number of causes account for the large '
                                             'majority of the problem, while a long list of other causes each '
                                             'contribute only a little. This is the **80/20 rule** — not a strict law, '
                                             'but a pattern reliable enough to build a prioritization tool around.\n'
                                             '\n'
                                             'A **Pareto chart** makes this pattern visible. Causes are listed along '
                                             'the bottom, sorted from most frequent (or most costly) to least, as bars '
                                             'in descending order — visually, the chart looks like a staircase going '
                                             'down. A cumulative percentage line is often overlaid on top, climbing '
                                             'toward 100% as you move across the bars, which makes it easy to see '
                                             'exactly where the "vital few" cutoff falls — for example, the chart '
                                             'might show that the first three causes (out of fifteen total) already '
                                             'account for 78% of all defects.\n'
                                             '\n'
                                             'The practical value here is discipline: instead of a team debating '
                                             'everyone\'s favorite theory about what\'s "really" causing the problem, '
                                             'the Pareto chart lets the actual frequency data settle the argument '
                                             'about where to start. Tackling the tallest bars first produces the '
                                             'biggest improvement for the effort spent — attacking the '
                                             'fifteenth-largest cause first, while ignoring the largest one, is a poor '
                                             "use of a team's limited time, even if that fifteenth cause happens to be "
                                             'the one someone feels most strongly about.',
                         'knowledge_check': [{'number': 1,
                                              'question': 'What does the 80/20 rule generally observe about defect '
                                                          'data?',
                                              'options': [{'key': 'a',
                                                           'text': 'A small number of causes typically account for the '
                                                                   'large majority of the problem',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'All causes contribute equally to every problem',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': '80% of causes are always unfixable',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'It only applies to manufacturing defects',
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 2,
                                              'question': 'How are bars typically arranged on a Pareto chart?',
                                              'options': [{'key': 'a',
                                                           'text': 'In descending order, from most frequent/costly to '
                                                                   'least',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'In alphabetical order',
                                                           'correct': False},
                                                          {'key': 'c', 'text': 'In random order', 'correct': False},
                                                          {'key': 'd',
                                                           'text': 'In ascending order, smallest first',
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 3,
                                              'question': 'Why is it usually smarter to attack the tallest bars on a '
                                                          'Pareto chart first?',
                                              'options': [{'key': 'a',
                                                           'text': 'It produces the largest improvement for the effort '
                                                                   'spent, compared to spreading effort evenly',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': "It's required by Six Sigma certification rules",
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'Smaller causes are never worth fixing at all',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'It guarantees the problem will never recur',
                                                           'correct': False}],
                                              'answer': 'a'}],
                         'summary': ['Pareto charts sort causes by frequency or cost, largest to smallest, often with '
                                     'a cumulative line.',
                                     'The 80/20 rule: a small number of causes ("vital few") usually account for most '
                                     'of the problem.',
                                     'Prioritizing the tallest bars first makes the best use of limited improvement '
                                     'time.'],
                         'hands_on_activity': '',
                         'worked_solution': '',
                         'module_title': 'Module 1: Team Member Toolkit'},
                        {'code': 'Y05',
                         'title': 'Workplace Organization: 5S in Depth',
                         'opening_question': 'Have you ever wasted real time hunting for a tool that used to have an '
                                             'obvious home? What changed?',
                         'concepts': ['**Sort (Seiri)**: remove anything not needed for current work.',
                                      '**Set in Order (Seiton)**: give everything that remains a clear, logical, '
                                      'marked location.',
                                      '**Shine (Seiso)**: clean the workspace thoroughly, which also helps surface '
                                      'early signs of wear or malfunction.',
                                      '**Standardize (Seiketsu)**: create visual controls and simple procedures so the '
                                      "first three steps don't quietly decay.",
                                      '**Sustain (Shitsuke)**: build habits and periodic checks that keep 5S part of '
                                      'daily practice, not a one-time event.',
                                      '**Socratic prompt:** Of the five steps, which one has no dramatic '
                                      '"before/after" photo — and why might that make it the easiest step to neglect?'],
                         'terms': ['5S (Seiri/Seiton/Seiso/Seiketsu/Shitsuke)', 'Red-Tagging'],
                         'math': [],
                         'teach_back': 'Teach the approach back to me in your own words.',
                         'learning_objectives': ['Describe all five steps of 5S: Sort, Set in Order, Shine, '
                                                 'Standardize, and Sustain',
                                                 'Apply the first three steps to a real or example workspace',
                                                 'Explain why "Sustain" is typically the hardest step to maintain over '
                                                 'time'],
                         'full_explanation': '5S is one of the most commonly taught Lean tools because its logic is '
                                             'intuitive, even though maintaining it in practice is harder than it '
                                             'looks. Each step builds on the one before it.\n'
                                             '\n'
                                             "**Sort (Seiri)** starts by removing anything that isn't actually needed "
                                             'for the work currently being done — a common technique is "red-tagging" '
                                             'uncertain items (marking them, then relocating or discarding them after '
                                             'a set period if nobody claims them) rather than agonizing over every '
                                             'item individually. **Set in Order (Seiton)** takes what remains and '
                                             'gives it a clear, marked, logical home — the guiding principle is that a '
                                             "tool used constantly should be within arm's reach, while something used "
                                             'rarely can be stored further away. **Shine (Seiso)** means cleaning the '
                                             "area thoroughly, which isn't just cosmetic: a clean machine makes a "
                                             'small oil leak or a loose bolt immediately visible, while a dirty one '
                                             'hides the same problem until it becomes a bigger failure. **Standardize '
                                             '(Seiketsu)** turns the first three steps into a repeatable standard — '
                                             'labels, floor markings, checklists, and "how it should look" reference '
                                             "photos — so the workspace doesn't quietly drift back to its old, "
                                             'cluttered state within a few weeks. **Sustain (Shitsuke)** is the '
                                             'ongoing discipline of actually maintaining all of this: periodic audits, '
                                             'shared accountability, and making 5S part of how the team normally '
                                             'operates rather than something done once for an inspection.\n'
                                             '\n'
                                             "Here's the honest challenge worth naming directly: Sort, Set in Order, "
                                             'and Shine produce a satisfying, visible "before and after" — anyone can '
                                             'see the difference in a single afternoon. Standardize and especially '
                                             "Sustain produce no such dramatic moment; they're just quiet, ongoing "
                                             'discipline with no obvious payoff photo. This is exactly why most 5S '
                                             'initiatives that fail, fail at Sustain — not because the first three '
                                             'steps were done poorly, but because nothing was built to keep them from '
                                             'fading once the initial enthusiasm wore off.',
                         'knowledge_check': [{'number': 1,
                                              'question': 'What is the purpose of "red-tagging" items during the Sort '
                                                          'step?',
                                              'options': [{'key': 'a',
                                                           'text': 'To flag uncertain items for relocation or removal, '
                                                                   'rather than deciding on each one individually up '
                                                                   'front',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'To mark items that are never allowed to be moved',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'To identify which employee owns each item',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'To replace the need for the Shine step',
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 2,
                                              'question': 'Why does the Shine step double as a form of inspection?',
                                              'options': [{'key': 'a',
                                                           'text': 'A clean surface or machine makes small problems '
                                                                   'like leaks or loose parts immediately visible',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'Cleaning always fixes mechanical problems directly',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'It replaces the need for maintenance staff',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'It only applies to office environments',
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 3,
                                              'question': 'Why is "Sustain" typically the step where 5S initiatives '
                                                          'fail?',
                                              'options': [{'key': 'a',
                                                           'text': 'It requires ongoing discipline with no dramatic '
                                                                   'visible payoff, unlike the first three steps',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': "It's technically the easiest step to perform",
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'It only applies to large factories',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'It happens before Sort in the sequence',
                                                           'correct': False}],
                                              'answer': 'a'}],
                         'summary': ['5S: Sort, Set in Order, Shine, Standardize, Sustain — each step builds on the '
                                     'last.',
                                     'Shine doubles as an early-warning inspection, not just cleaning.',
                                     'Sustain is the hardest step because it has no dramatic "before/after" moment, '
                                     'only ongoing discipline.'],
                         'hands_on_activity': '',
                         'worked_solution': '',
                         'module_title': 'Module 1: Team Member Toolkit'},
                        {'code': 'Y06',
                         'title': 'Basic Data Collection: Check Sheets and Simple Charts',
                         'opening_question': 'If your manager asks "how often does this problem happen," and you '
                                             "don't have any data, what can you honestly say?",
                         'concepts': ['A **check sheet** is a simple form used to tally how often something happens, '
                                      'in real time, as it happens.',
                                      'A **run chart** plots a measurement over time (e.g., daily defect count), '
                                      'making trends and patterns visible that a memory or gut feeling can easily miss '
                                      'or exaggerate.',
                                      '**Anecdote** ("it feels like a lot") is not the same as **data** (an actual '
                                      'recorded pattern) — and Six Sigma consistently favors the latter before acting.',
                                      '**Socratic prompt:** If you remember every time a problem happened, but never '
                                      "notice all the times it didn't, how might your memory alone give you a "
                                      'distorted picture of how often it actually occurs?'],
                         'terms': ['Check Sheet', 'Run Chart', 'Data vs. Anecdote'],
                         'math': [],
                         'teach_back': 'Teach the approach back to me in your own words.',
                         'learning_objectives': ['Use a check sheet to tally occurrences of a problem',
                                                 'Read a simple run chart showing a measurement plotted over time',
                                                 'Explain the difference between an anecdote ("I feel like it happens '
                                                 'a lot") and an actual data pattern'],
                         'full_explanation': 'Human memory is a poor substitute for actual data, and not because '
                                             "people are dishonest — it's because memory is naturally biased toward "
                                             'whatever stood out emotionally. A single dramatic failure tends to be '
                                             'remembered far more vividly than dozens of ordinary successes, which can '
                                             'make a rare problem feel far more common than it actually is (or, just '
                                             "as easily, make a frequent problem feel rarer than it really is, if it's "
                                             'become normalized).\n'
                                             '\n'
                                             "A **check sheet** solves this simply: it's a form with the possible "
                                             'issue types listed down the side, where someone makes a tally mark each '
                                             "time one occurs, over a defined period. There's no complicated "
                                             'statistics involved — just an honest, real-time count instead of a '
                                             'memory reconstructed after the fact. Over a week or two, this produces a '
                                             'genuine picture of frequency: which problem actually happens most, not '
                                             'which one is most memorable.\n'
                                             '\n'
                                             'A **run chart** takes this a step further by plotting a measurement over '
                                             'time — for example, daily defect counts across a month, connected point '
                                             'to point on a simple line graph. This reveals patterns invisible to '
                                             'memory alone: maybe defects spike every Monday, or climb steadily over '
                                             "the month, or actually stay flat despite everyone's impression that "
                                             '"it\'s been getting worse lately." None of this requires statistical '
                                             'formulas to be useful — simply seeing the plotted pattern is often '
                                             'enough to point a team in the right direction for the Analyze phase that '
                                             'follows.\n'
                                             '\n'
                                             'The core habit this lesson is building: when someone says "I think this '
                                             'happens all the time," the appropriate Six Sigma response isn\'t to '
                                             'argue — it\'s to ask, "let\'s find out — can we track it for two weeks '
                                             'and see?"',
                         'knowledge_check': [{'number': 1,
                                              'question': 'Why might memory alone give a distorted picture of how '
                                                          'often a problem really occurs?',
                                              'options': [{'key': 'a',
                                                           'text': 'Memory tends to overweight dramatic or emotional '
                                                                   'events compared to ordinary, unremarkable '
                                                                   'occurrences',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'Memory is always more accurate than written data',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'Check sheets are less reliable than memory',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'Problems that happen rarely are never memorable',
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 2,
                                              'question': 'What is the main purpose of a check sheet?',
                                              'options': [{'key': 'a',
                                                           'text': 'To tally how often something happens, in real '
                                                                   'time, as it occurs',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'To calculate financial cost automatically',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'To replace the need for a process map',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'To predict future defects using a formula',
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 3,
                                              'question': 'What advantage does a run chart offer over a single tally '
                                                          'count?',
                                              'options': [{'key': 'a',
                                                           'text': 'It shows patterns over time, such as spikes on '
                                                                   'certain days or a gradual trend',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'It requires no data collection at all',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'It eliminates the need for any further analysis',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'It only works for financial data',
                                                           'correct': False}],
                                              'answer': 'a'}],
                         'summary': ['Memory is a poor substitute for data — it overweights dramatic events and misses '
                                     'ordinary patterns.',
                                     'Check sheets provide a simple, real-time tally of how often something actually '
                                     'happens.',
                                     'Run charts reveal trends and patterns over time that a gut feeling can miss '
                                     'entirely.'],
                         'hands_on_activity': '',
                         'worked_solution': '',
                         'module_title': 'Module 1: Team Member Toolkit'},
                        {'code': 'Y07',
                         'title': 'Your Role as a Yellow Belt on a Project Team',
                         'opening_question': 'A Green Belt asks you to track defects on your line for two weeks. Why '
                                             "might your accuracy in doing that matter more than you'd initially "
                                             'think?',
                         'concepts': ['A **Yellow Belt** is an active, part-time team member — not just broadly aware '
                                      '(White Belt), and not co-leading the analysis (Green Belt).',
                                      'Typical duties: collecting data accurately, providing subject-matter input, '
                                      'testing pilot changes on the floor, and following (and reporting on) new '
                                      'standard work.',
                                      'Constructive pushback: raising a concern with specifics ("this step doesn\'t '
                                      'match what actually happens on second shift") is far more useful than silent '
                                      'compliance or vague complaint.',
                                      '**Socratic prompt:** If a Yellow Belt notices a flaw in a proposed fix but says '
                                      'nothing to avoid seeming difficult, who ultimately bears the cost of that '
                                      'silence?'],
                         'terms': ['Yellow Belt Role', 'Team Member Responsibilities', 'Constructive Pushback'],
                         'math': [],
                         'teach_back': 'Teach the approach back to me in your own words.',
                         'learning_objectives': ["Describe the Yellow Belt's typical responsibilities on a project "
                                                 'team',
                                                 'Distinguish the Yellow Belt role from both White Belt (awareness '
                                                 'only) and Green Belt (project co-lead)',
                                                 'Identify constructive ways to raise concerns or push back during a '
                                                 'project'],
                         'full_explanation': 'The Yellow Belt role sits in a specific, useful middle ground. A White '
                                             'Belt is trained to recognize and support Six Sigma thinking broadly, but '
                                             "isn't expected to be an active participant in a specific project. A "
                                             'Green Belt (and above) leads the deeper analysis, owns the charter, and '
                                             "is accountable for the project's outcome. A Yellow Belt is neither "
                                             "purely passive nor fully in charge — they're an active contributor whose "
                                             'reliability directly affects whether the project succeeds.\n'
                                             '\n'
                                             'In practice, this means a few concrete responsibilities carry real '
                                             'weight. **Data collection** is often delegated to Yellow Belts precisely '
                                             "because they're closest to the process — but data collected carelessly, "
                                             'or "cleaned up" to look better than reality, can send an entire analysis '
                                             'in the wrong direction without anyone realizing it until much later. '
                                             '**Subject-matter input** — genuinely knowing how the process behaves day '
                                             'to day — is something a Yellow Belt often has and an outside analyst '
                                             "doesn't; withholding that knowledge (out of habit, distrust, or simply "
                                             'not being asked directly) deprives the project of exactly the insight it '
                                             'needs most. **Piloting changes** means a Yellow Belt is frequently the '
                                             'first person actually trying a proposed fix under real conditions, and '
                                             "honest feedback about what worked and what didn't is far more valuable "
                                             'to the project than polite agreement that everything went fine. '
                                             "**Following new standard work** — and reporting honestly if it isn't "
                                             'working as intended — is what determines whether a Control phase '
                                             'actually holds, long after the project team has moved on to other '
                                             'things.\n'
                                             '\n'
                                             'This also means knowing how to raise a concern constructively matters as '
                                             'much as having one. Vague complaints ("this new process is annoying") '
                                             'tend to get dismissed. Specific, concrete observations ("this new step '
                                             "doesn't account for what actually happens on second shift, and here's "
                                             'what goes wrong when it doesn\'t") are far more likely to get taken '
                                             'seriously and actually improve the outcome — and staying silent about a '
                                             "real flaw to avoid seeming difficult doesn't protect the project; it "
                                             'just delays the cost of that flaw until it surfaces later, usually at a '
                                             'worse time.',
                         'knowledge_check': [{'number': 1,
                                              'question': "How does a Yellow Belt's role differ from a White Belt's?",
                                              'options': [{'key': 'a',
                                                           'text': 'A Yellow Belt actively participates on a specific '
                                                                   'project team, while a White Belt maintains broad '
                                                                   'awareness without a project role',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'A Yellow Belt leads the statistical analysis, '
                                                                   'while a White Belt does not',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'There is no meaningful difference between the two '
                                                                   'roles',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'A White Belt always outranks a Yellow Belt',
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 2,
                                              'question': 'Why is careless or "cleaned up" data collection by a Yellow '
                                                          'Belt particularly risky for a project?',
                                              'options': [{'key': 'a',
                                                           'text': 'It can send the entire analysis in the wrong '
                                                                   'direction without anyone realizing it until much '
                                                                   'later',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': "It only affects the Yellow Belt's own performance "
                                                                   'review',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'Data collection has no real impact on project '
                                                                   'outcomes',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'Green Belts always re-collect all the data '
                                                                   'themselves anyway',
                                                           'correct': False}],
                                              'answer': 'a'},
                                             {'number': 3,
                                              'question': 'What makes a piece of pushback during a project '
                                                          'constructive rather than dismissible?',
                                              'options': [{'key': 'a',
                                                           'text': "Being specific and concrete about what's actually "
                                                                   'going wrong, rather than vague or general',
                                                           'correct': False},
                                                          {'key': 'b',
                                                           'text': 'Complaining as loudly and often as possible',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'Waiting until after the project closes to mention '
                                                                   'it',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'Avoiding mentioning any concerns at all',
                                                           'correct': False}],
                                              'answer': 'a'}],
                         'summary': ['Yellow Belt sits between White Belt (aware) and Green Belt (co-leads) — an '
                                     'active, part-time contributor.',
                                     'Accurate data, honest subject-matter input, real pilot feedback, and '
                                     "follow-through on standard work are the Yellow Belt's core contributions.",
                                     'Specific, concrete pushback is far more useful — and more likely to be heard — '
                                     'than silence or vague complaint.'],
                         'hands_on_activity': '',
                         'worked_solution': '',
                         'module_title': 'Module 1: Team Member Toolkit'},
                        {'code': 'Y08',
                         'title': "A First Look at DMADV: When There's No Existing Process to Fix",
                         'opening_question': "Golden Crust's leadership decides to launch a brand-new stuffed-crust "
                                             "flatbread — a product line that's never existed at the company before. "
                                             'There\'s no "flatbread process" for you to walk onto, observe, and '
                                             'collect data on, the way you would tally defects on an existing line. '
                                             "Does everything you've learned about being a good DMAIC team member "
                                             'still apply here — or does something fundamentally change?',
                         'concepts': ['**DMADV**: Define, Measure, Analyze, Design, Verify — used to build a new '
                                      'product, service, or process, rather than fix an existing one.',
                                      "**Socratic prompt:** In DMAIC, you're often the one collecting real data from "
                                      "an existing process. In DMADV, there's no existing process to collect data from "
                                      'yet — so what kind of information would a Yellow Belt actually be gathering '
                                      'during Define and Measure instead?',
                                      "A Yellow Belt's honest, practical feedback matters just as much in DMADV as "
                                      'DMAIC — what changes is *when* it happens: reacting to early concepts and '
                                      "prototypes before they're locked in, rather than reacting to problems in an "
                                      'existing process.'],
                         'terms': ['DMADV (Team Member View)', 'Prototype Feedback', 'Pilot Testing'],
                         'math': [],
                         'teach_back': 'Teach the approach back to me in your own words.',
                         'learning_objectives': ['Explain what DMADV is and how it differs from DMAIC at a practical '
                                                 'level',
                                                 "Describe what a Yellow Belt's contribution looks like in each DMADV "
                                                 'phase',
                                                 'Recognize which of your existing DMAIC team-member habits transfer '
                                                 'directly to a DMADV project'],
                         'full_explanation': 'The core habits that make you a good DMAIC team member — giving honest '
                                             'input, paying attention to floor-level reality, not staying quiet when '
                                             "something looks like it won't work — transfer directly to DMADV. What "
                                             "changes is the *timing and type* of what you're contributing, since "
                                             "there's no existing process to observe or historical data to collect.\n"
                                             '\n'
                                             'In **Define** and **Measure**, instead of helping verify an existing '
                                             'baseline, you might be asked for input during early concept discussions '
                                             '— what do you think customers actually want from a stuffed-crust '
                                             'flatbread, based on what you hear from customers or coworkers? In '
                                             '**Analyze**, instead of a fishbone session digging into why an existing '
                                             'process fails, you might help compare early prototype concepts — tasting '
                                             'samples, commenting on which feels more "Golden Crust" in style. In '
                                             '**Design**, you might pilot a proposed new production method on a small '
                                             "scale, flagging practical problems (a recipe step that's genuinely hard "
                                             'to execute consistently on the actual equipment, not just in a test '
                                             "kitchen). In **Verify**, you're often the one running or supporting the "
                                             'pilot batch that confirms the new process actually works at real '
                                             'production scale — reporting honestly if something that looked fine on '
                                             "paper doesn't hold up on the floor.\n"
                                             '\n'
                                             "The underlying discipline — don't guess, get real information, speak up "
                                             "early rather than staying quiet — is identical to DMAIC. It's simply "
                                             'applied to something being built for the first time, rather than '
                                             'something being fixed.',
                         'knowledge_check': [{'number': 1,
                                              'question': "What's the main practical difference in a Yellow Belt's "
                                                          'contribution between DMAIC and DMADV?',
                                              'options': [{'key': 'a',
                                                           'text': "In DMADV there's no existing process or historical "
                                                                   'data yet, so contributions shift toward early '
                                                                   'concept feedback, prototype input, and pilot '
                                                                   'testing *(correct)*',
                                                           'correct': True},
                                                          {'key': 'b',
                                                           'text': 'Yellow Belts have no role at all in DMADV projects '
                                                                   '*(their honest, practical input remains just as '
                                                                   'valuable — only the timing and content shift)*',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'DMADV requires a Yellow Belt to perform '
                                                                   'statistical analysis instead of the Black Belt '
                                                                   "*(that responsibility doesn't shift in either "
                                                                   'framework)*',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'DMAIC and DMADV require entirely unrelated skill '
                                                                   'sets *(the underlying habits transfer directly)*',
                                                           'correct': False}],
                                              'answer': ''},
                                             {'number': 2,
                                              'question': 'In the "Analyze" phase of a DMADV project, what might a '
                                                          'Yellow Belt typically be doing?',
                                              'options': [{'key': 'a',
                                                           'text': 'Comparing early prototype concepts and giving '
                                                                   'practical feedback on which feels right '
                                                                   '*(correct)*',
                                                           'correct': True},
                                                          {'key': 'b',
                                                           'text': 'Running a fishbone session on an existing '
                                                                   "process's defect data *(there's no existing "
                                                                   'process yet to run root-cause analysis on)*',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': "Approving the project's final financial benefits "
                                                                   "*(that's a leadership/champion role)*",
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'Writing the final control plan *(a later-phase '
                                                                   "responsibility, and DMADV's Verify differs from "
                                                                   "DMAIC's Control)*",
                                                           'correct': False}],
                                              'answer': ''},
                                             {'number': 3,
                                              'question': 'Why does "speaking up early rather than staying quiet" '
                                                          'matter just as much in DMADV as DMAIC?',
                                              'options': [{'key': 'a',
                                                           'text': "Whether reacting to an existing process's flaws or "
                                                                   "an early prototype's flaws, staying quiet means "
                                                                   'the team finds out the hard way later, after more '
                                                                   'time and resources are spent *(correct)*',
                                                           'correct': True},
                                                          {'key': 'b',
                                                           'text': 'It only matters in DMAIC, since DMADV projects '
                                                                   'never have flaws to catch *(new product '
                                                                   'development is often more prone to unforeseen '
                                                                   'issues, not less)*',
                                                           'correct': False},
                                                          {'key': 'c',
                                                           'text': 'DMADV teams are immune to the risks of passive '
                                                                   'team members *(the same risk applies regardless of '
                                                                   'framework)*',
                                                           'correct': False},
                                                          {'key': 'd',
                                                           'text': 'This habit is only relevant once a product has '
                                                                   'already launched *(catching issues before launch, '
                                                                   'during Design/Verify, is exactly when it matters '
                                                                   'most)*',
                                                           'correct': False}],
                                              'answer': ''}],
                         'summary': ['DMADV builds something new; DMAIC improves something existing — but a Yellow '
                                     "Belt's core habits transfer directly to both.",
                                     'In DMADV, contributions shift toward concept feedback, prototype input, and '
                                     "pilot testing, since there's no existing process or historical data yet.",
                                     'Speaking up early about a flaw in a new concept is just as important as speaking '
                                     'up about a flaw in an existing process.'],
                         'hands_on_activity': '',
                         'worked_solution': '',
                         'module_title': 'Module 2: DMAIC and DMADV'}]},
 'green': {'name': 'Green Belt',
           'tagline': 'Lead structured improvement projects.',
           'description': 'Develop the DMAIC, Lean, measurement, analysis, improvement, and control skills required to '
                          'lead improvement work.',
           'modules': [{'code': 'G01',
                        'title': 'Introduction to Six Sigma and Organizational Goals',
                        'opening_question': 'Golden Crust Bakeries just lost its largest grocery contract after '
                                            'inspectors found repeated loaves under the labeled weight. The CEO '
                                            'announces the company is adopting Six Sigma. The operations director '
                                            'mutters afterward: *"We already have a quality control department — '
                                            'what\'s actually different about this?"* If you were advising the CEO, '
                                            'what would you say is genuinely different about Six Sigma versus the '
                                            'quality control department Golden Crust already has?',
                        'concepts': ['Sigma level converts directly to a defect rate. Approximate DPMO by level: **1σ '
                                     '≈ 690,000**, **2σ ≈ 308,000**, **3σ ≈ 66,800**, **4σ ≈ 6,210**, **5σ ≈ 233**, '
                                     '**6σ ≈ 3.4**.',
                                     "**Socratic prompt:** Golden Crust's packaging line needs to hold loaf weight "
                                     'within a 2-gram tolerance. If that process is currently running at roughly 4 '
                                     'sigma, about how many loaves per million fall outside tolerance? Given that '
                                     'Golden Crust bakes 2 million loaves a year, roughly how many mis-weighted loaves '
                                     'does that represent — and does "4 sigma" still sound acceptable once it\'s a '
                                     'real number instead of a percentage?',
                                     'Traditional "quality control" is typically **appraisal** — inspecting output '
                                     "after it's made and catching what's already wrong. Six Sigma pushes further "
                                     'upstream: finding *why* the process drifts out of tolerance in the first place '
                                     'and fixing that.',
                                     "**Socratic prompt:** If Golden Crust's inspectors are already catching some "
                                     'underweight loaves before shipping, why did enough still slip through to cost '
                                     'them a major contract?',
                                     'Six Sigma originated at Motorola (1986) and was popularized enterprise-wide by '
                                     'GE under Jack Welch (1995) — largely as a response to competitive quality '
                                     'pressure, not academic interest in statistics.'],
                        'terms': ['Sigma Level', 'DPMO', 'Appraisal vs. Prevention', 'Six Sigma (origin)'],
                        'math': [{'name': 'DPMO',
                                  'formula': 'DPMO = DPO × 1,000,000',
                                  'explanation': 'Expresses defects per opportunity on a one-million-opportunity '
                                                 'basis.',
                                  'variables': 'DPMO = defects per million opportunities; DPO = defects per '
                                               'opportunity; 1,000,000 = one million opportunities.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain what "six sigma" means as a statistical performance target, '
                                                'using actual DPMO figures',
                                                "Distinguish Six Sigma's prevention-focused approach from traditional "
                                                'after-the-fact quality inspection',
                                                'Describe the historical origin and business case for Six Sigma'],
                        'full_explanation': 'The operations director\'s objection — "we already have quality control" '
                                            '— is exactly the objection Six Sigma was built to move past. A quality '
                                            'control department, in most organizations, catches defective output '
                                            "*after* it's produced: someone inspects loaves, weighs samples, pulls out "
                                            "obvious rejects. That's valuable, but it's fundamentally reactive. It "
                                            "doesn't change the underlying rate at which the process produces bad "
                                            'loaves in the first place — it just tries to catch more of them before '
                                            'they leave the building.\n'
                                            '\n'
                                            'This is where sigma level becomes a genuinely useful number rather than a '
                                            "technical curiosity. If Golden Crust's weight-control process is running "
                                            'at roughly 4 sigma, that corresponds to about 6,210 defects per million '
                                            'opportunities — which sounds small as a percentage (0.62%) but translates '
                                            "to roughly 12,420 mis-weighted loaves a year at Golden Crust's volume. "
                                            'Inspectors sampling a fraction of output will inevitably miss some of '
                                            'those, especially if inspection itself is inconsistent or understaffed — '
                                            'which is exactly how enough bad loaves reached a grocery auditor to cost '
                                            'the company a contract.\n'
                                            '\n'
                                            'Six Sigma\'s answer isn\'t "inspect harder." It\'s to treat the 12,420 '
                                            'defective loaves as a symptom of a process that drifts — a scale that '
                                            "isn't calibrated often enough, a mixing step that's inconsistent batch to "
                                            "batch, packaging equipment that isn't monitored for drift — and to find "
                                            'and fix that root cause so the defect rate itself drops, not just the '
                                            'fraction that gets caught. This mirrors why Motorola developed the '
                                            'discipline in the 1980s under real competitive pressure from Japanese '
                                            'manufacturers producing more consistent quality at lower cost, and why GE '
                                            'later tied Six Sigma training directly to management incentives: the goal '
                                            'was never more inspectors, it was fewer defects being created in the '
                                            'first place.',
                        'knowledge_check': [{'number': 1,
                                             'question': "Golden Crust's packaging process runs at approximately 4 "
                                                         'sigma. About how many loaves per million fall outside the '
                                                         'weight tolerance at this level?',
                                             'options': [{'key': 'a', 'text': '≈6,210 *(correct)*', 'correct': True},
                                                         {'key': 'b',
                                                          'text': '≈3.4 *(This is the six sigma figure, not four sigma '
                                                                  '— a common mix-up between the *target* level and '
                                                                  "this process's *current* level.)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': '≈66,800 *(This is closer to 3 sigma — a full sigma '
                                                                  'level lower than described.)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': '0 *(No real process, however well-run, produces '
                                                                  "zero defects — that's the entire reason DPMO is "
                                                                  'measured rather than assumed.)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': "Why didn't Golden Crust's existing quality control "
                                                         'department prevent the contract loss?',
                                             'options': [{'key': 'a',
                                                          'text': 'Inspection catches some defective output after the '
                                                                  "fact, but doesn't reduce the underlying rate at "
                                                                  'which the process creates defects *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Quality control departments serve no purpose once a '
                                                                  'defect rate is known *(inspection still matters — '
                                                                  "it's Appraisal, one piece of the picture, just not "
                                                                  'sufficient alone)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The inspectors were not trained in Six Sigma *(the '
                                                                  "issue isn't inspector training — it's that "
                                                                  "inspection alone doesn't fix a drifting process)*",
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': '4 sigma performance is actually considered '
                                                                  'excellent in food manufacturing *(the point of '
                                                                  'converting to a real loaf count is precisely to '
                                                                  'show why "sounds fine as a percentage" can still '
                                                                  'mean thousands of real defects)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Which company is most credited with formalizing Six Sigma in '
                                                         'the 1980s, in response to competitive quality pressure?',
                                             'options': [{'key': 'a', 'text': 'Motorola *(correct)*', 'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Toyota *(Toyota is most associated with Lean and '
                                                                  "the Toyota Production System, not Six Sigma's "
                                                                  'origin)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'General Electric *(GE popularized Six Sigma '
                                                                  "enterprise-wide starting in 1995, but didn't "
                                                                  'originate it)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Golden Crust Bakeries *(this is the running case '
                                                                  'example, not a real historical originator)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Sigma level converts directly to a real defect count — a small-sounding '
                                    'percentage can represent thousands of actual defective units at scale.',
                                    'Inspection (Appraisal) catches some defects after the fact; Six Sigma targets the '
                                    'process itself so fewer defects are created in the first place.',
                                    'Six Sigma originated at Motorola (1986), popularized by GE (1995), both under '
                                    'real competitive pressure.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Six Sigma and Org (Corrected, Full Depth)'},
                       {'code': 'G02',
                        'title': 'Six Sigma and Organizational Goals',
                        'opening_question': "Golden Crust's CEO has three candidate Six Sigma projects on the table: "
                                            '(1) reduce changeover time on the sandwich-bread line — projected savings '
                                            '**$18,000/year**; (2) fix the weight-consistency problem that cost the '
                                            'grocery contract — projected savings **$650,000/year** in recovered '
                                            'contract revenue; (3) redesign the online ordering site to look more '
                                            'modern, championed by the marketing director, with no clear savings '
                                            "figure at all. Which should be greenlit first — and is the CEO's decision "
                                            'really just about which number is biggest?',
                        'concepts': ['**Strategic alignment**: a project earns funding and staffing because it moves a '
                                     'metric leadership recognizes — not merely because the number sounds impressive '
                                     'in isolation.',
                                     '**Socratic prompt:** The website redesign has real support (the marketing '
                                     'director wants it) but no clear savings figure and no connection to a '
                                     'leadership-tracked metric. Should that disqualify it from being a Six Sigma '
                                     'project — even though someone senior wants it done?',
                                     '**Goal cascading**: a high-level goal ("stop losing contracts over quality") '
                                     'cascades into a specific, measurable project target ("bring loaf-weight '
                                     'variation within tolerance to recover the grocery contract").',
                                     '**Socratic prompt:** Project 1 (changeover time, $18,000/year) is a legitimate, '
                                     'clean Six Sigma project. Project 2 (weight consistency, $650,000/year) is '
                                     'dramatically larger. Beyond the size of the number, what else makes Project 2 '
                                     'more strategically urgent than Project 1 right now?',
                                     'A **project champion** — typically a senior leader with authority over the '
                                     'affected process — secures resources and removes obstacles; project completion '
                                     'rates are consistently higher when a champion is genuinely engaged, not just '
                                     'nominally assigned.'],
                        'terms': ['Strategic Alignment', 'Goal Cascading', 'Project Champion'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain why project selection should trace back to a strategic goal '
                                                'leadership actually tracks, not just any available savings number',
                                                'Describe how goal cascading turns a strategic objective into a '
                                                'measurable project target',
                                                'Identify why an engaged project champion matters as much as the '
                                                'financial case'],
                        'full_explanation': 'On dollar figures alone, Project 2 (weight consistency, $650,000/year) '
                                            'dwarfs Project 1 ($18,000/year) by more than 35 times — but the real case '
                                            "for prioritizing it isn't just the size of the number. It's that Project "
                                            '2 directly addresses the exact failure that already cost Golden Crust a '
                                            'named, contracted customer — a failure the CEO is personally accountable '
                                            'for explaining to the board. Project 1 is a legitimate efficiency gain, '
                                            "but it doesn't trace back to any urgent, board-visible pain point the way "
                                            'Project 2 does. This is what "strategic alignment" means in practice: not '
                                            'just "this project saves money," but "this project moves a number '
                                            'leadership is already watching, for a reason leadership already cares '
                                            'about."\n'
                                            '\n'
                                            'Project 3 — the website redesign — illustrates the opposite case clearly. '
                                            'It has real internal support (the marketing director wants it), but it '
                                            'has no measurable goal, no clear connection to a strategic metric '
                                            'leadership tracks, and no obvious problem statement beyond "it looks '
                                            'dated." Enthusiasm from a stakeholder isn\'t the same thing as strategic '
                                            'alignment; without a goal statement that cascades from an actual '
                                            "organizational priority, this isn't really a Six Sigma project — it's a "
                                            "design preference wearing Six Sigma's structure as a costume.\n"
                                            '\n'
                                            "Goal cascading is what turns Golden Crust's broad strategic pain "
                                            '("we\'re losing contracts over inconsistent quality") into something a '
                                            'Green Belt can actually execute against: a specific goal statement like '
                                            '"reduce loaf-weight variance on the packaging line so that 99.9% of '
                                            'loaves fall within ±2 grams of target weight by Q3." And because this '
                                            "project is tied to an already-lost, named contract, it's very likely to "
                                            'attract a genuinely engaged **project champion** — probably the VP '
                                            'overseeing that customer relationship, who has direct personal incentive '
                                            'to see it succeed, not just a nominal name on the charter.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why should Project 2 (weight consistency) likely be '
                                                         'prioritized over Project 1 (changeover time), beyond its '
                                                         'larger dollar figure?',
                                             'options': [{'key': 'a',
                                                          'text': 'It directly addresses a specific, already-realized '
                                                                  'failure the CEO is accountable for — a '
                                                                  'board-visible strategic pain point, not just a '
                                                                  'generic efficiency gain *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Larger dollar figures should always automatically '
                                                                  'be prioritized regardless of other factors *(size '
                                                                  'matters, but strategic urgency and traceability to '
                                                                  'a leadership priority matter independently of '
                                                                  'size)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Project 1 is not a legitimate Six Sigma project at '
                                                                  "all *(it is legitimate — it's just less urgent, not "
                                                                  'illegitimate)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Changeover time projects are never worth pursuing '
                                                                  '*(this overstates the case — smaller, well-scoped '
                                                                  'projects are often worthwhile, just not always the '
                                                                  'top priority)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What is the core problem with the website redesign as a Six '
                                                         'Sigma project candidate?',
                                             'options': [{'key': 'a',
                                                          'text': 'It lacks a measurable goal statement connected to a '
                                                                  'strategic metric leadership actually tracks '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The marketing director is not senior enough to '
                                                                  "sponsor any project *(seniority isn't the stated "
                                                                  'issue — the missing goal/metric connection is)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Website projects can never be valid Six Sigma '
                                                                  'projects under any circumstances *(too absolute — a '
                                                                  'website project *could* qualify if tied to a '
                                                                  'measurable, strategically relevant goal, such as '
                                                                  'cart abandonment rate tied to lost revenue)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It costs too much money to be worth considering '
                                                                  '*(no cost figure was even given — the issue is the '
                                                                  'missing measurable goal, not cost)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why does an engaged project champion matter beyond simply '
                                                         'approving the charter?',
                                             'options': [{'key': 'a',
                                                          'text': 'A champion with direct personal stake in the '
                                                                  'outcome is more likely to secure resources and '
                                                                  'remove obstacles than one assigned in name only '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Champions are responsible for performing the '
                                                                  "statistical analysis themselves *(that's the "
                                                                  "Green/Black Belt's role, not the champion's)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'A project cannot legally proceed without a '
                                                                  "champion's signature *(this describes bureaucratic "
                                                                  'formality, not the actual functional reason a '
                                                                  'champion matters)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Champions exist only to represent the project in '
                                                                  "year-end reports *(this undersells the champion's "
                                                                  'active role in removing real obstacles during the '
                                                                  'project)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Prioritize projects that trace back to a strategic goal leadership already tracks '
                                    '— not simply the largest number or the loudest internal advocate.',
                                    'Goal cascading turns broad strategic pain into a specific, measurable, executable '
                                    'project target.',
                                    'An engaged project champion, with a real personal stake, meaningfully improves a '
                                    "project's odds of actually finishing."],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Six Sigma and Org (Corrected, Full Depth)'},
                       {'code': 'G03',
                        'title': 'Lean Principles in the Organization',
                        'opening_question': "Walking Golden Crust's packaging line, you notice workers make roughly "
                                            '**40 trips per shift** to a supply closet 80 feet away for more packaging '
                                            'tape, and boxes routinely pile up waiting for a single, often-overloaded '
                                            'labeling machine. Using the eight categories of waste (TIMWOODS), which '
                                            'categories do you suspect are present here — and how would you actually '
                                            'confirm your guess with data, rather than just trusting your first '
                                            'impression?',
                        'concepts': ['**TIMWOODS**: Transportation, Inventory, Motion, Waiting, Overproduction, '
                                     'Overprocessing, Defects, Skills.',
                                     '**Socratic prompt:** The 40 daily trips to the supply closet look like '
                                     '**Motion** waste. But is it actually waste, or could it be necessary? What would '
                                     "you need to measure before concluding it's genuinely non-value-added?",
                                     '**Socratic prompt:** Boxes piling up in front of an overloaded labeling machine '
                                     '— is this **Waiting** waste for the boxes, or could it also point to a deeper '
                                     '**Overproduction** problem upstream? What would distinguish the two?',
                                     'Value-added activity meets three tests: the customer would pay for it, it '
                                     "transforms the product, and it's done correctly the first time. A trip to a "
                                     "supply closet passes none of these tests from the customer's perspective."],
                        'terms': ['TIMWOODS', 'Motion', 'Overproduction', 'Waiting', 'Value-Added/Non-Value-Added'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Identify TIMWOODS waste categories in a real workplace observation',
                                                'Distinguish value-added from non-value-added activity using the '
                                                "customer's perspective",
                                                'Explain why confirming an observed waste with data matters before '
                                                'acting on it'],
                        'full_explanation': "It's tempting to walk a floor, spot something that looks inefficient, and "
                                            'declare it "waste" on the spot — but Lean thinking requires confirming '
                                            'that instinct with real observation before acting on it, the same way Six '
                                            'Sigma requires data before concluding a root cause. The 40 daily trips to '
                                            'the supply closet are a strong candidate for **Motion** waste: workers '
                                            'spending time walking rather than actually packaging bread. But '
                                            'confirming it means asking a specific question — how much total time does '
                                            'this consume across a shift, and is there a real constraint preventing '
                                            'the tape from being stored closer to the point of use? If a simple change '
                                            '(moving a tape dispenser 75 feet closer) eliminates the trips with no '
                                            "meaningful downside, the original setup was pure waste. If there's a "
                                            'genuine reason for the distance — limited counter space, a safety '
                                            'separation rule — then the "waste" is more nuanced than it first '
                                            'appeared, and jumping to "just move it closer" without checking could '
                                            'create a new problem.\n'
                                            '\n'
                                            'The boxes piling up in front of the labeling machine illustrate a '
                                            'similarly easy-to-misdiagnose situation. On the surface, this looks like '
                                            '**Waiting** waste — boxes sitting idle rather than moving through the '
                                            "process. But it's worth asking whether the real issue is upstream: if the "
                                            'packaging step is producing boxes faster than the labeling machine can '
                                            "process them, the pile isn't really the labeling machine's fault — it's "
                                            '**Overproduction** upstream creating a bottleneck downstream. Speeding up '
                                            'or adding a second labeling machine would treat the symptom (the pile) '
                                            'without addressing the actual mismatch in production rates between the '
                                            'two steps — a classic case of a visible waste hiding a less visible root '
                                            'cause.\n'
                                            '\n'
                                            'This is the practical value of TIMWOODS as a checklist rather than a '
                                            'diagnosis in itself: it tells you *where to look*, not automatically '
                                            "*what's true*. Confirming which categories are genuinely present — and "
                                            'which cause is upstream of which symptom — is exactly the kind of '
                                            'measurement discipline that separates Lean thinking from simply '
                                            'eyeballing a floor and guessing.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'The 40 daily trips to the supply closet are a candidate for '
                                                         'which TIMWOODS category?',
                                             'options': [{'key': 'a',
                                                          'text': 'Motion *(correct — unnecessary movement by people)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Transportation *(Transportation refers to '
                                                                  'unnecessary movement of materials/information '
                                                                  'between process steps, not a person walking to '
                                                                  'retrieve a single item — Motion is the closer fit '
                                                                  'here)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Overproduction *(no excess product is being made in '
                                                                  'this observation)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Skills *(this refers to underutilized employee '
                                                                  'talent, unrelated to walking distance)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why might the boxes piling up in front of the labeling '
                                                         'machine actually point to an upstream Overproduction '
                                                         'problem, rather than simply Waiting waste at the labeling '
                                                         'step?',
                                             'options': [{'key': 'a',
                                                          'text': 'If the packaging step upstream produces faster than '
                                                                  'labeling can process, the real mismatch is in '
                                                                  'production rates, not a flaw in the labeling step '
                                                                  'itself *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Waiting waste never has an upstream cause *(it '
                                                                  'frequently does — this is exactly why root-cause '
                                                                  'thinking matters instead of fixing the visible '
                                                                  'symptom)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Adding a second labeling machine is always the '
                                                                  'correct fix regardless of the cause *(this could '
                                                                  'address a genuine capacity issue, but if the real '
                                                                  "cause is upstream overproduction, it wouldn't fix "
                                                                  'the underlying mismatch)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'This scenario cannot involve more than one type of '
                                                                  'waste at once *(multiple waste categories '
                                                                  'frequently co-occur and interact)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why is it important to confirm a suspected waste with actual '
                                                         'measurement before acting on it?',
                                             'options': [{'key': 'a',
                                                          'text': 'Acting on an unconfirmed guess risks fixing the '
                                                                  'wrong thing, or missing a real constraint that '
                                                                  'makes the "waste" more complicated than it first '
                                                                  'appears *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Measurement is only required for Six Sigma '
                                                                  'projects, never for Lean observations *(Lean and '
                                                                  'Six Sigma both rely on confirming assumptions with '
                                                                  'real data)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'TIMWOODS categories are only valid once confirmed '
                                                                  'by a supervisor *(the issue is confirming with '
                                                                  'data, not supervisor approval)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Visible waste is always obvious enough that no '
                                                                  'confirmation is needed *(this is precisely the '
                                                                  'assumption that leads to wrong fixes, as shown in '
                                                                  'both examples above)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['TIMWOODS is a checklist for where to look for waste — not an automatic diagnosis; '
                                    'confirm with real data before acting.',
                                    'A visible waste (like boxes waiting) can be a symptom of a different, upstream '
                                    "root cause (like overproduction) — fixing the visible symptom alone doesn't fix "
                                    'the mismatch.',
                                    "Value-added activity must pass the customer's test: would they pay for it, does "
                                    'it transform the product, and is it done right the first time.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Six Sigma and Org (Corrected, Full Depth)'},
                       {'code': 'G04',
                        'title': 'Design for Six Sigma (DFSS) Methodologies',
                        'opening_question': 'Golden Crust wants to launch a new gluten-free protein bread line. R&D '
                                            'wants to start baking test batches immediately and adjust the recipe '
                                            'based on customer taste-test feedback as problems come up. The COO '
                                            'instead wants to run this as a formal Design for Six Sigma project before '
                                            'a single test batch is baked. Six months from now, what practical '
                                            'difference will this decision actually make — assuming both paths '
                                            'eventually produce a bread that tastes good?',
                        'concepts': ['**DFSS** designs a new product/process to meet quality targets from the start; '
                                     '**DMAIC** improves an existing one. Golden Crust has no existing protein bread '
                                     'process to improve — this is a DFSS situation by definition.',
                                     '**Socratic prompt:** R&D\'s "bake first, adjust based on feedback" approach will '
                                     "eventually produce a bread people like. So what does the COO's DFSS approach "
                                     'actually add, if both paths get there eventually?',
                                     '**DMADV**: Define (goals, customer requirements) → Measure (translate needs into '
                                     'measurable CTQs) → Analyze (evaluate design alternatives against those CTQs) → '
                                     'Design (build and predict performance) → Verify (confirm performance via pilot '
                                     'before full launch).',
                                     '**Socratic prompt:** If Golden Crust skips straight to baking test batches '
                                     'without first defining measurable CTQs (shelf life, cost per loaf, protein '
                                     "content per serving, allergen cross-contamination risk), what's most likely to "
                                     'go wrong later — even if the taste tests all go well?'],
                        'terms': ['DFSS', 'DMADV', 'Critical to Quality (CTQ)'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain when DFSS is the appropriate approach instead of DMAIC',
                                                'Describe the DMADV framework and what each phase is meant to lock '
                                                'down',
                                                'Explain why fixing a design flaw becomes dramatically more expensive '
                                                "the later it's caught"],
                        'full_explanation': "The R&D team's instinct — bake something, get feedback, adjust — isn't "
                                            "wrong exactly, it's just optimizing for the wrong variable first: taste, "
                                            'in isolation, before anything else is defined. Design for Six Sigma '
                                            'exists precisely for situations like this new protein bread line, where '
                                            "there's no existing process to improve — only a blank slate that needs to "
                                            'be built correctly from the start, because retrofitting quality into a '
                                            'product after launch is dramatically more expensive than designing it in '
                                            'from day one.\n'
                                            '\n'
                                            'DMADV formalizes this. **Define** would establish not just "make a '
                                            'protein bread people like" but specific goals: target launch date, target '
                                            'margin, target customer segment. **Measure** translates vague goals into '
                                            'measurable **Critical to Quality (CTQ)** requirements — a minimum shelf '
                                            'life (say, 10 days unrefrigerated), a maximum cost per loaf to hit a '
                                            'target retail price, a minimum protein content per serving to support the '
                                            'marketing claim, and an allergen cross-contamination limit given Golden '
                                            "Crust's shared equipment with wheat-based products. **Analyze** would "
                                            'then evaluate different recipe and process concepts against those CTQs '
                                            '*before* committing to one — for instance, comparing two protein sources '
                                            'on cost, taste, and shelf-life trade-offs, rather than falling in love '
                                            'with the first version that tastes good. **Design** builds out the chosen '
                                            'concept in detail, including predicting how it will perform against every '
                                            'CTQ. **Verify** confirms it actually holds up — through a real pilot '
                                            'production run, not just a test kitchen batch — before full-scale '
                                            'launch.\n'
                                            '\n'
                                            'This matters because of exactly the scenario the Socratic prompt raises: '
                                            "R&D's test batches could produce a delicious bread that fails every other "
                                            'CTQ at once — spoiling in 4 days instead of 10, costing more per loaf '
                                            'than the target retail price allows, or risking allergen '
                                            "cross-contamination that wasn't checked until a customer complaint or, "
                                            'worse, a recall. A design flaw caught during the Analyze phase, on paper, '
                                            'might cost an afternoon of discussion. The same flaw caught after a '
                                            'product launch could mean a costly recall, reputational damage, and a '
                                            'repeat of the very kind of quality failure that got Golden Crust into Six '
                                            'Sigma in the first place with the grocery contract.',
                        'knowledge_check': [{'number': 1,
                                             'question': "Why is Golden Crust's new protein bread line a DFSS "
                                                         'situation rather than a DMAIC situation?',
                                             'options': [{'key': 'a',
                                                          'text': 'There is no existing process to improve — a new '
                                                                  'product/process is being designed from scratch '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'DFSS is required for all food industry projects '
                                                                  '*(the deciding factor is "new design" vs. "existing '
                                                                  'process," not industry)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'DMAIC cannot be used for any product-related '
                                                                  'project *(DMAIC is regularly used to improve '
                                                                  'existing product lines, just not to design new '
                                                                  'ones)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'The COO simply prefers DFSS regardless of the '
                                                                  'situation *(the case for DFSS here is structural — '
                                                                  'no existing process exists — not a matter of '
                                                                  'preference)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What does "Measure" accomplish in the DMADV framework, in '
                                                         'this scenario?',
                                             'options': [{'key': 'a',
                                                          'text': 'Translating broad goals into specific, measurable '
                                                                  'CTQs like shelf life, cost per loaf, and protein '
                                                                  'content *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Baking the first test batch of bread *(that would '
                                                                  'fall under Design/prototyping, not Measure)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Measuring how much competitors charge for similar '
                                                                  'products *(potentially useful market research, but '
                                                                  'not what Measure specifically accomplishes within '
                                                                  'DMADV)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Finalizing the exact recipe *(that's part of "
                                                                  'Design, which comes after CTQs are defined)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why is a design flaw caught during "Analyze" cheaper to fix '
                                                         'than the same flaw caught after launch?',
                                             'options': [{'key': 'a',
                                                          'text': 'Before anything is manufactured or shipped, fixing '
                                                                  'a flaw might cost a discussion; after launch, it '
                                                                  'can mean a costly recall and reputational damage '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Flaws caught during Analyze are always minor, while '
                                                                  'flaws caught after launch are always major '
                                                                  "*(severity isn't guaranteed by timing alone — but "
                                                                  'the cost of fixing a given flaw reliably increases '
                                                                  "the later it's caught)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'DMADV guarantees no flaws will ever reach launch '
                                                                  '*(no framework guarantees zero flaws — DFSS reduces '
                                                                  'the risk and cost of flaws reaching launch, it '
                                                                  "doesn't eliminate it)*",
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Recipe taste is the only CTQ that matters for a '
                                                                  'bread product *(the scenario explicitly includes '
                                                                  'shelf life, cost, protein content, and allergen '
                                                                  'risk as CTQs beyond taste)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ["DFSS applies when there's no existing process to improve — a new product or "
                                    'process is being designed from the ground up.',
                                    'DMADV: Define, Measure, Analyze, Design, Verify — CTQs get locked in before '
                                    'anything is built at scale.',
                                    'A flaw caught early (on paper, during Analyze) is dramatically cheaper to fix '
                                    'than the same flaw caught after launch.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Six Sigma and Org (Corrected, Full Depth)'},
                       {'code': 'G05',
                        'title': 'Introduction to Define Phase',
                        'opening_question': "Two days after Golden Crust's CEO approves the weight-consistency "
                                            'project, the newly assigned team meets and immediately starts researching '
                                            'new digital scales to buy. Three weeks later, in a status update, the CEO '
                                            'asks: "Which SKU is this fixing, and how much variance are we actually '
                                            'trying to eliminate?" Nobody on the team can answer precisely. What went '
                                            'wrong, and at what point should it have been caught?',
                        'concepts': ['Define exists to lock in specifics — which product, which measurement, which '
                                     'timeframe, what "done" looks like — before any solution is chosen.',
                                     '**Socratic prompt:** The team skipped straight to "buy new scales." What '
                                     'decision did that skip past, and why does skipping it tend to surface as a '
                                     'problem *later* rather than immediately?',
                                     'A vague charter (no named SKU, no specific tolerance) leaves the team unable to '
                                     'prove, later, whether they solved the actual problem or a different one '
                                     'entirely.'],
                        'terms': ['Define Phase', 'Problem Statement', 'Goal Statement', 'Charter'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain what the Define phase must establish before any data '
                                                'collection or fix begins',
                                                "Identify Define's core deliverables: problem statement, goal "
                                                'statement, scope, charter',
                                                'Recognize the risk of jumping to a perceived solution before the '
                                                'problem is actually defined'],
                        'full_explanation': "Researching new scales wasn't an unreasonable instinct — but it "
                                            'substituted a guessed solution for an actual problem definition, which is '
                                            'exactly what Define exists to prevent. Before choosing any fix, the team '
                                            'needs to agree, in writing, on specifics: which product (the whole-wheat '
                                            'sandwich loaf that the grocery client rejected), which measurement (loaf '
                                            'weight against a 2-gram tolerance), which timeframe (a defect spike '
                                            'correlating with a shift change), and what success looks like (99.9% of '
                                            'loaves within tolerance, verified over a full production month).\n'
                                            '\n'
                                            'Without this, new scales might genuinely help — old scales could be part '
                                            'of the problem — or the team might completely miss the real driver, for '
                                            'instance if the actual cause is a mixing-time inconsistency introduced by '
                                            "a new night-shift operator, something no new scale would touch. The CEO's "
                                            'question three weeks in is exactly the question a completed Define phase '
                                            'would already have answered in writing before any solution research '
                                            'began.\n'
                                            '\n'
                                            "This is why Define's deliverables aren't paperwork for its own sake: a "
                                            'specific problem and goal statement are what let the team — and '
                                            'leadership — verify later whether the project solved the right problem, '
                                            'rather than discovering, after money is already spent on new scales, that '
                                            'the defect rate never moved because the real cause was never identified.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What did the team skip by jumping straight to researching '
                                                         'new scales?',
                                             'options': [{'key': 'a',
                                                          'text': 'Agreeing on a specific problem and goal statement '
                                                                  'before selecting a solution *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Getting CEO approval for the project *(already '
                                                                  'approved — the issue is what happened after)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Hiring a Black Belt to lead the project *(the issue '
                                                                  'is whether the problem was defined, not who leads '
                                                                  'it)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Choosing project management software *(irrelevant '
                                                                  'to the actual gap)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why might new scales fail to fix the defect rate?',
                                             'options': [{'key': 'a',
                                                          'text': 'If the real cause is something else — like '
                                                                  "mixing-time variation — new scales wouldn't touch "
                                                                  'it *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Scales are always too expensive for the budget '
                                                                  "*(cost isn't the issue raised)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Equipment purchases require board approval that '
                                                                  "can't be obtained *(not stated in the scenario)*",
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Six Sigma projects can't include equipment "
                                                                  'purchases *(no such rule; the issue is verifying '
                                                                  'the cause first)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'What should a completed Define phase have produced here?',
                                             'options': [{'key': 'a',
                                                          'text': 'A specific problem statement (SKU, tolerance, '
                                                                  'timeframe) and goal statement, agreed before any '
                                                                  'fix is chosen *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'A finalized purchase order for equipment '
                                                                  '*(premature, and belongs later if at all)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "A completed root-cause analysis *(that's Analyze, "
                                                                  'after Measure)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "A finished control plan *(that's Control, far "
                                                                  'downstream)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Define locks in problem statement, goal statement, and scope before any solution '
                                    'is picked.',
                                    'Skipping to a perceived fix risks solving the wrong problem — discovered '
                                    'expensively, later.',
                                    'A specific charter is what lets the team prove, afterward, that the real problem '
                                    'was actually solved.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Define Phase (Full Module, 8 Lessons)'},
                       {'code': 'G06',
                        'title': 'Project Identification',
                        'opening_question': "Golden Crust's leadership has three candidates: changeover-time reduction "
                                            '($18,000/year), weight-consistency ($650,000/year in recovered contract '
                                            'revenue), and a website redesign (no clear savings figure, but the '
                                            'marketing director wants it badly). Beyond gut feeling, how would you '
                                            "formally score these three so the decision doesn't just come down to "
                                            'whoever argues loudest in the room?',
                        'concepts': ['Common criteria: financial impact, strategic alignment, feasibility, data '
                                     'availability, risk.',
                                     '**Socratic prompt:** The website redesign has real internal support but no '
                                     'financial figure and no measurable goal. Scored honestly against these five '
                                     "criteria, where does it likely rank — and does that ranking depend on who's "
                                     'asking?',
                                     'A weighted matrix assigns each criterion a weight (e.g., financial impact 40%, '
                                     'alignment 25%, feasibility 20%, data availability 10%, risk 5%) and scores each '
                                     'project 1–5 per criterion.'],
                        'terms': ['Project Selection Criteria', 'Weighted Scoring Matrix'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Apply selection criteria beyond raw dollar savings',
                                                'Build a simple weighted scoring matrix to compare candidate projects',
                                                'Explain why feasibility and data availability matter as much as '
                                                'financial impact'],
                        'full_explanation': 'Running the numbers: weight-consistency scores financial impact 5/5 '
                                            '(largest figure, tied to a lost named contract), alignment 5/5 (the CEO '
                                            'is personally accountable for this exact failure), feasibility 4/5 (audit '
                                            'data already exists), data availability 4/5 (daily line data already '
                                            'collected). Changeover-time scores respectably but without urgency '
                                            '(impact 2/5, alignment 3/5). The website redesign scores poorly on impact '
                                            '(1/5 — no figure exists) and alignment (1/5 — no tracked metric), '
                                            "regardless of how loudly it's championed in the room.\n"
                                            '\n'
                                            'The weighted math confirms what intuition suggests, but now with a '
                                            'documented, defensible number attached — which matters the next time '
                                            'someone in leadership asks why weight-consistency got priority over a '
                                            'popular internal request. Without a formal method, project selection '
                                            'tends to reward whoever has the most organizational influence, not '
                                            'necessarily the project that will do the most good.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why does a scoring matrix help even when the "obvious" '
                                                         'answer seems clear?',
                                             'options': [{'key': 'a',
                                                          'text': 'It documents a defensible method rather than '
                                                                  'relying on who argues most persuasively *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'It always produces a surprising result *(often '
                                                                  'confirms intuition — the value is defensibility)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'It removes the need for leadership approval '
                                                                  '*(approval is still required)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It only matters with 5+ candidates *(useful even '
                                                                  'with two or three)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why does the website redesign score poorly on strategic '
                                                         'alignment?',
                                             'options': [{'key': 'a',
                                                          'text': "It doesn't map to any metric leadership already "
                                                                  'tracks, regardless of internal enthusiasm '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "The marketing director isn't senior enough to "
                                                                  'propose projects *(not the stated issue)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Website projects are always excluded *(too absolute '
                                                                  '— one tied to a real tracked metric could score '
                                                                  'well)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It costs too much money *(no cost figure was even '
                                                                  'given)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': "What's the risk of skipping formal selection criteria?",
                                             'options': [{'key': 'a',
                                                          'text': 'Selection can default to whoever has the most '
                                                                  'influence, not the most impact *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Projects always fail without a matrix '
                                                                  '*(overstated)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Leadership always refuses unscored projects *(not '
                                                                  'universally true)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'A matrix guarantees success *(it improves odds; it '
                                                                  "doesn't guarantee outcomes)*",
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Score candidates on financial impact, alignment, feasibility, data availability, '
                                    'and risk — not gut feeling.',
                                    'A weighted matrix makes selection defensible and limits the influence of whoever '
                                    'argues loudest.',
                                    "Internal enthusiasm isn't the same as strategic alignment."],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Define Phase (Full Module, 8 Lessons)'},
                       {'code': 'G07',
                        'title': 'Voice of the Customer',
                        'opening_question': "Golden Crust's grocery client didn't just reject loaves informally — "
                                            'their contract specifies "500g ± 2g, verified by random audit, maximum '
                                            '0.5% failure rate before penalty clauses apply." If the project team only '
                                            'interviews their own shift supervisors about the problem, what critical '
                                            'requirement source are they missing entirely?',
                        'concepts': ['The contract itself is a VOC source — arguably the most authoritative one '
                                     "available, since it's already documented and negotiated.",
                                     '**Socratic prompt:** Shift supervisors believe "a gram or two doesn\'t matter." '
                                     'The contract specifies a 0.5% failure threshold with real financial penalties. '
                                     'Whose definition of "acceptable" should the project target?',
                                     'CTQ tree: broad need ("meet contract terms") → driver ("consistent loaf weight") '
                                     '→ measurable spec ("500g ± 2g, ≤0.5% out-of-tolerance").'],
                        'terms': ['Voice of the Customer (VOC)', 'CTQ Tree'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Distinguish direct customer requirements (contract terms) from '
                                                'internal assumptions',
                                                'Translate a customer requirement into a specific CTQ',
                                                'Identify multiple VOC sources beyond a single interview'],
                        'full_explanation': 'If the team only interviews internal shift supervisors — who may '
                                            "genuinely believe small variances don't matter, based on years of "
                                            'informal practice — they risk designing the project around an assumption '
                                            "that directly contradicts the customer's documented standard. Translating "
                                            'the contract into a CTQ tree makes the target unambiguous: broad need → '
                                            '"loaf weight must be tightly controlled" → specific spec: 500g ± 2g, '
                                            '≤0.5% out-of-tolerance. Every later phase should trace back to this exact '
                                            'number, not a looser internal sense of "close enough."\n'
                                            '\n'
                                            "It's still worth gathering other VOC sources beyond the contract — prior "
                                            "complaint history, the failed audit report, and the shift supervisors' "
                                            'input — not to redefine "acceptable," but because supervisors may know '
                                            'something about *why* the variance happens that the contract document '
                                            "can't reveal on its own.",
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why is the contract language a strong VOC source?',
                                             'options': [{'key': 'a',
                                                          'text': "It's a documented, already-negotiated requirement — "
                                                                  'more authoritative than an informal internal '
                                                                  'assumption *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Contracts are never useful for VOC *(opposite is '
                                                                  'generally true when contracts specify quality terms '
                                                                  'directly)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'It replaces the need for any other VOC input '
                                                                  '*(other sources still add context, like *why* '
                                                                  'variance occurs)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "It's only relevant to Control *(VOC is gathered in "
                                                                  'Define, to set the target every later phase works '
                                                                  'toward)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': "What's the risk of only interviewing shift supervisors?",
                                             'options': [{'key': 'a',
                                                          'text': 'Their sense of "acceptable" may contradict the '
                                                                  "customer's actual documented standard *(correct)*",
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Supervisors are never a valid information source '
                                                                  '*(they can still reveal *why* variance occurs)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "Interviews aren't a legitimate VOC method *(they "
                                                                  'are — the issue is which source sets the standard)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Supervisors must sign the charter *(not the issue '
                                                                  'here)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'What does the CTQ tree accomplish?',
                                             'options': [{'key': 'a',
                                                          'text': 'Translates a broad need into an unambiguous, '
                                                                  'measurable target every phase can trace back to '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Replaces the charter *(it supports the charter, '
                                                                  "doesn't replace it)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Calculates financial return *(a separate '
                                                                  'evaluation)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Assigns blame for the defect *(CTQ trees define '
                                                                  'requirements, not fault)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ["A contract's quality terms are a strong, already-documented VOC source.",
                                    'A CTQ tree translates a broad need into a specific, measurable target.',
                                    'Multiple VOC sources each add a different piece of the picture.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Define Phase (Full Module, 8 Lessons)'},
                       {'code': 'G08',
                        'title': 'Project Management Basics',
                        'opening_question': "The project has a hard deadline: the grocery client's contract review is "
                                            'in 12 weeks. With five DMAIC phases ahead, how would you divide 12 weeks '
                                            'across them — and what happens to the whole timeline if Measure alone '
                                            'quietly runs three weeks over?',
                        'concepts': ['Rough 12-week allocation: Define (1 week), Measure (3), Analyze (3), Improve '
                                     '(3), Control (2).',
                                     "**Socratic prompt:** If Measure runs three weeks over and the deadline doesn't "
                                     "move, which later phase absorbs it — and what's likely to suffer?",
                                     '**Scope control**: keeping boundaries fixed (this SKU, this line, these shifts) '
                                     'prevents scope creep from silently extending the timeline.'],
                        'terms': ['DMAIC Timeline', 'Milestones', 'Scope Control'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Apply basic scheduling (milestones, timeline allocation) to a DMAIC '
                                                'project',
                                                'Explain why scope control protects the schedule',
                                                'Identify the practical risk of one phase running over'],
                        'full_explanation': 'If Measure runs three weeks over — say, because the team discovers the '
                                            'data collection process itself is unreliable and has to fix that first — '
                                            "the deadline doesn't move just because one phase took longer. Something "
                                            'downstream absorbs it: most commonly Control gets compressed to almost '
                                            'nothing, meaning a fix goes live without a real monitoring plan, or '
                                            'Analyze gets rushed, raising the risk of confirming the wrong root cause '
                                            'under time pressure.\n'
                                            '\n'
                                            'This is why scope control matters as much as scheduling. If the team lets '
                                            'scope quietly expand mid-project — deciding to "also check a second '
                                            'product line while we\'re at it" — that consumes time that was never '
                                            'budgeted, without ever appearing as an explicit decision anyone approved. '
                                            'Holding scope to exactly what the charter specifies is one of the most '
                                            'effective, low-cost ways to protect an already-tight schedule.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'If Measure runs three weeks over and the deadline is fixed, '
                                                         "what's the likely consequence?",
                                             'options': [{'key': 'a',
                                                          'text': 'A later phase, often Control, gets compressed to '
                                                                  'absorb the lost time *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The deadline automatically extends *(the scenario '
                                                                  "states it's fixed)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Define must be redone *(unaffected by a later '
                                                                  'overrun)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Nothing changes *(phases directly affect each other '
                                                                  'on a fixed deadline)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why is scope control described as protecting the schedule?',
                                             'options': [{'key': 'a',
                                                          'text': 'Quiet scope expansion consumes unbudgeted time '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Scope has no real timeline effect *(it directly '
                                                                  'consumes schedule time)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Scope control only matters in Control phase *(it '
                                                                  'matters throughout)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Charter scope can change freely with no consequence '
                                                                  '*(changes have real time costs)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why is rushing Analyze under time pressure risky?',
                                             'options': [{'key': 'a',
                                                          'text': 'It raises the risk of confirming the wrong root '
                                                                  'cause without adequate verification *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Analyze has no bearing on whether the fix works '
                                                                  "*(root-cause accuracy directly determines the fix's "
                                                                  'validity)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Analyze is designed to be rushed *(no such '
                                                                  'standard)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It only affects Control, not Improve *(a wrong root '
                                                                  'cause undermines Improve directly)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Divide the DMAIC timeline into rough phase allocations with milestones against a '
                                    'hard deadline.',
                                    "An overrun in an early phase gets absorbed downstream, often at that phase's "
                                    'expense.',
                                    'Holding scope to exactly what the charter specifies protects the schedule.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Define Phase (Full Module, 8 Lessons)'},
                       {'code': 'G09',
                        'title': 'Management and Planning Tools',
                        'opening_question': 'The team has gathered dozens of loose comments — "the scale in bay 3 '
                                            'seems off," "night shift mixes dough differently," "boxes sometimes '
                                            'underfilled." Before jumping to root-cause analysis, how would you '
                                            'organize this pile into something actionable?',
                        'concepts': ['**Affinity diagram**: sorts unstructured observations into natural groupings '
                                     'that emerge from the data, rather than a predetermined category list.',
                                     '**Socratic prompt:** A fishbone diagram sorts causes into predetermined '
                                     'categories. An affinity diagram lets groupings emerge. Which fits better as a '
                                     '*first* step for this messy list?',
                                     '**Prioritization matrix**: scores competing clusters against weighted criteria '
                                     '(impact, feasibility) to decide what to investigate first.'],
                        'terms': ['Affinity Diagram', 'Prioritization Matrix'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Apply an affinity diagram to organize unstructured input',
                                                'Apply a prioritization matrix to rank competing causes or ideas',
                                                'Explain when these tools fit better than jumping straight to a '
                                                'fishbone diagram'],
                        'full_explanation': "The comments don't obviously sort into fixed fishbone categories without "
                                            'some forcing. An affinity diagram lets the team cluster related '
                                            'observations organically — here, likely into "equipment/calibration" (the '
                                            'scale), "shift-to-shift process variation" (night-shift mixing), and '
                                            '"packaging line issues" (underfilled boxes) — a structure that emerged '
                                            'from the data, not one imposed in advance.\n'
                                            '\n'
                                            'Once those clusters exist, a prioritization matrix — scoring each against '
                                            'weighted impact and feasibility — gives the team a defensible next step, '
                                            'rather than chasing whichever comment was mentioned most recently. Use an '
                                            "affinity diagram when categories aren't yet obvious; use a fishbone "
                                            'diagram once a specific effect and known categories are already in hand.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why might an affinity diagram fit better than a fishbone '
                                                         'diagram here?',
                                             'options': [{'key': 'a',
                                                          'text': "Comments don't fit predetermined categories; "
                                                                  'groupings should emerge from the data *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Affinity diagrams are always used first regardless '
                                                                  'of situation *(depends on whether categories are '
                                                                  'known)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "Fishbone diagrams only apply in Improve *(they're "
                                                                  'common in Analyze and elsewhere)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Affinity diagrams eliminate further root-cause work '
                                                                  "*(they organize input; don't confirm cause)*",
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What does a prioritization matrix decide?',
                                             'options': [{'key': 'a',
                                                          'text': 'Which cluster to investigate first, based on '
                                                                  'weighted criteria *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Which employee is at fault *(ranks issues, not '
                                                                  'people)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The exact statistical root cause *(requires further '
                                                                  'investigation)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "The project's total budget *(unrelated)*",
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'When does a fishbone diagram fit better than an affinity '
                                                         'diagram?',
                                             'options': [{'key': 'a',
                                                          'text': 'When a specific effect and known categories are '
                                                                  'already in hand *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'When input is completely unstructured *(affinity '
                                                                  'diagram fits better there)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "They can never be used together *(they're often "
                                                                  'used in sequence)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Only in manufacturing *(used across service '
                                                                  'settings too)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Affinity diagrams organize unstructured input into natural, emergent groupings.',
                                    'Prioritization matrices rank competing causes against weighted criteria.',
                                    'Choose the tool based on whether categories are already known.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Define Phase (Full Module, 8 Lessons)'},
                       {'code': 'G10',
                        'title': 'Business Results for Projects',
                        'opening_question': 'Six months after project closure, the CFO asks in a board meeting: "did '
                                            'we actually get the $650,000 back, or did the team just get good at '
                                            'hitting a number on a chart?" How do you make the project\'s business '
                                            'results verifiable enough to answer that with confidence?',
                        'concepts': ["**Hard savings**: verifiable, like the actual renewed contract's revenue.",
                                     '**Soft savings**: real but harder to verify, like "reduced supervisor stress."',
                                     '**Socratic prompt:** If loaf-weight variance is now within tolerance but the '
                                     "contract still isn't renewed, has the project delivered its claimed $650,000?"],
                        'terms': ['Hard Savings', 'Soft Savings', 'Benefits Verification'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Distinguish hard savings from soft savings',
                                                'Explain why financial benefits should be verified with Finance, not '
                                                'self-reported',
                                                'Connect a technical metric to an actual business result'],
                        'full_explanation': "A technical win (weight within tolerance) doesn't automatically guarantee "
                                            'the claimed business result, if renewal depends on more than one factor — '
                                            'say, a separate delivery-reliability dispute. This is why business '
                                            'results should be tracked as distinct from the technical metric. The '
                                            "CFO's skepticism is legitimate, and the way to answer it is joint "
                                            'verification with Finance, using standards Finance already trusts: did '
                                            'the contract actually renew, at what value, and does the fix hold up a '
                                            'full quarter later — not just at the moment the team declares victory.\n'
                                            '\n'
                                            'A renewed contract is about as clean a hard saving as exists. A soft '
                                            "benefit — like reduced supervisor stress — may be real, but shouldn't be "
                                            'added to the $650,000 headline as if equally verifiable; doing so risks '
                                            'the whole claim looking inflated on close examination.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why verify financial benefits jointly with Finance?',
                                             'options': [{'key': 'a',
                                                          'text': 'It uses standards Finance already trusts, making '
                                                                  'the claim credible *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Teams are legally barred from self-reporting *(no '
                                                                  "such rule; it's about credibility)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Finance always overturns estimates *(not the point '
                                                                  '— independent verification is)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It removes the need for a charter *(unrelated)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What distinguishes hard from soft savings?',
                                             'options': [{'key': 'a',
                                                          'text': 'Hard savings are directly verifiable in the P&L; '
                                                                  'soft savings are real but harder to price '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "Hard savings are always larger *(size isn't the "
                                                                  'distinguishing factor)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Soft savings should be excluded entirely *(they can '
                                                                  'be noted, just not added to the hard figure)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "There's no real difference *(the distinction "
                                                                  'affects reporting confidence)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': "What's the risk if the metric improves but the contract "
                                                         "isn't renewed?",
                                             'options': [{'key': 'a',
                                                          'text': 'The project may hit its technical target without '
                                                                  'delivering the claimed business result *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "This can't happen once the metric improves *(it "
                                                                  'can, if other factors are involved)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The metric becomes irrelevant *(it may still '
                                                                  'represent real improvement)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Finance must fix the root cause *(Finance verifies '
                                                                  'the claim, not the technical fix)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Track business results as distinct from the technical metric.',
                                    'Verify financial benefits jointly with Finance.',
                                    'Keep hard and soft savings clearly distinguished.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Define Phase (Full Module, 8 Lessons)'},
                       {'code': 'G11',
                        'title': 'Team Dynamics and Performance',
                        'opening_question': 'The project team includes the Line 2 shift supervisor who was on shift '
                                            'when the audit failed. In the first meeting she stays silent, later '
                                            'telling a colleague: "they basically brought me in to blame me." What '
                                            'should the Green Belt actually do about this?',
                        'concepts': ['A team member who feels blamed tends to quietly withhold information rather than '
                                     'object openly.',
                                     '**Socratic prompt:** If she knows something relevant about night-shift mixing '
                                     'but stays quiet, what does that cost the project — and would anyone even know '
                                     'something was missing?',
                                     'Reset: explicitly separate "understanding what happened" from "assigning blame," '
                                     'led by the Green Belt directly, since it needs organizational weight behind it.'],
                        'terms': ['Team Dynamics', 'Root-Cause Data Quality'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Recognize signs a team member feels blamed rather than included',
                                                'Apply steps to reset a team member\'s role from "suspect" to '
                                                '"contributor"',
                                                'Explain why team dynamics directly affect data quality, not just '
                                                'morale'],
                        'full_explanation': "A team member who feels blamed doesn't announce she's withholding "
                                            'information — she simply stops volunteering it, and the gap is invisible '
                                            "because there's no obvious place it would have appeared. The fix is a "
                                            'deliberate reset, not a vague team-building gesture: the Green Belt '
                                            'explicitly separating understanding from blame, directly — "we\'re not '
                                            "here to find fault, we're here because you know things about that shift "
                                            'nobody else does, and we need that."\n'
                                            '\n'
                                            "This matters beyond morale because the project's root-cause accuracy "
                                            'depends on exactly this kind of frontline knowledge. If the "night shift '
                                            'mixes dough differently" comment from Lesson 05 came from someone else, '
                                            'and the person who actually knows *why* stays quiet, the project may '
                                            'investigate the wrong explanation entirely.',
                        'knowledge_check': [{'number': 1,
                                             'question': "What's the main risk of a team member feeling blamed?",
                                             'options': [{'key': 'a',
                                                          'text': 'She may quietly withhold information the team never '
                                                                  'realizes is missing *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "She'll openly refuse to attend meetings *(the risk "
                                                                  'is subtler — quiet disengagement)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The charter must be rewritten *(unrelated to this '
                                                                  'issue)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'The CEO must be informed immediately *(not the '
                                                                  'appropriate first response)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why should the Green Belt, specifically, reset the '
                                                         'situation?',
                                             'options': [{'key': 'a',
                                                          'text': 'Direct reassurance from the project lead carries '
                                                                  "more weight than a peer's *(correct)*",
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "Peers can't speak in meetings *(no such rule)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Only the Green Belt may talk to supervisors '
                                                                  '*(overstated)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'The CEO must approve team communication '
                                                                  '*(unnecessary escalation)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why does this matter beyond morale?',
                                             'options': [{'key': 'a',
                                                          'text': 'A disengaged team member is a silent gap in '
                                                                  'frontline knowledge that can misdirect root-cause '
                                                                  'conclusions *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'It only affects happiness, not the technical '
                                                                  'outcome *(the scenario shows it can affect root '
                                                                  'cause directly)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'It only matters if formally complained about *(the '
                                                                  'risk exists regardless)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "It's outside the Green Belt's responsibility "
                                                                  '*(managing this is part of the role)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['A blamed team member tends to withhold information quietly rather than object.',
                                    'The Green Belt should explicitly separate understanding from blame, directly.',
                                    'Team dynamics directly affect root-cause accuracy, not just morale.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Define Phase (Full Module, 8 Lessons)'},
                       {'code': 'G12',
                        'title': 'Case Study: The Golden Crust Define Phase, Completed',
                        'opening_question': 'Review this charter and identify one thing a rigorous Define phase should '
                                            'still catch before moving to Measure. (Consider: is there a named project '
                                            'champion?',
                        'concepts': [],
                        'terms': [],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': [],
                        'full_explanation': '**Problem Statement:** Between March and April, the whole-wheat sandwich '
                                            "loaf (SKU #4021) on packaging Line 2 exceeded the grocery client's "
                                            'contracted weight tolerance (500g ± 2g) above the 0.5% contractual '
                                            "penalty threshold, resulting in the client's non-renewal notice dated May "
                                            '3.\n'
                                            '\n'
                                            '**Goal Statement:** Reduce the out-of-tolerance rate for SKU #4021 on '
                                            'Line 2 to below 0.1% by end of Q3, verified over a full production month, '
                                            'to support contract renewal.\n'
                                            '\n'
                                            '**Scope:** SKU #4021 only, Line 2 only, all three shifts. Out of scope: '
                                            'other SKUs, Line 1.\n'
                                            '\n'
                                            '**CTQ:** Loaf weight 500g ± 2g, ≤0.1% out-of-tolerance (tighter than the '
                                            "client's own 0.5%, to rebuild trust with margin).\n"
                                            '\n'
                                            '**Team:** Green Belt (lead), Line 2 shift supervisor (all shifts), a '
                                            'quality auditor, the maintenance lead (for the scale-calibration lead '
                                            "from Lesson 05's affinity diagram).\n"
                                            '\n'
                                            '**Selection rationale:** Highest weighted score from Lesson 02 — impact '
                                            '5/5, alignment 5/5, feasibility 4/5, data availability 4/5.\n'
                                            '\n'
                                            '**Exercise:** Review this charter and identify one thing a rigorous '
                                            'Define phase should still catch before moving to Measure. (Consider: is '
                                            'there a named project champion? Does the charter explain *why* the '
                                            'maintenance lead specifically was included, given the affinity diagram '
                                            'grouped calibration separately from shift-related causes? A strong '
                                            "charter should connect each team member's presence to a specific, "
                                            'already-identified thread of the investigation — not just "seemed '
                                            'relevant.")',
                        'knowledge_check': [],
                        'summary': [],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Define Phase (Full Module, 8 Lessons)'},
                       {'code': 'G13',
                        'title': 'Measure Phase',
                        'opening_question': "The Define charter set a goal: get SKU #4021's out-of-tolerance rate "
                                            'below 0.1%. But nobody yet knows what the *current* out-of-tolerance rate '
                                            'actually is — only that it was "high enough to lose a contract." Before '
                                            'Golden Crust can prove any improvement, what does the team need to '
                                            "establish first, and why can't Analyze or Improve begin without it?",
                        'concepts': ['**Baseline**: a confirmed, current-state measurement of the CTQ metric, using '
                                     'real collected data — not an estimate or impression.',
                                     '**Socratic prompt:** If the team estimates the current out-of-tolerance rate '
                                     'from memory ("feels like maybe 2%") instead of measuring it, what happens if the '
                                     "real number turns out to be 4%, or 0.8%? Does the project's urgency, or its "
                                     'later "improvement," mean the same thing either way?',
                                     'Measure\'s deliverable answers "how big is the problem, really" — without it, no '
                                     "later claim of improvement can be verified, since there's no confirmed starting "
                                     'point to compare against.'],
                        'terms': ['Baseline', 'Measure Phase Deliverable'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain what a "baseline" is and why establishing it is Measure\'s '
                                                'core deliverable',
                                                'Describe the risk of skipping straight to root-cause analysis without '
                                                'a verified baseline',
                                                'Identify what "verified" data collection means in this context'],
                        'full_explanation': 'It\'s tempting to treat the Define-phase goal ("below 0.1%") as enough to '
                                            'start fixing things — but without a verified baseline, the team has no '
                                            'way to prove, later, that anything actually improved. If the real '
                                            'starting point turns out to be 4% (a serious problem) rather than the '
                                            'assumed 2%, the team may be underestimating how much work Analyze and '
                                            'Improve actually need to do. If it turns out to be 0.8%, the team may '
                                            'have overestimated the urgency and misjudged how large a fix is '
                                            'warranted.\n'
                                            '\n'
                                            'This matters beyond just accuracy for its own sake: at the very end of '
                                            'the project, when the team reports "we reduced the out-of-tolerance rate '
                                            'from X% to 0.08%," that claim is only as credible as the verified X% '
                                            "baseline it's being compared against. A baseline based on memory or "
                                            'impression can be challenged by anyone skeptical of the results — '
                                            'including, eventually, the CFO from the Define-phase Lesson 06 case, who '
                                            'already made clear he expects verifiable numbers, not confident-sounding '
                                            'claims.',
                        'knowledge_check': [{'number': 1,
                                             'question': "Why can't Analyze begin meaningfully without a verified "
                                                         'baseline?',
                                             'options': [{'key': 'a',
                                                          'text': "There's no confirmed starting point to measure "
                                                                  'root-cause impact against, or to prove later '
                                                                  'improvement *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "Analyze doesn't require any data at all *(Analyze "
                                                                  'depends heavily on data, starting with the '
                                                                  'baseline)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Baselines are only needed for the Control phase '
                                                                  "*(they're needed from Measure onward)*",
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'The CEO must personally approve the baseline number '
                                                                  '*(not a stated requirement — the issue is '
                                                                  'verification, not sign-off)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': "What's the risk of estimating the current defect rate from "
                                                         'memory rather than measuring it?',
                                             'options': [{'key': 'a',
                                                          'text': 'The estimate could be significantly wrong, '
                                                                  'misjudging how large a problem actually needs to be '
                                                                  'solved *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Estimates are always more accurate than '
                                                                  'measurements *(the opposite is the concern here)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Memory-based estimates are required by the DMAIC '
                                                                  'method *(not required — DMAIC specifically calls '
                                                                  'for measured data)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'This only matters if the CEO asks directly *(the '
                                                                  'risk exists regardless of who asks)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': "Why does Measure's deliverable matter to a final project "
                                                         'report?',
                                             'options': [{'key': 'a',
                                                          'text': 'A claimed improvement is only as credible as the '
                                                                  "verified baseline it's compared against *(correct)*",
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "Final reports don't reference the baseline at all "
                                                                  '*(they typically depend on it directly for '
                                                                  'before/after comparison)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Only Finance needs the baseline number *(the whole '
                                                                  'team, and leadership, rely on it)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'The baseline can be updated retroactively after the '
                                                                  'project ends *(a baseline established after the '
                                                                  "fact isn't a real baseline)*",
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['A baseline is a confirmed, measured starting point — not an estimate.',
                                    'Later claims of improvement are only as credible as the verified baseline behind '
                                    'them.',
                                    'Measure answers "how big is the problem, really," setting up everything that '
                                    'follows.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Measure Phase (Full Module, 8 Lessons)'},
                       {'code': 'G14',
                        'title': 'Process Analysis and Documentation',
                        'opening_question': 'When the team walks packaging Line 2 to map the process step by step, '
                                            'they discover the official process document says loaves are weighed '
                                            'automatically at the end of the line — but night shift, due to a broken '
                                            'auto-weigher, has been manually re-checking every tenth loaf for the past '
                                            'two months instead, a workaround nobody documented or told day shift '
                                            'about. What does this discovery reveal about the value of process mapping '
                                            'over trusting official documentation alone?',
                        'concepts': ['**Process mapping**: walking and documenting what actually happens, step by '
                                     'step, rather than relying on what a procedure document says should happen.',
                                     '**Socratic prompt:** If this gap between "documented process" and "actual '
                                     'process" existed for two full months without anyone flagging it upward, what '
                                     'does that suggest about what else might be undocumented across the other two '
                                     'shifts?',
                                     "A workaround like manual re-checking of every tenth loaf isn't inherently wrong "
                                     "— but if it's inconsistent, undocumented, and not equally applied across shifts, "
                                     "it becomes a hidden source of variation the team wouldn't find just by reading a "
                                     'procedure manual.'],
                        'terms': ['Process Mapping', 'Documented vs. Actual Process'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Apply basic process mapping to document the actual (not assumed) '
                                                'process',
                                                'Explain why undocumented workarounds are a common, hidden source of '
                                                'variation',
                                                'Use process documentation findings as an early lead before formal '
                                                'data collection begins'],
                        'full_explanation': 'This is exactly the kind of finding process mapping is designed to '
                                            'surface: the official documentation describes a fully automated '
                                            'weigh-check, but reality on night shift has been a partial, manual '
                                            "substitute for two months, invisible to anyone who didn't actually walk "
                                            "the floor and ask what's really happening. If the team had instead relied "
                                            'only on the written procedure, they would have proceeded assuming full '
                                            'automated coverage across all three shifts — a false assumption that '
                                            'could derail every subsequent Measure-phase calculation.\n'
                                            '\n'
                                            'The discovery also raises an important question before any further data '
                                            'collection: if this significant a gap went unreported for two months, '
                                            "what else might differ shift to shift that nobody's mentioned yet? This "
                                            'is precisely why process mapping happens early in Measure, before '
                                            'finalizing a data collection plan — a plan built on the documented '
                                            'process alone might unintentionally collect inconsistent data (some '
                                            'loaves fully weighed, some only 1-in-10 checked) without the team '
                                            'realizing the sampling itself is uneven across shifts.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What did process mapping reveal that reading the official '
                                                         'documentation alone would have missed?',
                                             'options': [{'key': 'a',
                                                          'text': 'Night shift has been manually re-checking only '
                                                                  '1-in-10 loaves for two months, unlike the '
                                                                  'documented full automated check *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "The scale needs replacement *(that's a separate, "
                                                                  'related concern raised elsewhere, not what mapping '
                                                                  'revealed here)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The grocery contract terms *(unrelated to this '
                                                                  'specific finding)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "The CEO's approval process *(unrelated)*",
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why does this finding matter before finalizing a data '
                                                         'collection plan?',
                                             'options': [{'key': 'a',
                                                          'text': 'A plan based on the documented process alone might '
                                                                  'collect inconsistent data without the team '
                                                                  'realizing sampling is uneven across shifts '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'It has no bearing on data collection, only on team '
                                                                  'morale *(it directly affects what data collection '
                                                                  'can assume about coverage)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'It confirms the documented process is accurate *(it '
                                                                  'shows the opposite — a real gap between documented '
                                                                  'and actual process)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It means data collection should be skipped entirely '
                                                                  '*(the opposite — it makes careful data collection '
                                                                  'more important, not less)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'What does the two-month duration of this undocumented gap '
                                                         'suggest?',
                                             'options': [{'key': 'a',
                                                          'text': 'Other undocumented differences may exist across '
                                                                  "shifts that haven't been mentioned yet *(correct)*",
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'This is the only possible gap between documentation '
                                                                  'and practice *(a reasonable next step is to check '
                                                                  'for more, not assume this is isolated)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Night shift staff should be immediately disciplined '
                                                                  '*(not the stated concern — the issue is '
                                                                  'documentation and process consistency)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'The auto-weigher was never actually broken *(the '
                                                                  'scenario states it was broken, prompting the '
                                                                  'workaround)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Process mapping documents what actually happens, not just what a procedure says '
                                    'should happen.',
                                    'Undocumented workarounds are a common, easily missed source of variation.',
                                    'A significant undocumented gap raises the question of what else might differ '
                                    'across shifts.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Measure Phase (Full Module, 8 Lessons)'},
                       {'code': 'G15',
                        'title': 'Probability and Statistics',
                        'opening_question': 'A quality auditor pulls 30 loaves from Line 2 and finds an average weight '
                                            'of 501.2g with a standard deviation of 3.1g. The contract tolerance is '
                                            '500g ± 2g (i.e., 498g–502g). Just from the average alone, does this '
                                            'process look fine — and what does the standard deviation actually tell '
                                            "you that the average can't?",
                        'concepts': ['**Mean**: the average value. **Standard deviation**: a measure of how spread out '
                                     'individual values are around that average.',
                                     '**Socratic prompt:** The tolerance width is only 4g total (498–502g), and the '
                                     'standard deviation here is 3.1g — larger than half the tolerance width. What '
                                     'does that suggest about how much of the distribution likely falls outside spec, '
                                     'even though the average (501.2g) looks deceptively close to the 500g target?',
                                     'The empirical rule (for roughly normal data): about 68% of values fall within 1 '
                                     'standard deviation of the mean, about 95% within 2 standard deviations.'],
                        'terms': ['Mean', 'Standard Deviation', 'Empirical Rule'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'Sample standard deviation',
                                  'formula': 's = √s²',
                                  'explanation': 'Expresses process spread in the original measurement units.',
                                  'variables': 's = sample standard deviation; s² = sample variance; √ = square-root '
                                               'operation.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain mean and standard deviation as basic descriptive statistics',
                                                'Understand why the average alone can hide variation risk',
                                                'Apply basic probability reasoning to a real sample'],
                        'full_explanation': "An average of 501.2g looks reassuring at first glance — it's only 1.2g "
                                            'off the 500g target, well within the ±2g tolerance on its own. But the '
                                            'average describes only the center of the distribution, not its spread, '
                                            "and the standard deviation here (3.1g) is doing the real damage: it's "
                                            'larger than half of the entire 4-gram tolerance window. That means a '
                                            'substantial share of individual loaves are landing well outside the '
                                            '498–502g range, even though the *average* of all loaves looks fine.\n'
                                            '\n'
                                            'Using the empirical rule roughly: if the true mean is 501.2g and standard '
                                            'deviation is 3.1g, one standard deviation below the mean is already at '
                                            '498.1g — right at the edge of the lower tolerance limit — and one '
                                            'standard deviation above is 504.3g, already outside the upper limit. This '
                                            'means significantly more than half the distribution is likely landing '
                                            'outside tolerance on the high side alone, once you account for the full '
                                            'spread rather than just the average. This is exactly the trap a Green '
                                            'Belt needs to avoid: reporting "the average looks fine" without also '
                                            'reporting the spread is a genuinely misleading summary of the same data.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why is reporting the average alone (501.2g) potentially '
                                                         'misleading here?',
                                             'options': [{'key': 'a',
                                                          'text': 'The standard deviation (3.1g) is larger than half '
                                                                  'the tolerance width, meaning many individual loaves '
                                                                  'likely fall outside spec despite the average '
                                                                  'looking close to target *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The average is always the most important number '
                                                                  'regardless of spread *(this scenario shows exactly '
                                                                  "why that's not true)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'A standard deviation of 3.1g is always considered '
                                                                  "excellent *(it's large relative to a 4g-wide "
                                                                  'tolerance, which is the actual concern)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Averages cannot be calculated from small samples '
                                                                  '*(a 30-loaf sample can support a basic average and '
                                                                  'standard deviation calculation)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What does the empirical rule roughly tell you about a mean '
                                                         'of 501.2g and SD of 3.1g against a 498–502g tolerance?',
                                             'options': [{'key': 'a',
                                                          'text': 'One standard deviation above the mean (504.3g) '
                                                                  'already exceeds the upper limit, suggesting a large '
                                                                  'share of loaves fall outside tolerance *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'All loaves are guaranteed to fall within tolerance '
                                                                  '*(the math suggests the opposite)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The empirical rule only applies to samples larger '
                                                                  "than 1,000 *(it's a general approximation usable "
                                                                  'even with smaller samples, with appropriate '
                                                                  'caution)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Standard deviation has no relationship to tolerance '
                                                                  "limits *(it's directly relevant to how much of the "
                                                                  'distribution falls within a spec window)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'What is the practical lesson for a Green Belt reporting this '
                                                         'kind of data?',
                                             'options': [{'key': 'a',
                                                          'text': 'Report both the average and the spread (standard '
                                                                  'deviation) — the average alone can hide a serious '
                                                                  'tolerance problem *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Only the average needs to be reported to leadership '
                                                                  "*(this exact scenario shows why that's misleading)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Standard deviation is only relevant in the Analyze '
                                                                  "phase *(it's directly relevant here, in Measure, to "
                                                                  'understanding baseline capability)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'A 30-loaf sample is too small to calculate any '
                                                                  "statistics *(it's sufficient for a basic "
                                                                  'descriptive baseline, discussed further in Lesson '
                                                                  '04)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['The mean describes the center; the standard deviation describes the spread — both '
                                    'are needed to understand real risk against a tolerance.',
                                    'A tight-looking average can still hide a large share of individual values falling '
                                    'outside spec.',
                                    'The empirical rule gives a rough sense of how much of a distribution falls within '
                                    'a given range.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Measure Phase (Full Module, 8 Lessons)'},
                       {'code': 'G16',
                        'title': 'Collecting and Summarizing Data',
                        'opening_question': 'Building on the 30-loaf sample from Lesson 03, the auditor now wants a '
                                            "full baseline. Should she sample from just day shift, since it's most "
                                            'convenient, or does the plan need to include all three shifts — and why '
                                            "does it matter, given what Lesson 02 already revealed about night shift's "
                                            'workaround?',
                        'concepts': ['**Stratified sampling**: deliberately sampling across known subgroups (here, all '
                                     "three shifts) rather than sampling only where it's convenient.",
                                     '**Socratic prompt:** If data is only collected from day shift, and the real '
                                     'problem is concentrated on night shift (given the broken auto-weigher workaround '
                                     'from Lesson 02), what would the baseline look like — falsely reassuring, or '
                                     'accurately alarming?',
                                     '**Operational definition**: agreeing exactly what counts as "out of tolerance" '
                                     '(which scale, what rounding rule, measured at what point in the process) so '
                                     'different people collecting data get consistent results.'],
                        'terms': ['Stratified Sampling', 'Operational Definition'],
                        'math': [{'name': 'Sample standard deviation',
                                  'formula': 's = √s²',
                                  'explanation': 'Expresses process spread in the original measurement units.',
                                  'variables': 's = sample standard deviation; s² = sample variance; √ = square-root '
                                               'operation.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Design a basic sampling plan that accounts for known process '
                                                'differences',
                                                'Explain the role of an operational definition in data collection',
                                                'Summarize collected data descriptively (mean, range, and basic '
                                                'shape)'],
                        'full_explanation': 'Sampling only from day shift would be more convenient — but given Lesson '
                                            "02's discovery that night shift has been operating under a two-month "
                                            'undocumented workaround, a day-shift-only baseline would almost certainly '
                                            'understate the real problem, since it would miss exactly the shift most '
                                            'likely to be driving the defect rate. A credible baseline needs '
                                            '**stratified sampling**: drawing loaves from all three shifts, in numbers '
                                            'proportional to their production volume, so the final baseline reflects '
                                            'the whole process rather than just its best-behaved segment.\n'
                                            '\n'
                                            'Before collecting this data, the team also needs an **operational '
                                            'definition**: which scale will be used for measurement (given the earlier '
                                            "discovery of a backup scale used during the auto-weigher's downtime, this "
                                            'matters directly), what counts as "out of tolerance" (strictly outside '
                                            '498–502g, or with some rounding allowance), and at what point in the '
                                            'process the loaf is weighed (immediately after baking, or after cooling, '
                                            'since loaves can lose moisture weight as they cool). Without this '
                                            'agreement, two different people collecting data — say, one auditor and '
                                            'one shift supervisor — could reasonably produce different counts from the '
                                            'exact same physical loaves, simply because they were applying different '
                                            'unstated rules.\n'
                                            '\n'
                                            'Once collected consistently, the data can be summarized descriptively: '
                                            'not just the overall mean and standard deviation, but broken out by '
                                            'shift, which is exactly what will let the team confirm or rule out the '
                                            "suspicion that night shift's workaround is a major driver — setting up "
                                            'the distribution check in the very next lesson.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why would a day-shift-only sample likely understate the real '
                                                         'defect rate?',
                                             'options': [{'key': 'a',
                                                          'text': 'It would miss night shift, the segment most likely '
                                                                  'driving the problem given the undocumented '
                                                                  'workaround *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Day shift always produces more defects than other '
                                                                  'shifts *(the scenario suggests the opposite '
                                                                  'concern)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "Sample size doesn't matter as long as it's "
                                                                  'convenient *(convenience sampling here risks '
                                                                  'missing the real problem)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'All shifts are guaranteed to perform identically '
                                                                  '*(this is precisely the untested assumption '
                                                                  'stratified sampling avoids)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why does an operational definition matter before data '
                                                         'collection begins?',
                                             'options': [{'key': 'a',
                                                          'text': 'Without it, different people measuring the same '
                                                                  'loaves could get inconsistent results due to '
                                                                  'unstated differing assumptions *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "It's only relevant for financial data, not physical "
                                                                  'measurements *(it applies to any data collection '
                                                                  'where consistency matters)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'It replaces the need for a sampling plan *(it '
                                                                  'complements a sampling plan; both are needed)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "It's a formality with no effect on the resulting "
                                                                  'data *(inconsistent definitions produce genuinely '
                                                                  'inconsistent data)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why break out the baseline data by shift rather than just '
                                                         'reporting one overall number?',
                                             'options': [{'key': 'a',
                                                          'text': 'It lets the team test the specific suspicion that '
                                                                  "night shift's workaround is a major driver, rather "
                                                                  'than hiding that in an aggregate figure *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Shift-level data is required by the grocery '
                                                                  'contract *(not the stated reason here)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'An aggregate number is always more accurate than '
                                                                  'shift-level breakdowns *(breaking out by shift '
                                                                  'reveals patterns an aggregate would hide)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It has no analytical value beyond bookkeeping *(it '
                                                                  'directly supports the investigation building toward '
                                                                  'Analyze)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Stratified sampling ensures a baseline reflects the whole process, including '
                                    'known problem areas, not just the most convenient shift.',
                                    'An operational definition keeps data collection consistent across different '
                                    'people and instruments.',
                                    'Breaking data out by shift (not just reporting an aggregate) can reveal patterns '
                                    'the whole-process number would hide.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Measure Phase (Full Module, 8 Lessons)'},
                       {'code': 'G17',
                        'title': 'Statistical Distributions',
                        'opening_question': "The auditor's full baseline sample (300 loaves across all three shifts) "
                                            'produces a histogram that looks lopsided rather than the smooth bell '
                                            'curve expected. Why does it matter whether the loaf-weight data actually '
                                            'follows a normal distribution before calculating anything like process '
                                            'capability in Lesson 07?',
                        'concepts': ['**Normal distribution**: a symmetric, bell-shaped pattern many statistical tools '
                                     '(including the capability calculation coming in Lesson 07) assume the data '
                                     'roughly follows.',
                                     "**Socratic prompt:** Given that night shift's manual "
                                     're-weighing-every-tenth-loaf workaround means only some loaves get corrected '
                                     "before shipping, could that explain why the combined 300-loaf histogram doesn't "
                                     'look like one smooth bell curve, but something more like two overlapping '
                                     'distributions layered on top of each other?',
                                     'A lopsided or multi-peaked (bimodal) histogram often indicates the data is '
                                     'actually a mixture of two or more different underlying processes, rather than '
                                     'one process that happens to be non-normal.'],
                        'terms': ['Normal Distribution', 'Histogram', 'Bimodal Distribution'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'Cp',
                                  'formula': 'Cp = (USL − LSL) / (6σ)',
                                  'explanation': 'Potential process capability based on specification width relative '
                                                 'to process variation, without accounting for centering.',
                                  'variables': 'Cp = potential capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; σ = process standard deviation.'},
                                 {'name': 'Cpk',
                                  'formula': 'Cpk = min[(USL − μ)/(3σ), (μ − LSL)/(3σ)]',
                                  'explanation': 'Capability index that accounts for both process spread and process '
                                                 'centering.',
                                  'variables': 'Cpk = centered capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; μ = process mean; σ = process standard '
                                               'deviation; min = smaller of the two one-sided capability values.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain the normal distribution and why capability calculations '
                                                'generally assume it',
                                                'Describe how to visually check for normality using a histogram',
                                                'Interpret what a non-normal or lopsided distribution might indicate '
                                                'about the underlying process'],
                        'full_explanation': 'A lopsided histogram is a signal worth investigating before doing '
                                            'anything further with the data — not just a technical nuisance to work '
                                            "around. Given everything uncovered so far, there's a specific, testable "
                                            "hypothesis available: if night shift's workaround only corrects 1 in 10 "
                                            'loaves, the other 9 loaves per batch on night shift are shipping without '
                                            'any real weight verification at all, while day and afternoon shifts (with '
                                            'a fully functioning automated system) are being checked consistently. '
                                            "Combining all three shifts' data into one histogram could easily produce "
                                            'exactly this kind of lopsided or bimodal pattern — not because "the '
                                            'process" is inherently non-normal, but because the 300-loaf sample '
                                            'actually contains two meaningfully different sub-processes blended '
                                            'together.\n'
                                            '\n'
                                            "This distinction matters directly for Lesson 07's capability calculation, "
                                            'which assumes something close to a single, normal distribution. '
                                            "Calculating a single Cp/Cpk value across data that's actually a mixture "
                                            "of two different processes would produce a number that doesn't cleanly "
                                            'describe either sub-process — potentially masking just how much worse '
                                            "night shift's numbers really are, hidden inside a blended average. The "
                                            'appropriate next step, suggested directly by this pattern, is to split '
                                            'the histogram by shift and check normality within each shift separately, '
                                            'rather than assuming one capability number can represent all three.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What might explain the lopsided, non-bell-shaped histogram '
                                                         'in the combined 300-loaf sample?',
                                             'options': [{'key': 'a',
                                                          'text': 'The data may be a mixture of two different '
                                                                  "sub-processes — night shift's partial manual check "
                                                                  "versus the other shifts' full automated check — "
                                                                  'rather than one non-normal process *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The scale used for the sample was definitely broken '
                                                                  '*(not confirmed by this observation alone)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'All Six Sigma data is expected to look lopsided '
                                                                  '*(the opposite — normality is generally expected '
                                                                  'and useful to check)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'The sample size of 300 is too small to produce a '
                                                                  'meaningful histogram *(300 is generally a '
                                                                  'reasonable sample size for this kind of check)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why does this matter for the capability calculation planned '
                                                         'in Lesson 07?',
                                             'options': [{'key': 'a',
                                                          'text': 'Calculating one Cp/Cpk value across a mixture of '
                                                                  'two different sub-processes could mask how much '
                                                                  "worse one shift's numbers really are *(correct)*",
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "Capability calculations don't require any "
                                                                  'assumption about distribution shape *(most standard '
                                                                  'capability calculations assume something close to '
                                                                  'normal)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'This issue only affects the Control phase, not '
                                                                  "Measure *(it's directly relevant to how "
                                                                  'Measure-phase data should be analyzed)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'A lopsided histogram always means the data should '
                                                                  'be discarded entirely *(the better response is to '
                                                                  'split and re-examine the data, not discard it)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': "What's the suggested next step given this finding?",
                                             'options': [{'key': 'a',
                                                          'text': 'Split the histogram by shift and check normality '
                                                                  'within each shift separately *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Ignore the histogram shape and proceed directly to '
                                                                  "Lesson 07's calculation *(this risks a misleading "
                                                                  'combined capability number)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Discard the night-shift data entirely *(that data '
                                                                  'is exactly what needs closer examination, not '
                                                                  'removal)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Replace the sample with a new 300-loaf sample from '
                                                                  'day shift only *(this would repeat the sampling '
                                                                  'bias flagged in Lesson 04)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Many capability calculations assume data is roughly normally distributed.',
                                    'A lopsided or multi-peaked histogram often signals a mixture of different '
                                    'sub-processes, not just one non-normal process.',
                                    'Splitting data by a known subgroup (like shift) can reveal patterns a combined '
                                    'histogram hides.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Measure Phase (Full Module, 8 Lessons)'},
                       {'code': 'G18',
                        'title': 'Measurement System Analysis',
                        'opening_question': 'Before trusting any of this data, the maintenance lead mentions that Line '
                                            "2's primary scale hasn't been calibrated in 14 months, and the backup "
                                            "scale used during the auto-weigher's breakdown has never been checked "
                                            'against the primary one at all. Why should this concern come before any '
                                            'conclusions are drawn from the baseline data collected so far?',
                        'concepts': ['**MSA**: confirms how much of the variation seen in data comes from the '
                                     'measurement system itself, versus the actual process being measured.',
                                     '**Repeatability**: does the same scale, used the same way, give a consistent '
                                     'reading for the same loaf? **Reproducibility**: do different scales (or '
                                     'different people using them) agree with each other?',
                                     '**Socratic prompt:** If the backup scale reads systematically 1.5g heavier than '
                                     'the primary scale, and night shift used the backup scale for two months, how '
                                     'much of the "process variation" seen in Lesson 05\'s lopsided histogram might '
                                     'actually just be a measurement artifact — not a real difference in loaf weight '
                                     'at all?'],
                        'terms': ['Measurement System Analysis (MSA)', 'Repeatability', 'Reproducibility'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain the purpose of Measurement System Analysis (MSA)',
                                                'Describe repeatability and reproducibility at a conceptual level',
                                                'Understand why measurement variation must be ruled out before '
                                                'trusting process variation conclusions'],
                        'full_explanation': 'This is a genuinely important question to raise before drawing any '
                                            'conclusions, because an uncalibrated or unreconciled measurement system '
                                            "can manufacture the appearance of a process problem that isn't fully "
                                            'real. If the backup scale used exclusively by night shift for two months '
                                            'reads systematically 1.5g heavier than the properly calibrated primary '
                                            'scale, then some portion of what looked like "night shift has worse '
                                            'weight variation" in Lesson 05\'s data could actually be an artifact of '
                                            'using a different, uncalibrated instrument — not necessarily a real '
                                            'difference in how the dough is being mixed or baked on that shift.\n'
                                            '\n'
                                            'This is exactly what MSA is designed to catch. A basic check would '
                                            'involve having the same set of loaves weighed on both the primary and '
                                            'backup scales (testing reproducibility — do they agree with each other), '
                                            'and having the same loaf weighed multiple times on the same scale '
                                            '(testing repeatability — is the scale even consistent with itself). If '
                                            'this reveals a genuine 1.5g systematic offset between scales, the team '
                                            'can mathematically correct for it in the existing data, or, better, '
                                            'recalibrate the backup scale and recollect a clean sample — either way, '
                                            'this must happen *before* the team decides how much of the observed '
                                            'variation is a real process problem to fix versus a measurement problem '
                                            'to correct first.\n'
                                            '\n'
                                            'Skipping this step risks the Analyze phase chasing a partially fictional '
                                            "root cause — investigating why night shift's dough handling supposedly "
                                            'produces heavier loaves, when a meaningful part of that apparent '
                                            'difference might simply disappear once the measurement system itself is '
                                            'fixed.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why does an uncalibrated backup scale matter before trusting '
                                                         'the baseline data?',
                                             'options': [{'key': 'a',
                                                          'text': 'A systematic scale offset could account for part of '
                                                                  'the apparent "process difference" between shifts, '
                                                                  'without any real difference in the dough itself '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Scale calibration only affects the Control phase, '
                                                                  "not Measure *(it's directly relevant here, before "
                                                                  'drawing Measure-phase conclusions)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Backup scales are never used in real production and '
                                                                  'can be ignored *(this scenario shows they were '
                                                                  'actively used for two months)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'MSA is only relevant for the Black Belt curriculum '
                                                                  "*(it's a Green Belt Measure-phase topic as shown "
                                                                  'here)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What does "reproducibility" specifically test in this '
                                                         'scenario?',
                                             'options': [{'key': 'a',
                                                          'text': 'Whether the primary and backup scales agree with '
                                                                  'each other on the same loaves *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Whether the same scale gives a consistent reading '
                                                                  "on repeated use *(that's repeatability, a related "
                                                                  'but distinct concept)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Whether the recipe is reproducible from batch to '
                                                                  'batch *(unrelated to measurement system testing)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Whether the CEO's approval can be reproduced for "
                                                                  'future projects *(unrelated)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': "What's the risk of skipping this MSA step and proceeding "
                                                         'straight to root-cause analysis?',
                                             'options': [{'key': 'a',
                                                          'text': 'The team may investigate a partially fictional root '
                                                                  "cause, chasing a process explanation for what's "
                                                                  'actually a measurement artifact *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'There is no real risk, since MSA is optional in '
                                                                  'most projects *(MSA is a standard, important '
                                                                  'Measure-phase step precisely to avoid this risk)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Skipping MSA only affects the timeline, not the '
                                                                  'conclusions *(it can directly affect whether the '
                                                                  'conclusions themselves are valid)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'MSA only matters if the CFO specifically requests '
                                                                  "it *(it's a standard best practice regardless of "
                                                                  'who asks)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['MSA determines how much of observed variation comes from the measurement system '
                                    'itself, versus the real process.',
                                    'Repeatability checks consistency within one instrument; reproducibility checks '
                                    'agreement across instruments or people.',
                                    'Skipping MSA risks investigating a partially fictional root cause in Analyze.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Measure Phase (Full Module, 8 Lessons)'},
                       {'code': 'G19',
                        'title': 'Process and Performance Capability',
                        'opening_question': 'With the scale calibration issue now flagged and corrected, and using '
                                            'only verified, reconciled data, the team recalculates: mean = 500.4g, '
                                            'standard deviation = 1.1g, against the 500g ± 2g tolerance (USL = 502g, '
                                            'LSL = 498g). Calculate Cpk and interpret whether this process is now '
                                            'capable of meeting the contract requirement.',
                        'concepts': ['**Cp** = (USL − LSL) ÷ (6 × σ) — measures whether the tolerance width is wide '
                                     'enough for the process spread, ignoring centering.',
                                     '**Cpk** = the smaller of [(USL − mean) ÷ (3 × σ)] and [(mean − LSL) ÷ (3 × σ)] — '
                                     'accounts for both spread and centering.',
                                     '**Socratic prompt:** Before calculating anything, does a mean of 500.4g (very '
                                     'close to the 500g target) and a standard deviation of 1.1g (much smaller than '
                                     "Lesson 03's 3.1g) suggest this process has genuinely improved since the "
                                     'scale-calibration fix — or could you already guess that from the numbers alone, '
                                     'before doing the formal calculation?'],
                        'terms': ['Process Capability', 'Cp', 'Cpk'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'Sample standard deviation',
                                  'formula': 's = √s²',
                                  'explanation': 'Expresses process spread in the original measurement units.',
                                  'variables': 's = sample standard deviation; s² = sample variance; √ = square-root '
                                               'operation.'},
                                 {'name': 'Cp',
                                  'formula': 'Cp = (USL − LSL) / (6σ)',
                                  'explanation': 'Potential process capability based on specification width relative '
                                                 'to process variation, without accounting for centering.',
                                  'variables': 'Cp = potential capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; σ = process standard deviation.'},
                                 {'name': 'Cpk',
                                  'formula': 'Cpk = min[(USL − μ)/(3σ), (μ − LSL)/(3σ)]',
                                  'explanation': 'Capability index that accounts for both process spread and process '
                                                 'centering.',
                                  'variables': 'Cpk = centered capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; μ = process mean; σ = process standard '
                                               'deviation; min = smaller of the two one-sided capability values.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Calculate Cp and Cpk from real, verified data',
                                                'Interpret what a Cpk value means practically',
                                                'Connect Cpk back to sigma level and DPMO from earlier in the '
                                                'curriculum'],
                        'full_explanation': 'Working the actual numbers: Cp = (502 − 498) ÷ (6 × 1.1) = 4 ÷ 6.6 ≈ '
                                            '**0.61**. Cpk = the smaller of [(502 − 500.4) ÷ (3 × 1.1)] = 1.6 ÷ 3.3 ≈ '
                                            '0.485, and [(500.4 − 498) ÷ (3 × 1.1)] = 2.4 ÷ 3.3 ≈ 0.727. The smaller '
                                            'value, **Cpk ≈ 0.49**, is the reported capability.\n'
                                            '\n'
                                            'A Cpk of 0.49 is well below 1.0 — the commonly used minimum threshold for '
                                            'a process considered "capable" of meeting its tolerance — and far below '
                                            '1.33, a common target for a genuinely robust process. In plain terms: '
                                            'even after removing the measurement-system artifact from Lesson 06, the '
                                            "underlying process still isn't reliably hitting its target consistently "
                                            'enough to meet the 0.1% out-of-tolerance goal. This is a realistic and '
                                            'important teaching moment — fixing one real problem (the miscalibrated '
                                            'scale) improved the numbers substantially (standard deviation dropped '
                                            "from 3.1g to 1.1g) but didn't single-handedly solve the whole problem. "
                                            'Real capability work remains for the Analyze and Improve phases ahead.\n'
                                            '\n'
                                            "It's also worth connecting this back to the very first lesson of the "
                                            'whole curriculum: a Cpk around 0.49 corresponds to a sigma level '
                                            'meaningfully below 3 sigma — nowhere near the six sigma target, and a '
                                            'long way even from a merely adequate four-sigma process. This gives the '
                                            'team, and leadership, a very concrete number to track improvement against '
                                            'going into Analyze and Improve.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What is the calculated Cpk value for this process, given '
                                                         'mean = 500.4g, σ = 1.1g, USL = 502g, LSL = 498g?',
                                             'options': [{'key': 'a',
                                                          'text': '≈0.49 *(correct — the smaller of the two one-sided '
                                                                  'calculations)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': '≈0.61 *(this is the Cp value, which ignores '
                                                                  'centering — not Cpk)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': '≈0.73 *(this is only the upper-side calculation, '
                                                                  'not the smaller, binding value)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': '≈1.33 *(this would represent a robust, '
                                                                  'well-controlled process — not what this data '
                                                                  'shows)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why is Cpk (rather than just Cp) the more informative number '
                                                         'here?',
                                             'options': [{'key': 'a',
                                                          'text': 'Cpk accounts for how centered the process is, not '
                                                                  'just whether the tolerance is theoretically wide '
                                                                  'enough for the spread *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Cp and Cpk always produce the same number *(they '
                                                                  'differ here — 0.61 vs. 0.49 — precisely because the '
                                                                  "process isn't perfectly centered)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "Cpk is only relevant for Black Belt projects *(it's "
                                                                  'a standard Green Belt Measure-phase calculation, as '
                                                                  'shown here)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Cpk ignores the standard deviation entirely *(it '
                                                                  'directly depends on standard deviation, in the '
                                                                  'denominator of both one-sided calculations)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': "What does a Cpk of 0.49 suggest about the project's "
                                                         'remaining work?',
                                             'options': [{'key': 'a',
                                                          'text': 'The process, even after fixing the measurement '
                                                                  "issue, still isn't reliably capable of meeting the "
                                                                  '0.1% out-of-tolerance goal — real work remains in '
                                                                  'Analyze and Improve *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The project is essentially finished, since the '
                                                                  'measurement issue is resolved *(a Cpk well below '
                                                                  '1.0 shows real capability work remains)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Cpk values below 1.0 are considered excellent in '
                                                                  'food manufacturing *(the opposite — below 1.0 '
                                                                  'generally indicates a process not yet capable)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'This Cpk value means the standard deviation must be '
                                                                  'recalculated *(the standard deviation was already '
                                                                  'used correctly to reach this Cpk)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Cp measures whether tolerance width matches process spread; Cpk also accounts for '
                                    'centering.',
                                    'A Cpk below 1.0 generally indicates a process not yet capable of reliably meeting '
                                    'its tolerance.',
                                    'Fixing one real issue (measurement calibration) can meaningfully improve the '
                                    'numbers without single-handedly solving the whole problem.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Measure Phase (Full Module, 8 Lessons)'},
                       {'code': 'G20',
                        'title': 'Case Study: The Golden Crust Measure Phase, Completed',
                        'opening_question': 'Given Cpk = 0.49, which lever is likely to matter more for Analyze and '
                                            'Improve to focus on — recentering the process (getting the mean closer to '
                                            'exactly 500g) or reducing variation (lowering σ further)?',
                        'concepts': [],
                        'terms': [],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'Cp',
                                  'formula': 'Cp = (USL − LSL) / (6σ)',
                                  'explanation': 'Potential process capability based on specification width relative '
                                                 'to process variation, without accounting for centering.',
                                  'variables': 'Cp = potential capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; σ = process standard deviation.'},
                                 {'name': 'Cpk',
                                  'formula': 'Cpk = min[(USL − μ)/(3σ), (μ − LSL)/(3σ)]',
                                  'explanation': 'Capability index that accounts for both process spread and process '
                                                 'centering.',
                                  'variables': 'Cpk = centered capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; μ = process mean; σ = process standard '
                                               'deviation; min = smaller of the two one-sided capability values.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': [],
                        'full_explanation': '**Baseline established:** Original combined sample (Lesson 03) showed '
                                            'mean 501.2g, SD 3.1g — but this blended two sub-processes (Lesson 05) and '
                                            'included an uncorrected measurement artifact (Lesson 06). After '
                                            'stratified sampling, operational definition agreement, and scale '
                                            'reconciliation, the verified baseline is: mean 500.4g, SD 1.1g, **Cpk ≈ '
                                            '0.49**.\n'
                                            '\n'
                                            '**Exercise:** Given Cpk = 0.49, which lever is likely to matter more for '
                                            'Analyze and Improve to focus on — recentering the process (getting the '
                                            'mean closer to exactly 500g) or reducing variation (lowering σ further)? '
                                            'Work both scenarios:\n'
                                            '- *Recentering only* (mean → 500g exactly, σ stays 1.1g): Cpk = '
                                            'min[(502−500)/3.3, (500−498)/3.3] = min[0.606, 0.606] = **0.606**.\n'
                                            '- *Reducing variation only* (σ → 0.6g, mean stays 500.4g): Cpk = '
                                            'min[(502−500.4)/1.8, (500.4−498)/1.8] = min[0.889, 1.333] = **0.889**.\n'
                                            '\n'
                                            'Reducing variation produces a substantially larger capability improvement '
                                            'than recentering alone — a strong signal that Analyze and Improve should '
                                            'focus on *why* the process varies (the shift-to-shift differences and '
                                            'equipment issues already surfaced) rather than simply adjusting the '
                                            'target setpoint.',
                        'knowledge_check': [],
                        'summary': [],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Measure Phase (Full Module, 8 Lessons)'},
                       {'code': 'G21',
                        'title': 'Introduction to Analyze Phase',
                        'opening_question': 'Measure left the team with a Cpk of 0.49 and a strong signal that '
                                            'reducing variation — not just recentering — is the priority. But "reduce '
                                            'variation" isn\'t itself an actionable root cause. What specifically does '
                                            'Analyze need to produce before Improve can begin?',
                        'concepts': ["Analyze's deliverable is a **specific, evidence-backed root cause** — not a "
                                     'plausible-sounding theory the team feels confident about.',
                                     '**Socratic prompt:** The Define-phase affinity diagram (Lesson 05) already '
                                     'grouped candidate causes into equipment/calibration, shift-to-shift variation, '
                                     'and packaging line issues. Which of these are still live suspects after '
                                     "Measure's findings, and which has already been partly addressed?",
                                     "A hunch becomes a confirmed root cause only once it's tested against real data — "
                                     "Analyze's job is to run that test, not simply pick the most plausible-sounding "
                                     'story.'],
                        'terms': ['Analyze Phase Deliverable', 'Root Cause (Confirmed vs. Hunch)'],
                        'math': [{'name': 'Cp',
                                  'formula': 'Cp = (USL − LSL) / (6σ)',
                                  'explanation': 'Potential process capability based on specification width relative '
                                                 'to process variation, without accounting for centering.',
                                  'variables': 'Cp = potential capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; σ = process standard deviation.'},
                                 {'name': 'Cpk',
                                  'formula': 'Cpk = min[(USL − μ)/(3σ), (μ − LSL)/(3σ)]',
                                  'explanation': 'Capability index that accounts for both process spread and process '
                                                 'centering.',
                                  'variables': 'Cpk = centered capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; μ = process mean; σ = process standard '
                                               'deviation; min = smaller of the two one-sided capability values.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ["Explain Analyze's core deliverable: a verified, data-backed root "
                                                'cause',
                                                'Distinguish a "hunch" from a confirmed root cause',
                                                'Connect Define-phase candidate causes to what Analyze will actually '
                                                'test'],
                        'full_explanation': 'It would be easy, at this point, to declare "night shift is the problem" '
                                            'and move straight to Improve — the affinity diagram flagged '
                                            "shift-to-shift variation early, and Measure's data seemed to support it. "
                                            "But that's exactly the kind of plausible-sounding conclusion Analyze "
                                            'exists to test rigorously before anyone acts on it. The '
                                            'equipment/calibration cluster from Define has already been partly '
                                            'addressed (Lesson 06 of Measure caught and corrected a real '
                                            "scale-calibration issue) — but partly addressed isn't the same as fully "
                                            'resolved, and the remaining Cpk of 0.49 shows real variation still exists '
                                            'even after that fix.\n'
                                            '\n'
                                            'This means Analyze has genuine, still-open work to do: confirming whether '
                                            'the remaining variation really is concentrated on night shift (as '
                                            'suspected), and if so, digging into *why* — is it the dough-mixing '
                                            "difference mentioned back in Define's affinity diagram, something about "
                                            'the manual reweighing workaround itself, or something not yet considered '
                                            'at all? The next two lessons introduce the two main tools for this: '
                                            'hypothesis testing, to confirm whether an observed difference (like night '
                                            'shift vs. day shift) is statistically real rather than sample noise, and '
                                            'exploratory data analysis, to visually surface patterns a hypothesis test '
                                            'alone might miss.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why shouldn\'t the team simply declare "night shift is the '
                                                         'problem" and move to Improve immediately?',
                                             'options': [{'key': 'a',
                                                          'text': "That conclusion hasn't yet been tested against real "
                                                                  "data — it's a plausible hunch, not a confirmed root "
                                                                  'cause *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Night shift is definitely not the cause of any '
                                                                  "variation *(the scenario doesn't rule this out — it "
                                                                  "says it needs testing, not that it's false)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Analyze phase only applies to equipment issues, not '
                                                                  'shift differences *(Analyze can investigate any '
                                                                  'candidate cause, including shift-based ones)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'The affinity diagram from Define is no longer '
                                                                  'relevant *(it remains a useful source of candidate '
                                                                  'causes to test)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': "Why isn't the scale-calibration fix from Measure enough to "
                                                         'close out the equipment/calibration cluster?',
                                             'options': [{'key': 'a',
                                                          'text': 'The remaining Cpk of 0.49 shows real variation '
                                                                  'still exists even after that fix, meaning the '
                                                                  'cluster may not be fully resolved *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The scale-calibration fix had no measurable effect '
                                                                  'on the data *(Measure showed a substantial '
                                                                  'improvement — SD dropped from 3.1g to 1.1g — but '
                                                                  "the process still isn't fully capable)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Equipment issues are never relevant to Analyze '
                                                                  'phase work *(they can still be relevant if '
                                                                  "capability hasn't fully improved)*",
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'The maintenance lead must reconfirm the fix before '
                                                                  'Analyze can begin *(not the stated requirement — '
                                                                  'the issue is what the remaining data shows)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': "What is Analyze's core deliverable, as described here?",
                                             'options': [{'key': 'a',
                                                          'text': 'A specific, evidence-backed root cause, not just a '
                                                                  'plausible theory *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "A finalized control plan *(that's a Control-phase "
                                                                  'deliverable)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "A signed project charter *(that's a Define-phase "
                                                                  'deliverable)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "A calculated Cpk value *(that was Measure's "
                                                                  'deliverable, already completed)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ["Analyze's deliverable is a specific, evidence-backed root cause — not a "
                                    'plausible-sounding hunch.',
                                    "Partial progress (like the scale-calibration fix) doesn't mean a candidate cause "
                                    'cluster is fully resolved.',
                                    'Hypothesis testing and exploratory data analysis are the two main tools for '
                                    'confirming or ruling out candidate causes.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Analyze Phase (Full Module, 4 Lessons)'},
                       {'code': 'G22',
                        'title': 'Hypothesis Testing',
                        'opening_question': "The team suspects night shift's loaf weights are more variable than day "
                                            "shift's. Day shift sample: mean 500.3g, SD 0.9g, n=100. Night shift "
                                            'sample: mean 500.6g, SD 1.8g, n=100. Is this difference in variability '
                                            'real, or could it just be sample noise?',
                        'concepts': ['**Null hypothesis**: there is no real difference in variability between day and '
                                     'night shift — any observed difference is just random sample noise.',
                                     '**Alternative hypothesis**: there is a real difference in variability between '
                                     'the shifts.',
                                     '**Socratic prompt:** If a statistical test on this data returns a p-value of '
                                     "0.01, what can you conclude — and what can't you conclude — about *why* night "
                                     'shift is more variable?'],
                        'terms': ['Null Hypothesis', 'Alternative Hypothesis', 'p-value'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'Sample standard deviation',
                                  'formula': 's = √s²',
                                  'explanation': 'Expresses process spread in the original measurement units.',
                                  'variables': 's = sample standard deviation; s² = sample variance; √ = square-root '
                                               'operation.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain the null and alternative hypothesis at a conceptual level',
                                                'Apply this framework to comparing variability between two shifts',
                                                'Interpret a p-value result without overclaiming what it proves'],
                        'full_explanation': "The raw numbers look like a meaningful difference — night shift's "
                                            "standard deviation (1.8g) is double day shift's (0.9g) — but with two "
                                            "samples of 100 loaves each, there's always some chance this gap could "
                                            'arise from ordinary sample-to-sample noise rather than a genuine '
                                            "underlying difference in the two shifts' actual processes. This is "
                                            'exactly what a hypothesis test is built to check: it starts by assuming '
                                            'the null hypothesis (no real difference) and calculates how likely it '
                                            'would be to see a gap this large, purely by chance, if that null '
                                            'hypothesis were actually true.\n'
                                            '\n'
                                            "If the resulting p-value comes back at 0.01, that means there's only "
                                            'about a 1% chance of seeing a variability gap this large between two '
                                            'samples if day and night shift were genuinely performing identically — '
                                            'small enough that most practitioners would reject the null hypothesis and '
                                            "conclude the difference is statistically real, not noise. But it's "
                                            "important to be precise about what this conclusion does and doesn't "
                                            'establish: a p-value of 0.01 supports "night shift\'s variability really '
                                            'is different from day shift\'s" — it says nothing at all about *why*. It '
                                            "doesn't confirm the manual reweighing workaround is the cause, doesn't "
                                            "rule out some other unexamined factor, and doesn't quantify how much of a "
                                            'business problem this difference actually represents. Confirming that a '
                                            'real difference exists is a necessary step before investigating its cause '
                                            "— but it's not the same as identifying the cause itself, which is exactly "
                                            'why exploratory data analysis, in the next lesson, is still needed.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What does the null hypothesis represent in this comparison?',
                                             'options': [{'key': 'a',
                                                          'text': 'There is no real difference in variability between '
                                                                  'day and night shift; any observed gap is due to '
                                                                  'sample noise *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Night shift is definitely the cause of the weight '
                                                                  'problem *(that would be closer to an unproven '
                                                                  'conclusion, not the null hypothesis)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The scale calibration issue has been fully resolved '
                                                                  '*(unrelated to this specific hypothesis test)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Day shift and night shift use different recipes '
                                                                  '*(not stated or tested here)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'If the test returns p = 0.01, what can be concluded?',
                                             'options': [{'key': 'a',
                                                          'text': 'The variability difference between shifts is likely '
                                                                  'statistically real, not just sample noise '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The manual reweighing workaround has been confirmed '
                                                                  "as the specific cause *(a p-value doesn't identify "
                                                                  'the mechanism behind a confirmed difference)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The problem has been completely solved *(confirming '
                                                                  'a real difference is a step toward, not the end of, '
                                                                  'resolving the problem)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Day shift has zero variability *(day shift's SD of "
                                                                  '0.9g is low but not zero)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'What is a hypothesis test unable to tell you, even with a '
                                                         'very small p-value?',
                                             'options': [{'key': 'a',
                                                          'text': 'The underlying reason *why* the confirmed '
                                                                  'difference exists *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Whether a difference exists at all *(that is what '
                                                                  'the test is designed to assess)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Whether the samples were collected at all '
                                                                  '*(unrelated to what the test measures)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'The sample sizes used in the comparison *(those are '
                                                                  'known inputs to the test, not something it needs to '
                                                                  'reveal)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['A hypothesis test checks whether an observed difference is likely real or could '
                                    'be explained by sample noise.',
                                    'A small p-value supports rejecting the null hypothesis — concluding a real '
                                    'difference likely exists.',
                                    'Confirming a real difference exists is not the same as identifying why it '
                                    'exists.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Analyze Phase (Full Module, 4 Lessons)'},
                       {'code': 'G23',
                        'title': 'Exploratory Data Analysis',
                        'opening_question': 'A scatter plot of loaf weight against time-of-day shows a cluster of '
                                            'high-variance points specifically during the first two hours of night '
                                            'shift, tapering off later in the shift. What does this pattern suggest '
                                            'about the root cause, and how is this different from what the hypothesis '
                                            'test in Lesson 02 alone could tell you?',
                        'concepts': ['**Exploratory Data Analysis (EDA)**: visually examining data (scatter plots, box '
                                     'plots, time-series plots) to surface patterns, rather than only testing a single '
                                     'predefined hypothesis.',
                                     '**Socratic prompt:** The variance spike is concentrated in the *first two hours* '
                                     'of night shift specifically, not the whole shift evenly. What does that narrower '
                                     'pattern suggest that a simple "night shift vs. day shift" comparison couldn\'t '
                                     'reveal on its own?',
                                     'A visual pattern like this points toward a specific, testable mechanism — not '
                                     'just a broad "shift" difference, but something tied to what changes in the first '
                                     'two hours specifically.'],
                        'terms': ['Exploratory Data Analysis (EDA)', 'Scatter Plot'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Use scatter plots and box plots to visually surface patterns '
                                                "hypothesis testing alone wouldn't reveal",
                                                'Connect a visual pattern to a plausible, testable mechanism',
                                                'Explain EDA as complementary to, not a replacement for, hypothesis '
                                                'testing'],
                        'full_explanation': "Lesson 02's hypothesis test confirmed that night shift, overall, has more "
                                            "variability than day shift — but it couldn't say anything about *when "
                                            'within the shift* that variability occurs, because a standard two-group '
                                            'comparison collapses an entire shift into one summary statistic. This is '
                                            'exactly the gap EDA fills: plotting individual loaf weights against '
                                            "time-of-day reveals that the extra variability isn't spread evenly across "
                                            "all eight hours of night shift — it's concentrated specifically in the "
                                            'first two hours, tapering off as the shift continues.\n'
                                            '\n'
                                            'This narrower, more specific pattern points toward a plausible, testable '
                                            'mechanism that a blunt "night shift vs. day shift" framing would have '
                                            'missed entirely: something that changes specifically at the *start* of '
                                            'night shift and then stabilizes. Two candidates worth investigating: the '
                                            'manual reweighing backlog (if the broken auto-weigher creates a queue of '
                                            "unchecked loaves that's worst right when the shift starts and gets worked "
                                            'down over time), or dough temperature (if the proofing room cools '
                                            'overnight during the gap between afternoon and night shift, and takes '
                                            "roughly two hours to stabilize once night shift's baking begins). Either "
                                            'mechanism would produce exactly this kind of "high variance early, '
                                            'tapering off" pattern — and distinguishing between them is now a '
                                            'specific, answerable question, rather than the vague "reduce night shift '
                                            'variation" the team started with.\n'
                                            '\n'
                                            'This is the practical value of EDA alongside hypothesis testing: the '
                                            'hypothesis test confirmed *that* a real difference exists; the scatter '
                                            'plot revealed *when* it occurs, narrowing the investigation to a '
                                            'specific, testable window instead of an entire eight-hour shift.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What did the scatter plot reveal that the Lesson 02 '
                                                         'hypothesis test alone could not?',
                                             'options': [{'key': 'a',
                                                          'text': 'The extra variability is concentrated in the first '
                                                                  'two hours of night shift specifically, not spread '
                                                                  'evenly across the whole shift *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Night shift has more variability than day shift '
                                                                  '*(the hypothesis test already established this)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The scale needs recalibration *(already addressed '
                                                                  'in the Measure phase)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "The sample size was too small *(sample size wasn't "
                                                                  'the issue being tested here)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why does this narrower pattern matter for the investigation?',
                                             'options': [{'key': 'a',
                                                          'text': 'It points toward a specific, testable mechanism '
                                                                  'tied to shift-start conditions, rather than a vague '
                                                                  'overall "shift difference" *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'It rules out any equipment-related cause entirely '
                                                                  '*(a shift-start reweighing backlog is still an '
                                                                  'equipment-related candidate)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'It confirms the root cause without any further '
                                                                  'testing needed *(it narrows the investigation; it '
                                                                  "doesn't yet confirm which specific mechanism is "
                                                                  'responsible)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It has no bearing on what Improve phase should '
                                                                  'target *(a narrower root cause directly shapes what '
                                                                  'Improve phase should fix)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'What is the relationship between EDA and hypothesis testing, '
                                                         'based on this lesson?',
                                             'options': [{'key': 'a',
                                                          'text': "They're complementary — the hypothesis test "
                                                                  'confirms a real difference exists, and EDA reveals '
                                                                  'more specific patterns within it *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'EDA replaces the need for hypothesis testing '
                                                                  'entirely *(both tools contributed distinct, '
                                                                  'necessary information here)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Hypothesis testing replaces the need for EDA '
                                                                  'entirely *(the scatter plot revealed something the '
                                                                  'hypothesis test could not)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'They must always be performed in a fixed, required '
                                                                  'order *(no such strict rule — both add value '
                                                                  'regardless of sequence)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['EDA (scatter plots, box plots) reveals patterns a single aggregate hypothesis '
                                    "test can't show.",
                                    'A narrow, specific visual pattern points toward a testable mechanism, not just a '
                                    'broad category of cause.',
                                    'EDA and hypothesis testing are complementary tools, each answering a different '
                                    'question.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Analyze Phase (Full Module, 4 Lessons)'},
                       {'code': 'G24',
                        'title': 'Case Study: The Golden Crust Analyze Phase, Completed',
                        'opening_question': 'Given this specific, narrowed root cause, what should Improve phase '
                                            'actually target — and why would simply telling night-shift staff to "be '
                                            'more careful with dough temperature" likely fail as a fix?',
                        'concepts': [],
                        'terms': [],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': [],
                        'full_explanation': "**Root cause investigation, narrowed:** Lesson 02's hypothesis test "
                                            "confirmed night shift's variability is statistically real (p = 0.01). "
                                            "Lesson 03's scatter plot narrowed this further: the variance spike "
                                            'concentrates in the first two hours of night shift, pointing to two live '
                                            'candidate mechanisms — the manual reweighing backlog (tied to the '
                                            'still-unrepaired auto-weigher) and dough temperature stabilization at '
                                            'shift start (tied to overnight proofing-room cooling).\n'
                                            '\n'
                                            '**Confirming which mechanism matters:** The team pulls proofing-room '
                                            'temperature logs and finds they drop notably during the '
                                            'afternoon-to-night shift changeover gap, and take roughly two hours to '
                                            'stabilize once night-shift baking resumes — matching the variance '
                                            "pattern's timing almost exactly. Meanwhile, reviewing the manual "
                                            'reweighing log shows the backlog is roughly constant throughout the '
                                            "shift, not concentrated early — its timing pattern doesn't match the "
                                            'observed variance spike as closely.\n'
                                            '\n'
                                            '**Confirmed root cause:** Dough temperature instability during the first '
                                            'two hours of night shift, driven by proofing-room cooling during the '
                                            'shift changeover gap — not primarily the manual reweighing workaround, '
                                            "which remains a separate, still-worth-fixing issue but isn't the primary "
                                            'driver of the variance pattern.\n'
                                            '\n'
                                            '**Exercise:** Given this specific, narrowed root cause, what should '
                                            'Improve phase actually target — and why would simply telling night-shift '
                                            'staff to "be more careful with dough temperature" likely fail as a fix? '
                                            '(Consider: this is an environmental/equipment issue — proofing-room '
                                            'temperature control during a changeover gap — not a behavioral one. A fix '
                                            "aimed at the room's temperature control system, rather than staff "
                                            'behavior, is far more likely to actually work.)',
                        'knowledge_check': [],
                        'summary': [],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Analyze Phase (Full Module, 4 Lessons)'},
                       {'code': 'G25',
                        'title': 'Introduction to Improve Phase',
                        'opening_question': 'Analyze confirmed the root cause: proofing-room cooling during the shift '
                                            'changeover gap. Marco is ready to install an insulated curtain over the '
                                            'proofing room door this week and move on. What should Improve phase '
                                            'actually produce before that fix gets rolled out to every shift '
                                            'permanently?',
                        'concepts': ["Improve's deliverable is a **validated fix** — one with real data showing it "
                                     'works — not simply "a plausible idea that got installed."',
                                     '**Socratic prompt:** If Marco installs the curtain on all shifts immediately and '
                                     'declares victory without piloting it first, what risk is the team accepting?'],
                        'terms': ['Validated Solution', 'Pilot'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ["Explain Improve's deliverable: a validated solution with pilot "
                                                'evidence, not just an implemented idea',
                                                'Describe why piloting on a subset of shifts matters before full '
                                                'rollout',
                                                'Connect the confirmed root cause to what a real solution needs to '
                                                'address'],
                        'full_explanation': "Marco's instinct to move fast is understandable — the team has spent "
                                            'months getting to a confirmed root cause, and installing a curtain feels '
                                            'like real progress after all that analysis. But "install a plausible fix" '
                                            'and "confirm the fix actually works" are different milestones, and '
                                            'Improve phase exists specifically to keep the team from skipping straight '
                                            'from the first to declaring the second.\n'
                                            '\n'
                                            'The specific risk in going straight to full rollout is that the curtain '
                                            'might only partially fix the problem — proofing-room temperature might '
                                            'stabilize faster than before, but not as completely as needed, especially '
                                            "if there's a second contributing factor (like inconsistent auxiliary "
                                            "heating) that the curtain alone doesn't address. Without a pilot — "
                                            'installing the fix on one or two shifts first and measuring the actual '
                                            'before/after difference in dough temperature and loaf weight variance — '
                                            'the team has no clean way to know whether the curtain alone is '
                                            'sufficient, or whether it needs to be paired with something else. '
                                            'Committing to full rollout before that evidence exists risks spending the '
                                            "project's remaining budget and credibility on a fix that turns out to be "
                                            'only half the solution.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What does Improve phase actually require, beyond installing '
                                                         'a plausible fix?',
                                             'options': [{'key': 'a',
                                                          'text': 'Pilot data confirming the fix produces a real, '
                                                                  'measured improvement *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "Sign-off from the CEO alone *(sign-off doesn't "
                                                                  'substitute for actual performance data)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'A press release announcing the fix *(irrelevant to '
                                                                  'whether the fix works)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Nothing further — installation is sufficient *(this '
                                                                  'is exactly the risk the lesson describes)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What risk does skipping a pilot and going straight to full '
                                                         'rollout create?',
                                             'options': [{'key': 'a',
                                                          'text': 'The team may not learn whether the fix is fully '
                                                                  'sufficient or needs to be paired with something '
                                                                  'else, until after full commitment *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Full rollout is always faster and has no downside '
                                                                  '*(it has the described downside: no clean '
                                                                  'before/after evidence)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Piloting is only relevant for statistical '
                                                                  'processes, not equipment fixes *(piloting applies '
                                                                  'to any fix that needs verification before full '
                                                                  'commitment)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Marco's instinct is always wrong *(the issue isn't "
                                                                  "Marco's judgment personally — it's the missing "
                                                                  'validation step)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why is "the root cause is confirmed" not the same as "the '
                                                         'fix is validated"?',
                                             'options': [{'key': 'a',
                                                          'text': 'Confirming the cause tells you what to target; '
                                                                  'validating the fix confirms the specific solution '
                                                                  'chosen actually addresses it well enough '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'They are the same thing *(they are different '
                                                                  'milestones, as described)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Root cause confirmation is unnecessary once a fix '
                                                                  'is proposed *(root cause confirmation is what makes '
                                                                  'the fix targeted rather than a guess)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Fix validation only matters for statistical '
                                                                  'processes *(it applies to any proposed fix, '
                                                                  'equipment-based or otherwise)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ["Improve's real deliverable is a validated fix, evidenced by pilot data — not "
                                    'simply an installed idea.',
                                    'Piloting on a subset before full rollout protects against committing fully to a '
                                    'partial solution.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Improve Phase (Full Module, 6 Lessons)'},
                       {'code': 'G26',
                        'title': 'Design of Experiments (DOE)',
                        'opening_question': 'The team has identified two candidate fixes for the proofing-room '
                                            'temperature gap: an **insulated curtain** over the doorway, and a '
                                            '**timer-controlled auxiliary heater** that kicks on during the changeover '
                                            'window. Testing them one at a time — a month each — would take two months '
                                            'before any conclusion. How could testing both factors together, using a '
                                            'simple factorial design, get an answer faster and reveal something '
                                            'single-factor testing might miss entirely?',
                        'concepts': ['A **2×2 factorial design** tests two factors (Curtain: On/Off, Heater: On/Off) '
                                     'across all four combinations, rather than testing each factor separately.',
                                     '**Socratic prompt:** If the curtain alone reduces temperature swing by 40%, and '
                                     'the heater alone reduces it by 30%, would you expect the combination to reduce '
                                     'it by roughly 70%? What would it mean if the actual combined result was much '
                                     'better, or much worse, than that simple sum?'],
                        'terms': ['Factorial Design', 'Interaction Effect'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'Factorial combinations',
                                  'formula': 'Number of combinations = 2^k',
                                  'explanation': 'Number of treatment combinations in a two-level full factorial '
                                                 'experiment with k factors.',
                                  'variables': 'k = number of factors; 2 = number of levels per factor; 2^k = total '
                                               'treatment combinations.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain the basic logic of a 2×2 factorial experiment',
                                                'Interpret a small factorial results table, including a possible '
                                                'interaction effect',
                                                'Explain why testing factors together can reveal something '
                                                'one-at-a-time testing cannot'],
                        'full_explanation': 'Testing the curtain for a month, then the heater for a separate month, '
                                            'would eventually produce two individual answers — but it would never '
                                            'reveal how the two factors behave *together*, which matters enormously if '
                                            'they interact. A **2×2 factorial design** solves this efficiently: '
                                            'instead of two sequential month-long tests, the team runs all four '
                                            'combinations (Curtain Off/Heater Off, Curtain On/Heater Off, Curtain '
                                            'Off/Heater On, Curtain On/Heater On) across four shorter test windows, '
                                            'and compares the resulting dough temperature variance across all four.\n'
                                            '\n'
                                            'Suppose the results come back like this (average dough temperature swing '
                                            'during the changeover window, in °F):\n'
                                            '\n'
                                            '| | Heater Off | Heater On |\n'
                                            '|---|---|---|\n'
                                            '| **Curtain Off** | 8.2°F swing | 5.9°F swing |\n'
                                            '| **Curtain On** | 4.6°F swing | 1.8°F swing |\n'
                                            '\n'
                                            'Curtain alone (Off→On, Heater Off): swing drops from 8.2 to 4.6 — a 3.6°F '
                                            'improvement. Heater alone (Off→On, Curtain Off): swing drops from 8.2 to '
                                            '5.9 — a 2.3°F improvement. If the two effects were simply additive, '
                                            'combining both should produce roughly 8.2 − 3.6 − 2.3 = 2.3°F. But the '
                                            'actual combined result is 1.8°F — better than the simple sum predicts. '
                                            'This is a real, if modest, **positive interaction**: the curtain and '
                                            'heater work better together than their individual effects would suggest, '
                                            'likely because the curtain traps the warm air the heater produces rather '
                                            'than letting it escape through the doorway gap. A team testing these '
                                            'factors one at a time, sequentially, would have correctly identified the '
                                            'curtain as the stronger single factor — but would never have discovered '
                                            'that combining both produces an even better result than either alone.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What does a 2×2 factorial design test, compared to testing '
                                                         'each factor separately?',
                                             'options': [{'key': 'a',
                                                          'text': 'All four combinations of two factors together, '
                                                                  'revealing possible interactions between them '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "Only the single best-performing factor *(that's "
                                                                  'what one-at-a-time testing would tell you — '
                                                                  'factorial design tests combinations)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Whether the process is normally distributed '
                                                                  "*(that's a separate statistical question, not what "
                                                                  'a factorial design tests)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Whether the Champion approves the pilot *(unrelated '
                                                                  'to what the experimental design itself tests)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'In the data table, what does the combined result (1.8°F) '
                                                         'being better than the simple sum (2.3°F) suggest?',
                                             'options': [{'key': 'a',
                                                          'text': 'A positive interaction — the curtain and heater '
                                                                  'reinforce each other beyond what either does alone '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The data must be measured incorrectly *(the result '
                                                                  'is a plausible, real interaction effect, not '
                                                                  'necessarily an error)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The heater has no effect at all *(the heater does '
                                                                  'have an effect, both alone and combined with the '
                                                                  'curtain)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Factorial designs cannot detect interactions '
                                                                  '*(detecting interactions is precisely what '
                                                                  'factorial designs are good at)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why would testing the curtain and heater sequentially, one '
                                                         'at a time, risk missing something important?',
                                             'options': [{'key': 'a',
                                                          'text': "It would identify each factor's individual effect "
                                                                  "but couldn't reveal how they perform together, "
                                                                  'including any interaction *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Sequential testing is always faster than factorial '
                                                                  'testing *(the scenario shows factorial testing as '
                                                                  'the faster path to a complete answer)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Sequential testing always produces more accurate '
                                                                  'individual results *(both approaches can measure '
                                                                  'individual effects; the key gap is missing the '
                                                                  'interaction)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'There is no meaningful difference between the two '
                                                                  'approaches *(there is — the interaction insight is '
                                                                  'only visible in the factorial approach)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['A 2×2 factorial design tests all combinations of two factors, not just each '
                                    'factor alone.',
                                    'Comparing the combined result to the simple sum of individual effects reveals '
                                    'whether an interaction exists.',
                                    'A positive interaction means two factors work better together than their '
                                    'individual effects alone would predict.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Improve Phase (Full Module, 6 Lessons)'},
                       {'code': 'G27',
                        'title': 'Root Cause Analysis (Verifying the Fix)',
                        'opening_question': 'The curtain-and-heater combination tested best in the DOE. Before '
                                            'ordering equipment for every shift, what should the team check to make '
                                            'sure this fix actually addresses the confirmed root cause — rather than '
                                            'just being the best-performing option among the ones they happened to '
                                            'think of?',
                        'concepts': ['A solution should be explicitly traced back to the Analyze-phase root cause '
                                     'statement: does it directly address *proofing-room cooling during the shift '
                                     'changeover gap*, or does it just correlate with improvement for some other '
                                     'reason?',
                                     "**Socratic prompt:** Suppose the heater's timer malfunctions and stays on far "
                                     'longer than intended one night. What new problem could this introduce that '
                                     "didn't exist before the fix — and is that a reasonable risk to check for before "
                                     'full rollout?'],
                        'terms': ['Root Cause Verification', 'FMEA (Failure Mode and Effects Analysis', 'lightweight)'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain why a solution should be checked against the confirmed root '
                                                'cause statement before being finalized',
                                                'Apply a lightweight FMEA-style check to identify new risks a proposed '
                                                'fix might introduce',
                                                'Distinguish "best-performing option tested" from "actually addresses '
                                                'the root cause"'],
                        'full_explanation': 'It would be easy to treat "this combination scored best in the DOE" as '
                                            'sufficient justification to move forward — but a high-performing result '
                                            "in a controlled test doesn't automatically confirm the fix is addressing "
                                            'the actual confirmed root cause (proofing-room cooling during the '
                                            'changeover gap) rather than some coincidental factor specific to the test '
                                            "window. Before finalizing, it's worth explicitly re-checking: does the "
                                            'curtain-and-heater combination directly target temperature stability '
                                            'during that specific gap? In this case, yes — both factors act directly '
                                            'on room temperature during exactly the window Analyze identified, which '
                                            'is a good sign the DOE result reflects a genuine fix rather than a '
                                            'coincidence.\n'
                                            '\n'
                                            "But confirming the fix addresses the *original* problem isn't the same as "
                                            "confirming it doesn't introduce a *new* one. This is where a lightweight "
                                            'FMEA-style check earns its place: walking through plausible failure modes '
                                            'of the fix itself, not just its intended benefit. The heater timer '
                                            'malfunctioning and running too long is a clear, plausible example — it '
                                            'could over-warm the proofing room well past the target range, potentially '
                                            'over-proofing the dough and creating a new consistency problem that '
                                            "didn't exist in the original process at all. This doesn't mean the fix "
                                            'should be abandoned; it means the solution needs a safeguard — for '
                                            'instance, a temperature cutoff or alarm — before being rolled out to '
                                            'every shift, rather than being treated as risk-free simply because it '
                                            'tested well in the DOE.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why isn\'t "this option scored best in the DOE" sufficient '
                                                         'justification on its own to finalize the fix?',
                                             'options': [{'key': 'a',
                                                          'text': 'It should also be checked against the confirmed '
                                                                  'root cause statement and reviewed for new risks it '
                                                                  'might introduce *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'DOE results are never reliable *(DOE results are '
                                                                  'reliable evidence — the point is that further '
                                                                  'verification is still worthwhile before full '
                                                                  'rollout)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The root cause was never actually confirmed *(it '
                                                                  'was confirmed in Analyze — the task here is tracing '
                                                                  'the fix back to it)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'FMEA replaces the need for DOE entirely *(they '
                                                                  'serve different, complementary purposes)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What new risk does the heater timer malfunctioning scenario '
                                                         'illustrate?',
                                             'options': [{'key': 'a',
                                                          'text': 'A fix aimed at solving one problem can introduce a '
                                                                  'new failure mode — like over-proofing from excess '
                                                                  "heat — that didn't exist before *(correct)*",
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Heaters should never be used in any bakery process '
                                                                  '*(overly broad — the issue is a specific '
                                                                  'malfunction risk, not heaters in general)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The DOE results are invalidated by this possibility '
                                                                  '*(the DOE results remain valid; the issue is a '
                                                                  'separate risk to safeguard against before rollout)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "This risk is irrelevant to the Improve phase *(it's "
                                                                  "directly relevant — it's exactly the kind of risk "
                                                                  'Improve phase should catch before finalizing the '
                                                                  'fix)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'What is a reasonable next step once this new risk is '
                                                         'identified?',
                                             'options': [{'key': 'a',
                                                          'text': 'Add a safeguard, such as a temperature cutoff or '
                                                                  'alarm, before finalizing the fix for full rollout '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Abandon the curtain-and-heater solution entirely '
                                                                  '*(the underlying fix remains sound; it needs a '
                                                                  'safeguard, not abandonment)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Ignore the risk since the DOE already validated the '
                                                                  'solution *(DOE validated performance under test '
                                                                  "conditions — it didn't specifically test for this "
                                                                  'failure mode)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Delay the entire project indefinitely *(a targeted '
                                                                  'safeguard is a proportionate response, not an '
                                                                  'indefinite delay)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Trace a proposed solution back to the confirmed root cause statement before '
                                    'finalizing it.',
                                    'A lightweight FMEA-style check can surface new risks a fix introduces, even when '
                                    'it performed well in testing.',
                                    'Identifying a new risk usually calls for a safeguard, not abandoning an otherwise '
                                    'sound fix.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Improve Phase (Full Module, 6 Lessons)'},
                       {'code': 'G28',
                        'title': 'Lean Tools',
                        'opening_question': "Beyond the temperature fix, Define's affinity diagram (Lesson 05) also "
                                            'flagged the manual reweighing workaround for the still-broken '
                                            'auto-weigher as a real issue — just not the primary root cause. Should '
                                            "the team fix this now too, even though it isn't what's driving the "
                                            'confirmed variance problem?',
                        'concepts': ['**Standard work** documents the correct, consistent procedure for the shift '
                                     'changeover (e.g., a written checklist for verifying proofing-room temperature '
                                     'before baking resumes).',
                                     '**Visual management**: a temperature gauge with a clearly marked target range, '
                                     'so any operator can see at a glance whether the room is in or out of the safe '
                                     'zone — not just Marco.',
                                     "**Socratic prompt:** The reweighing workaround wasn't the primary root cause, "
                                     "but it's still a real source of manual error and wasted time. Does fixing the "
                                     'primary root cause make this secondary issue less worth addressing, or does it '
                                     "just mean it's no longer the *urgent* item?"],
                        'terms': ['Standard Work', 'Visual Management'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'Factorial combinations',
                                  'formula': 'Number of combinations = 2^k',
                                  'explanation': 'Number of treatment combinations in a two-level full factorial '
                                                 'experiment with k factors.',
                                  'variables': 'k = number of factors; 2 = number of levels per factor; 2^k = total '
                                               'treatment combinations.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Apply standard work and visual management to support a technical fix',
                                                'Explain why addressing a secondary issue (like the reweighing '
                                                'workaround) can still be worthwhile alongside the primary fix',
                                                'Distinguish a Lean housekeeping fix from the primary '
                                                'statistical/technical solution'],
                        'full_explanation': 'The confirmed root cause — proofing-room temperature during the '
                                            'changeover gap — deserves the primary fix (curtain and heater with a '
                                            "safeguard), but that doesn't mean every other issue flagged back in "
                                            'Define should simply be forgotten. The manual reweighing workaround, tied '
                                            'to the still-unrepaired auto-weigher, is a good example of a secondary '
                                            'issue worth addressing through simpler Lean tools rather than a full '
                                            'DOE-driven fix of its own.\n'
                                            '\n'
                                            '**Standard work** — a written, specific checklist for the shift '
                                            'changeover procedure, including verifying the proofing room has reached '
                                            'its target temperature range before baking resumes — turns "Marco knows '
                                            'how to check this" into something any operator on any shift can follow '
                                            'consistently, reducing the risk of the fix depending entirely on one '
                                            "experienced person's memory. **Visual management** complements this "
                                            'directly: a simple, clearly marked temperature gauge (green zone = safe '
                                            'to proceed, red zone = wait) lets any operator confirm the room is ready '
                                            'at a glance, rather than needing to interpret a raw number or remember a '
                                            'target range from memory.\n'
                                            '\n'
                                            "Addressing the reweighing workaround doesn't require anywhere near the "
                                            "same rigor as the temperature fix did — it doesn't need a factorial "
                                            'experiment, just a straightforward process cleanup: repair or replace the '
                                            'auto-weigher, and in the meantime, standardize the manual reweighing '
                                            "procedure so it's done consistently rather than as an ad hoc workaround. "
                                            'This illustrates a useful principle for Improve phase generally: not '
                                            'every issue on the original affinity diagram needs the same depth of '
                                            'statistical rigor — the primary, confirmed root cause earns a DOE-tested '
                                            'fix, while known secondary issues can often be resolved with simpler Lean '
                                            'housekeeping tools, addressed in parallel rather than left indefinitely '
                                            'unaddressed.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What does "standard work" add to the shift changeover '
                                                         'procedure?',
                                             'options': [{'key': 'a',
                                                          'text': 'A written, specific, consistent procedure that '
                                                                  "doesn't depend on one experienced person's memory "
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'It replaces the need for the temperature safeguard '
                                                                  'discussed in the previous lesson *(it complements '
                                                                  "the fix; it doesn't replace the safeguard itself)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "It's only relevant to statistical processes, not "
                                                                  'manual procedures *(it directly applies to a manual '
                                                                  'procedure here)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It requires no documentation, only verbal '
                                                                  'instructions *(the point of standard work is that '
                                                                  'it is documented, not just verbally understood)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why is visual management (a marked temperature gauge) useful '
                                                         'here?',
                                             'options': [{'key': 'a',
                                                          'text': 'It lets any operator confirm the room is ready at a '
                                                                  'glance, without needing to interpret a raw number '
                                                                  'from memory *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'It eliminates the need for the temperature fix '
                                                                  'entirely *(it supports consistent verification of '
                                                                  'the fix, not a replacement for it)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "It's only useful for Marco personally *(the "
                                                                  'described benefit is specifically that any '
                                                                  'operator, not just Marco, can use it)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It has no practical function beyond appearance *(it '
                                                                  'has a direct functional purpose: quick, consistent '
                                                                  'verification)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why might it still be worth fixing the reweighing '
                                                         "workaround, even though it isn't the primary root cause?",
                                             'options': [{'key': 'a',
                                                          'text': 'It remains a real source of manual error and wasted '
                                                                  'time, and can be addressed with simpler tools '
                                                                  'alongside the primary fix *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'It should be ignored entirely now that the primary '
                                                                  "root cause is confirmed *(the lesson argues it's "
                                                                  'still worth addressing, just not urgently)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'It requires the same DOE rigor as the temperature '
                                                                  'fix *(it can be addressed with simpler Lean tools, '
                                                                  'not full experimental design)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Addressing it would delay the primary fix '
                                                                  'indefinitely *(it can be handled in parallel, not '
                                                                  'as a blocking delay)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Standard work and visual management support a technical fix by making it '
                                    'consistent and easy to verify for any operator.',
                                    "Secondary issues from Define's original brainstorm are still worth fixing — just "
                                    'with proportionate effort, not the same rigor as the primary root cause.',
                                    'Not every improvement needs a DOE; some just need straightforward process '
                                    'cleanup.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Improve Phase (Full Module, 6 Lessons)'},
                       {'code': 'G29',
                        'title': 'Selecting a Solution',
                        'opening_question': "The DOE showed the curtain-and-heater combination performs best, but it's "
                                            'also the most expensive option tested, and now needs an added temperature '
                                            'safeguard on top of that. How should the team make a defensible final '
                                            'decision — weighing performance against cost and risk — rather than '
                                            'simply picking whatever performed best in the test, regardless of what it '
                                            'costs to implement everywhere?',
                        'concepts': ['A **solution-selection matrix** scores each candidate option against multiple '
                                     'criteria (performance, cost, implementation risk, ease of rollout) rather than a '
                                     'single "best test result" metric.',
                                     '**Socratic prompt:** If the curtain-alone option performs meaningfully worse '
                                     'than the combination, but costs a third as much and requires no new safeguard, '
                                     'how would you decide whether that trade-off is worth it — and who should weigh '
                                     'in on that decision besides you?'],
                        'terms': ['Solution-Selection Matrix', 'Trade-off Analysis'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Apply a simple solution-selection matrix weighing performance, cost, '
                                                'and risk',
                                                "Explain why the best-performing option in testing isn't automatically "
                                                'the right final choice',
                                                'Make and justify a defensible final recommendation to a champion'],
                        'full_explanation': "It's tempting to treat the DOE's best-performing combination as the "
                                            'automatic final answer — but "best-performing in the test" and "best '
                                            'choice to implement everywhere" aren\'t guaranteed to be the same '
                                            'decision once cost and risk enter the picture. The curtain-and-heater '
                                            'combination reduced temperature swing to 1.8°F, clearly the strongest '
                                            'result — but it also costs more to install across every shift, and now '
                                            'requires an added temperature safeguard given the risk identified in '
                                            'Lesson 03. The curtain-alone option, by contrast, reduced swing to 4.6°F '
                                            '— a real, meaningful improvement over the 8.2°F baseline, though not as '
                                            'strong — at roughly a third of the cost and without needing the '
                                            'additional safeguard at all.\n'
                                            '\n'
                                            'A simple **solution-selection matrix** makes this trade-off explicit '
                                            'rather than leaving it implicit: score each option (curtain alone, heater '
                                            'alone, both) against performance, cost, implementation risk, and rollout '
                                            'speed, rather than defaulting to whichever option "won" on a single '
                                            "metric. This doesn't necessarily mean choosing the cheaper option — it "
                                            'means making the trade-off visible and defensible, and importantly, '
                                            "recognizing that this decision isn't purely technical. Whether a further "
                                            '2.8°F improvement (4.6°F vs. 1.8°F) is worth the added cost and '
                                            'complexity of the heater-plus-safeguard is a judgment call blending '
                                            'quality outcome, budget, and operational risk — exactly the kind of '
                                            'decision a champion (and possibly finance) should weigh in on, rather '
                                            'than the Green Belt simply picking the technically superior option in '
                                            'isolation and presenting it as a fait accompli.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why isn\'t "best-performing in the DOE" automatically the '
                                                         'correct final choice?',
                                             'options': [{'key': 'a',
                                                          'text': 'Cost, added complexity, and risk (like the required '
                                                                  'safeguard) also matter, and the best-performing '
                                                                  'option may not be the best overall trade-off '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'DOE results are unreliable for making real '
                                                                  'decisions *(DOE results are reliable performance '
                                                                  'evidence — the issue is that performance alone '
                                                                  "isn't the only relevant factor)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The Champion always overrules DOE results '
                                                                  "regardless of the data *(the Champion's role is to "
                                                                  'weigh in on the trade-off, not to disregard the '
                                                                  'data)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'The best-performing option is always the cheapest '
                                                                  'anyway *(in this scenario, the opposite is true — '
                                                                  "it's the most expensive option)*",
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why should the champion (and possibly finance) weigh in on '
                                                         'this specific decision?',
                                             'options': [{'key': 'a',
                                                          'text': 'The choice blends quality outcome with cost and '
                                                                  'operational risk — a judgment call beyond a purely '
                                                                  'technical decision *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The Green Belt is not qualified to understand the '
                                                                  'DOE results *(the Green Belt understands the '
                                                                  'technical results well — the issue is the broader '
                                                                  'trade-off, not technical competence)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Champions are required to approve every technical '
                                                                  'detail of every fix *(the reasoning given is about '
                                                                  'the nature of this specific trade-off, not blanket '
                                                                  'approval authority)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Finance always makes the final technical call on '
                                                                  "Six Sigma projects *(Finance's role here is input "
                                                                  'on the cost trade-off, not overriding technical '
                                                                  'judgment generally)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'What is the purpose of a solution-selection matrix in this '
                                                         'context?',
                                             'options': [{'key': 'a',
                                                          'text': 'To make the trade-off between performance, cost, '
                                                                  'and risk explicit and defensible, rather than '
                                                                  'leaving it implicit *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'To guarantee the cheapest option is always chosen '
                                                                  "*(it doesn't predetermine the outcome — it "
                                                                  'structures the comparison)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'To replace the need for champion or finance input '
                                                                  '*(it supports that input by making trade-offs '
                                                                  'visible, not replacing the conversation)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'To eliminate the need for DOE results entirely *(it '
                                                                  'uses the DOE results as one key input, not a '
                                                                  'replacement for them)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ["The best-performing tested option isn't automatically the right final choice once "
                                    'cost and risk are considered.',
                                    'A solution-selection matrix makes trade-offs between performance, cost, and risk '
                                    'explicit and defensible.',
                                    'Decisions blending quality outcome with cost and complexity deserve champion (and '
                                    'often finance) input, not a purely technical call.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Improve Phase (Full Module, 6 Lessons)'},
                       {'code': 'G30',
                        'title': 'Case Study',
                        'opening_question': '1. The Cpk improved from 0.49 to roughly 1.15 — a meaningful gain, but '
                                            'still short of the commonly used "capable process" threshold of 1.33. '
                                            'Should the team recommend full rollout now, or continue refining the fix '
                                            'first?',
                        'concepts': [],
                        'terms': [],
                        'math': [{'name': 'Cp',
                                  'formula': 'Cp = (USL − LSL) / (6σ)',
                                  'explanation': 'Potential process capability based on specification width relative '
                                                 'to process variation, without accounting for centering.',
                                  'variables': 'Cp = potential capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; σ = process standard deviation.'},
                                 {'name': 'Cpk',
                                  'formula': 'Cpk = min[(USL − μ)/(3σ), (μ − LSL)/(3σ)]',
                                  'explanation': 'Capability index that accounts for both process spread and process '
                                                 'centering.',
                                  'variables': 'Cpk = centered capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; μ = process mean; σ = process standard '
                                               'deviation; min = smaller of the two one-sided capability values.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': [],
                        'full_explanation': '*(Case studies apply everything from the module to a single extended '
                                            'scenario.)*\n'
                                            '\n'
                                            '**Scenario:** After the solution-selection matrix, Sam (the champion) and '
                                            'the team agree to pilot the full curtain-and-heater combination, with the '
                                            'added temperature safeguard, on night shift for four weeks before '
                                            'deciding on full rollout.\n'
                                            '\n'
                                            '**Pilot results:**\n'
                                            '- Pre-pilot baseline: mean loaf weight 500.4g, SD 1.1g, Cpk ≈ 0.49\n'
                                            '- Pilot (curtain + heater + safeguard, night shift only, 4 weeks): mean '
                                            'loaf weight 500.1g, SD 0.55g, Cpk ≈ 1.15\n'
                                            '- Safeguard activated twice during the pilot (once due to a timer delay, '
                                            'once due to a sensor miscalibration) — both times before any dough was '
                                            'affected, and both root-caused and corrected within the pilot window.\n'
                                            '\n'
                                            '**Case Questions:**\n'
                                            '1. The Cpk improved from 0.49 to roughly 1.15 — a meaningful gain, but '
                                            'still short of the commonly used "capable process" threshold of 1.33. '
                                            'Should the team recommend full rollout now, or continue refining the fix '
                                            'first? What would you want to know before deciding?\n'
                                            '2. The safeguard activated twice during the pilot, and both times caught '
                                            'a real problem before it affected product. Is this evidence the safeguard '
                                            'is working as intended, or evidence the underlying fix is still '
                                            'unreliable? Could it be both?\n'
                                            '3. Given the pilot data, what would you include in the recommendation '
                                            'memo to Sam — and what would you deliberately leave for the Control phase '
                                            'to address, rather than trying to solve everything before rollout?',
                        'knowledge_check': [],
                        'summary': [],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Improve Phase (Full Module, 6 Lessons)'},
                       {'code': 'G31',
                        'title': 'Introduction to Control Phase',
                        'opening_question': "The pilot's Cpk of 1.15 was strong enough that Sam approved full rollout "
                                            'to every shift. Before the team considers this project closed, what does '
                                            'Control phase actually need to establish?',
                        'concepts': ["Control's deliverable is evidence that the improvement **holds up over time** "
                                     'across all shifts — not just a four-week pilot result on one shift.',
                                     '**Socratic prompt:** If the team declares the project closed immediately after '
                                     'full rollout, with no monitoring plan in place, what happens if performance '
                                     'quietly drifts back toward the old baseline six months from now — and who would '
                                     'even notice?'],
                        'terms': ['Sustained Performance', 'Monitoring Plan'],
                        'math': [{'name': 'Cp',
                                  'formula': 'Cp = (USL − LSL) / (6σ)',
                                  'explanation': 'Potential process capability based on specification width relative '
                                                 'to process variation, without accounting for centering.',
                                  'variables': 'Cp = potential capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; σ = process standard deviation.'},
                                 {'name': 'Cpk',
                                  'formula': 'Cpk = min[(USL − μ)/(3σ), (μ − LSL)/(3σ)]',
                                  'explanation': 'Capability index that accounts for both process spread and process '
                                                 'centering.',
                                  'variables': 'Cpk = centered capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; μ = process mean; σ = process standard '
                                               'deviation; min = smaller of the two one-sided capability values.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ["Explain Control's deliverable: a monitoring plan proving performance "
                                                'is sustained, not just a good pilot result',
                                                'Describe why "it worked in the pilot" isn\'t sufficient grounds for '
                                                'project closure',
                                                'Identify the risk of declaring victory immediately after rollout '
                                                'without ongoing monitoring'],
                        'full_explanation': 'A strong pilot result is genuinely good news, but it answers a narrower '
                                            'question than it might seem: it confirms the fix worked on one shift, for '
                                            'four weeks, while the project team was actively paying close attention. '
                                            "It doesn't yet confirm the fix holds up across every shift, over months, "
                                            "once the project team's attention naturally shifts to other priorities — "
                                            'which is exactly the gap Control phase exists to close.\n'
                                            '\n'
                                            "The real risk in skipping this isn't that the fix is secretly wrong; it's "
                                            'that *nobody would notice* if performance quietly drifted back toward the '
                                            "old baseline. Equipment can wear, a new operator on a shift Marco doesn't "
                                            'work might not follow the standard-work checklist as consistently, or a '
                                            'facilities change (like a new HVAC schedule) could reintroduce hidden '
                                            'variation. Without an active monitoring plan — someone watching real data '
                                            'on a regular cadence, with clear criteria for what counts as a warning '
                                            'sign — this kind of drift is often invisible internally until the exact '
                                            'outcome the project was meant to prevent happens again: the grocery '
                                            "customer's own audit catching a problem before Golden Crust does.",
                        'knowledge_check': [{'number': 1,
                                             'question': "Why isn't a strong pilot result alone sufficient grounds for "
                                                         'closing the project?',
                                             'options': [{'key': 'a',
                                                          'text': 'It confirms the fix worked on one shift for a '
                                                                  'limited window under close attention — not that it '
                                                                  'holds up across all shifts over time without that '
                                                                  'attention *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Pilot results are inherently unreliable *(the pilot '
                                                                  'data is real evidence — the issue is its limited '
                                                                  'scope and duration, not its reliability)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Cpk above 1.0 always guarantees permanent success '
                                                                  '*(no capability figure guarantees permanence '
                                                                  'without ongoing monitoring)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Control phase is optional once a pilot succeeds '
                                                                  '*(Control phase specifically exists to confirm '
                                                                  'sustained performance beyond the pilot)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What is the specific risk of skipping an active monitoring '
                                                         'plan after rollout?',
                                             'options': [{'key': 'a',
                                                          'text': 'Performance could drift back toward the old '
                                                                  'baseline without anyone internally noticing until '
                                                                  'an external audit catches it *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The fix will definitely fail within a week *(no '
                                                                  'such certainty is claimed — the risk is undetected '
                                                                  'drift, not guaranteed failure)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Monitoring plans are only useful for statistical '
                                                                  'processes, not equipment fixes *(monitoring applies '
                                                                  'to any implemented fix meant to sustain over time)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'There is no real risk once a champion has approved '
                                                                  "rollout *(champion approval doesn't substitute for "
                                                                  'ongoing monitoring)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': "What does Control phase's deliverable actually consist of?",
                                             'options': [{'key': 'a',
                                                          'text': 'Evidence, through ongoing monitoring, that the '
                                                                  'improvement holds up over time across all shifts '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'A final report summarizing the pilot alone *(a '
                                                                  "pilot summary alone doesn't confirm sustained "
                                                                  'performance)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'A certificate of completion signed by the CEO *(a '
                                                                  "signature doesn't substitute for actual sustained "
                                                                  'performance evidence)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Removing the project team from the process entirely '
                                                                  '*(handoff should be planned, but the deliverable is '
                                                                  'the monitoring evidence itself, not team removal)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ["Control's real deliverable is evidence the improvement holds up over time, across "
                                    'all shifts — not just a strong pilot.',
                                    'Skipping monitoring risks invisible drift back toward the old baseline, '
                                    'potentially caught only by an external audit.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Control Phase (Full Module, 5 Lessons)'},
                       {'code': 'G32',
                        'title': 'Statistical Process Control (SPC)',
                        'opening_question': 'Now that the fix is rolled out to every shift, how does the team tell the '
                                            'difference between normal day-to-day variation in loaf weight and a real '
                                            'signal that the process is drifting back out of control?',
                        'concepts': ["**Control limits** are calculated from the process's own natural variation "
                                     '(typically ±3 standard deviations from the process mean); **specification '
                                     'limits** (like the ±2g contract tolerance) come from the customer requirement '
                                     "and have nothing to do with the process's actual behavior.",
                                     '**Socratic prompt:** If a control chart shows one point beyond the upper control '
                                     'limit, but that loaf is still well within the ±2g specification, should the team '
                                     'investigate anyway?'],
                        'terms': ['Control Limits', 'Specification Limits', 'Control Chart'],
                        'math': [{'name': 'Sample standard deviation',
                                  'formula': 's = √s²',
                                  'explanation': 'Expresses process spread in the original measurement units.',
                                  'variables': 's = sample standard deviation; s² = sample variance; √ = square-root '
                                               'operation.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain the difference between control limits and specification '
                                                'limits',
                                                'Interpret a basic control chart signal (a point beyond control '
                                                'limits)',
                                                'Explain why a chart can trigger an investigation even when the '
                                                'product is still within specification'],
                        'full_explanation': "It's a common and understandable instinct to only worry about a data "
                                            'point if it actually falls outside the ±2g specification — after all, '
                                            "that's the number the customer contract cares about. But **control "
                                            "limits** are a different, and in some ways more useful, signal: they're "
                                            'calculated from how the process itself has been behaving (based on its '
                                            "own mean and standard deviation), not from the customer's requirement. A "
                                            'process running steadily at mean 500.1g with SD 0.55g would have control '
                                            'limits roughly at 500.1 ± (3 × 0.55) ≈ 498.45g to 501.75g — narrower than '
                                            'the ±2g specification, and entirely independent of it.\n'
                                            '\n'
                                            'This is exactly why a point beyond the control limit deserves '
                                            'investigation even when the loaf is still within specification: it means '
                                            'something about the *process itself* has shifted from its normal '
                                            'behavior, even if the immediate output happens to still be acceptable. '
                                            'Catching this early — say, a subtle sensor drift on the temperature '
                                            'safeguard, or an operator skipping a standard-work step — gives the team '
                                            'a chance to correct course before that shift compounds into an actual '
                                            'out-of-spec loaf, rather than waiting for a real defect to appear before '
                                            "reacting. This is the core value of SPC: it uses the process's own "
                                            'behavior as an early-warning system, distinct from and ahead of the '
                                            "customer's specification limits.",
                        'knowledge_check': [{'number': 1,
                                             'question': 'What is the key difference between control limits and '
                                                         'specification limits?',
                                             'options': [{'key': 'a',
                                                          'text': "Control limits come from the process's own natural "
                                                                  'variation; specification limits come from the '
                                                                  "customer's requirement, independent of how the "
                                                                  'process actually behaves *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'They are always numerically identical *(they are '
                                                                  'typically different, and can be narrower or wider '
                                                                  'than each other depending on the process)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Specification limits are calculated from process '
                                                                  'data, and control limits come from the customer '
                                                                  'contract *(this reverses the actual definitions)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Control limits only apply to Six Sigma projects, '
                                                                  'never to any other quality system *(control limits '
                                                                  'are a general SPC concept, not exclusive to Six '
                                                                  'Sigma)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why might a team investigate a point beyond the control '
                                                         'limit even if the product is still within specification?',
                                             'options': [{'key': 'a',
                                                          'text': 'It signals the process itself has shifted from '
                                                                  'normal behavior, offering a chance to correct '
                                                                  'course before an actual defect occurs *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Points beyond control limits always mean the '
                                                                  'product is defective *(the point is still within '
                                                                  'spec in this scenario — the signal is about process '
                                                                  'behavior, not existing defects)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "It's required by law regardless of practical value "
                                                                  '*(the stated reason is early-warning practical '
                                                                  'value, not a legal requirement)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Control charts are only useful after a defect has '
                                                                  'already occurred *(the value described here is '
                                                                  'specifically pre-emptive, before a defect occurs)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'What does SPC fundamentally provide that specification '
                                                         'limits alone do not?',
                                             'options': [{'key': 'a',
                                                          'text': "An early-warning signal based on the process's own "
                                                                  'behavior, ahead of when an actual defect would '
                                                                  'occur *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'A guarantee that no defect will ever occur *(no '
                                                                  "such guarantee is described — it's about earlier "
                                                                  'detection, not elimination of all risk)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'A replacement for specification limits entirely '
                                                                  '*(both serve distinct, complementary purposes)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'A method for negotiating a new customer contract '
                                                                  "*(unrelated to SPC's actual function)*",
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ["Control limits reflect the process's own natural variation; specification limits "
                                    "reflect the customer's requirement — they're independent of each other.",
                                    'A signal beyond control limits is worth investigating even when the product is '
                                    'still within specification, since it can catch a developing problem early.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Control Phase (Full Module, 5 Lessons)'},
                       {'code': 'G33',
                        'title': 'Control Plan',
                        'opening_question': 'Marco is going on vacation for two weeks right after the full rollout. If '
                                            "the temperature safeguard trips while he's away, does anyone else on any "
                                            'shift know exactly what to do?',
                        'concepts': ["A **control plan** documents: what's being monitored (dough temperature, loaf "
                                     "weight), how often (each shift changeover, daily aggregate review), who's "
                                     'responsible (by role, not by name), and the specific response procedure when a '
                                     'signal occurs.',
                                     '**Socratic prompt:** If the control plan says "Marco checks the temperature '
                                     'gauge at changeover," what happens the day Marco isn\'t there — and how would '
                                     'writing the plan differently have prevented this gap entirely?'],
                        'terms': ['Control Plan', 'Role-Based Responsibility'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ["Identify the core elements of a control plan (what's monitored, how "
                                                'often, by whom, and the response procedure)',
                                                'Explain why a control plan should be written around roles, not '
                                                'specific named individuals',
                                                'Apply this thinking to a real handoff scenario'],
                        'full_explanation': 'A control plan that quietly depends on one specific person is a control '
                                            "plan with an unaddressed single point of failure — and Marco's upcoming "
                                            'vacation is exactly the kind of ordinary, predictable event that exposes '
                                            'this gap immediately. If the plan literally reads "Marco checks the '
                                            'gauge," it stops functioning the moment Marco isn\'t physically present, '
                                            'which will happen regularly for entirely normal reasons: vacations, '
                                            'illness, eventual promotion, or simply a schedule rotation that puts '
                                            'someone else on duty.\n'
                                            '\n'
                                            'The fix is straightforward but easy to overlook when a plan is written by '
                                            '(and implicitly for) the person who happens to be most involved during '
                                            'the project itself: define every responsibility by **role** — "the shift '
                                            'lead on duty" — rather than by name. Paired with the standard-work '
                                            'checklist and visual management from Improve phase, this means any '
                                            'qualified shift lead, on any shift, on any day, can follow the same '
                                            'documented procedure: check the gauge at changeover, log the reading, and '
                                            'follow a specific, written escalation procedure (who to call, what to do '
                                            'with product already in process) if the safeguard trips or a reading '
                                            'falls outside the expected range. This is what actually makes a control '
                                            'plan durable past the life of the project team — it survives staff '
                                            'turnover, vacations, and shift rotations, because it was never dependent '
                                            "on one specific person's presence in the first place.",
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why is writing a control plan around a specific named '
                                                         'individual risky?',
                                             'options': [{'key': 'a',
                                                          'text': 'The plan stops functioning whenever that person is '
                                                                  'unavailable, which will happen for entirely '
                                                                  'ordinary reasons like vacation or turnover '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Named individuals are always less reliable than '
                                                                  "roles *(the issue isn't reliability of the person — "
                                                                  "it's availability over time)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "It's illegal to name individuals in a control plan "
                                                                  '*(no such legal issue is described — the concern is '
                                                                  'operational durability)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It has no real practical downside *(the vacation '
                                                                  'scenario shows a direct, practical downside)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What should replace "Marco checks the temperature gauge" in '
                                                         'a durable control plan?',
                                             'options': [{'key': 'a',
                                                          'text': '"The shift lead on duty checks the temperature '
                                                                  'gauge," defined by role rather than by name '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Removing the temperature check from the control '
                                                                  'plan entirely *(the check remains necessary — only '
                                                                  "the responsible party's description needs to "
                                                                  'change)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Requiring Marco to be present on every shift '
                                                                  "indefinitely *(this isn't practical or sustainable "
                                                                  'long-term)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Automating the check with no human review at all '
                                                                  '*(the lesson describes a role-based human '
                                                                  'procedure, not full automation as the described '
                                                                  'fix)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'What makes a control plan durable past the life of the '
                                                         'original project team?',
                                             'options': [{'key': 'a',
                                                          'text': 'Defining responsibilities by role and pairing them '
                                                                  'with standard work and visual management, so it '
                                                                  "works regardless of who's on shift *(correct)*",
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Ensuring the same people remain on the project team '
                                                                  "forever *(this isn't realistic or described as the "
                                                                  'solution)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Keeping the plan informal and undocumented so it '
                                                                  'can change easily *(informality is exactly what '
                                                                  'creates the single-point-of-failure risk)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Limiting the plan to only the Green Belt's personal "
                                                                  'knowledge *(this recreates the same '
                                                                  'single-point-of-failure problem at a different '
                                                                  'level)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ["A control plan should specify who's responsible by role, not by named individual, "
                                    'so it survives vacations, turnover, and shift changes.',
                                    'Pairing role-based responsibility with standard work and visual management makes '
                                    "the plan durable past the project team's direct involvement."],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Control Phase (Full Module, 5 Lessons)'},
                       {'code': 'G34',
                        'title': 'Lean Tools for Process Control',
                        'opening_question': 'Six months after rollout, is there any reason to think the standard-work '
                                            'checklist from Improve phase is still actually being followed on every '
                                            'shift, rather than quietly skipped once the excitement of the fix has '
                                            'faded?',
                        'concepts': ['A **layered process audit** — a brief, periodic, often unannounced check by '
                                     'someone other than the routine operator — verifies that a standard-work '
                                     'procedure is actually being followed, not just that it exists on paper.',
                                     '**Socratic prompt:** The temperature gauge (visual management from Improve) '
                                     'makes it easy to check compliance in the moment. Does that mean compliance is '
                                     'guaranteed to continue six months from now, without anyone checking on the '
                                     'checking?'],
                        'terms': ['Layered Process Audit', 'Sustain (revisited)'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Apply periodic audits to verify a standard-work procedure is still '
                                                'being followed over time',
                                                "Explain why visual controls alone aren't sufficient without periodic "
                                                'verification',
                                                'Connect this to the general risk that "Sustain" is where process '
                                                'improvements most often quietly fail'],
                        'full_explanation': 'This is the same underlying risk that shows up in almost every Lean '
                                            'initiative, under a different name each time: the first steps (installing '
                                            'a fix, writing a checklist, marking a visual gauge) are usually done '
                                            'well, precisely because the project team is paying close attention. What '
                                            "tends to fail, months later, isn't the initial fix — it's whether anyone "
                                            'is still checking that the fix is being used correctly, once the project '
                                            "team's attention has naturally moved elsewhere. This is exactly the "
                                            '"Sustain" problem from 5S, showing up again here in the context of a '
                                            'completed Six Sigma project.\n'
                                            '\n'
                                            'A **layered process audit** — a short, periodic, sometimes unannounced '
                                            "check, ideally performed by someone other than the shift lead who's "
                                            'supposed to be doing the routine check — directly addresses this. It '
                                            "doesn't need to be elaborate: a quality engineer or supervisor "
                                            'spot-checking, once a week or once a month, whether the temperature log '
                                            'is actually being filled in consistently, whether the visual gauge '
                                            'reading matches the recorded value, and whether the standard-work '
                                            'checklist is genuinely being followed rather than just posted on a wall, '
                                            'is often enough to catch drift in the follow-through long before it shows '
                                            'up as an actual quality problem. Pairing the visual control (which makes '
                                            "correct behavior easy) with a periodic audit (which verifies it's still "
                                            'happening) closes the exact gap that "Sustain" describes — a control '
                                            "that's easy to follow, but nobody ever checks whether it actually is "
                                            'being followed.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why might a standard-work checklist and visual gauge stop '
                                                         'being reliably followed months after rollout, even though '
                                                         'nothing was changed about the equipment itself?',
                                             'options': [{'key': 'a',
                                                          'text': 'Project-team attention naturally shifts elsewhere '
                                                                  'over time, and without periodic verification, '
                                                                  'compliance can quietly drift without anyone '
                                                                  'noticing *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The equipment inevitably breaks down after a few '
                                                                  'months *(the described risk is about '
                                                                  'behavior/compliance, not equipment failure '
                                                                  'specifically)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Visual controls are inherently unreliable from day '
                                                                  'one *(visual controls work well initially — the '
                                                                  'risk is sustained follow-through over time, not '
                                                                  'initial reliability)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Standard work only applies during a project's "
                                                                  'active phase *(the whole point of Control phase is '
                                                                  'making it apply well beyond the active project)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What does a layered process audit specifically verify?',
                                             'options': [{'key': 'a',
                                                          'text': 'That a documented procedure is actually being '
                                                                  'followed in practice, not just that it exists on '
                                                                  'paper *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'That the equipment is still under warranty '
                                                                  '*(unrelated to what a layered process audit '
                                                                  'checks)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'That the original DOE results were correct *(the '
                                                                  'DOE results were already validated earlier — the '
                                                                  'audit checks ongoing compliance, not the original '
                                                                  'experiment)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'That the Champion still supports the project '
                                                                  "*(unrelated to the audit's actual function)*",
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why does having someone other than the routine operator '
                                                         'perform the audit matter?',
                                             'options': [{'key': 'a',
                                                          'text': 'An outside check helps catch drift that the routine '
                                                                  'operator, immersed in daily habits, might not '
                                                                  'notice in themselves *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The routine operator is assumed to be dishonest '
                                                                  "*(the reasoning isn't about honesty — it's about an "
                                                                  "outside perspective catching drift that's easy to "
                                                                  'miss from the inside)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Only supervisors are legally allowed to perform any '
                                                                  'checks *(no such blanket legal rule is implied)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It has no real added benefit over self-checking '
                                                                  '*(an outside perspective is specifically valuable '
                                                                  'for catching drift a routine operator might not '
                                                                  'notice)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ["Standard work and visual controls make correct behavior easy, but don't guarantee "
                                    'it continues without periodic verification.',
                                    'Layered process audits — brief, periodic checks, ideally by someone other than '
                                    'the routine operator — verify ongoing compliance.',
                                    'This mirrors the "Sustain" risk from 5S: initial fixes are usually done well; '
                                    'ongoing follow-through is where drift most often occurs unnoticed.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Control Phase (Full Module, 5 Lessons)'},
                       {'code': 'G35',
                        'title': 'Case Study: The Golden Crust Project, Closed',
                        'opening_question': '1. The final Cpk (1.27) is close to, but still technically below, the '
                                            'commonly used "capable process" threshold of 1.33. Should Golden Crust '
                                            'treat this project as fully successful, or is there a reasonable case for '
                                            'a follow-on project?',
                        'concepts': [],
                        'terms': [],
                        'math': [{'name': 'Cp',
                                  'formula': 'Cp = (USL − LSL) / (6σ)',
                                  'explanation': 'Potential process capability based on specification width relative '
                                                 'to process variation, without accounting for centering.',
                                  'variables': 'Cp = potential capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; σ = process standard deviation.'},
                                 {'name': 'Cpk',
                                  'formula': 'Cpk = min[(USL − μ)/(3σ), (μ − LSL)/(3σ)]',
                                  'explanation': 'Capability index that accounts for both process spread and process '
                                                 'centering.',
                                  'variables': 'Cpk = centered capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; μ = process mean; σ = process standard '
                                               'deviation; min = smaller of the two one-sided capability values.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': [],
                        'full_explanation': '*(Case studies apply everything from the module to a single extended '
                                            'scenario, wrapping up the full DMAIC journey.)*\n'
                                            '\n'
                                            '**Full project summary:**\n'
                                            '- **Define:** Problem — grocery contract suspended over inconsistent loaf '
                                            'weight ($650,000/year at risk). Goal — bring packaging line into '
                                            'compliance, sustained across two consecutive quarterly audits.\n'
                                            '- **Measure:** Baseline confirmed at mean 500.4g, SD 1.1g, Cpk ≈ 0.49, '
                                            'after correcting a real scale-calibration issue along the way.\n'
                                            '- **Analyze:** Root cause confirmed as proofing-room cooling during the '
                                            'night-shift changeover gap, narrowed via hypothesis testing and '
                                            'exploratory data analysis.\n'
                                            '- **Improve:** DOE identified a curtain-and-heater combination as the '
                                            'strongest fix (with a positive interaction effect); a lightweight '
                                            'FMEA-style check added a temperature safeguard; standard work and visual '
                                            'management supported consistent execution; a solution-selection matrix '
                                            'justified the added cost against the performance gain.\n'
                                            '- **Control:** Full rollout followed a successful pilot (Cpk ≈ 1.15); a '
                                            'control chart, role-based control plan, and layered process audits were '
                                            'put in place to sustain performance.\n'
                                            '\n'
                                            '**Six months post-rollout data:** Mean loaf weight 500.05g, SD 0.51g, Cpk '
                                            '≈ 1.27 — a further improvement over the pilot, attributed largely to the '
                                            'layered process audits catching two early instances of the standard-work '
                                            'checklist being skipped, before either instance produced an out-of-spec '
                                            "loaf. The grocery contract has been fully reinstated, with the customer's "
                                            'own quarterly audit results cited as the reason.\n'
                                            '\n'
                                            '**Case Questions:**\n'
                                            '1. The final Cpk (1.27) is close to, but still technically below, the '
                                            'commonly used "capable process" threshold of 1.33. Should Golden Crust '
                                            'treat this project as fully successful, or is there a reasonable case for '
                                            'a follow-on project? What would you want to know before deciding either '
                                            'way?\n'
                                            '2. The layered process audits catching two near-misses is presented as a '
                                            'success of the Control phase. Could the same two near-misses also be read '
                                            'as early evidence the "Sustain" risk from Lesson 04 is already starting '
                                            'to show up, just three months after rollout? Are these two '
                                            'interpretations actually in conflict?\n'
                                            '3. Looking back across the entire DMAIC project, which single decision '
                                            "point — Define's goal statement, Measure's scale recalibration, Analyze's "
                                            "narrowing to the changeover-gap pattern, Improve's DOE, or Control's "
                                            'role-based plan — do you think had the largest effect on the final '
                                            'outcome, and why? Would a different Green Belt reasonably pick a '
                                            'different answer?',
                        'knowledge_check': [],
                        'summary': [],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Control Phase (Full Module, 5 Lessons)'},
                       {'code': 'G36',
                        'title': 'Define (DMADV): Setting the Goal Before Building Anything',
                        'opening_question': "Golden Crust's COO wants to launch a gluten-free protein bread line "
                                            'within eight months, targeting health-conscious retail customers. R&D is '
                                            'eager to start baking test batches this week. Before any baking happens, '
                                            'what does a DMADV Define phase need to establish — and how is it similar '
                                            'to, and different from, the Define phase you already know from DMAIC?',
                        'concepts': ["DMADV's Define phase, like DMAIC's, requires a business case, goal statement, "
                                     "and scope — but the goal describes a target for something that doesn't exist "
                                     'yet, not a current-state problem.',
                                     "**Socratic prompt:** DMAIC's Define phase (Define Module, Lesson 01) warned "
                                     'against starting Measure before scope was explicit. Does that same risk apply '
                                     'here — could Golden Crust "measure" anything meaningful about a protein bread '
                                     "line before Define locks down what's actually being built?",
                                     'A DMADV goal statement typically specifies a target launch date, target customer '
                                     'segment, and a business outcome — parallel in structure to a DMAIC goal '
                                     'statement, but aimed at something new rather than an improvement delta.'],
                        'terms': ['DMADV Define', 'Goal Statement (New Product)'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain what a DMADV Define phase establishes before any design work '
                                                'begins',
                                                "Compare DMADV's Define phase to the DMAIC Define phase you already "
                                                'know',
                                                'Identify the specific goal, scope, and business case elements needed '
                                                'for a new-product project'],
                        'full_explanation': 'It\'s tempting to treat "we\'re launching a new product" as different '
                                            'enough from "we\'re fixing an old process" that the discipline of Define '
                                            "doesn't fully apply. But the risk DMAIC's Define phase exists to prevent "
                                            '— proceeding without agreement on scope and goals — is, if anything, '
                                            "larger in a DMADV project, because there's no existing process to fall "
                                            "back on if the team's assumptions turn out wrong.\n"
                                            '\n'
                                            "Golden Crust's DMADV Define phase needs a business case (why this "
                                            'product, why now — likely a market trend toward high-protein, gluten-free '
                                            'snacking, tied to a specific revenue target), a goal statement (e.g., '
                                            '"launch a gluten-free protein bread line meeting defined CTQs, ready for '
                                            'retail distribution within 8 months, targeting $1.2M in incremental '
                                            'annual revenue"), and scope (which retail channels, which regions, '
                                            'retail-only or including foodservice/bulk accounts). Critically, it also '
                                            "needs an explicit list of what's *not* yet decided — the exact recipe, "
                                            'the exact protein source, the exact price point — because those are '
                                            'precisely what the rest of DMADV exists to determine. Naming them as "not '
                                            'yet decided, to be determined via DMADV" prevents R&D\'s instinct to lock '
                                            "in a recipe this week from quietly narrowing the team's options before "
                                            'Measure and Analyze have properly evaluated alternatives.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why does Define matter just as much in a DMADV project as in '
                                                         'DMAIC, arguably more?',
                                             'options': [{'key': 'a',
                                                          'text': "There's no existing process to fall back on if the "
                                                                  "team's assumptions turn out wrong — everything is "
                                                                  'being built from an unverified starting point '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'DMADV projects never carry real business risk *(new '
                                                                  'product launches carry real, often larger, business '
                                                                  'risk)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Define is only a formality in DMADV *(it serves the '
                                                                  'same functional risk-reduction purpose as in '
                                                                  'DMAIC)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'DMADV skips Define entirely *(Define is the first '
                                                                  'phase in both frameworks)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What should a DMADV goal statement specify, based on this '
                                                         'example?',
                                             'options': [{'key': 'a',
                                                          'text': 'Target launch date, target customer segment, and a '
                                                                  'measurable business outcome *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "The exact final recipe *(that's determined later, "
                                                                  'in Design — locking it in now would undermine '
                                                                  'Measure and Analyze)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Only the marketing campaign plan *(marketing '
                                                                  "planning isn't itself the goal statement's "
                                                                  'content)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Nothing measurable, since the product doesn't exist "
                                                                  'yet *(a goal statement should still be specific and '
                                                                  'measurable, even for something new)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why is it important to explicitly list what\'s "not yet '
                                                         'decided" during Define?',
                                             'options': [{'key': 'a',
                                                          'text': 'It prevents the team from prematurely narrowing '
                                                                  'options before Measure and Analyze can properly '
                                                                  'evaluate alternatives *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'It has no practical effect on the project '
                                                                  '*(premature narrowing is a real, common risk in '
                                                                  'new-product development)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'It replaces the need for a goal statement *(both '
                                                                  'serve different, complementary purposes)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Only the COO is allowed to decide what's undecided "
                                                                  '*(this is a team planning practice, not a '
                                                                  'single-person authority issue)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ["DMADV's Define phase establishes business case, goal, and scope for something new "
                                    "— parallel in structure to DMAIC's Define, aimed at a target rather than a "
                                    'current-state problem.',
                                    'Naming what\'s explicitly "not yet decided" prevents premature narrowing of '
                                    'options before later phases can properly evaluate them.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'DMADV Module: Design for Six Sigma in Practice (5 Lessons)'},
                       {'code': 'G37',
                        'title': 'Measure (DMADV): Turning Customer Needs Into Numbers',
                        'opening_question': "Golden Crust's marketing team says customers want a protein bread that's "
                                            '"filling, doesn\'t taste like cardboard, and won\'t go stale in the '
                                            'cupboard." None of those three phrases is something R&D can actually '
                                            'design against directly. What has to happen to these statements before '
                                            'Analyze can meaningfully compare recipe options?',
                        'concepts': ['Translating "filling" → a minimum protein content per serving (≥12g); "doesn\'t '
                                     'taste like cardboard" → a minimum taste-panel score (≥7/10 average); "won\'t go '
                                     'stale" → a minimum shelf life (≥10 days unrefrigerated).',
                                     '**Socratic prompt:** If the team sets "protein content: as high as possible" '
                                     'instead of a specific number like "≥12g," what problem does that create when '
                                     'Analyze compares a 12g concept against an 18g concept with worse taste?',
                                     'A simple QFD-style translation table connects each customer statement to a '
                                     'specific CTQ, target value, and priority weight, since not every requirement '
                                     'matters equally.'],
                        'terms': ['CTQ Translation', 'QFD (Quality Function Deployment)', 'Priority Weighting'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Translate vague customer language into specific, numeric CTQ targets',
                                                'Use a simple QFD-style approach to connect customer needs to '
                                                'measurable specifications',
                                                'Explain why setting a numeric target — not just a direction — matters '
                                                'for later phases'],
                        'full_explanation': '"Filling," "doesn\'t taste like cardboard," and "won\'t go stale" are '
                                            'exactly the kind of customer language the earlier DMAIC VOC lesson warned '
                                            'against treating as directly actionable — they need translation into '
                                            'something specific enough to design around, the same way "consistent '
                                            'weight" needed translation into "±2 grams of 500 grams."\n'
                                            '\n'
                                            'A simple translation table makes this explicit:\n'
                                            '\n'
                                            '| Customer Statement | CTQ | Target | Priority |\n'
                                            '|---|---|---|---|\n'
                                            '| "Filling" | Protein per serving | ≥12g | High |\n'
                                            '| "Doesn\'t taste like cardboard" | Taste panel score | ≥7/10 average | '
                                            'High |\n'
                                            '| "Won\'t go stale" | Shelf life, unrefrigerated | ≥10 days | Medium |\n'
                                            '| (implied by retail viability) | Cost per loaf | ≤$1.35 | High |\n'
                                            '\n'
                                            'Setting an actual minimum (≥12g), rather than "as much as possible," '
                                            'matters directly for the next phase: without it, Analyze has no '
                                            'principled way to compare a 12g option against an 18g option if the 18g '
                                            'option tastes worse — the team could easily over-optimize a number nobody '
                                            'asked to maximize, at the direct expense of taste, an equally important '
                                            'CTQ. A specific target, once met, lets the team stop optimizing that '
                                            'dimension and focus tradeoffs elsewhere.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why translate "filling" into a specific number like "≥12g of '
                                                         'protein" rather than "as much as possible"?',
                                             'options': [{'key': 'a',
                                                          'text': 'Without a specific minimum, the team has no '
                                                                  'principled way to compare options and might '
                                                                  'over-optimize one CTQ at the expense of others, '
                                                                  'like taste *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Numbers are only needed for financial CTQs, not '
                                                                  'sensory ones *(numeric targets matter for any CTQ '
                                                                  'that needs comparison across design options)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Customer language should never be translated into '
                                                                  "numbers *(that's exactly what CTQ translation is "
                                                                  'for)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': '"As much as possible" is always correct for a '
                                                                  "nutritional CTQ *(more isn't always better — it can "
                                                                  'trade off against other requirements)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What does a QFD-style translation table connect?',
                                             'options': [{'key': 'a',
                                                          'text': "A customer's statement to a specific, measurable "
                                                                  'CTQ, its target value, and a priority weight '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "The recipe directly to a nutrition label *(that's a "
                                                                  'downstream output, not what this table produces)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The project timeline to the goal statement *(a '
                                                                  'different planning tool)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Employee roles to project tasks *(that's a RACI "
                                                                  'matrix, not a QFD table)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why does "cost per loaf ≤$1.35" appear even though no '
                                                         'customer literally said that phrase?',
                                             'options': [{'key': 'a',
                                                          'text': "It's an implied requirement for retail viability — "
                                                                  'a CTQ can come from business constraints, not only '
                                                                  'literal customer language *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'It was added in error *(cost is a legitimate, '
                                                                  'commonly implied CTQ tied to retail pricing '
                                                                  'viability)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'All CTQs must come from a direct customer quote '
                                                                  '*(voice of the business is also a legitimate '
                                                                  'source)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Cost targets are only relevant in Verify *(cost '
                                                                  'needs to be a target from Measure onward, so '
                                                                  'Analyze and Design can be evaluated against it)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Vague customer language must be translated into specific, numeric CTQ targets '
                                    'before design comparison is possible.',
                                    'A QFD-style table connects customer statements to CTQs, targets, and priority.',
                                    'A specific minimum lets the team stop optimizing one dimension and properly weigh '
                                    'trade-offs against others.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'DMADV Module: Design for Six Sigma in Practice (5 Lessons)'},
                       {'code': 'G38',
                        'title': 'Analyze (DMADV): Comparing Design Concepts Against CTQs',
                        'opening_question': 'R&D has developed three candidate protein sources: pea protein, '
                                            'whey-based protein, and soy protein isolate. Each performs differently on '
                                            'cost, taste, and shelf life. How should the team choose — by whoever '
                                            'advocates most persuasively, or something more systematic?',
                        'concepts': ['A weighted decision matrix scores each concept against each CTQ, using the '
                                     'priority weights from Measure, producing a comparable total score per option.',
                                     '**Socratic prompt:** If Concept A scores highest overall but fails the minimum '
                                     'shelf-life CTQ (9 days against a 10-day requirement), should it still win, just '
                                     'because its total score is highest?',
                                     "DMADV's Analyze phase parallels DMAIC's Analyze phase in spirit: both require "
                                     'evidence-backed conclusions, not the most persuasive story in the room — the '
                                     'difference is comparing design alternatives rather than diagnosing root causes.'],
                        'terms': ['Weighted Decision Matrix', 'Hard Minimum CTQ'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Build and use a weighted decision matrix to compare design concepts '
                                                'against CTQs',
                                                'Interpret a decision matrix result without treating it as an '
                                                'unquestionable final answer',
                                                'Explain why Analyze in DMADV parallels root-cause analysis in DMAIC, '
                                                'despite comparing options rather than diagnosing a problem'],
                        'full_explanation': 'Using the CTQs and priorities from Measure, a weighted decision matrix '
                                            'might look like:\n'
                                            '\n'
                                            '| CTQ (Weight) | Pea Protein | Whey-Based | Soy Isolate |\n'
                                            '|---|---|---|---|\n'
                                            '| Protein ≥12g (High=3) | 14g → 5 | 16g → 5 | 13g → 4 |\n'
                                            '| Taste ≥7/10 (High=3) | 6.8/10 → 3 | 8.1/10 → 5 | 7.2/10 → 4 |\n'
                                            '| Shelf life ≥10 days (Med=2) | 12 days → 5 | 9 days → 2 | 11 days → 4 |\n'
                                            '| Cost ≤$1.35 (High=3) | $1.10 → 5 | $1.55 → 2 | $1.25 → 4 |\n'
                                            '\n'
                                            '*(Each cell rated 1–5 against its target, multiplied by weight, then '
                                            'summed.)*\n'
                                            '\n'
                                            'Weighted totals: Pea Protein = (5×3)+(3×3)+(5×2)+(5×3) = 15+9+10+15 = '
                                            '**49**. Whey-Based = (5×3)+(5×3)+(2×2)+(2×3) = 15+15+4+6 = **40**. Soy '
                                            'Isolate = (4×3)+(4×3)+(4×2)+(4×3) = 12+12+8+12 = **44**.\n'
                                            '\n'
                                            'Pea protein scores highest overall (49) — but whey-based, despite the '
                                            'highest taste score, misses the shelf-life minimum outright (9 days '
                                            'against a required 10), which disqualifies it regardless of its otherwise '
                                            'strong total. This is the key discipline in using a decision matrix: it '
                                            'ranks trade-offs among concepts that already clear every hard minimum CTQ '
                                            "— it isn't a substitute for checking those minimums first, and a high "
                                            "total score doesn't override a failed non-negotiable requirement.\n"
                                            '\n'
                                            "This mirrors DMAIC's Analyze phase in an important way: both require the "
                                            "team to resist settling on the most appealing story (here, whey's strong "
                                            'taste score) without checking it against the actual evidence and '
                                            'requirements — just as a fishbone-session "hunch" needs data confirmation '
                                            'before becoming an accepted root cause.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why might pea protein be selected despite whey-based scoring '
                                                         'higher on taste?',
                                             'options': [{'key': 'a',
                                                          'text': 'Whey-based fails the hard minimum shelf-life '
                                                                  'requirement (9 days vs. 10 required), disqualifying '
                                                                  'it regardless of its taste score or weighted total '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Taste is not actually a valid CTQ *(taste was '
                                                                  'explicitly established as a high-priority CTQ in '
                                                                  'Measure)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Pea protein always outperforms whey-based on every '
                                                                  "criterion *(it doesn't — whey-based scores higher "
                                                                  'specifically on taste)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Weighted totals are irrelevant to the decision '
                                                                  '*(they matter for comparing options that meet all '
                                                                  'hard minimums, just not as an override of a failed '
                                                                  'minimum)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What is the purpose of weighting each CTQ, rather than '
                                                         'treating them all equally?',
                                             'options': [{'key': 'a',
                                                          'text': 'It reflects that not every requirement matters '
                                                                  'equally — high-priority CTQs should influence the '
                                                                  'total more than lower-priority ones *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Weighting is a formality with no effect on the '
                                                                  'outcome *(different weights can and do change which '
                                                                  'option scores highest)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Only cost should ever be weighted *(all CTQs '
                                                                  'identified in Measure, with their priorities, '
                                                                  'should be reflected)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Weighting replaces the need to check hard minimum '
                                                                  'requirements *(hard minimums must still be checked '
                                                                  'separately)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': "How does DMADV's Analyze phase parallel DMAIC's Analyze "
                                                         'phase?',
                                             'options': [{'key': 'a',
                                                          'text': 'Both require evidence-backed conclusions rather '
                                                                  'than the most persuasive or appealing option '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'They are identical in every respect *(DMADV '
                                                                  'compares design alternatives; DMAIC diagnoses root '
                                                                  'causes of an existing problem)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "DMADV's Analyze phase doesn't require any data *(it "
                                                                  'explicitly requires numeric CTQ performance data)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Only DMAIC's Analyze phase requires resisting an "
                                                                  'appealing but unsupported conclusion *(this '
                                                                  'discipline applies equally in DMADV)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['A weighted decision matrix compares design concepts against CTQs, using priority '
                                    'weights from Measure.',
                                    "A high total score doesn't override a failed hard minimum CTQ — check minimums "
                                    'first.',
                                    "DMADV's Analyze phase shares DMAIC's core discipline: evidence over the most "
                                    'appealing story.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'DMADV Module: Design for Six Sigma in Practice (5 Lessons)'},
                       {'code': 'G39',
                        'title': 'Design (DMADV): Building Out the Chosen Concept in Detail',
                        'opening_question': "With pea protein selected as the winning concept, R&D still hasn't "
                                            'finalized the actual recipe — proportions, baking time, packaging method. '
                                            'What does "Design" need to accomplish here, beyond simply "make the bread '
                                            'now"?',
                        'concepts': ['Design finalizes the specific formulation, process steps, and packaging in '
                                     'detail — and predicts, via small-batch testing, how well the result performs '
                                     'against every CTQ before committing to a full pilot.',
                                     '**Socratic prompt:** Analyze used a single taste-panel score per concept (6.8/10 '
                                     'for pea protein). Is that one number enough to finalize a recipe, or does Design '
                                     'need something more precise — like testing multiple proportions of pea protein '
                                     'to find the specific formulation that actually clears the 7/10 threshold?',
                                     'Predicting CTQ performance in Design, before Verify, catches problems on a '
                                     'small, cheap scale rather than in the more expensive full pilot.'],
                        'terms': ['DMADV Design Phase', 'Iterative Formulation Testing'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain what Design accomplishes beyond selecting a winning concept',
                                                'Describe the importance of predicting CTQ performance before '
                                                'full-scale testing',
                                                'Identify the risk of treating "Design" as simply executing without '
                                                'further verification of assumptions'],
                        'full_explanation': 'Selecting "pea protein" as the winning concept doesn\'t answer several '
                                            'important remaining questions: exactly what ratio of pea protein to '
                                            'flour, what baking temperature and time, what packaging seals in '
                                            'freshness for the required 10-day shelf life. Design is where these '
                                            "specifics get worked out — and it's worth noticing that the original "
                                            'pea-protein taste score (6.8/10) is actually below the 7/10 minimum CTQ. '
                                            "Analyze's decision matrix compared *concepts* at a coarse level; Design "
                                            'now has to refine the specific formulation until it actually clears the '
                                            'CTQ, not simply assume concept selection alone guarantees success.\n'
                                            '\n'
                                            'This might mean testing three or four specific pea-protein-to-flour '
                                            'ratios in small batches, running each through the same taste panel, and '
                                            'picking the formulation that reaches or exceeds 7/10 — while checking '
                                            "this adjustment doesn't push cost or protein content back out of their "
                                            'own targets. Design work is inherently iterative: adjusting one variable '
                                            'to hit one CTQ can shift performance on another, and the team needs to '
                                            'converge on a formulation that satisfies all of them simultaneously.\n'
                                            '\n'
                                            'The value of doing this rigorously in Design, rather than jumping '
                                            'straight to a full-scale pilot, is cost: testing four small-batch '
                                            'formulations in a test kitchen is inexpensive and fast compared to '
                                            'running a full production-line pilot that later turns out to need the '
                                            'same adjustment.',
                        'knowledge_check': [{'number': 1,
                                             'question': "Why isn't the original 6.8/10 taste score from Analyze "
                                                         'sufficient to finalize the recipe?',
                                             'options': [{'key': 'a',
                                                          'text': 'It falls below the 7/10 minimum CTQ, meaning the '
                                                                  'specific formulation still needs refinement, not '
                                                                  'just a concept-level decision *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Taste scores from Analyze are never relevant to '
                                                                  'Design *(the Analyze-phase score is exactly what '
                                                                  'signals more refinement is needed)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': '6.8/10 already exceeds the requirement *(it falls '
                                                                  'short of the 7/10 minimum)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Taste is not actually one of the established CTQs '
                                                                  '*(it was explicitly established as a high-priority '
                                                                  'CTQ)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why is small-batch testing during Design more cost-effective '
                                                         'than jumping straight to a full pilot?',
                                             'options': [{'key': 'a',
                                                          'text': 'It catches and resolves formulation gaps cheaply '
                                                                  'and quickly, before committing to a more expensive '
                                                                  'full-scale pilot *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Small-batch testing is always identical in cost to '
                                                                  "a full pilot *(it's specifically cheaper and "
                                                                  'faster)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Full pilots never reveal new problems *(they can, '
                                                                  'and often do)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Design-phase testing is optional and rarely used in '
                                                                  "practice *(it's a standard, important part of "
                                                                  'DMADV)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'What does the formulation-testing process illustrate about '
                                                         'Design being "iterative"?',
                                             'options': [{'key': 'a',
                                                          'text': 'Adjusting one variable to meet one CTQ can shift '
                                                                  'performance on another, requiring convergence on a '
                                                                  'formulation that satisfies all CTQs simultaneously '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Design only requires one single test to succeed '
                                                                  '*(the process requires testing multiple '
                                                                  'formulations)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'CTQs never interact during formulation work *(the '
                                                                  'scenario shows a need to check that a taste '
                                                                  "adjustment doesn't push cost or protein out of "
                                                                  'target)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Iteration means repeating Analyze's decision matrix "
                                                                  '*(iteration here refers to refining the chosen '
                                                                  "concept's specifics)*",
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Design finalizes formulation and process details, refining the chosen concept '
                                    'until it actually clears every CTQ.',
                                    'Iterative small-batch testing during Design is far cheaper than discovering the '
                                    'same gap during a full pilot.',
                                    'CTQs can interact — adjusting for one may affect another, requiring convergence '
                                    'on a formulation that satisfies all simultaneously.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'DMADV Module: Design for Six Sigma in Practice (5 Lessons)'},
                       {'code': 'G40',
                        'title': 'Verify (DMADV): Confirming Performance Before Full Launch',
                        'opening_question': 'The refined pea-protein formulation now scores 7.4/10 on taste, 12.5g '
                                            'protein per serving, and $1.28 cost per loaf in small-batch testing — all '
                                            'CTQs cleared. Before Golden Crust commits to full retail production, what '
                                            "does Verify still need to confirm that small-batch testing alone can't?",
                        'concepts': ['Small-batch, test-kitchen results confirm the *recipe* works — a pilot '
                                     'production run confirms the *process* works at real scale, with real equipment '
                                     'and real shift-to-shift variation.',
                                     "**Socratic prompt:** If the test kitchen's oven bakes six loaves at a time under "
                                     'close supervision, and the actual production line bakes hundreds per shift '
                                     'across three shifts, is there any reason to expect the CTQ numbers to hold up '
                                     'identically at scale?',
                                     "A pilot run's CTQ performance can be assessed with the same capability thinking "
                                     "from DMAIC's Measure phase — checking not just the average, but the spread, "
                                     "against each CTQ's minimum."],
                        'terms': ['Pilot Production Run', 'One-Sided Capability', 'Verify (Exit Criteria)'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'Sample standard deviation',
                                  'formula': 's = √s²',
                                  'explanation': 'Expresses process spread in the original measurement units.',
                                  'variables': 's = sample standard deviation; s² = sample variance; √ = square-root '
                                               'operation.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain what a pilot production run confirms that small-batch testing '
                                                'cannot',
                                                'Interpret basic capability data from a DMADV pilot, connecting back '
                                                'to Cpk from the DMAIC Measure phase',
                                                'Identify what "verified" means as the exit criteria for a DMADV '
                                                'project'],
                        'full_explanation': 'Small-batch success is real progress, but it answers a narrower question '
                                            'than it might seem: it confirms the recipe *can* meet its CTQs under '
                                            'ideal, closely supervised conditions — not that it reliably will, across '
                                            'hundreds of loaves per shift, on real equipment, across three shifts with '
                                            'different operators. This is precisely the gap Verify exists to close, '
                                            "and it should feel familiar: it's the same logic DMAIC's Control phase "
                                            "used when a strong four-week pilot result on one shift still wasn't "
                                            'enough to close that project — full-scale, real-world confirmation '
                                            'matters beyond a promising small test.\n'
                                            '\n'
                                            'Running an actual pilot batch — say, one full production shift, several '
                                            'hundred loaves — lets the team apply the same capability thinking from '
                                            'DMAIC Measure. Suppose the pilot batch shows protein content with mean '
                                            '12.6g and standard deviation 0.4g, against a CTQ minimum of 12g. Since '
                                            'this is a one-sided minimum specification, the relevant calculation is a '
                                            'one-sided capability index: (mean − minimum) ÷ (3 × σ) = (12.6 − 12) ÷ (3 '
                                            '× 0.4) = 0.6 ÷ 1.2 = **0.5**. This is well below the 1.0 threshold '
                                            'generally considered capable — meaning that even though the *average* '
                                            'clears the 12g minimum, the *variation* across loaves is wide enough that '
                                            'a meaningful share of individual loaves likely fall below 12g, which the '
                                            'average alone would hide.\n'
                                            '\n'
                                            'This is exactly the kind of finding Verify exists to catch before full '
                                            'launch: a promising average masking risky variation, only visible once '
                                            'real production-scale data — not test-kitchen results — is examined with '
                                            'the same statistical rigor already applied to the weight-consistency '
                                            'project. "Verified" doesn\'t mean "the average looks good" — it means the '
                                            'full distribution of real pilot-scale performance clears every CTQ with '
                                            "acceptable capability, the same bar DMAIC's Control phase held the "
                                            'weight-consistency project to before declaring it truly finished.',
                        'knowledge_check': [{'number': 1,
                                             'question': "Why isn't small-batch, test-kitchen success sufficient to "
                                                         'confirm the product is ready for full launch?',
                                             'options': [{'key': 'a',
                                                          'text': "It doesn't confirm the process holds up at real "
                                                                  'production scale, with real equipment and '
                                                                  'shift-to-shift variation the small batch never '
                                                                  'encountered *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Test-kitchen results are always inaccurate '
                                                                  "*(they're real evidence — the issue is their "
                                                                  'limited scale and conditions)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "CTQs don't apply to test-kitchen batches *(the same "
                                                                  'CTQs apply — the concern is whether they hold up at '
                                                                  'scale)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Verify is optional once Design succeeds *(Verify is '
                                                                  'required precisely because Design-phase success '
                                                                  'alone is insufficient)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Given mean = 12.6g, σ = 0.4g, and a minimum CTQ of 12g, what '
                                                         'does the one-sided capability calculation (≈0.5) suggest?',
                                             'options': [{'key': 'a',
                                                          'text': 'Even though the average clears the minimum, '
                                                                  'variation across loaves is wide enough that a '
                                                                  'meaningful share likely fall below the 12g '
                                                                  'requirement *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The process is fully capable and ready for launch '
                                                                  '*(a capability index of 0.5, well below 1.0, '
                                                                  'indicates real risk)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The average itself is below the minimum *(the '
                                                                  'average, 12.6g, is above the 12g minimum — '
                                                                  'variation is the issue)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'This calculation is unrelated to anything covered '
                                                                  'earlier in the curriculum *(it directly reuses the '
                                                                  'capability logic from DMAIC Measure)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why does "verified" mean more than just "the average looks '
                                                         'good"?',
                                             'options': [{'key': 'a',
                                                          'text': 'A promising average can mask risky variation that '
                                                                  'puts a meaningful share of individual units outside '
                                                                  'spec, which only a full capability assessment '
                                                                  'reveals *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Averages are never useful in a DMADV project '
                                                                  '*(averages are necessary but insufficient — '
                                                                  'variation must also be checked)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': '"Verified" only refers to financial performance, '
                                                                  'not product quality *(it refers to CTQ performance '
                                                                  'broadly)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Capability calculations don't apply to one-sided "
                                                                  'minimum specifications *(this lesson explicitly '
                                                                  'applies one to exactly this situation)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['A pilot production run confirms real-scale process performance, not just recipe '
                                    'feasibility under ideal, small-batch conditions.',
                                    'Capability thinking (mean and variation together, not average alone) applies to '
                                    'DMADV Verify the same way it applied to DMAIC Measure.',
                                    '"Verified" means the full distribution of real pilot performance clears every CTQ '
                                    'with acceptable capability — not just a good-looking average.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'DMADV Module: Design for Six Sigma in Practice (5 Lessons)'}]},
 'black': {'name': 'Black Belt',
           'tagline': 'Lead complex, cross-functional improvement.',
           'description': 'Extend Green Belt capability into strategy, economics, advanced analysis, experimental '
                          'design, and organizational change.',
           'modules': [{'code': 'B01',
                        'title': 'The Basics of Six Sigma',
                        'opening_question': "As a Black Belt, you'll lead projects that are handed off from Green "
                                            'Belts or are too complex for a part-time team member to run alone. So — '
                                            "precisely what is different about how you're expected to *understand* Six "
                                            'Sigma, compared to a Green Belt?',
                        'concepts': ['**Sigma shift**: the commonly used 1.5σ adjustment between short-term and '
                                     'long-term process performance, reflecting real-world drift over time.',
                                     '**Yield**: First Time Yield (FTY) measures pass rate at one step; Rolled '
                                     'Throughput Yield (RTY) multiplies FTY across every step in a process, exposing '
                                     "hidden failure a single-step view can't.",
                                     '**Socratic prompt:** If Rolled Throughput Yield is always lower than any '
                                     "individual step's yield, what does that tell you about judging a whole process "
                                     'by its final inspection pass rate alone?',
                                     '**Evolution of quality**: Shewhart (statistical control) → Deming (PDCA, '
                                     'systemic thinking) → Juran (cost of quality, vital few) → Crosby (zero defects) '
                                     '→ TQM → Six Sigma → Lean Six Sigma.',
                                     '**Deliverables**: charter, VOC/CTQ tree, process maps, data collection plan, '
                                     'root cause analysis, improvement plan, control plan, and financial benefit '
                                     'documentation.',
                                     '**VOC / VOB / VOE**: customer, business, and employee "voices" all feed '
                                     "requirements — and they don't always agree.",
                                     '**KANO categories**: Basic/Must-be, Performance, Delighters (Excitement), '
                                     'Indifferent, Reverse.',
                                     '**Role hierarchy**: White → Yellow → Green → Black Belt → Master Black Belt → '
                                     'Champion/Sponsor → Process Owner.'],
                        'terms': ['Sigma Shift',
                                  'First Time Yield (FTY)',
                                  'Rolled Throughput Yield (RTY)',
                                  'VOC/VOB/VOE',
                                  'Kano Analysis',
                                  'Master Black Belt (MBB)'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'Z-score',
                                  'formula': 'z = (x − μ) / σ',
                                  'explanation': 'Number of standard deviations an observation is from the population '
                                                 'mean.',
                                  'variables': 'z = standardized score; x = observed value; μ = population mean; σ = '
                                               'population standard deviation.'},
                                 {'name': 'DPMO',
                                  'formula': 'DPMO = DPO × 1,000,000',
                                  'explanation': 'Expresses defects per opportunity on a one-million-opportunity '
                                                 'basis.',
                                  'variables': 'DPMO = defects per million opportunities; DPO = defects per '
                                               'opportunity; 1,000,000 = one million opportunities.'},
                                 {'name': 'Yield',
                                  'formula': 'Yield = good units / total units',
                                  'explanation': 'Share of units meeting the defined acceptance rule.',
                                  'variables': 'Yield = proportion of acceptable units; good units = units meeting the '
                                               'acceptance requirement; total units = all units evaluated.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain sigma shift and the difference between First Time Yield and '
                                                'Rolled Throughput Yield, and why both matter for accurately assessing '
                                                'performance',
                                                'Trace how the continuous improvement discipline evolved into modern '
                                                'Lean Six Sigma',
                                                'Distinguish Voice of the Customer, Voice of the Business, and Voice '
                                                'of the Employee, and apply Kano analysis to prioritize requirements',
                                                'Describe the Six Sigma role hierarchy, including what specifically '
                                                'distinguishes a Black Belt and a Master Black Belt'],
                        'full_explanation': '**Six Sigma, Lean, sigma shift, and yield, at Black Belt depth.** You '
                                            'already know Six Sigma targets ~3.4 DPMO and Lean targets waste '
                                            'elimination. At the Black Belt level, two refinements matter. First, '
                                            '**sigma shift**: a process measured over a short window (say, one week) '
                                            'typically looks tighter than it performs over a year, because means '
                                            'drift, materials vary, and operators change. The 1.5-sigma shift is a '
                                            'widely used correction that converts a short-term capability estimate '
                                            "into a more realistic long-term defect estimate — it's why a process "
                                            'quoted as "six sigma" (long-term) corresponds to a 4.5-sigma short-term '
                                            'Z-score. Second, **yield**: First Time Yield (FTY) is simply the '
                                            'percentage of units that pass a given step without rework or scrap. But a '
                                            "multi-step process's *true* performance is better captured by **Rolled "
                                            "Throughput Yield (RTY)** — the product of every step's FTY. A process "
                                            'with five steps each running 95% FTY looks fine step-by-step, but its RTY '
                                            'is only about 77% (0.95⁵) — meaning nearly a quarter of units experience '
                                            'a defect somewhere along the way, even though no single step "looks bad" '
                                            'in isolation. This is a core reason Black Belts insist on measuring the '
                                            'whole value stream, not just the final inspection point.\n'
                                            '\n'
                                            '**How continuous improvement got here.** Walter Shewhart introduced '
                                            'statistical control charts in the 1920s, giving quality a mathematical '
                                            'foundation. W. Edwards Deming built on this with the Plan-Do-Check-Act '
                                            '(PDCA) cycle and an emphasis on systemic causes of variation over blaming '
                                            'individual workers. Joseph Juran contributed the "vital few vs. trivial '
                                            'many" idea (the root of Pareto analysis in a quality context) and the '
                                            'concept of quantifying the cost of quality. Philip Crosby popularized '
                                            '"zero defects" as a cultural standard, not just a statistical target. '
                                            'These threads combined into Total Quality Management (TQM) in the 1980s, '
                                            'which Six Sigma then formalized with rigorous statistical methodology, '
                                            'and which Lean Six Sigma later merged with waste-elimination thinking '
                                            'from the Toyota Production System.\n'
                                            '\n'
                                            "**Deliverables and problem-solving strategy.** A Six Sigma project isn't "
                                            "complete because a chart looks better — it's complete when a defined set "
                                            'of deliverables exists: a signed charter, a VOC-derived CTQ tree, '
                                            'current-state process maps, a data collection plan, documented root cause '
                                            'analysis, a validated improvement, a control plan, and a financial '
                                            'benefit statement your finance department would sign off on. Underlying '
                                            'all of this is a **structured problem-solving strategy** — DMAIC (or PDCA '
                                            'at a smaller scale) — chosen deliberately over unstructured '
                                            'trial-and-error, because unstructured fixes tend to treat symptoms and '
                                            'don\'t hold up once the "current crisis" fades.\n'
                                            '\n'
                                            '**Hearing the customer, the business, and the employee.** A **VOC '
                                            'campaign** is a planned, multi-method effort (not a single survey) to '
                                            'capture customer needs — combining **VOC tools** like structured '
                                            'interviews, surveys, focus groups, complaint/warranty data, and even '
                                            'social listening. But customer voice alone is incomplete. **VOB (Voice of '
                                            'the Business)** captures constraints the organization itself imposes — '
                                            'profitability targets, regulatory requirements, strategic fit — and **VOE '
                                            '(Voice of the Employee)** captures insight from the people who run the '
                                            'process daily, who often see failure modes and workarounds that never '
                                            'reach a customer survey. **Kano analysis** helps reconcile all three by '
                                            'classifying requirements into categories: **Basic/Must-be** (expected — '
                                            "their absence causes dissatisfaction, but their presence doesn't add "
                                            'delight), **Performance** (satisfaction rises linearly with how well you '
                                            'deliver them), **Delighters/Excitement** (unexpected features that '
                                            "disproportionately boost satisfaction), **Indifferent** (customers don't "
                                            'care either way), and **Reverse** (some customers actively prefer less of '
                                            'a feature). Black Belts use Kano to decide which CTQs are worth '
                                            'over-delivering on and which are simply table stakes.\n'
                                            '\n'
                                            '**Roles, and what drives adoption.** The Six Sigma role hierarchy runs '
                                            'from **White Belt** (basic awareness) through **Yellow Belt** (part-time '
                                            'team member) and **Green Belt** (project co-lead, still has a "day job") '
                                            'up to **Black Belt** — typically a full-time or near full-time role '
                                            'leading complex, cross-functional projects and mentoring Green Belts. The '
                                            '**Master Black Belt (MBB)** sits above that: an expert trainer, coach, '
                                            'and statistical resource who works across many projects and often reports '
                                            'directly to a VP of quality or deployment leader, rather than owning a '
                                            'single project. The **Project Champion** is a business leader (not a '
                                            'statistician) whose job is securing resources and removing organizational '
                                            'obstacles. What **drives** organizations to adopt Six Sigma in the first '
                                            "place is rarely academic interest — it's usually competitive pressure, "
                                            'customer demands, regulatory compliance, a costly quality failure, or '
                                            'leadership deciding quality needs to become a genuine strategic '
                                            'differentiator rather than an afterthought.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'A five-step process runs 95% First Time Yield at every step. '
                                                         'What does this imply about its Rolled Throughput Yield?',
                                             'options': [{'key': 'a',
                                                          'text': 'RTY will be noticeably lower than 95%, since it '
                                                                  'compounds across all five steps',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'RTY will equal 95%, since every step is identical',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'RTY is irrelevant if every step passes inspection',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'RTY only applies to service processes, not '
                                                                  'manufacturing',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 2,
                                             'question': 'What is the primary purpose of the 1.5 sigma shift?',
                                             'options': [{'key': 'a',
                                                          'text': 'To convert a short-term capability estimate into a '
                                                                  'more realistic long-term defect estimate',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'To adjust for measurement system error only',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'To simplify reporting by rounding sigma levels',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'To apply only when sample sizes are very small',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 3,
                                             'question': 'Under Kano analysis, a "Basic/Must-be" requirement is best '
                                                         'described as:',
                                             'options': [{'key': 'a',
                                                          'text': 'A feature whose absence causes dissatisfaction, but '
                                                                  "whose presence doesn't create delight",
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'A feature customers actively dislike',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'A feature only some customers care about',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'A feature that always disproportionately boosts '
                                                                  'satisfaction',
                                                          'correct': False}],
                                             'answer': 'a'}],
                        'summary': ['Sigma shift adjusts short-term capability estimates to reflect realistic '
                                    'long-term performance.',
                                    "RTY (not single-step FTY) reveals a process's true end-to-end defect exposure.",
                                    "Quality's evolution: Shewhart → Deming → Juran → Crosby → TQM → Six Sigma → Lean "
                                    'Six Sigma.',
                                    'VOC, VOB, and VOE together — reconciled via Kano analysis — form a complete '
                                    'requirements picture.',
                                    'Role hierarchy: White → Yellow → Green → Black Belt → Master Black Belt → '
                                    'Champion.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Module 1: Define Phase (Lessons 01–04)'},
                       {'code': 'B02',
                        'title': 'The Fundamentals of Six Sigma',
                        'opening_question': 'If two processes have the exact same defect *count*, but one produces ten '
                                            'times more units per day than the other, are they equally "bad"? What '
                                            'does that tell you about why raw defect counts alone are a poor Six Sigma '
                                            'metric?',
                        'concepts': ['**SIPOC**: Suppliers, Inputs, Process, Outputs, Customers — a high-level map '
                                     'that defines process boundaries before detailed measurement begins.',
                                     '**Project Charter**: the formal one-page agreement on scope and goals (covered '
                                     'in full depth in Lesson 03).',
                                     '**CTQ (Critical to Quality)**: specific, measurable characteristics translated '
                                     'from VOC via a CTQ tree.',
                                     '**COPQ (PAF model)**: Prevention costs, Appraisal costs, Internal Failure costs, '
                                     'External Failure costs.',
                                     '**Pareto Analysis**: the 80/20 principle — a small number of causes typically '
                                     'account for the majority of defects.',
                                     '**Socratic prompt:** If 80% of your defects trace back to just 15% of your '
                                     'causes, why would spreading improvement effort evenly across *all* causes be a '
                                     "poor use of a Black Belt's time?",
                                     '**Basic metrics**: DPU (defects per unit), DPO (defects per opportunity), DPMO '
                                     '(defects per million opportunities) — building blocks for sigma level '
                                     'conversion.'],
                        'terms': ['SIPOC', 'CTQ Tree', 'COPQ (PAF Model)', 'Pareto Analysis', 'DPU', 'DPO', 'DPMO'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'DPO',
                                  'formula': 'DPO = defects / (units × opportunities)',
                                  'explanation': 'Normalizes defects by the number of defect opportunities.',
                                  'variables': 'DPO = defects per opportunity; defects = number of defects; units = '
                                               'units processed; opportunities = defect opportunities per unit.'},
                                 {'name': 'DPMO',
                                  'formula': 'DPMO = DPO × 1,000,000',
                                  'explanation': 'Expresses defects per opportunity on a one-million-opportunity '
                                                 'basis.',
                                  'variables': 'DPMO = defects per million opportunities; DPO = defects per '
                                               'opportunity; 1,000,000 = one million opportunities.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Describe a process using SIPOC and explain why process boundaries '
                                                'matter before you measure anything',
                                                'Define Critical to Quality (CTQ) characteristics and explain how they '
                                                'connect VOC to measurable requirements',
                                                'Calculate a basic Cost of Poor Quality (COPQ) estimate using the '
                                                'Prevention-Appraisal-Failure model',
                                                'Apply Pareto analysis and explain the statistical logic behind the '
                                                '80/20 rule',
                                                'Identify basic Six Sigma metrics (DPU, DPO, DPMO) and how they relate '
                                                'to sigma level'],
                        'full_explanation': '**Defining the process itself: SIPOC.** Before you can measure anything '
                                            'meaningfully, you have to agree on where the process starts and ends. '
                                            '**SIPOC** (Suppliers → Inputs → Process → Outputs → Customers) is the '
                                            'standard high-level tool for this: it forces the team to name who '
                                            'supplies inputs, what those inputs are, the major process steps (usually '
                                            '5–7, deliberately high-level), what outputs result, and who receives '
                                            'them. Skipping this step is a common cause of scope creep later — teams '
                                            'start collecting data before agreeing on what\'s actually "in" the '
                                            'process.\n'
                                            '\n'
                                            "**Project Charter, briefly.** The charter formalizes the project's "
                                            'business case, problem statement, goal statement, scope, and team — the '
                                            'full breakdown of each element is covered in Lesson 03, since it deserves '
                                            'its own deep treatment.\n'
                                            '\n'
                                            '**CTQ: connecting VOC to something measurable.** A customer rarely says '
                                            '"I need a cycle time of 4.2 hours" — they say "I need this fast." '
                                            'Translating a vague need like that into a specific, measurable '
                                            'requirement is the job of a **CTQ tree**: it starts with a broad need, '
                                            'breaks it into drivers, and ends in a measurable specification (e.g., '
                                            '"fast" → "order fulfillment" → "cycle time ≤ 4 hours from order to '
                                            'ship"). Every improvement metric a project tracks should trace back to a '
                                            'CTQ, which in turn traces back to an actual voice-of-customer statement.\n'
                                            '\n'
                                            '**Cost of Poor Quality, and how to calculate it.** COPQ is typically '
                                            'broken into four categories under the **PAF model**: **Prevention** costs '
                                            '(training, process design, quality planning — spent to avoid defects in '
                                            'the first place), **Appraisal** costs (inspection, testing, audits — '
                                            'spent to catch defects before they reach the customer), **Internal '
                                            'Failure** costs (scrap, rework, downtime — defects caught before the '
                                            'customer sees them), and **External Failure** costs (warranty claims, '
                                            'returns, complaint handling, lost customers — defects the customer '
                                            'experiences directly, generally the most expensive category). A '
                                            'simplified calculation might look like: if a plant spends $50,000/year on '
                                            'inspection (appraisal), $120,000/year on scrap and rework (internal '
                                            'failure), and $200,000/year on warranty claims and returns (external '
                                            'failure), with $30,000/year on preventive training (prevention), total '
                                            'COPQ = $400,000/year. Expressing this as a percentage of revenue (say, '
                                            'revenue is $10M, so COPQ is 4% of revenue) makes the number meaningful to '
                                            'leadership and gives the project a clear financial target to reduce.\n'
                                            '\n'
                                            "**Pareto analysis.** Named after economist Vilfredo Pareto's observation "
                                            'that a small share of the population held most of the wealth, Juran '
                                            'applied the same "vital few vs. trivial many" logic to quality: in most '
                                            'defect data, roughly 80% of the problem traces back to roughly 20% of the '
                                            'causes. A **Pareto chart** sorts causes by frequency (or cost) in '
                                            'descending bars, with a cumulative percentage line overlaid — visually '
                                            'showing exactly where the "vital few" cutoff falls. This matters '
                                            'practically: a Black Belt with limited time should attack the tallest '
                                            'bars first, not spread effort evenly across every possible cause.\n'
                                            '\n'
                                            '**Basic Six Sigma metrics.** **DPU (Defects Per Unit)** is the average '
                                            'number of defects found per unit produced — note this counts defects, not '
                                            'defective units (a unit can have more than one defect). **DPO (Defects '
                                            'Per Opportunity)** normalizes DPU by the number of ways a defect could '
                                            'occur on a single unit, since a complex product naturally has more '
                                            'opportunities for defects than a simple one. **DPMO (Defects Per Million '
                                            'Opportunities)** simply scales DPO by one million, giving a standardized '
                                            'number that can be converted directly into a sigma level using a standard '
                                            'conversion table — which is what makes it possible to compare a '
                                            "completely different process (say, a call center's error rate) to a "
                                            "manufacturing line's defect rate on the same sigma scale.",
                        'knowledge_check': [{'number': 1,
                                             'question': 'What is the purpose of a SIPOC diagram?',
                                             'options': [{'key': 'a',
                                                          'text': 'To define process boundaries and major elements '
                                                                  'before detailed measurement begins',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'To calculate financial return on a project',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'To replace the need for a project charter',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'To measure process capability directly',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 2,
                                             'question': 'Under the PAF model of COPQ, which category typically '
                                                         'represents the *most expensive* type of failure cost?',
                                             'options': [{'key': 'a',
                                                          'text': 'External Failure (warranty, returns, lost '
                                                                  'customers)',
                                                          'correct': False},
                                                         {'key': 'b', 'text': 'Prevention', 'correct': False},
                                                         {'key': 'c', 'text': 'Appraisal', 'correct': False},
                                                         {'key': 'd', 'text': 'Internal Failure', 'correct': False}],
                                             'answer': 'a — though this can vary by industry, external failure is '
                                                       'generally the costliest because it includes lost customer '
                                                       'trust and future revenue, not just direct repair cost'},
                                            {'number': 3,
                                             'question': 'Why does DPMO allow comparison across very different '
                                                         'processes (e.g., manufacturing vs. a call center)?',
                                             'options': [{'key': 'a',
                                                          'text': 'It standardizes defect rate to a common '
                                                                  'million-opportunity scale that converts directly to '
                                                                  'sigma level',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'It only counts defective units, not total defects',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'It ignores the number of opportunities per unit',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It requires the same sample size for every process',
                                                          'correct': False}],
                                             'answer': 'a'}],
                        'summary': ['SIPOC defines process boundaries before measurement starts.',
                                    'CTQ trees translate vague VOC statements into specific, measurable requirements.',
                                    'COPQ (Prevention, Appraisal, Internal Failure, External Failure) gives poor '
                                    'quality a financial number leadership understands.',
                                    'Pareto analysis identifies the "vital few" causes worth attacking first.',
                                    'DPU → DPO → DPMO → Sigma Level is the standard metric conversion chain.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Module 1: Define Phase (Lessons 01–04)'},
                       {'code': 'B03',
                        'title': 'Lean Six Sigma Projects',
                        'opening_question': "If two candidate projects would each take three months of a Black Belt's "
                                            'time, but one is projected to save $20,000 and the other $400,000, is the '
                                            'choice really as simple as "pick the bigger number"? What else might '
                                            'matter?',
                        'concepts': ['**Project selection roadmap**: a structured funnel — from a long list of '
                                     'potential problems, through feasibility and impact screening, down to a short '
                                     'list a Champion approves.',
                                     '**Charter elements**: Business Case, Problem Statement, Goal Statement, Scope, '
                                     'Key Milestones, Team Selection.',
                                     "**Tuckman's stages**: Forming, Storming, Norming, Performing, Adjourning.",
                                     '**RACI/RASIC**: Responsible, Accountable, Consulted, Informed (+ Support in '
                                     'RASIC) — clarifies who does what on cross-functional teams.',
                                     '**Socratic prompt:** If a project\'s "goal statement" only says "improve '
                                     'customer satisfaction," how would you know when the project is actually '
                                     'finished?',
                                     '**Financial evaluation**: expected benefits, KPIs, benefits capture, and Net '
                                     "Present Value (NPV) as ways to make a project's value concrete and verifiable."],
                        'terms': ['Project Selection Roadmap',
                                  'Project Charter',
                                  "Tuckman's Stages",
                                  'RACI/RASIC Matrix',
                                  'KPI',
                                  'Net Present Value (NPV)'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'NPV',
                                  'formula': 'NPV = Σ[CFₜ / (1 + r)^t] − initial investment',
                                  'explanation': 'Discounted economic value of a project based on the timing of cash '
                                                 'flows.',
                                  'variables': 'NPV = net present value; CFₜ = cash flow in period t; r = discount '
                                               'rate per period; t = time period; initial investment = upfront cash '
                                               'outflow; Σ = sum across periods.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Describe a structured approach to selecting and prioritizing Lean Six '
                                                'Sigma projects',
                                                'Write each core element of a project charter: business case, problem '
                                                'statement, goal statement, scope, milestones, and team',
                                                "Apply Tuckman's stages of team formation and a RACI/RASIC matrix to "
                                                'manage project team dynamics',
                                                'Estimate expected financial benefits using basic KPIs and Net Present '
                                                'Value (NPV)'],
                        'full_explanation': '**Selecting and prioritizing projects.** Not every problem worth solving '
                                            'is worth a Black Belt project. A **project selection roadmap** typically '
                                            'starts with a broad list of candidate problems (often surfaced through '
                                            'VOC, VOB, and VOE data, or leadership priorities), then screens them '
                                            'against criteria like expected financial impact, feasibility within a '
                                            'reasonable timeframe, data availability, and strategic alignment (see '
                                            'Green Belt Module 1, Lesson 02). Projects that pass this screen go to a '
                                            'Champion for formal approval and charter sign-off — this roadmap exists '
                                            'precisely to prevent Black Belts from spending months on a technically '
                                            'interesting but low-value problem.\n'
                                            '\n'
                                            '**The project charter, element by element.** The **Business Case** '
                                            'states, in a few sentences, why this project matters now — typically tied '
                                            'to a cost, revenue, or risk figure leadership recognizes. The **Problem '
                                            'Statement** describes the current, undesirable state in specific, '
                                            'measurable, neutral terms (what, where, when, how big — deliberately '
                                            'avoiding an assumed cause or solution baked into the wording). The **Goal '
                                            'Statement** states the target state in equally measurable terms, '
                                            'following a "reduce/increase [metric] from [baseline] to [target] by '
                                            '[date]" structure — vague goals like "improve customer satisfaction" fail '
                                            'the test of "how would you know when you\'re done?" The **Scope** defines '
                                            "what's in and out of bounds (which product lines, which sites, which "
                                            'process steps) — scope creep is one of the most common reasons Black Belt '
                                            'projects overrun their timeline. **Key Milestones** break the DMAIC '
                                            'timeline into checkpoints with target dates, giving the Champion '
                                            'visibility without needing to review raw data weekly. **Team Selection** '
                                            "identifies who's needed — not just for technical skill, but for "
                                            'representing every part of the process the project touches, since a team '
                                            'missing a key function (e.g., IT, or a specific shift) tends to produce '
                                            "solutions that don't survive contact with reality.\n"
                                            '\n'
                                            "**Managing the team itself.** Bruce Tuckman's model describes how teams "
                                            'typically develop: **Forming** (polite, cautious, unclear roles), '
                                            '**Storming** (conflict emerges as people push back on approach or '
                                            'authority), **Norming** (the team settles into working agreements and '
                                            'mutual trust), and **Performing** (the team executes efficiently, with '
                                            'conflict handled constructively) — with **Adjourning** added later to '
                                            'describe the wind-down once a project closes. A Black Belt who expects '
                                            'Storming and treats it as a normal, temporary phase — rather than a sign '
                                            "the team is failing — tends to navigate it far better than one who's "
                                            'caught off guard by it. To clarify who does what on a cross-functional '
                                            'team, a **RACI matrix** (Responsible — does the work; Accountable — owns '
                                            'the outcome; Consulted — provides input beforehand; Informed — kept '
                                            'updated afterward) is mapped against every task. **RASIC** adds a fifth '
                                            'role, **Support**, for people who assist the Responsible party without '
                                            'owning the task themselves — useful on larger projects where '
                                            '"Responsible" alone doesn\'t capture everyone actually doing hands-on '
                                            'work.\n'
                                            '\n'
                                            "**Making the value concrete: financial evaluation.** A project's "
                                            '**expected financial benefits** should be estimated *before* work begins '
                                            '(as part of the charter) and then verified afterward — this before/after '
                                            'discipline is what separates a credible Six Sigma project from an '
                                            'anecdote. **Developing project metrics** means choosing measures that '
                                            'will actually detect whether the improvement worked (not just '
                                            "easy-to-collect proxies), and a subset of those become the project's "
                                            '**KPIs (Key Performance Indicators)** — the few numbers a Champion will '
                                            'actually track over time. **Financial evaluation and benefits capture** '
                                            'is the formal process (often run jointly with Finance) of confirming the '
                                            'savings actually materialized in the P&L, not just on paper — "hard" '
                                            'savings (real cost reduction) are typically weighted more heavily than '
                                            '"soft" savings (e.g., time freed up that isn\'t reallocated to something '
                                            'else of value). For projects with benefits spread over multiple years, '
                                            '**Net Present Value (NPV)** accounts for the fact that a dollar saved '
                                            'next year is worth less than a dollar saved today: NPV = Σ [CFₜ / (1+r)ᵗ] '
                                            '− initial investment, where CFₜ is the cash flow in year t and r is the '
                                            'discount rate. A project with a large but distant payoff can have a lower '
                                            'NPV than a smaller, faster one — which is exactly why "biggest projected '
                                            'savings" isn\'t always the right selection criterion on its own.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What distinguishes a well-written Problem Statement from a '
                                                         'poorly written one?',
                                             'options': [{'key': 'a',
                                                          'text': 'It describes the current state in specific, '
                                                                  'measurable, neutral terms without assuming a cause '
                                                                  'or solution',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'It proposes the solution the team plans to '
                                                                  'implement',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "It's written entirely by the Project Champion",
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'It always blames a specific department',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 2,
                                             'question': 'According to Tuckman\'s model, what does the "Storming" '
                                                         'phase represent?',
                                             'options': [{'key': 'a',
                                                          'text': 'A normal, temporary phase where conflict emerges as '
                                                                  'the team works out roles and approach',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'A sign the project should be cancelled',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The final phase before a project closes',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'A phase that only happens on failing teams',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 3,
                                             'question': 'Why might a project with a smaller total projected savings '
                                                         'have a *higher* NPV than a project with larger total '
                                                         'savings?',
                                             'options': [{'key': 'a',
                                                          'text': 'Because NPV discounts future cash flows, so a '
                                                                  'faster payoff can outweigh a larger but more '
                                                                  'distant one',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'NPV always favors the larger total savings '
                                                                  'regardless of timing',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'NPV ignores the discount rate',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'NPV only applies to projects under $10,000',
                                                          'correct': False}],
                                             'answer': 'a'}],
                        'summary': ['A project selection roadmap filters candidate problems before a Champion approves '
                                    'a charter.',
                                    'Charter elements — Business Case, Problem Statement, Goal Statement, Scope, '
                                    'Milestones, Team — each serve a distinct purpose; a weak Goal Statement '
                                    'especially undermines the whole project.',
                                    "Tuckman's stages (Forming, Storming, Norming, Performing, Adjourning) describe "
                                    'normal team development; RACI/RASIC clarifies task ownership.',
                                    'NPV accounts for the time value of money when comparing projects with benefits '
                                    'spread over time.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Module 1: Define Phase (Lessons 01–04)'},
                       {'code': 'B04',
                        'title': 'The Lean Enterprise',
                        'opening_question': 'If Lean and Six Sigma both aim to improve a process, why do most modern '
                                            'practitioners insist on combining them rather than picking just one?',
                        'concepts': ['**Lean** targets speed and waste elimination; **Six Sigma** targets variation '
                                     'and defect elimination — together they address both "too slow/wasteful" and "too '
                                     'inconsistent."',
                                     '**3Ms**: Muda (waste), Mura (unevenness), Muri (overburden) — Mura and Muri '
                                     'often *cause* Muda, so addressing only the visible waste without its root '
                                     'unevenness or overburden tends to have the waste reappear.',
                                     '**DOWNTIME**: an alternate mnemonic for the same eight wastes as TIMWOODS — '
                                     'Defects, Overproduction, Waiting, Non-utilized talent, Transportation, '
                                     'Inventory, Motion, Extra-processing.',
                                     '**Socratic prompt:** If Muri (overburdening a person or machine) causes rushed '
                                     'work, and rushed work causes Muda (defects, rework), which one should a Black '
                                     'Belt address first — the visible waste, or its root cause?',
                                     '**5S**: Sort (Seiri), Set in Order (Seiton), Shine (Seiso), Standardize '
                                     '(Seiketsu), Sustain (Shitsuke).'],
                        'terms': ['Lean Six Sigma',
                                  'Muda/Mura/Muri',
                                  'TIMWOODS',
                                  'DOWNTIME',
                                  '5S (Seiri/Seiton/Seiso/Seiketsu/Shitsuke)'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ["Explain Lean's core principles and how Lean methodology complements "
                                                "Six Sigma's statistical rigor",
                                                'Distinguish Muda, Mura, and Muri (the 3Ms of Lean) and explain how '
                                                'they relate to each other',
                                                'Compare the TIMWOODS and DOWNTIME waste frameworks',
                                                'Apply all five steps of 5S to a real workspace'],
                        'full_explanation': "**Why Lean and Six Sigma are paired.** Lean's core principle is that any "
                                            'activity failing to add customer value is waste, and the way to find '
                                            "waste is to map the value stream and shorten it. Six Sigma's core "
                                            'principle is that variation is the enemy of quality, and the way to '
                                            'reduce it is structured measurement and root-cause analysis. A process '
                                            "can be fast but wildly inconsistent (Lean without Six Sigma won't fix "
                                            'that), or extremely consistent but painfully slow and wasteful (Six Sigma '
                                            "without Lean won't fix that either). **Lean Methodology** in practice "
                                            'means running value stream mapping and waste-elimination tools (5S, '
                                            "kanban, standard work) alongside DMAIC's statistical toolkit within the "
                                            'same project — which is why the discipline is more accurately called '
                                            '**Lean Six Sigma** rather than treating the two as competitors.\n'
                                            '\n'
                                            '**The 3Ms: Muda, Mura, Muri.** Most practitioners know Muda (waste — the '
                                            'TIMWOODS/DOWNTIME categories) but skip past its two root causes. **Mura** '
                                            "is unevenness or inconsistency in workload or demand — a process that's "
                                            'idle one hour and overwhelmed the next. **Muri** is overburden — asking a '
                                            'person, machine, or system to operate beyond a sustainable capacity. The '
                                            'relationship matters: Mura (uneven demand) often forces Muri (overburden '
                                            'during the spikes), and Muri, in turn, produces Muda — rushed work '
                                            'creates defects, exhausted equipment breaks down, overworked staff make '
                                            'mistakes. A Black Belt who only attacks the visible Muda (say, adding '
                                            "inspectors to catch defects) without addressing the Mura/Muri that's "
                                            'actually causing the rushed, inconsistent work will typically see the '
                                            'waste return once attention moves elsewhere.\n'
                                            '\n'
                                            "**Two names, one set of wastes.** You've already seen **TIMWOODS** "
                                            '(Transportation, Inventory, Motion, Waiting, Overproduction, '
                                            'Overprocessing, Defects, Skills). **DOWNTIME** is simply a different, '
                                            'equally common mnemonic covering the same eight categories in a different '
                                            'order and with slightly different labels: **D**efects, '
                                            '**O**verproduction, **W**aiting, **N**on-utilized talent, '
                                            '**T**ransportation, **I**nventory, **M**otion, **E**xtra-processing. '
                                            'Neither ordering is more "correct" — different organizations and training '
                                            'programs simply adopted different acronyms for the identical underlying '
                                            'list. What matters is recognizing all eight categories regardless of '
                                            'which acronym your organization uses.\n'
                                            '\n'
                                            '**5S, in detail.** 5S is a workplace organization method with five '
                                            'sequential steps. **Sort (Seiri)** — remove anything not needed for the '
                                            'current work, using a "red tag" process to flag and relocate/discard '
                                            'uncertain items rather than leaving them "just in case." **Set in Order '
                                            '(Seiton)** — arrange what remains so that everything has a clearly '
                                            'marked, logical place, minimizing motion waste (the classic principle: a '
                                            "tool used often should be within arm's reach, not across the room). "
                                            '**Shine (Seiso)** — clean the workspace thoroughly, which does double '
                                            'duty as a first-line inspection (a clean machine makes a leak or a loose '
                                            'bolt visible immediately, whereas grime hides early failure signs). '
                                            '**Standardize (Seiketsu)** — create the visual controls, checklists, and '
                                            'agreed procedures that keep Sort/Set in Order/Shine from decaying back to '
                                            'the old state within a week. **Sustain (Shitsuke)** — build the habits, '
                                            'audits, and accountability that make 5S part of the culture rather than a '
                                            'one-time event; this last step is where most 5S initiatives actually '
                                            'fail, since the first three steps produce a satisfying visible '
                                            '"before/after," while Sustain requires ongoing discipline with no '
                                            'dramatic payoff moment.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What is the relationship between Mura, Muri, and Muda?',
                                             'options': [{'key': 'a',
                                                          'text': 'Mura (unevenness) often forces Muri (overburden), '
                                                                  'which in turn produces Muda (waste)',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'They are three unrelated, independent categories of '
                                                                  'waste',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Muda always causes Mura',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Muri only applies to machines, never to people',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 2,
                                             'question': 'TIMWOODS and DOWNTIME both refer to:',
                                             'options': [{'key': 'a',
                                                          'text': 'The same eight categories of waste, using different '
                                                                  'mnemonics',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': 'Two entirely different sets of Lean tools',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Two different numbers of waste categories',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'A comparison between Lean and Six Sigma',
                                                          'correct': False}],
                                             'answer': 'a'},
                                            {'number': 3,
                                             'question': 'Which 5S step is most commonly cited as the reason 5S '
                                                         'initiatives fail over time?',
                                             'options': [{'key': 'a',
                                                          'text': 'Sustain — because it requires ongoing discipline '
                                                                  'without a dramatic visible payoff',
                                                          'correct': False},
                                                         {'key': 'b',
                                                          'text': "Sort — because it's too difficult to decide what to "
                                                                  'remove',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Shine — because cleaning takes too much time',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Set in Order — because labeling is too costly',
                                                          'correct': False}],
                                             'answer': 'a'}],
                        'summary': ['Lean (speed/waste) and Six Sigma (variation/defects) are complementary, not '
                                    'competing, disciplines.',
                                    'Mura and Muri are root causes that frequently produce visible Muda — addressing '
                                    'only the waste without its root cause tends to be temporary.',
                                    'TIMWOODS and DOWNTIME describe the same eight wastes with different mnemonics.',
                                    "5S's five steps (Sort, Set in Order, Shine, Standardize, Sustain) build toward a "
                                    'sustained habit, not a one-time cleanup — Sustain is where most initiatives '
                                    'actually fail.'],
                        'hands_on_activity': 'Walk through a real workspace you use regularly — a physical desk, a '
                                             'shared team drive, or a digital project folder. Identify at least one '
                                             'example of Muda, one of Mura, and one of Muri in that space. Then apply '
                                             "the first three S's (Sort, Set in Order, Shine) to one area of it.",
                        'worked_solution': 'Using a shared team file drive as the workspace:\n'
                                           '- **Muda (waste):** dozens of duplicate "final_v2_FINAL" versions of the '
                                           'same document — searching for the right one wastes time on every use '
                                           '(Motion/Waiting waste).\n'
                                           '- **Mura (unevenness):** the drive is barely touched most of the month, '
                                           'then everyone dumps files into it frantically right before a monthly '
                                           'report deadline.\n'
                                           '- **Muri (overburden):** the one team member who "owns" the folder '
                                           'structure is expected to manually reorganize it after every deadline '
                                           'crunch, on top of their normal workload.\n'
                                           '- **Sort:** archive or delete outdated duplicate files, keeping only the '
                                           'current version of each document.\n'
                                           '- **Set in Order:** create a clear folder structure with a consistent '
                                           'naming convention (e.g., `YYYY-MM_ProjectName_v#`), so files have one '
                                           'obvious home.\n'
                                           '- **Shine:** do a quick pass to fix broken links, remove empty folders, '
                                           'and standardize file names to the new convention.\n'
                                           'This example also illustrates the Mura → Muri → Muda chain directly: '
                                           "fixing the folder structure once (Sort/Set in Order) doesn't fix the "
                                           'underlying problem if the end-of-month rush (Mura) that caused the mess '
                                           'keeps recurring — which is what Standardize and Sustain exist to address.',
                        'module_title': 'Module 1: Define Phase (Lessons 01–04)'},
                       {'code': 'B05',
                        'title': 'Process Definition',
                        'opening_question': 'Corporate wants a comparison of weight-consistency performance across '
                                            'Plants A, B, and C. Before pulling a single number, what needs to be true '
                                            'about how each plant actually defines and measures "loaf weight" for that '
                                            'comparison to mean anything at all?',
                        'concepts': ['Comparing raw numbers across plants is only valid if each plant is measuring '
                                     '**the same thing, at the same point in the process, the same way**.',
                                     '**Socratic prompt:** Plant A weighs loaves after a 20-minute cooling period; you '
                                     'later learn Plant B weighs them straight off the oven line, and Plant C weighs a '
                                     'sample after packaging. Before any statistical comparison, what does this '
                                     'difference alone already tell you about whether the three datasets can be '
                                     'compared directly?'],
                        'terms': ['Process Definition (Multi-Site)', 'Operational Definition (Cross-Site)'],
                        'math': [],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Identify process-definition risks specific to comparing data across '
                                                'multiple sites',
                                                'Apply SIPOC thinking to confirm measurement points are actually '
                                                'equivalent across plants',
                                                'Explain why an operational definition must be re-verified, not '
                                                'assumed, in a multi-site rollup'],
                        'full_explanation': 'A single-plant Green Belt project can often get away with an informal '
                                            'understanding of "where we measure weight," because everyone on that one '
                                            'team already shares the same mental model. A cross-plant Black Belt '
                                            "comparison can't rely on that shared understanding — it has to be "
                                            "verified explicitly, because it's entirely plausible each plant developed "
                                            'its own convention independently, with nobody ever noticing the '
                                            'inconsistency since no one had previously compared the raw numbers side '
                                            'by side.\n'
                                            '\n'
                                            'This is exactly what turns up here: Plant A measures after a 20-minute '
                                            'cooling period, Plant B measures straight off the oven line (while the '
                                            'loaf is still losing moisture rapidly), and Plant C measures a packaged '
                                            'sample later still. Bread continues to lose weight as it cools and its '
                                            'moisture content stabilizes — meaning "500g" measured immediately off the '
                                            'oven at Plant B is not the same physical measurement as "500g" measured '
                                            'after cooling at Plant A, even though both appear in a spreadsheet under '
                                            'the identical column header "loaf weight (g)." Treating these as directly '
                                            'comparable numbers, without first confirming or adjusting for the '
                                            'measurement point, would produce a comparison that looks statistically '
                                            'rigorous while actually comparing three different things.\n'
                                            '\n'
                                            "The fix isn't necessarily forcing every plant to change its process "
                                            'immediately — it may be operationally reasonable for each to weigh at a '
                                            'different point for their own internal control purposes. But for a valid '
                                            'cross-plant comparison, the Black Belt needs either a standardized '
                                            'measurement point across all three plants for this specific study, or a '
                                            'way to mathematically account for the expected weight difference at each '
                                            'measurement stage before comparing the underlying process performance. '
                                            'Skipping this step and comparing raw numbers directly would be a classic '
                                            'and easily avoidable error — reaching a conclusion about which plant is '
                                            '"worse" based on a difference in *when* they measured, not necessarily '
                                            'how well the process actually performs.',
                        'knowledge_check': [{'number': 1,
                                             'question': "Why can't Plant A, B, and C's raw weight data be compared "
                                                         'directly, as described in this scenario?',
                                             'options': [{'key': 'a',
                                                          'text': 'They measure weight at different points in the '
                                                                  'process, and loaves lose weight as they cool, '
                                                                  'making the numbers not directly equivalent '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The plants use different currencies for reporting '
                                                                  'cost *(unrelated to the measurement issue '
                                                                  'described)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Raw data can never be compared across any two '
                                                                  'locations under any circumstances *(the issue here '
                                                                  'is specifically the differing measurement point, '
                                                                  'not a blanket rule against cross-site comparison)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Plant B's oven is defective *(no defect is "
                                                                  'described — the issue is measurement timing, not '
                                                                  'equipment malfunction)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What should the Black Belt do before drawing conclusions '
                                                         "from the three plants' data?",
                                             'options': [{'key': 'a',
                                                          'text': 'Either standardize the measurement point across '
                                                                  'plants for this study, or mathematically account '
                                                                  'for the expected weight difference at each stage '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "Simply report the raw numbers as-is, since they're "
                                                                  'all labeled "loaf weight" *(this would produce a '
                                                                  'misleading comparison, exactly the risk described)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "Discard Plant B and Plant C's data entirely *(the "
                                                                  'data can likely still be used, once the '
                                                                  'measurement-point issue is addressed)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Assume the difference is negligible without '
                                                                  'checking *(this assumption is exactly what the '
                                                                  'lesson warns against verifying rather than '
                                                                  'assuming)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why might this inconsistency have gone unnoticed before a '
                                                         'cross-plant comparison was attempted?',
                                             'options': [{'key': 'a',
                                                          'text': 'Each plant may have developed its own convention '
                                                                  'independently, with no prior need to compare raw '
                                                                  'numbers side by side across sites *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "It's impossible for two plants to ever measure "
                                                                  'differently *(the scenario directly shows this is '
                                                                  'possible and has happened)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Corporate always audits measurement methodology '
                                                                  'before any local process change *(no such standing '
                                                                  'audit is implied in the scenario)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'This kind of inconsistency is extremely rare in '
                                                                  "multi-site organizations *(it's a common and "
                                                                  'realistic risk in exactly this kind of rollup, not '
                                                                  'a rare edge case)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Cross-plant comparisons require verifying that each site measures the same '
                                    'variable, at the same process point, the same way.',
                                    'An identical column header ("loaf weight") does not guarantee an identical '
                                    'underlying measurement.',
                                    'Standardize the measurement point, or explicitly account for known differences, '
                                    'before comparing performance across sites.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Measure Phase (Full Module, 4 Lessons)'},
                       {'code': 'B06',
                        'title': 'Six Sigma Statistics',
                        'opening_question': 'With measurement points now standardized (all three plants agree to weigh '
                                            'post-cooling for this study), the raw data comes back: Plant A mean '
                                            '500.05g (SD 0.51g), Plant B mean 500.8g (SD 1.4g), Plant C mean 499.6g '
                                            '(SD 0.9g). Corporate wants "the statistics." Is reporting these six '
                                            'numbers alone a sufficient statistical summary?',
                        'concepts': ['**Central tendency** (mean) tells you where a process is centered; **spread** '
                                     '(standard deviation) tells you how consistent it is — a plant can be '
                                     'well-centered and still highly variable, or off-center and fairly consistent.',
                                     '**Socratic prompt:** Plant B is off-center (500.8g vs. the 500g target) and has '
                                     'the largest spread (SD 1.4g). Plant C is closer to target (499.6g) but still has '
                                     'a wider spread than Plant A (0.9g vs 0.51g). Which plant do you suspect has the '
                                     'worse actual capability against the ±2g tolerance — and is that answer obvious '
                                     'just from looking at the means alone?',
                                     "Before computing capability indices, it's worth checking whether each plant's "
                                     'data is even approximately **normally distributed** — capability formulas assume '
                                     'normality, and applying them to a distribution that looks meaningfully skewed '
                                     'can produce a misleading index.'],
                        'terms': ['Central Tendency', 'Spread (Standard Deviation)', 'Normality Check'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'Sample standard deviation',
                                  'formula': 's = √s²',
                                  'explanation': 'Expresses process spread in the original measurement units.',
                                  'variables': 's = sample standard deviation; s² = sample variance; √ = square-root '
                                               'operation.'},
                                 {'name': 'Cp',
                                  'formula': 'Cp = (USL − LSL) / (6σ)',
                                  'explanation': 'Potential process capability based on specification width relative '
                                                 'to process variation, without accounting for centering.',
                                  'variables': 'Cp = potential capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; σ = process standard deviation.'},
                                 {'name': 'Cpk',
                                  'formula': 'Cpk = min[(USL − μ)/(3σ), (μ − LSL)/(3σ)]',
                                  'explanation': 'Capability index that accounts for both process spread and process '
                                                 'centering.',
                                  'variables': 'Cpk = centered capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; μ = process mean; σ = process standard '
                                               'deviation; min = smaller of the two one-sided capability values.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Distinguish central tendency (mean) from spread (standard deviation) '
                                                'and explain why both matter together',
                                                "Explain why checking a distribution's shape matters before drawing "
                                                'further statistical conclusions',
                                                "Identify what these six numbers do, and don't, yet tell you about "
                                                "each plant's actual capability"],
                        'full_explanation': 'Six summary numbers feel like "the statistics" corporate asked for, but '
                                            'on their own, they can mislead exactly the way the Socratic prompt '
                                            'suggests: judging Plant B "worst" purely because its mean is furthest '
                                            "from target ignores that Plant C's spread is also meaningfully worse than "
                                            "Plant A's, even though Plant C's mean looks closer to target. Mean and "
                                            'standard deviation each answer a different question — where is the '
                                            'process centered, and how consistent is it — and a real capability '
                                            'judgment needs both together, not either one read in isolation. This is '
                                            'exactly why the next lesson introduces Cp/Cpk: a way to combine centering '
                                            'and spread into a single index relative to the specification.\n'
                                            '\n'
                                            "Before getting there, though, it's worth pausing on an assumption baked "
                                            'into every capability formula: that the underlying data is approximately '
                                            "normally distributed. If Plant B's process, for instance, actually has a "
                                            'skewed distribution — say, because of an occasional but not-rare '
                                            'equipment hiccup that produces a cluster of unusually heavy loaves — a '
                                            'capability index computed assuming normality could understate or '
                                            'overstate the real risk of producing an out-of-spec loaf. A simple '
                                            "histogram or normal probability plot of each plant's data, checked before "
                                            'computing Cpk, is a quick and worthwhile step: it either confirms the '
                                            'normality assumption is reasonable, or flags that a different approach '
                                            "(which Black Belt's Analyze module addresses in more depth) is needed "
                                            'before trusting a standard capability number.',
                        'knowledge_check': [{'number': 1,
                                             'question': "Why can't Plant B be immediately assumed the "
                                                         'worst-performing plant based on its mean alone?',
                                             'options': [{'key': 'a',
                                                          'text': 'Its mean is furthest from target, but a full '
                                                                  'judgment also needs spread — and Plant C, despite a '
                                                                  'closer mean, still has a wider spread than Plant A '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Mean is always irrelevant to capability *(mean is a '
                                                                  "necessary part of the picture — it's just not "
                                                                  'sufficient alone)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "Plant B's data is obviously fabricated *(no such "
                                                                  'claim is made or implied)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'All three plants perform identically once rounded '
                                                                  '*(the numbers given are meaningfully different '
                                                                  'across plants)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why does checking for normality matter before computing a '
                                                         'capability index like Cpk?',
                                             'options': [{'key': 'a',
                                                          'text': 'Capability formulas assume approximate normality, '
                                                                  'and applying them to meaningfully skewed data can '
                                                                  'produce a misleading index *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Normality checks are only relevant for hypothesis '
                                                                  'testing, never for capability *(they matter for '
                                                                  "capability too, since Cpk's formula assumes "
                                                                  'normality)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'All real-world manufacturing data is always '
                                                                  'perfectly normal *(this is not a safe assumption, '
                                                                  'and is exactly why checking matters)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Normality only matters if the sample size is under '
                                                                  '10 *(sample size and normality are related but '
                                                                  'distinct considerations — checking shape matters '
                                                                  'regardless of exact sample size)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'What is the practical risk of reporting only mean and '
                                                         'standard deviation as "the statistics" without further '
                                                         'context?',
                                             'options': [{'key': 'a',
                                                          'text': 'It invites premature conclusions (like judging '
                                                                  'Plant B worst on mean alone) without the combined '
                                                                  'view a capability index or distribution check would '
                                                                  'provide *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Mean and standard deviation are never useful '
                                                                  'numbers to report *(they are useful and necessary — '
                                                                  'just not sufficient as the complete picture alone)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Corporate never actually wants numerical detail '
                                                                  '*(the scenario shows corporate specifically asked '
                                                                  'for statistics — the concern is completeness, not '
                                                                  'whether numbers are wanted)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'This risk only applies to bakery data specifically '
                                                                  '*(the same risk applies broadly, to any process '
                                                                  'being judged on mean/SD alone)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Mean and standard deviation each answer a different question; judging performance '
                                    'from either alone risks a misleading conclusion.',
                                    'Capability indices combine centering and spread — but assume approximate '
                                    'normality, which should be checked, not assumed.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Measure Phase (Full Module, 4 Lessons)'},
                       {'code': 'B07',
                        'title': 'Measurement System Analysis',
                        'opening_question': 'Before trusting any cross-plant comparison, corporate asks a fair '
                                            "question: are Plant B and Plant C's scales even measuring as consistently "
                                            "as Plant A's scale does? How would you actually answer that, rather than "
                                            'just assuming all three scales are equally trustworthy?',
                        'concepts': ['**Repeatability**: variation when the *same* operator measures the *same* part '
                                     'multiple times on the *same* gage. **Reproducibility**: variation when '
                                     '*different* operators measure the *same* part on the *same* gage.',
                                     "**Socratic prompt:** Suppose Plant B's Gage R&R study shows repeatability is "
                                     'fine (the same operator gets consistent readings), but reproducibility is poor '
                                     '(different operators get meaningfully different readings for the same loaf). '
                                     'What does this specific pattern suggest about where the problem actually lives — '
                                     "the scale itself, or something about how it's used?",
                                     'A **%Gage R&R** above roughly 30% of the tolerance is generally considered '
                                     'unacceptable — meaning the measurement system itself is consuming too much of '
                                     'the allowable tolerance, leaving too little room to reliably distinguish real '
                                     'process variation from measurement noise.'],
                        'terms': ['Gage R&R', 'Repeatability', 'Reproducibility', '%Gage R&R'],
                        'math': [{'name': 'Cp',
                                  'formula': 'Cp = (USL − LSL) / (6σ)',
                                  'explanation': 'Potential process capability based on specification width relative '
                                                 'to process variation, without accounting for centering.',
                                  'variables': 'Cp = potential capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; σ = process standard deviation.'},
                                 {'name': 'Cpk',
                                  'formula': 'Cpk = min[(USL − μ)/(3σ), (μ − LSL)/(3σ)]',
                                  'explanation': 'Capability index that accounts for both process spread and process '
                                                 'centering.',
                                  'variables': 'Cpk = centered capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; μ = process mean; σ = process standard '
                                               'deviation; min = smaller of the two one-sided capability values.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain the difference between repeatability and reproducibility in a '
                                                'Gage R&R study',
                                                'Interpret a basic %Gage R&R result relative to the tolerance',
                                                'Explain why an MSA finding can invalidate an otherwise-reasonable '
                                                'capability comparison'],
                        'full_explanation': 'It\'s tempting to treat "the scale is calibrated" as equivalent to "the '
                                            'measurement system is trustworthy," but a Gage R&R study checks something '
                                            "calibration alone doesn't: whether the *system* of gage plus operator "
                                            'plus procedure produces consistent results, not just whether the gage '
                                            'itself reads a known weight correctly in isolation. Running a Gage R&R at '
                                            'Plant B — having two or three operators each weigh the same set of sample '
                                            'loaves multiple times — separates the total measurement variation into '
                                            "repeatability (operator-to-operator consistency isn't involved yet — same "
                                            'operator, same loaf, repeated) and reproducibility (different operators, '
                                            'same loaf).\n'
                                            '\n'
                                            'Suppose the study finds repeatability is solid, but reproducibility is '
                                            'weak — different operators produce meaningfully different readings for '
                                            'the identical loaf. This is a specific, useful diagnostic: it points away '
                                            'from the scale itself (which is producing consistent readings when the '
                                            'same person uses it the same way) and toward operator technique — perhaps '
                                            'inconsistent loaf placement, inconsistent timing relative to the cooling '
                                            'process discussed in Lesson 01, or simply inconsistent training on the '
                                            'weighing procedure across shifts. This is a very different, and generally '
                                            'cheaper, fix than a bad scale would require: standardizing the weighing '
                                            'procedure and retraining operators, rather than replacing equipment.\n'
                                            '\n'
                                            'This matters directly for the cross-plant capability comparison: if Plant '
                                            "B's %Gage R&R comes back above the commonly used 30% threshold, some "
                                            "meaningful portion of Plant B's apparently worse capability (Cpk) could "
                                            'actually be measurement noise rather than real process variation — '
                                            "meaning the plant's true underlying performance might be better than its "
                                            'raw capability number suggests, until the measurement system itself is '
                                            'fixed and the comparison is redone on trustworthy data.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What does "repeatability" specifically measure in a Gage R&R '
                                                         'study?',
                                             'options': [{'key': 'a',
                                                          'text': 'Variation when the same operator measures the same '
                                                                  'part multiple times on the same gage *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Variation between different operators measuring the '
                                                                  "same part *(that's reproducibility, not "
                                                                  'repeatability)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Variation between different plants entirely *(Gage '
                                                                  'R&R examines the measurement system at one '
                                                                  'location, not cross-plant variation directly)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Whether the gage has been recently calibrated '
                                                                  '*(calibration is a separate check from '
                                                                  'repeatability/reproducibility)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'If Plant B shows good repeatability but poor '
                                                         'reproducibility, what does this suggest?',
                                             'options': [{'key': 'a',
                                                          'text': 'The issue likely lies in operator technique or '
                                                                  'training, rather than the gage itself *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The scale is definitely broken and needs '
                                                                  'replacement *(good repeatability suggests the scale '
                                                                  'itself is behaving consistently when used the same '
                                                                  'way)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The result is inconclusive and provides no useful '
                                                                  'information *(it provides a specific, actionable '
                                                                  'diagnostic direction)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Reproducibility is irrelevant to measurement system '
                                                                  'quality *(reproducibility is a core component of a '
                                                                  'Gage R&R assessment)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': "Why might Plant B's apparently poor Cpk be partly misleading "
                                                         'before an MSA is performed?',
                                             'options': [{'key': 'a',
                                                          'text': 'Some of the observed variation could be measurement '
                                                                  'noise from an inconsistent measurement system, '
                                                                  'rather than true process variation *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Cpk calculations never require any consideration of '
                                                                  'measurement systems *(measurement system quality '
                                                                  'directly affects how much of observed variation '
                                                                  'reflects the real process versus measurement '
                                                                  'noise)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'MSA findings can never affect a capability '
                                                                  'conclusion *(they directly can, as described)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Plant B's Cpk is guaranteed to improve once MSA is "
                                                                  'performed, regardless of findings *(the effect on '
                                                                  'Cpk depends on what the MSA specifically finds, not '
                                                                  'a guaranteed direction)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Repeatability (same operator/part/gage) and reproducibility (different '
                                    'operators/same part) separate two distinct sources of measurement variation.',
                                    'A weak reproducibility result with strong repeatability points toward operator '
                                    'technique, not necessarily the gage itself.',
                                    'Poor %Gage R&R can make true process variation look worse than it is — resolve '
                                    'measurement system issues before trusting a capability comparison.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Measure Phase (Full Module, 4 Lessons)'},
                       {'code': 'B08',
                        'title': 'Process and Performance Capability',
                        'opening_question': 'With measurement systems now verified, corporate wants a single number '
                                            'per plant to compare. Cpk was used back in the original Plant A project — '
                                            'but is Cpk actually the right index for a *company-wide* rollup spanning '
                                            'several months of data across three plants?',
                        'concepts': ['**Cp/Cpk**: capability calculated from short-term, stable-process variation — a '
                                     'best-case estimate of what the process is *capable* of under controlled '
                                     'conditions.',
                                     '**Pp/Ppk**: capability calculated from long-term data, including normal '
                                     'shift-to-shift and month-to-month variation — a more realistic estimate of what '
                                     'customers actually experience over time.',
                                     "**Socratic prompt:** Plant A's original pilot Cpk (1.15, over four weeks on one "
                                     'shift) and its six-month figure (1.27, across all shifts) used different data '
                                     'windows. Which one is more comparable to a rollup spanning several months across '
                                     'three whole plants — and why might using the narrower, short-term number for '
                                     'this comparison be misleading?'],
                        'terms': ['Cp/Cpk', 'Pp/Ppk', 'Long-Term vs. Short-Term Capability'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'Cp',
                                  'formula': 'Cp = (USL − LSL) / (6σ)',
                                  'explanation': 'Potential process capability based on specification width relative '
                                                 'to process variation, without accounting for centering.',
                                  'variables': 'Cp = potential capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; σ = process standard deviation.'},
                                 {'name': 'Cpk',
                                  'formula': 'Cpk = min[(USL − μ)/(3σ), (μ − LSL)/(3σ)]',
                                  'explanation': 'Capability index that accounts for both process spread and process '
                                                 'centering.',
                                  'variables': 'Cpk = centered capability index; USL = upper specification limit; LSL '
                                               '= lower specification limit; μ = process mean; σ = process standard '
                                               'deviation; min = smaller of the two one-sided capability values.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ["Calculate Cpk from a plant's mean, standard deviation, and "
                                                'specification limits',
                                                'Distinguish Cp/Cpk (short-term, potential capability) from Pp/Ppk '
                                                '(long-term, performance capability)',
                                                'Explain why a company-wide, multi-month rollup is better represented '
                                                'by Ppk than Cpk'],
                        'full_explanation': "Using Plant A's original four-week pilot Cpk (1.15) is tempting because "
                                            "it's already calculated and was reported as a project success — but it "
                                            'reflects short-term, closely monitored conditions on a single shift, not '
                                            'the kind of long-term, all-shift, all-month performance corporate is '
                                            'actually asking about across three plants. This is exactly the '
                                            'distinction between **Cp/Cpk** and **Pp/Ppk**: Cp/Cpk are typically '
                                            'calculated from data collected under stable, short-term conditions '
                                            '(sometimes called "process potential"), while Pp/Ppk are calculated from '
                                            'long-term data that naturally includes shift-to-shift differences, '
                                            'operator turnover, seasonal ingredient variation, and other normal '
                                            "sources of variation a short pilot window simply doesn't have time to "
                                            'capture.\n'
                                            '\n'
                                            'For a rollup meant to represent what the grocery customer actually '
                                            'experiences over months of deliveries from all three plants, Ppk is the '
                                            "more honest and appropriate index — precisely because it doesn't filter "
                                            'out the normal, real-world variation a short-term Cpk study is designed '
                                            "to exclude. Using Plant A's narrower, more favorable four-week Cpk figure "
                                            'in this context would make the comparison look better than it should, and '
                                            "wouldn't be a fair basis for comparing against Plant B and Plant C's "
                                            'long-term data.\n'
                                            '\n'
                                            "Applying this with real numbers: Plant A's six-month figures (mean "
                                            '500.05g, SD 0.51g) give Ppk = min[(502−500.05)/(3×0.51), '
                                            '(500.05−498)/(3×0.51)] = min[1.95/1.53, 2.05/1.53] = min[1.27, 1.34] ≈ '
                                            '**1.27**. Plant B (mean 500.8g, SD 1.4g) gives Ppk = '
                                            'min[(502−500.8)/(3×1.4), (500.8−498)/(3×1.4)] = min[1.2/4.2, 2.8/4.2] = '
                                            'min[0.29, 0.67] ≈ **0.29**. Plant C (mean 499.6g, SD 0.9g) gives Ppk = '
                                            'min[(502−499.6)/(3×0.9), (499.6−498)/(3×0.9)] = min[2.4/2.7, 1.6/2.7] = '
                                            "min[0.89, 0.59] ≈ **0.59**. This confirms the Socratic prompt's suspicion "
                                            'from Lesson 02: Plant B, despite not looking dramatically different from '
                                            'Plant C on mean alone, is meaningfully the worst performer once centering '
                                            'and spread are combined — a clear, defensible priority for the Analyze '
                                            'and Improve work to come.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What is the key difference between Cp/Cpk and Pp/Ppk?',
                                             'options': [{'key': 'a',
                                                          'text': 'Cp/Cpk reflect short-term, controlled-condition '
                                                                  'variation; Pp/Ppk reflect long-term variation '
                                                                  'including normal real-world sources like shift and '
                                                                  'seasonal differences *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'They are two different names for the exact same '
                                                                  'calculation *(they use similar formulas but are '
                                                                  'calculated from different data windows and '
                                                                  'represent different things)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Cp/Cpk are always more accurate than Pp/Ppk '
                                                                  '*(neither is universally "more accurate" — they '
                                                                  'answer different questions about different time '
                                                                  'horizons)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Pp/Ppk only apply to multi-plant comparisons *(they '
                                                                  'can apply to a single process too — the key factor '
                                                                  'is long-term versus short-term data, not number of '
                                                                  'sites)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why is Ppk more appropriate than the original four-week Cpk '
                                                         'for this company-wide rollup?',
                                             'options': [{'key': 'a',
                                                          'text': 'It reflects long-term, real-world variation across '
                                                                  'shifts and months, matching what the rollup is '
                                                                  'actually trying to represent *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "Ppk is always a larger number than Cpk *(this isn't "
                                                                  "guaranteed — in this scenario Plant A's numbers "
                                                                  "happen to be similar, but that's not a general "
                                                                  'rule)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Cpk cannot be calculated for bakery products *(Cpk '
                                                                  'can be calculated for any process with normally '
                                                                  'distributed data and known limits — the issue here '
                                                                  'is the data window, not the industry)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Corporate specifically banned the use of Cpk *(no '
                                                                  'such rule is stated — the issue is appropriateness '
                                                                  'of the metric for this specific comparison)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Based on the calculated Ppk values (A ≈1.27, B ≈0.29, C '
                                                         '≈0.59), which plant most clearly warrants priority attention '
                                                         'in the upcoming Analyze phase?',
                                             'options': [{'key': 'a',
                                                          'text': 'Plant B, with by far the lowest Ppk, indicating '
                                                                  'both off-center performance and high variability '
                                                                  'combined *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Plant A, since it has the highest number and thus '
                                                                  'the most room for further improvement *(a high Ppk '
                                                                  'indicates strong capability, not urgency for '
                                                                  'further work)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Plant C, since its mean was closest to the 500g '
                                                                  "target *(a closer mean alone doesn't offset Plant "
                                                                  "C's wider spread compared to Plant A — but Plant "
                                                                  "B's combined result is still worse)*",
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'All three plants are statistically identical once '
                                                                  'rounded *(the calculated Ppk values are clearly and '
                                                                  'meaningfully different)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Cp/Cpk reflect short-term, controlled capability; Pp/Ppk reflect long-term, '
                                    'real-world performance capability.',
                                    'A multi-month, multi-plant rollup should generally use Ppk, not a narrow '
                                    'short-term Cpk, for a fair and honest comparison.',
                                    'Combining centering and spread into a single index (rather than eyeballing mean '
                                    'and SD separately) can reveal a clear priority — here, Plant B.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'Measure Phase (Full Module, 4 Lessons)'},
                       {'code': 'B09',
                        'title': 'Define (DMADV): Enterprise-Scale New Product Launch',
                        'opening_question': 'Corporate wants the protein bread line launched simultaneously at Plants '
                                            'A, B, and C — each with different oven equipment, different regional '
                                            'supply contracts, and different labor costs. The single-plant Green Belt '
                                            'version of this project only had to define goals for one site. What '
                                            'changes about Define when the same launch has to succeed across three '
                                            'sites with real operational differences?',
                        'concepts': ['A multi-site DMADV project needs one shared business case and goal, but scope '
                                     'must explicitly account for real site-level differences (equipment, supply '
                                     'contracts, labor) rather than assuming uniformity.',
                                     "**Socratic prompt:** If Plant C's oven equipment can't reach the baking "
                                     "temperature the Green Belt's original recipe used, does that belong in Define's "
                                     'scope discussion, or is it something to discover later, during Design?',
                                     'A corporate-level champion (here, likely a VP of Manufacturing or Operations '
                                     "overseeing all three plants) has authority a single-plant champion doesn't — the "
                                     'ability to resolve resource conflicts *between* plants, not just within one.'],
                        'terms': ['Multi-Site Scope', 'Corporate Champion', 'Site-Level Constraint'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Identify what changes in a Define phase when a project spans multiple '
                                                'sites with different capabilities',
                                                'Explain why a single enterprise-level goal statement still needs '
                                                'site-specific scope considerations',
                                                'Describe the role of a corporate-level champion versus a single-plant '
                                                'champion'],
                        'full_explanation': 'The Green Belt version of this project could treat "the process" as a '
                                            'single, unified thing because it only had to work in one place, under one '
                                            'set of real-world constraints. A Black Belt leading the enterprise '
                                            "rollout doesn't have that luxury: Plant A, B, and C may have genuinely "
                                            'different oven capabilities, different regional flour suppliers with '
                                            'slightly different protein-to-moisture ratios, and different labor cost '
                                            'structures that affect what "profitable at $1.35 cost per loaf" even '
                                            'means locally.\n'
                                            '\n'
                                            "This means Define's scope section needs an explicit inventory of known "
                                            'site-level differences before the project proceeds — not because every '
                                            'difference needs to be resolved immediately, but because an unresolved, '
                                            "unflagged difference (like Plant C's oven ceiling temperature) can "
                                            'silently invalidate assumptions made much later in Design, at a point '
                                            'where discovering the problem is far more expensive to fix. If Plant C '
                                            'genuinely cannot reach the baking temperature the original single-plant '
                                            "recipe assumed, that's either a Design-phase constraint the team needs to "
                                            "solve for from the start (find a formulation that works at Plant C's "
                                            'lower maximum temperature), or a scope decision to make explicitly now '
                                            '(launch at Plants A and B first, defer Plant C pending an equipment '
                                            "upgrade) — but it shouldn't be an accidental discovery mid-project.\n"
                                            '\n'
                                            "This is also where the corporate-level champion's authority matters "
                                            "differently than a single-plant champion's. If Plants A and B need to "
                                            "temporarily divert staff time to support Plant C's pilot testing, only "
                                            'someone with authority across all three sites can make that call — a '
                                            "single-plant champion can advocate for their own plant's priorities, but "
                                            "can't resolve a genuine resource conflict between plants.",
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why does a known equipment limitation at one plant belong in '
                                                         "Define's scope discussion rather than being discovered "
                                                         'later?',
                                             'options': [{'key': 'a',
                                                          'text': 'A foreseeable constraint that could invalidate the '
                                                                  'entire concept at one site should be surfaced '
                                                                  "upfront, not discovered mid-project when it's far "
                                                                  'more expensive to address *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Equipment differences between plants are never '
                                                                  "relevant to a DMADV project *(they're highly "
                                                                  'relevant when they could invalidate a core '
                                                                  'assumption)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Design phase is specifically meant to discover '
                                                                  'unknown constraints, so this belongs there *(a '
                                                                  'known constraint, unlike an unknown one, should be '
                                                                  'surfaced as early as possible)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "Only Plant C's management needs to know about this "
                                                                  'constraint *(the whole project team needs this '
                                                                  'information to scope the project correctly)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What does a corporate-level champion have that a '
                                                         "single-plant champion doesn't?",
                                             'options': [{'key': 'a',
                                                          'text': 'Authority to resolve resource conflicts between '
                                                                  'plants, not just within one *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The ability to perform the statistical analysis '
                                                                  "personally *(that remains the Black Belt's role, "
                                                                  "not the champion's)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "Sole authority to approve the recipe *(that's a "
                                                                  'Design-phase technical decision, not a '
                                                                  'champion-level approval)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'No meaningful difference from a single-plant '
                                                                  'champion *(the cross-site resource authority is a '
                                                                  'real, meaningful difference)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why is it important to explicitly account for site-level '
                                                         'differences in scope, rather than assuming uniformity across '
                                                         'plants?',
                                             'options': [{'key': 'a',
                                                          'text': 'Assuming uniformity risks Design-phase work being '
                                                                  'invalidated later by a real, unaccounted-for site '
                                                                  'difference *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "Site-level differences are always minor and don't "
                                                                  'affect project outcomes *(as shown, an oven '
                                                                  'temperature limit could be a fundamental '
                                                                  'constraint)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Uniformity across plants is guaranteed once a goal '
                                                                  'statement is written *(a shared goal statement '
                                                                  "doesn't guarantee uniform operational capability)*",
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'This consideration only matters for financial '
                                                                  'planning, not technical design *(it directly '
                                                                  'affects technical feasibility, as shown by the oven '
                                                                  'example)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['A multi-site DMADV project needs a shared goal but must explicitly scope for real '
                                    'site-level differences in equipment, supply, and cost structure.',
                                    'Known constraints (like an equipment limitation) belong in Define, not as a '
                                    'mid-project surprise.',
                                    'A corporate-level champion resolves cross-site resource conflicts a single-plant '
                                    'champion cannot.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'DMADV Module: Design for Six Sigma at Enterprise Scale (5 Lessons)'},
                       {'code': 'B10',
                        'title': 'Measure (DMADV): Setting Statistically Defensible CTQ Targets',
                        'opening_question': 'The Green Belt project picked "≥7/10 average taste score" as a CTQ target '
                                            'somewhat informally. For a company-wide launch with real financial '
                                            'stakes, corporate wants that target statistically justified, not just '
                                            'chosen because it sounded reasonable. How would you use actual customer '
                                            'survey data to defend a specific target number?',
                        'concepts': ['A customer survey of n=150 respondents found 62% rated a prototype sample "would '
                                     'buy again" (≥7/10 equivalent).',
                                     'The **standard error** of this proportion: SE = √[p(1−p)/n] = √[0.62×0.38/150] = '
                                     '√0.00157 ≈ **0.0397**.',
                                     '**Socratic prompt:** If the point estimate is 62%, but the true population '
                                     'proportion could reasonably be anywhere in a range around that number, should '
                                     'the CTQ target be set at exactly 62% — or somewhere more conservative, and why?',
                                     'A 95% confidence interval: 0.62 ± (1.96 × 0.0397) = 0.62 ± 0.078 → **(54.2%, '
                                     '69.8%)**.'],
                        'terms': ['Confidence Interval', 'Standard Error', 'Point Estimate'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'Standard error of mean',
                                  'formula': 'SE = s / √n',
                                  'explanation': 'Estimates the sampling variability of the sample mean.',
                                  'variables': 'SE = standard error of the sample mean; s = sample standard deviation; '
                                               'n = sample size.'},
                                 {'name': '95% confidence interval',
                                  'formula': 'estimate ± critical value × SE',
                                  'explanation': 'Quantifies uncertainty around a population estimate under the '
                                                 'specified confidence level and statistical method.',
                                  'variables': 'estimate = sample-based point estimate; critical value = value from '
                                               'the relevant reference distribution; SE = standard error; ± = lower '
                                               'and upper interval bounds.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Calculate a confidence interval for a customer survey proportion',
                                                'Use a confidence interval to set a defensible, conservative CTQ '
                                                'target',
                                                'Explain why a point estimate alone is insufficient to justify a '
                                                'target at enterprise scale'],
                        'full_explanation': 'A single survey result — "62% said they\'d buy again" — is a point '
                                            'estimate, not a guarantee about the true underlying customer population. '
                                            'Because the survey sampled only 150 people out of a much larger potential '
                                            'customer base, that 62% carries real uncertainty, which is exactly what a '
                                            'confidence interval quantifies.\n'
                                            '\n'
                                            'Calculating it: with p = 0.62 and n = 150, the standard error is √[(0.62 '
                                            '× 0.38) / 150] = √(0.2356 / 150) = √0.00157 ≈ 0.0397. For a 95% '
                                            'confidence interval, multiply by 1.96 (the standard normal critical '
                                            'value): 1.96 × 0.0397 ≈ 0.078. This gives an interval of 0.62 ± 0.078, or '
                                            '**54.2% to 69.8%** — meaning the team can be 95% confident the true '
                                            'population proportion falls somewhere in that range, not necessarily '
                                            'exactly at 62%.\n'
                                            '\n'
                                            'This directly informs a defensible CTQ target: rather than setting the '
                                            'purchase-intent target at the point estimate of 62% (which assumes the '
                                            'survey nailed the true value exactly), a more defensible approach uses '
                                            'the *lower bound* of the confidence interval — something like "≥55% '
                                            'purchase intent" — as the actual CTQ minimum. This is conservative by '
                                            'design: even in the less favorable end of the plausible range the data '
                                            'supports, the product still needs to clear the bar. Setting the target at '
                                            'the point estimate alone risks appearing to meet the CTQ in later testing '
                                            'due to sampling variation alone, not real underlying customer preference '
                                            '— exactly the kind of statistically unjustified target corporate wants to '
                                            'avoid for a company-wide financial commitment.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What does the calculated 95% confidence interval (54.2%, '
                                                         '69.8%) represent?',
                                             'options': [{'key': 'a',
                                                          'text': 'The range within which the team can be 95% '
                                                                  'confident the true population purchase-intent '
                                                                  'proportion actually falls *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The exact true proportion, guaranteed *(a '
                                                                  'confidence interval expresses a range of plausible '
                                                                  'values, not a guarantee of the exact truth)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': "The range of possible survey sample sizes *(it's "
                                                                  'about the proportion itself, not sample size)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'A margin of error that applies only to Black Belt '
                                                                  'projects *(confidence intervals are a general '
                                                                  'statistical concept, not project-type-specific)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'Why use the lower bound of the confidence interval (≈54%) '
                                                         'rather than the point estimate (62%) to set the CTQ target?',
                                             'options': [{'key': 'a',
                                                          'text': "It's a conservative approach that still requires "
                                                                  'the product to clear the bar even at the less '
                                                                  'favorable end of the plausible range *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': "The point estimate is always wrong *(it's a real, "
                                                                  'unbiased estimate — the issue is the uncertainty '
                                                                  "around it, not that it's incorrect)*",
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Lower numbers are always better regardless of '
                                                                  'context *(the reasoning here is about statistical '
                                                                  'defensibility, not simply preferring lower '
                                                                  'numbers)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'The upper bound should always be used instead '
                                                                  '*(using the upper bound would be less conservative, '
                                                                  'not more)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why does sample size (n=150) matter to how wide the '
                                                         'confidence interval is?',
                                             'options': [{'key': 'a',
                                                          'text': 'A larger sample size generally produces a smaller '
                                                                  'standard error and a narrower confidence interval, '
                                                                  'all else equal *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Sample size has no effect on the confidence '
                                                                  "interval's width *(it directly affects the standard "
                                                                  'error calculation, and thus the interval width)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'A smaller sample size always produces a narrower '
                                                                  'interval *(the opposite is generally true)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Confidence intervals require exactly 150 '
                                                                  'respondents to be valid *(150 is simply this '
                                                                  "survey's actual sample size, not a required "
                                                                  'number)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['A survey point estimate carries real sampling uncertainty, quantified by a '
                                    'confidence interval.',
                                    'Using the lower bound of a confidence interval, rather than the point estimate, '
                                    'sets a more defensible, conservative CTQ target.',
                                    'Larger sample sizes generally produce narrower, more precise confidence '
                                    'intervals.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'DMADV Module: Design for Six Sigma at Enterprise Scale (5 Lessons)'},
                       {'code': 'B11',
                        'title': 'Analyze (DMADV): A Factorial Experiment to Compare Formulation Factors',
                        'opening_question': 'Rather than testing pea protein at a single baking temperature the way '
                                            'the Green Belt project did, corporate wants to know: does baking '
                                            'temperature actually matter for shelf life, and does its effect depend on '
                                            "which protein source is used? A single-factor test can't answer whether "
                                            'two factors interact. What kind of experiment can?',
                        'concepts': ['A **2² factorial design** tests two factors (protein source: pea vs. whey; '
                                     'baking temperature: 350°F vs. 375°F) at two levels each, in all four '
                                     "combinations — letting the team estimate each factor's effect, and potentially "
                                     'their interaction, from a single small experiment.',
                                     '**Socratic prompt:** If the team had only tested pea protein at both '
                                     'temperatures (ignoring whey entirely), could they have concluded anything about '
                                     'whether protein source itself affects shelf life?',
                                     'A **main effect** is the average change in the response (here, shelf life) '
                                     "attributable to changing one factor's level, averaged across the levels of the "
                                     'other factor.'],
                        'terms': ['Factorial Design', 'Main Effect', 'One-Factor-at-a-Time (limitation)'],
                        'math': [{'name': 'Yield',
                                  'formula': 'Yield = good units / total units',
                                  'explanation': 'Share of units meeting the defined acceptance rule.',
                                  'variables': 'Yield = proportion of acceptable units; good units = units meeting the '
                                               'acceptance requirement; total units = all units evaluated.'},
                                 {'name': 'Factorial combinations',
                                  'formula': 'Number of combinations = 2^k',
                                  'explanation': 'Number of treatment combinations in a two-level full factorial '
                                                 'experiment with k factors.',
                                  'variables': 'k = number of factors; 2 = number of levels per factor; 2^k = total '
                                               'treatment combinations.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain the purpose and structure of a simple 2×2 factorial '
                                                'experiment',
                                                'Calculate main effects from factorial experiment data',
                                                'Interpret what a main effect tells you about which factor to '
                                                'prioritize controlling'],
                        'full_explanation': 'The experiment yields four runs:\n'
                                            '\n'
                                            '| Run | Protein Source | Baking Temp | Shelf Life (days) |\n'
                                            '|---|---|---|---|\n'
                                            '| 1 | Pea | 350°F | 11 |\n'
                                            '| 2 | Pea | 375°F | 9 |\n'
                                            '| 3 | Whey | 350°F | 8 |\n'
                                            '| 4 | Whey | 375°F | 7 |\n'
                                            '\n'
                                            '**Main effect of protein source** = (average at pea) − (average at whey) '
                                            '= [(11+9)/2] − [(8+7)/2] = 10 − 7.5 = **+2.5 days**. Pea protein '
                                            'produces, on average, 2.5 more days of shelf life than whey-based '
                                            'protein, across both temperature settings.\n'
                                            '\n'
                                            '**Main effect of baking temperature** = (average at 350°F) − (average at '
                                            '375°F) = [(11+8)/2] − [(9+7)/2] = 9.5 − 8 = **+1.5 days**. Baking at the '
                                            'lower temperature (350°F) produces, on average, 1.5 more days of shelf '
                                            'life than the higher temperature, across both protein sources.\n'
                                            '\n'
                                            'Both effects point in a consistent direction across the four runs (pea '
                                            'protein and lower temperature both help shelf life in each comparison), '
                                            'which is itself a useful check — a genuine interaction would show up as '
                                            'the temperature effect flipping direction or changing size dramatically '
                                            "depending on which protein source is used, which isn't strongly evident "
                                            'in just four runs but would be worth confirming with a larger, replicated '
                                            'design before treating it as settled. For now, this small experiment '
                                            'gives the team a clear, ranked priority: protein source matters more (2.5 '
                                            'days) than baking temperature (1.5 days) for shelf life — informing where '
                                            'Design should focus its most careful control.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What does the main effect of protein source (+2.5 days) '
                                                         'represent?',
                                             'options': [{'key': 'a',
                                                          'text': 'The average shelf-life difference between pea and '
                                                                  'whey protein, averaged across both temperature '
                                                                  'settings *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The exact shelf life of every pea-protein loaf, '
                                                                  "regardless of temperature *(it's an average effect, "
                                                                  'not a guarantee for every individual case)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The interaction between protein source and '
                                                                  'temperature *(this is a main effect, not an '
                                                                  'interaction effect)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': "A measurement error that should be ignored *(it's a "
                                                                  'calculated, meaningful effect from real '
                                                                  'experimental data)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': "Why couldn't testing only pea protein at two temperatures "
                                                         'answer whether protein source itself matters?',
                                             'options': [{'key': 'a',
                                                          'text': "That design would only reveal temperature's effect "
                                                                  'for pea protein alone — it says nothing about '
                                                                  'whether switching protein source changes shelf life '
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Protein source never affects shelf life in bread '
                                                                  'products *(the factorial data explicitly shows a '
                                                                  '2.5-day protein source effect)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Testing one factor at a time is always sufficient '
                                                                  'in Six Sigma projects *(this is exactly the '
                                                                  'limitation a factorial design overcomes)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Temperature and protein source can never both be '
                                                                  'tested in the same experiment *(a factorial design '
                                                                  'tests both simultaneously, as shown here)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Based on the calculated main effects, which factor should '
                                                         'Design prioritize controlling more carefully?',
                                             'options': [{'key': 'a',
                                                          'text': 'Protein source, since its effect (2.5 days) is '
                                                                  "larger than baking temperature's effect (1.5 days) "
                                                                  '*(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Baking temperature, since it was tested second '
                                                                  "*(order of testing doesn't determine priority — "
                                                                  'effect size does)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Neither factor matters, since both effects are '
                                                                  'small *(a multi-day shelf-life difference is a '
                                                                  'meaningful, actionable effect)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Both factors have exactly equal importance *(2.5 '
                                                                  "days and 1.5 days are not equal — protein source's "
                                                                  'effect is larger)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ["A 2×2 factorial experiment tests two factors together, revealing each factor's "
                                    'main effect and potential interactions — more informative than testing one factor '
                                    'at a time.',
                                    "Main effects quantify the average impact of changing one factor's level, averaged "
                                    "across the other factor's levels.",
                                    'Ranking main effects by size tells the team where to focus tightest control '
                                    'during Design.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'DMADV Module: Design for Six Sigma at Enterprise Scale (5 Lessons)'},
                       {'code': 'B12',
                        'title': 'Design (DMADV): A Regression Model Predicting Shelf Life',
                        'opening_question': 'The factorial experiment showed protein source and temperature both '
                                            'matter, but R&D suspects the real driver behind both effects is simpler: '
                                            "moisture content of the finished loaf. If that's true, could a single "
                                            'regression model let Design predict shelf life directly from moisture '
                                            'content, without needing to separately track protein source and '
                                            'temperature as their own variables?',
                        'concepts': ['Given five formulation batches with measured moisture content and observed shelf '
                                     'life, a **simple linear regression** finds the best-fit line: ShelfLife = '
                                     'intercept + slope × Moisture%.',
                                     '**Socratic prompt:** If the regression shows a strong, consistent relationship '
                                     'between moisture content and shelf life, what does that suggest about *why* '
                                     'protein source and baking temperature affected shelf life in the earlier '
                                     'factorial experiment?',
                                     '**R²** indicates how much of the variation in shelf life is explained by '
                                     'moisture content alone — a high R² suggests moisture content is a strong, '
                                     'reliable predictor.'],
                        'terms': ['Simple Linear Regression', 'Slope', 'R² (Coefficient of Determination)'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'},
                                 {'name': 'Factorial combinations',
                                  'formula': 'Number of combinations = 2^k',
                                  'explanation': 'Number of treatment combinations in a two-level full factorial '
                                                 'experiment with k factors.',
                                  'variables': 'k = number of factors; 2 = number of levels per factor; 2^k = total '
                                               'treatment combinations.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Fit a simple linear regression model from real data',
                                                'Interpret the slope, intercept, and R² of a regression model',
                                                'Use a regression equation to set a Design-phase target for an input '
                                                'variable'],
                        'full_explanation': 'Five batches produced this data:\n'
                                            '\n'
                                            '| Moisture % | Shelf Life (days) |\n'
                                            '|---|---|\n'
                                            '| 32 | 12 |\n'
                                            '| 34 | 11 |\n'
                                            '| 36 | 9 |\n'
                                            '| 38 | 8 |\n'
                                            '| 40 | 6 |\n'
                                            '\n'
                                            'Mean moisture = 36%, mean shelf life = 9.2 days. Calculating the slope '
                                            'using the deviations from each mean: slope = (sum of [(x−mean x)(y−mean '
                                            'y)]) ÷ (sum of [(x−mean x)²]) = −30 ÷ 40 = **−0.75**. This means each '
                                            '1-percentage-point increase in moisture content is associated with a '
                                            '0.75-day *decrease* in shelf life — bread with more residual moisture '
                                            'spoils faster, which matches basic food-science intuition and gives the '
                                            'number real credibility.\n'
                                            '\n'
                                            'The intercept: 9.2 − (−0.75 × 36) = 9.2 + 27 = **36.2**. The regression '
                                            'equation: **Shelf Life = 36.2 − 0.75 × (Moisture %)**. Checking fit, R² '
                                            'for this data comes out to approximately **0.987** — meaning moisture '
                                            'content alone explains about 98.7% of the variation in shelf life across '
                                            'these five batches, an unusually strong fit that suggests moisture is '
                                            'indeed the dominant driver behind what the factorial experiment '
                                            'observed.\n'
                                            '\n'
                                            'This equation is directly usable for Design: to hit the 10-day shelf-life '
                                            'CTQ minimum, solve 10 = 36.2 − 0.75 × Moisture, giving Moisture ≈ 34.9%. '
                                            "Design's formulation target becomes: keep finished-loaf moisture content "
                                            'at or below approximately 34.9%, rather than managing protein source and '
                                            'temperature as two separate, harder-to-control levers. (In practice, a '
                                            'Black Belt would also compute a prediction interval around this estimate, '
                                            'not just a point prediction, since five data points is a small sample — '
                                            'but the point estimate already gives Design a clear, actionable target to '
                                            'design around.)',
                        'knowledge_check': [{'number': 1,
                                             'question': 'What does the calculated slope (−0.75) mean in practical '
                                                         'terms?',
                                             'options': [{'key': 'a',
                                                          'text': 'Each 1-percentage-point increase in moisture '
                                                                  'content is associated with a 0.75-day decrease in '
                                                                  'shelf life *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Moisture content has no relationship with shelf '
                                                                  'life *(a slope of −0.75 indicates a clear, negative '
                                                                  'relationship)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Shelf life causes moisture content to change '
                                                                  '*(regression describes association, and '
                                                                  'food-science logic here suggests moisture drives '
                                                                  'shelf life, not the reverse)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'The relationship is positive — more moisture means '
                                                                  'longer shelf life *(the negative slope indicates '
                                                                  'the opposite relationship)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What does an R² of approximately 0.987 suggest about this '
                                                         'regression model?',
                                             'options': [{'key': 'a',
                                                          'text': 'Moisture content alone explains about 98.7% of the '
                                                                  'variation in shelf life across these batches — an '
                                                                  'unusually strong fit *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The model explains almost none of the variation '
                                                                  '*(0.987 is very close to 1, indicating a very '
                                                                  'strong fit)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'R² has no bearing on how useful the model is *(a '
                                                                  'high R² indicates the model is a strong, reliable '
                                                                  'predictor)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'R² only applies to factorial experiments, not '
                                                                  'regression *(R² is a standard regression fit '
                                                                  'statistic)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'Why might moisture content be a more useful Design-phase '
                                                         'target than separately managing protein source and '
                                                         'temperature?',
                                             'options': [{'key': 'a',
                                                          'text': 'If moisture content is the more fundamental driver '
                                                                  "behind both factors' effects, controlling it "
                                                                  'directly may be simpler and more effective than '
                                                                  'managing two indirect levers *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Protein source and temperature have no real effect '
                                                                  'on the product *(the factorial experiment showed '
                                                                  'they do — likely by affecting moisture)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Regression models can never inform formulation '
                                                                  'targets *(this lesson directly demonstrates using '
                                                                  'one to set a formulation target)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Moisture content cannot be measured or controlled '
                                                                  'in production *(the data used to build the model '
                                                                  'came from real, measured production batches)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['A simple linear regression predicts a response (shelf life) from a single input '
                                    'variable (moisture content), using slope, intercept, and R² to describe the '
                                    "relationship's strength and direction.",
                                    'A high R² suggests the input variable is a strong, reliable predictor — and may '
                                    'be a more fundamental driver than variables that influence it indirectly.',
                                    'A regression equation can be solved to set a specific, actionable Design-phase '
                                    'formulation target.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'DMADV Module: Design for Six Sigma at Enterprise Scale (5 Lessons)'},
                       {'code': 'B13',
                        'title': 'Verify (DMADV): Hypothesis Testing Across Three Plants Before Rollout',
                        'opening_question': 'With the moisture-controlled formulation (≤34.9%) piloted at all three '
                                            'plants, corporate wants one answer before approving full rollout: do '
                                            'Plants A, B, and C actually perform the same, or does one plant need a '
                                            'separate, adjusted process? How would a Black Belt answer that with '
                                            'statistical rigor, rather than eyeballing three averages?',
                        'concepts': ["Comparing shelf-life results across three plants' pilot batches requires a "
                                     'formal hypothesis test (such as one-way ANOVA), not just a visual comparison of '
                                     'three average values.',
                                     "**Socratic prompt:** If Plant A's pilot batches average 10.3 days, Plant B's "
                                     "average 9.8 days, and Plant C's average 10.6 days, does that half-day spread "
                                     'necessarily mean the plants perform differently in any meaningful sense — or '
                                     'could it just be normal batch-to-batch variation?',
                                     'The null hypothesis for this test: there is no real difference in mean shelf '
                                     'life across the three plants. A resulting p-value above 0.05 means the data '
                                     "doesn't provide strong evidence against that null hypothesis — it does *not* "
                                     'prove the plants are identical.'],
                        'terms': ['One-Way ANOVA', 'p-value', 'Null Hypothesis (Multi-Group Comparison)'],
                        'math': [{'name': 'Mean',
                                  'formula': 'x̄ = Σx / n',
                                  'explanation': 'Average of observed values; sensitive to extreme values.',
                                  'variables': 'x = each observed value; n = number of observations; Σ = sum of all '
                                               'observed values; x̄ = sample mean.'}],
                        'teach_back': 'Teach the approach back to me in your own words.',
                        'learning_objectives': ['Explain the purpose of comparing multiple groups statistically before '
                                                'assuming uniform performance',
                                                'Interpret a hypothesis test result (p-value) in the context of a '
                                                'rollout decision',
                                                'Distinguish "no significant difference found" from "the plants are '
                                                'definitely identical"'],
                        'full_explanation': "Running a one-way ANOVA (or equivalent) on the three plants' pilot "
                                            'shelf-life data tests whether the observed differences between plant '
                                            'averages (10.3, 9.8, 10.6 days) are larger than what could plausibly '
                                            "arise from normal random variation within each plant's own batch-to-batch "
                                            'results. Suppose the test returns a p-value of **0.31**. Since 0.31 is '
                                            'well above the conventional 0.05 threshold, the team fails to reject the '
                                            "null hypothesis — the data doesn't provide strong evidence that the three "
                                            'plants genuinely differ in mean shelf-life performance. This supports '
                                            'proceeding with a single, standardized process and formulation across all '
                                            'three plants, rather than developing plant-specific adjustments.\n'
                                            '\n'
                                            "It's worth being precise about what this conclusion actually means, and "
                                            "what it doesn't. A p-value of 0.31 does not prove the three plants "
                                            "perform identically — it means the pilot data simply doesn't provide "
                                            'strong enough evidence of a real difference to justify treating them '
                                            "differently. If a real, smaller difference exists but wasn't detected due "
                                            "to limited pilot sample size, that's a genuine possibility a Black Belt "
                                            'should acknowledge, not something the p-value rules out entirely.\n'
                                            '\n'
                                            'Contrast this with a hypothetical alternative outcome: if the same test '
                                            'had returned a p-value of **0.02**, that would fall below the 0.05 '
                                            'threshold, providing evidence against the null hypothesis — suggesting a '
                                            'real, statistically significant difference between at least one plant and '
                                            'the others. In that scenario, the team would need a follow-up test (a '
                                            'pairwise comparison) to identify which specific plant differs, and likely '
                                            'a plant-specific formulation adjustment before rollout, rather than '
                                            'assuming one standardized process fits all three sites. The entire value '
                                            'of this Verify-phase step is replacing "the averages look close enough" '
                                            'with an actual statistical basis for the rollout decision.',
                        'knowledge_check': [{'number': 1,
                                             'question': 'Why is a formal hypothesis test needed instead of just '
                                                         'comparing the three plant averages by eye?',
                                             'options': [{'key': 'a',
                                                          'text': 'A small spread between averages could reflect '
                                                                  'normal random variation or a real difference — only '
                                                                  'a formal test, using within-plant variation, can '
                                                                  'distinguish the two *(correct)*',
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Comparing averages by eye is always sufficient for '
                                                                  'a rollout decision *(this is exactly the imprecise '
                                                                  'approach a formal test replaces)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Hypothesis tests are only needed when averages are '
                                                                  "identical *(they're most useful precisely when "
                                                                  'averages differ somewhat, to determine if the '
                                                                  'difference is meaningful)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'ANOVA cannot be used to compare more than two '
                                                                  'groups *(ANOVA is specifically designed to compare '
                                                                  'three or more groups)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 2,
                                             'question': 'What does a p-value of 0.31 actually indicate about the '
                                                         'three plants?',
                                             'options': [{'key': 'a',
                                                          'text': "The data doesn't provide strong evidence of a real "
                                                                  'difference between the plants — it does not prove '
                                                                  "they're identical *(correct)*",
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'The plants are proven to perform identically '
                                                                  '*(failing to reject the null hypothesis is not the '
                                                                  'same as proving it true)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'The experiment failed and should be discarded *(a '
                                                                  'p-value of 0.31 is a valid, interpretable result, '
                                                                  'not a failed experiment)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'There is a 31% chance the plants are actually '
                                                                  'different *(this misinterprets what a p-value '
                                                                  'represents — it does not directly state the '
                                                                  'probability that a hypothesis is true)*',
                                                          'correct': False}],
                                             'answer': ''},
                                            {'number': 3,
                                             'question': 'If the test had instead returned p = 0.02, what would be the '
                                                         'appropriate next step before rollout?',
                                             'options': [{'key': 'a',
                                                          'text': 'Run a follow-up pairwise comparison to identify '
                                                                  'which specific plant differs, and likely adjust '
                                                                  "that plant's formulation before rollout *(correct)*",
                                                          'correct': True},
                                                         {'key': 'b',
                                                          'text': 'Proceed with rollout exactly as planned, since 0.02 '
                                                                  'is a small number *(a p-value below 0.05 indicates '
                                                                  'evidence of a real difference, requiring further '
                                                                  'investigation, not proceeding as if nothing '
                                                                  'changed)*',
                                                          'correct': False},
                                                         {'key': 'c',
                                                          'text': 'Discard the entire DMADV project and restart from '
                                                                  'Define *(a significant difference at one plant '
                                                                  "doesn't invalidate the whole project — it calls for "
                                                                  'targeted adjustment)*',
                                                          'correct': False},
                                                         {'key': 'd',
                                                          'text': 'Conclude that hypothesis testing is unreliable and '
                                                                  'abandon statistical verification *(a significant '
                                                                  'result is a valid, informative finding, not a '
                                                                  'reason to distrust the method)*',
                                                          'correct': False}],
                                             'answer': ''}],
                        'summary': ['Comparing group averages by eye risks misjudging whether an observed spread '
                                    'reflects real difference or normal variation — a formal hypothesis test resolves '
                                    'this.',
                                    'A p-value above the significance threshold means insufficient evidence of a real '
                                    'difference — not proof of true equivalence.',
                                    'A significant result (low p-value) calls for follow-up investigation and targeted '
                                    'adjustment, not abandoning the project.'],
                        'hands_on_activity': '',
                        'worked_solution': '',
                        'module_title': 'DMADV Module: Design for Six Sigma at Enterprise Scale (5 Lessons)'}]}}


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





# Belt-level assessment: 20-question adaptive Questions.
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

