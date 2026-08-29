SCENARIO_DETAIL = {'b-customer-verification': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                                   'id': 'problem',
                                                   'prompt': 'What is the problem in measurable terms, and for whom?',
                                                   'requires': ['baseline', 'customer', 'problem']},
                                                  {'feedback': 'Turn plausible stories into testable hypotheses.',
                                                   'id': 'evidence',
                                                   'prompt': 'Which evidence would distinguish competing explanations?',
                                                   'requires': ['evidence', 'data', 'variation']},
                                                  {'feedback': 'Treat organizational incentives as part of the operating system.',
                                                   'id': 'people',
                                                   'prompt': 'Which stakeholder incentives could distort the information you are '
                                                             'receiving?',
                                                   'requires': ['incentive', 'political', 'social']}],
                             'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                                   'id': 'fast',
                                                   'label': 'Move quickly on the most visible solution',
                                                   'signal': 'speed'},
                                                  {'effect': 'Slower up front; improves the quality of the causal decision.',
                                                   'id': 'evidence',
                                                   'label': 'Collect targeted evidence before committing',
                                                   'signal': 'evidence'},
                                                  {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                                   'id': 'redesign',
                                                   'label': 'Redesign the process around the customer requirement',
                                                   'signal': 'design'}],
                             'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                             'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity '
                                                            'cost.',
                                                'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what '
                                                         'can be defended responsibly.',
                                                'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                                'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                          'consequences for people.',
                                                'political': 'Consider power, incentives, commitments, reputation, ownership, and '
                                                             'competing agendas.',
                                                'social': 'Consider team norms, status, trust, psychological safety, adoption, and '
                                                          'informal work practices.'},
                             'socratic_prompts': ['What do you know versus what are you assuming?',
                                                  'Whose definition of the problem are you using?',
                                                  'What evidence would change your mind?',
                                                  'Who benefits or loses if this recommendation is adopted?',
                                                  'What would make a technically correct solution fail organizationally?'],
                             'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                    'constraint than the other stakeholders.',
                                                                                    'The stakeholder has an incentive that can influence '
                                                                                    'which facts are emphasized.'],
                                                                          'incentive': 'Experiences the outcome and defines value '
                                                                                       'differently from internal teams.',
                                                                          'opening': 'Experiences the outcome and defines value '
                                                                                     'differently from internal teams. In customer '
                                                                                     'verification redesign, this stakeholder sees a '
                                                                                     'different part of the operating problem.',
                                                                          'role': 'Customer / user'},
                                              'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or '
                                                                              'constraint than the other stakeholders.',
                                                                              'The stakeholder has an incentive that can influence which '
                                                                              'facts are emphasized.'],
                                                                    'incentive': 'Wants a visible result and has a commitment to defend.',
                                                                    'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                               'customer verification redesign, this stakeholder sees a '
                                                                               'different part of the operating problem.',
                                                                    'role': 'Executive sponsor'},
                                              'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                            'than the other stakeholders.',
                                                                            'The stakeholder has an incentive that can influence which '
                                                                            'facts are emphasized.'],
                                                                  'incentive': 'Tests whether improvement becomes a credible economic '
                                                                               'benefit.',
                                                                  'opening': 'Tests whether improvement becomes a credible economic '
                                                                             'benefit. In customer verification redesign, this stakeholder '
                                                                             'sees a different part of the operating problem.',
                                                                  'role': 'Finance'},
                                              'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                     'constraint than the other stakeholders.',
                                                                                     'The stakeholder has an incentive that can influence '
                                                                                     'which facts are emphasized.'],
                                                                           'incentive': 'Sees workarounds, exceptions, friction, and '
                                                                                        'practical constraints.',
                                                                           'opening': 'Sees workarounds, exceptions, friction, and '
                                                                                      'practical constraints. In customer verification '
                                                                                      'redesign, this stakeholder sees a different part of '
                                                                                      'the operating problem.',
                                                                           'role': 'Frontline employee'},
                                              'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                          'than the other stakeholders.',
                                                                          'The stakeholder has an incentive that can influence which facts '
                                                                          'are emphasized.'],
                                                                'incentive': 'Owns service performance and operational continuity.',
                                                                'opening': 'Owns service performance and operational continuity. In '
                                                                           'customer verification redesign, this stakeholder sees a '
                                                                           'different part of the operating problem.',
                                                                'role': 'Process owner'},
                                              'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                            'than the other stakeholders.',
                                                                            'The stakeholder has an incentive that can influence which '
                                                                            'facts are emphasized.'],
                                                                  'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                               'requirements.',
                                                                  'opening': 'Protects policy, regulatory, control, and reputational '
                                                                             'requirements. In customer verification redesign, this '
                                                                             'stakeholder sees a different part of the operating problem.',
                                                                  'role': 'Risk / compliance'}}},
 'b-digital-onboarding': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                                'id': 'problem',
                                                'prompt': 'What is the problem in measurable terms, and for whom?',
                                                'requires': ['baseline', 'customer', 'problem']},
                                               {'feedback': 'Turn plausible stories into testable hypotheses.',
                                                'id': 'evidence',
                                                'prompt': 'Which evidence would distinguish competing explanations?',
                                                'requires': ['evidence', 'data', 'variation']},
                                               {'feedback': 'Treat organizational incentives as part of the operating system.',
                                                'id': 'people',
                                                'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                                'requires': ['incentive', 'political', 'social']}],
                          'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                                'id': 'fast',
                                                'label': 'Move quickly on the most visible solution',
                                                'signal': 'speed'},
                                               {'effect': 'Slower up front; improves the quality of the causal decision.',
                                                'id': 'evidence',
                                                'label': 'Collect targeted evidence before committing',
                                                'signal': 'evidence'},
                                               {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                                'id': 'redesign',
                                                'label': 'Redesign the process around the customer requirement',
                                                'signal': 'design'}],
                          'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                          'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                             'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can '
                                                      'be defended responsibly.',
                                             'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                             'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                       'consequences for people.',
                                             'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                          'agendas.',
                                             'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal '
                                                       'work practices.'},
                          'socratic_prompts': ['What do you know versus what are you assuming?',
                                               'Whose definition of the problem are you using?',
                                               'What evidence would change your mind?',
                                               'Who benefits or loses if this recommendation is adopted?',
                                               'What would make a technically correct solution fail organizationally?'],
                          'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                 'constraint than the other stakeholders.',
                                                                                 'The stakeholder has an incentive that can influence '
                                                                                 'which facts are emphasized.'],
                                                                       'incentive': 'Experiences the outcome and defines value differently '
                                                                                    'from internal teams.',
                                                                       'opening': 'Experiences the outcome and defines value differently '
                                                                                  'from internal teams. In digital account opening '
                                                                                  'redesign, this stakeholder sees a different part of the '
                                                                                  'operating problem.',
                                                                       'role': 'Customer / user'},
                                           'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                           'than the other stakeholders.',
                                                                           'The stakeholder has an incentive that can influence which '
                                                                           'facts are emphasized.'],
                                                                 'incentive': 'Wants a visible result and has a commitment to defend.',
                                                                 'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                            'digital account opening redesign, this stakeholder sees a '
                                                                            'different part of the operating problem.',
                                                                 'role': 'Executive sponsor'},
                                           'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                         'than the other stakeholders.',
                                                                         'The stakeholder has an incentive that can influence which facts '
                                                                         'are emphasized.'],
                                                               'incentive': 'Tests whether improvement becomes a credible economic '
                                                                            'benefit.',
                                                               'opening': 'Tests whether improvement becomes a credible economic benefit. '
                                                                          'In digital account opening redesign, this stakeholder sees a '
                                                                          'different part of the operating problem.',
                                                               'role': 'Finance'},
                                           'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                  'constraint than the other stakeholders.',
                                                                                  'The stakeholder has an incentive that can influence '
                                                                                  'which facts are emphasized.'],
                                                                        'incentive': 'Sees workarounds, exceptions, friction, and '
                                                                                     'practical constraints.',
                                                                        'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                                   'constraints. In digital account opening redesign, this '
                                                                                   'stakeholder sees a different part of the operating '
                                                                                   'problem.',
                                                                        'role': 'Frontline employee'},
                                           'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                       'the other stakeholders.',
                                                                       'The stakeholder has an incentive that can influence which facts '
                                                                       'are emphasized.'],
                                                             'incentive': 'Owns service performance and operational continuity.',
                                                             'opening': 'Owns service performance and operational continuity. In digital '
                                                                        'account opening redesign, this stakeholder sees a different part '
                                                                        'of the operating problem.',
                                                             'role': 'Process owner'},
                                           'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                         'than the other stakeholders.',
                                                                         'The stakeholder has an incentive that can influence which facts '
                                                                         'are emphasized.'],
                                                               'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                            'requirements.',
                                                               'opening': 'Protects policy, regulatory, control, and reputational '
                                                                          'requirements. In digital account opening redesign, this '
                                                                          'stakeholder sees a different part of the operating problem.',
                                                               'role': 'Risk / compliance'}}},
 'b-medication-administration': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                                       'id': 'problem',
                                                       'prompt': 'What is the problem in measurable terms, and for whom?',
                                                       'requires': ['baseline', 'customer', 'problem']},
                                                      {'feedback': 'Turn plausible stories into testable hypotheses.',
                                                       'id': 'evidence',
                                                       'prompt': 'Which evidence would distinguish competing explanations?',
                                                       'requires': ['evidence', 'data', 'variation']},
                                                      {'feedback': 'Treat organizational incentives as part of the operating system.',
                                                       'id': 'people',
                                                       'prompt': 'Which stakeholder incentives could distort the information you are '
                                                                 'receiving?',
                                                       'requires': ['incentive', 'political', 'social']}],
                                 'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                                       'id': 'fast',
                                                       'label': 'Move quickly on the most visible solution',
                                                       'signal': 'speed'},
                                                      {'effect': 'Slower up front; improves the quality of the causal decision.',
                                                       'id': 'evidence',
                                                       'label': 'Collect targeted evidence before committing',
                                                       'signal': 'evidence'},
                                                      {'effect': 'May deliver a stronger outcome but requires broader stakeholder '
                                                                 'alignment.',
                                                       'id': 'redesign',
                                                       'label': 'Redesign the process around the customer requirement',
                                                       'signal': 'design'}],
                                 'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                                 'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity '
                                                                'cost.',
                                                    'ethos': 'Consider professional responsibility, credibility, fairness, controls, and '
                                                             'what can be defended responsibly.',
                                                    'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                                    'pathos': 'Consider customer and employee experience, trust, frustration, workload, '
                                                              'and consequences for people.',
                                                    'political': 'Consider power, incentives, commitments, reputation, ownership, and '
                                                                 'competing agendas.',
                                                    'social': 'Consider team norms, status, trust, psychological safety, adoption, and '
                                                              'informal work practices.'},
                                 'socratic_prompts': ['What do you know versus what are you assuming?',
                                                      'Whose definition of the problem are you using?',
                                                      'What evidence would change your mind?',
                                                      'Who benefits or loses if this recommendation is adopted?',
                                                      'What would make a technically correct solution fail organizationally?'],
                                 'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome '
                                                                                        'or constraint than the other stakeholders.',
                                                                                        'The stakeholder has an incentive that can '
                                                                                        'influence which facts are emphasized.'],
                                                                              'incentive': 'Experiences the outcome and defines value '
                                                                                           'differently from internal teams.',
                                                                              'opening': 'Experiences the outcome and defines value '
                                                                                         'differently from internal teams. In medication '
                                                                                         'administration reliability, this stakeholder '
                                                                                         'sees a different part of the operating problem.',
                                                                              'role': 'Customer / user'},
                                                  'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                  'constraint than the other stakeholders.',
                                                                                  'The stakeholder has an incentive that can influence '
                                                                                  'which facts are emphasized.'],
                                                                        'incentive': 'Wants a visible result and has a commitment to '
                                                                                     'defend.',
                                                                        'opening': 'Wants a visible result and has a commitment to defend. '
                                                                                   'In medication administration reliability, this '
                                                                                   'stakeholder sees a different part of the operating '
                                                                                   'problem.',
                                                                        'role': 'Executive sponsor'},
                                                  'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                'constraint than the other stakeholders.',
                                                                                'The stakeholder has an incentive that can influence which '
                                                                                'facts are emphasized.'],
                                                                      'incentive': 'Tests whether improvement becomes a credible economic '
                                                                                   'benefit.',
                                                                      'opening': 'Tests whether improvement becomes a credible economic '
                                                                                 'benefit. In medication administration reliability, this '
                                                                                 'stakeholder sees a different part of the operating '
                                                                                 'problem.',
                                                                      'role': 'Finance'},
                                                  'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome '
                                                                                         'or constraint than the other stakeholders.',
                                                                                         'The stakeholder has an incentive that can '
                                                                                         'influence which facts are emphasized.'],
                                                                               'incentive': 'Sees workarounds, exceptions, friction, and '
                                                                                            'practical constraints.',
                                                                               'opening': 'Sees workarounds, exceptions, friction, and '
                                                                                          'practical constraints. In medication '
                                                                                          'administration reliability, this stakeholder '
                                                                                          'sees a different part of the operating problem.',
                                                                               'role': 'Frontline employee'},
                                                  'Process Owner': {'clues': ['This perspective emphasizes a different outcome or '
                                                                              'constraint than the other stakeholders.',
                                                                              'The stakeholder has an incentive that can influence which '
                                                                              'facts are emphasized.'],
                                                                    'incentive': 'Owns service performance and operational continuity.',
                                                                    'opening': 'Owns service performance and operational continuity. In '
                                                                               'medication administration reliability, this stakeholder '
                                                                               'sees a different part of the operating problem.',
                                                                    'role': 'Process owner'},
                                                  'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                'constraint than the other stakeholders.',
                                                                                'The stakeholder has an incentive that can influence which '
                                                                                'facts are emphasized.'],
                                                                      'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                                   'requirements.',
                                                                      'opening': 'Protects policy, regulatory, control, and reputational '
                                                                                 'requirements. In medication administration reliability, '
                                                                                 'this stakeholder sees a different part of the operating '
                                                                                 'problem.',
                                                                      'role': 'Risk / compliance'}}},
 'b-product-defects': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                             'id': 'problem',
                                             'prompt': 'What is the problem in measurable terms, and for whom?',
                                             'requires': ['baseline', 'customer', 'problem']},
                                            {'feedback': 'Turn plausible stories into testable hypotheses.',
                                             'id': 'evidence',
                                             'prompt': 'Which evidence would distinguish competing explanations?',
                                             'requires': ['evidence', 'data', 'variation']},
                                            {'feedback': 'Treat organizational incentives as part of the operating system.',
                                             'id': 'people',
                                             'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                             'requires': ['incentive', 'political', 'social']}],
                       'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                             'id': 'fast',
                                             'label': 'Move quickly on the most visible solution',
                                             'signal': 'speed'},
                                            {'effect': 'Slower up front; improves the quality of the causal decision.',
                                             'id': 'evidence',
                                             'label': 'Collect targeted evidence before committing',
                                             'signal': 'evidence'},
                                            {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                             'id': 'redesign',
                                             'label': 'Redesign the process around the customer requirement',
                                             'signal': 'design'}],
                       'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                       'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                          'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can be '
                                                   'defended responsibly.',
                                          'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                          'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                    'consequences for people.',
                                          'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                       'agendas.',
                                          'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal work '
                                                    'practices.'},
                       'socratic_prompts': ['What do you know versus what are you assuming?',
                                            'Whose definition of the problem are you using?',
                                            'What evidence would change your mind?',
                                            'Who benefits or loses if this recommendation is adopted?',
                                            'What would make a technically correct solution fail organizationally?'],
                       'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                              'constraint than the other stakeholders.',
                                                                              'The stakeholder has an incentive that can influence which '
                                                                              'facts are emphasized.'],
                                                                    'incentive': 'Experiences the outcome and defines value differently '
                                                                                 'from internal teams.',
                                                                    'opening': 'Experiences the outcome and defines value differently from '
                                                                               'internal teams. In new product defect escape, this '
                                                                               'stakeholder sees a different part of the operating '
                                                                               'problem.',
                                                                    'role': 'Customer / user'},
                                        'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                        'than the other stakeholders.',
                                                                        'The stakeholder has an incentive that can influence which facts '
                                                                        'are emphasized.'],
                                                              'incentive': 'Wants a visible result and has a commitment to defend.',
                                                              'opening': 'Wants a visible result and has a commitment to defend. In new '
                                                                         'product defect escape, this stakeholder sees a different part of '
                                                                         'the operating problem.',
                                                              'role': 'Executive sponsor'},
                                        'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                      'the other stakeholders.',
                                                                      'The stakeholder has an incentive that can influence which facts are '
                                                                      'emphasized.'],
                                                            'incentive': 'Tests whether improvement becomes a credible economic benefit.',
                                                            'opening': 'Tests whether improvement becomes a credible economic benefit. In '
                                                                       'new product defect escape, this stakeholder sees a different part '
                                                                       'of the operating problem.',
                                                            'role': 'Finance'},
                                        'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                               'constraint than the other stakeholders.',
                                                                               'The stakeholder has an incentive that can influence which '
                                                                               'facts are emphasized.'],
                                                                     'incentive': 'Sees workarounds, exceptions, friction, and practical '
                                                                                  'constraints.',
                                                                     'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                                'constraints. In new product defect escape, this '
                                                                                'stakeholder sees a different part of the operating '
                                                                                'problem.',
                                                                     'role': 'Frontline employee'},
                                        'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                    'the other stakeholders.',
                                                                    'The stakeholder has an incentive that can influence which facts are '
                                                                    'emphasized.'],
                                                          'incentive': 'Owns service performance and operational continuity.',
                                                          'opening': 'Owns service performance and operational continuity. In new product '
                                                                     'defect escape, this stakeholder sees a different part of the '
                                                                     'operating problem.',
                                                          'role': 'Process owner'},
                                        'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                      'the other stakeholders.',
                                                                      'The stakeholder has an incentive that can influence which facts are '
                                                                      'emphasized.'],
                                                            'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                         'requirements.',
                                                            'opening': 'Protects policy, regulatory, control, and reputational '
                                                                       'requirements. In new product defect escape, this stakeholder sees '
                                                                       'a different part of the operating problem.',
                                                            'role': 'Risk / compliance'}}},
 'b-supply-planning': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                             'id': 'problem',
                                             'prompt': 'What is the problem in measurable terms, and for whom?',
                                             'requires': ['baseline', 'customer', 'problem']},
                                            {'feedback': 'Turn plausible stories into testable hypotheses.',
                                             'id': 'evidence',
                                             'prompt': 'Which evidence would distinguish competing explanations?',
                                             'requires': ['evidence', 'data', 'variation']},
                                            {'feedback': 'Treat organizational incentives as part of the operating system.',
                                             'id': 'people',
                                             'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                             'requires': ['incentive', 'political', 'social']}],
                       'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                             'id': 'fast',
                                             'label': 'Move quickly on the most visible solution',
                                             'signal': 'speed'},
                                            {'effect': 'Slower up front; improves the quality of the causal decision.',
                                             'id': 'evidence',
                                             'label': 'Collect targeted evidence before committing',
                                             'signal': 'evidence'},
                                            {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                             'id': 'redesign',
                                             'label': 'Redesign the process around the customer requirement',
                                             'signal': 'design'}],
                       'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                       'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                          'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can be '
                                                   'defended responsibly.',
                                          'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                          'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                    'consequences for people.',
                                          'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                       'agendas.',
                                          'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal work '
                                                    'practices.'},
                       'socratic_prompts': ['What do you know versus what are you assuming?',
                                            'Whose definition of the problem are you using?',
                                            'What evidence would change your mind?',
                                            'Who benefits or loses if this recommendation is adopted?',
                                            'What would make a technically correct solution fail organizationally?'],
                       'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                              'constraint than the other stakeholders.',
                                                                              'The stakeholder has an incentive that can influence which '
                                                                              'facts are emphasized.'],
                                                                    'incentive': 'Experiences the outcome and defines value differently '
                                                                                 'from internal teams.',
                                                                    'opening': 'Experiences the outcome and defines value differently from '
                                                                               'internal teams. In supply planning forecast error, this '
                                                                               'stakeholder sees a different part of the operating '
                                                                               'problem.',
                                                                    'role': 'Customer / user'},
                                        'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                        'than the other stakeholders.',
                                                                        'The stakeholder has an incentive that can influence which facts '
                                                                        'are emphasized.'],
                                                              'incentive': 'Wants a visible result and has a commitment to defend.',
                                                              'opening': 'Wants a visible result and has a commitment to defend. In supply '
                                                                         'planning forecast error, this stakeholder sees a different part '
                                                                         'of the operating problem.',
                                                              'role': 'Executive sponsor'},
                                        'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                      'the other stakeholders.',
                                                                      'The stakeholder has an incentive that can influence which facts are '
                                                                      'emphasized.'],
                                                            'incentive': 'Tests whether improvement becomes a credible economic benefit.',
                                                            'opening': 'Tests whether improvement becomes a credible economic benefit. In '
                                                                       'supply planning forecast error, this stakeholder sees a different '
                                                                       'part of the operating problem.',
                                                            'role': 'Finance'},
                                        'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                               'constraint than the other stakeholders.',
                                                                               'The stakeholder has an incentive that can influence which '
                                                                               'facts are emphasized.'],
                                                                     'incentive': 'Sees workarounds, exceptions, friction, and practical '
                                                                                  'constraints.',
                                                                     'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                                'constraints. In supply planning forecast error, this '
                                                                                'stakeholder sees a different part of the operating '
                                                                                'problem.',
                                                                     'role': 'Frontline employee'},
                                        'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                    'the other stakeholders.',
                                                                    'The stakeholder has an incentive that can influence which facts are '
                                                                    'emphasized.'],
                                                          'incentive': 'Owns service performance and operational continuity.',
                                                          'opening': 'Owns service performance and operational continuity. In supply '
                                                                     'planning forecast error, this stakeholder sees a different part of '
                                                                     'the operating problem.',
                                                          'role': 'Process owner'},
                                        'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                      'the other stakeholders.',
                                                                      'The stakeholder has an incentive that can influence which facts are '
                                                                      'emphasized.'],
                                                            'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                         'requirements.',
                                                            'opening': 'Protects policy, regulatory, control, and reputational '
                                                                       'requirements. In supply planning forecast error, this stakeholder '
                                                                       'sees a different part of the operating problem.',
                                                            'role': 'Risk / compliance'}}},
 'g-call-resolution': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                             'id': 'problem',
                                             'prompt': 'What is the problem in measurable terms, and for whom?',
                                             'requires': ['baseline', 'customer', 'problem']},
                                            {'feedback': 'Turn plausible stories into testable hypotheses.',
                                             'id': 'evidence',
                                             'prompt': 'Which evidence would distinguish competing explanations?',
                                             'requires': ['evidence', 'data', 'variation']},
                                            {'feedback': 'Treat organizational incentives as part of the operating system.',
                                             'id': 'people',
                                             'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                             'requires': ['incentive', 'political', 'social']}],
                       'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                             'id': 'fast',
                                             'label': 'Move quickly on the most visible solution',
                                             'signal': 'speed'},
                                            {'effect': 'Slower up front; improves the quality of the causal decision.',
                                             'id': 'evidence',
                                             'label': 'Collect targeted evidence before committing',
                                             'signal': 'evidence'},
                                            {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                             'id': 'redesign',
                                             'label': 'Redesign the process around the customer requirement',
                                             'signal': 'design'}],
                       'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                       'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                          'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can be '
                                                   'defended responsibly.',
                                          'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                          'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                    'consequences for people.',
                                          'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                       'agendas.',
                                          'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal work '
                                                    'practices.'},
                       'socratic_prompts': ['What do you know versus what are you assuming?',
                                            'Whose definition of the problem are you using?',
                                            'What evidence would change your mind?',
                                            'Who benefits or loses if this recommendation is adopted?',
                                            'What would make a technically correct solution fail organizationally?'],
                       'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                              'constraint than the other stakeholders.',
                                                                              'The stakeholder has an incentive that can influence which '
                                                                              'facts are emphasized.'],
                                                                    'incentive': 'Experiences the outcome and defines value differently '
                                                                                 'from internal teams.',
                                                                    'opening': 'Experiences the outcome and defines value differently from '
                                                                               'internal teams. In contact centre first-call resolution, '
                                                                               'this stakeholder sees a different part of the operating '
                                                                               'problem.',
                                                                    'role': 'Customer / user'},
                                        'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                        'than the other stakeholders.',
                                                                        'The stakeholder has an incentive that can influence which facts '
                                                                        'are emphasized.'],
                                                              'incentive': 'Wants a visible result and has a commitment to defend.',
                                                              'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                         'contact centre first-call resolution, this stakeholder sees a '
                                                                         'different part of the operating problem.',
                                                              'role': 'Executive sponsor'},
                                        'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                      'the other stakeholders.',
                                                                      'The stakeholder has an incentive that can influence which facts are '
                                                                      'emphasized.'],
                                                            'incentive': 'Tests whether improvement becomes a credible economic benefit.',
                                                            'opening': 'Tests whether improvement becomes a credible economic benefit. In '
                                                                       'contact centre first-call resolution, this stakeholder sees a '
                                                                       'different part of the operating problem.',
                                                            'role': 'Finance'},
                                        'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                               'constraint than the other stakeholders.',
                                                                               'The stakeholder has an incentive that can influence which '
                                                                               'facts are emphasized.'],
                                                                     'incentive': 'Sees workarounds, exceptions, friction, and practical '
                                                                                  'constraints.',
                                                                     'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                                'constraints. In contact centre first-call resolution, '
                                                                                'this stakeholder sees a different part of the operating '
                                                                                'problem.',
                                                                     'role': 'Frontline employee'},
                                        'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                    'the other stakeholders.',
                                                                    'The stakeholder has an incentive that can influence which facts are '
                                                                    'emphasized.'],
                                                          'incentive': 'Owns service performance and operational continuity.',
                                                          'opening': 'Owns service performance and operational continuity. In contact '
                                                                     'centre first-call resolution, this stakeholder sees a different part '
                                                                     'of the operating problem.',
                                                          'role': 'Process owner'},
                                        'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                      'the other stakeholders.',
                                                                      'The stakeholder has an incentive that can influence which facts are '
                                                                      'emphasized.'],
                                                            'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                         'requirements.',
                                                            'opening': 'Protects policy, regulatory, control, and reputational '
                                                                       'requirements. In contact centre first-call resolution, this '
                                                                       'stakeholder sees a different part of the operating problem.',
                                                            'role': 'Risk / compliance'}}},
 'g-factory-changeover': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                                'id': 'problem',
                                                'prompt': 'What is the problem in measurable terms, and for whom?',
                                                'requires': ['baseline', 'customer', 'problem']},
                                               {'feedback': 'Turn plausible stories into testable hypotheses.',
                                                'id': 'evidence',
                                                'prompt': 'Which evidence would distinguish competing explanations?',
                                                'requires': ['evidence', 'data', 'variation']},
                                               {'feedback': 'Treat organizational incentives as part of the operating system.',
                                                'id': 'people',
                                                'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                                'requires': ['incentive', 'political', 'social']}],
                          'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                                'id': 'fast',
                                                'label': 'Move quickly on the most visible solution',
                                                'signal': 'speed'},
                                               {'effect': 'Slower up front; improves the quality of the causal decision.',
                                                'id': 'evidence',
                                                'label': 'Collect targeted evidence before committing',
                                                'signal': 'evidence'},
                                               {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                                'id': 'redesign',
                                                'label': 'Redesign the process around the customer requirement',
                                                'signal': 'design'}],
                          'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                          'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                             'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can '
                                                      'be defended responsibly.',
                                             'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                             'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                       'consequences for people.',
                                             'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                          'agendas.',
                                             'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal '
                                                       'work practices.'},
                          'socratic_prompts': ['What do you know versus what are you assuming?',
                                               'Whose definition of the problem are you using?',
                                               'What evidence would change your mind?',
                                               'Who benefits or loses if this recommendation is adopted?',
                                               'What would make a technically correct solution fail organizationally?'],
                          'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                 'constraint than the other stakeholders.',
                                                                                 'The stakeholder has an incentive that can influence '
                                                                                 'which facts are emphasized.'],
                                                                       'incentive': 'Experiences the outcome and defines value differently '
                                                                                    'from internal teams.',
                                                                       'opening': 'Experiences the outcome and defines value differently '
                                                                                  'from internal teams. In production changeover '
                                                                                  'variation, this stakeholder sees a different part of '
                                                                                  'the operating problem.',
                                                                       'role': 'Customer / user'},
                                           'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                           'than the other stakeholders.',
                                                                           'The stakeholder has an incentive that can influence which '
                                                                           'facts are emphasized.'],
                                                                 'incentive': 'Wants a visible result and has a commitment to defend.',
                                                                 'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                            'production changeover variation, this stakeholder sees a '
                                                                            'different part of the operating problem.',
                                                                 'role': 'Executive sponsor'},
                                           'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                         'than the other stakeholders.',
                                                                         'The stakeholder has an incentive that can influence which facts '
                                                                         'are emphasized.'],
                                                               'incentive': 'Tests whether improvement becomes a credible economic '
                                                                            'benefit.',
                                                               'opening': 'Tests whether improvement becomes a credible economic benefit. '
                                                                          'In production changeover variation, this stakeholder sees a '
                                                                          'different part of the operating problem.',
                                                               'role': 'Finance'},
                                           'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                  'constraint than the other stakeholders.',
                                                                                  'The stakeholder has an incentive that can influence '
                                                                                  'which facts are emphasized.'],
                                                                        'incentive': 'Sees workarounds, exceptions, friction, and '
                                                                                     'practical constraints.',
                                                                        'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                                   'constraints. In production changeover variation, this '
                                                                                   'stakeholder sees a different part of the operating '
                                                                                   'problem.',
                                                                        'role': 'Frontline employee'},
                                           'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                       'the other stakeholders.',
                                                                       'The stakeholder has an incentive that can influence which facts '
                                                                       'are emphasized.'],
                                                             'incentive': 'Owns service performance and operational continuity.',
                                                             'opening': 'Owns service performance and operational continuity. In '
                                                                        'production changeover variation, this stakeholder sees a '
                                                                        'different part of the operating problem.',
                                                             'role': 'Process owner'},
                                           'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                         'than the other stakeholders.',
                                                                         'The stakeholder has an incentive that can influence which facts '
                                                                         'are emphasized.'],
                                                               'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                            'requirements.',
                                                               'opening': 'Protects policy, regulatory, control, and reputational '
                                                                          'requirements. In production changeover variation, this '
                                                                          'stakeholder sees a different part of the operating problem.',
                                                               'role': 'Risk / compliance'}}},
 'g-hospital-pharmacy': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                               'id': 'problem',
                                               'prompt': 'What is the problem in measurable terms, and for whom?',
                                               'requires': ['baseline', 'customer', 'problem']},
                                              {'feedback': 'Turn plausible stories into testable hypotheses.',
                                               'id': 'evidence',
                                               'prompt': 'Which evidence would distinguish competing explanations?',
                                               'requires': ['evidence', 'data', 'variation']},
                                              {'feedback': 'Treat organizational incentives as part of the operating system.',
                                               'id': 'people',
                                               'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                               'requires': ['incentive', 'political', 'social']}],
                         'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                               'id': 'fast',
                                               'label': 'Move quickly on the most visible solution',
                                               'signal': 'speed'},
                                              {'effect': 'Slower up front; improves the quality of the causal decision.',
                                               'id': 'evidence',
                                               'label': 'Collect targeted evidence before committing',
                                               'signal': 'evidence'},
                                              {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                               'id': 'redesign',
                                               'label': 'Redesign the process around the customer requirement',
                                               'signal': 'design'}],
                         'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                         'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                            'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can '
                                                     'be defended responsibly.',
                                            'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                            'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                      'consequences for people.',
                                            'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                         'agendas.',
                                            'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal '
                                                      'work practices.'},
                         'socratic_prompts': ['What do you know versus what are you assuming?',
                                              'Whose definition of the problem are you using?',
                                              'What evidence would change your mind?',
                                              'Who benefits or loses if this recommendation is adopted?',
                                              'What would make a technically correct solution fail organizationally?'],
                         'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                'constraint than the other stakeholders.',
                                                                                'The stakeholder has an incentive that can influence which '
                                                                                'facts are emphasized.'],
                                                                      'incentive': 'Experiences the outcome and defines value differently '
                                                                                   'from internal teams.',
                                                                      'opening': 'Experiences the outcome and defines value differently '
                                                                                 'from internal teams. In outpatient pharmacy wait time, '
                                                                                 'this stakeholder sees a different part of the operating '
                                                                                 'problem.',
                                                                      'role': 'Customer / user'},
                                          'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                          'than the other stakeholders.',
                                                                          'The stakeholder has an incentive that can influence which facts '
                                                                          'are emphasized.'],
                                                                'incentive': 'Wants a visible result and has a commitment to defend.',
                                                                'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                           'outpatient pharmacy wait time, this stakeholder sees a '
                                                                           'different part of the operating problem.',
                                                                'role': 'Executive sponsor'},
                                          'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                        'than the other stakeholders.',
                                                                        'The stakeholder has an incentive that can influence which facts '
                                                                        'are emphasized.'],
                                                              'incentive': 'Tests whether improvement becomes a credible economic benefit.',
                                                              'opening': 'Tests whether improvement becomes a credible economic benefit. '
                                                                         'In outpatient pharmacy wait time, this stakeholder sees a '
                                                                         'different part of the operating problem.',
                                                              'role': 'Finance'},
                                          'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                 'constraint than the other stakeholders.',
                                                                                 'The stakeholder has an incentive that can influence '
                                                                                 'which facts are emphasized.'],
                                                                       'incentive': 'Sees workarounds, exceptions, friction, and practical '
                                                                                    'constraints.',
                                                                       'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                                  'constraints. In outpatient pharmacy wait time, this '
                                                                                  'stakeholder sees a different part of the operating '
                                                                                  'problem.',
                                                                       'role': 'Frontline employee'},
                                          'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                      'the other stakeholders.',
                                                                      'The stakeholder has an incentive that can influence which facts are '
                                                                      'emphasized.'],
                                                            'incentive': 'Owns service performance and operational continuity.',
                                                            'opening': 'Owns service performance and operational continuity. In outpatient '
                                                                       'pharmacy wait time, this stakeholder sees a different part of the '
                                                                       'operating problem.',
                                                            'role': 'Process owner'},
                                          'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                        'than the other stakeholders.',
                                                                        'The stakeholder has an incentive that can influence which facts '
                                                                        'are emphasized.'],
                                                              'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                           'requirements.',
                                                              'opening': 'Protects policy, regulatory, control, and reputational '
                                                                         'requirements. In outpatient pharmacy wait time, this stakeholder '
                                                                         'sees a different part of the operating problem.',
                                                              'role': 'Risk / compliance'}}},
 'g-insurance-claims': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                              'id': 'problem',
                                              'prompt': 'What is the problem in measurable terms, and for whom?',
                                              'requires': ['baseline', 'customer', 'problem']},
                                             {'feedback': 'Turn plausible stories into testable hypotheses.',
                                              'id': 'evidence',
                                              'prompt': 'Which evidence would distinguish competing explanations?',
                                              'requires': ['evidence', 'data', 'variation']},
                                             {'feedback': 'Treat organizational incentives as part of the operating system.',
                                              'id': 'people',
                                              'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                              'requires': ['incentive', 'political', 'social']}],
                        'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                              'id': 'fast',
                                              'label': 'Move quickly on the most visible solution',
                                              'signal': 'speed'},
                                             {'effect': 'Slower up front; improves the quality of the causal decision.',
                                              'id': 'evidence',
                                              'label': 'Collect targeted evidence before committing',
                                              'signal': 'evidence'},
                                             {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                              'id': 'redesign',
                                              'label': 'Redesign the process around the customer requirement',
                                              'signal': 'design'}],
                        'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                        'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                           'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can '
                                                    'be defended responsibly.',
                                           'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                           'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                     'consequences for people.',
                                           'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                        'agendas.',
                                           'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal '
                                                     'work practices.'},
                        'socratic_prompts': ['What do you know versus what are you assuming?',
                                             'Whose definition of the problem are you using?',
                                             'What evidence would change your mind?',
                                             'Who benefits or loses if this recommendation is adopted?',
                                             'What would make a technically correct solution fail organizationally?'],
                        'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                               'constraint than the other stakeholders.',
                                                                               'The stakeholder has an incentive that can influence which '
                                                                               'facts are emphasized.'],
                                                                     'incentive': 'Experiences the outcome and defines value differently '
                                                                                  'from internal teams.',
                                                                     'opening': 'Experiences the outcome and defines value differently '
                                                                                'from internal teams. In claims rework, this stakeholder '
                                                                                'sees a different part of the operating problem.',
                                                                     'role': 'Customer / user'},
                                         'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                         'than the other stakeholders.',
                                                                         'The stakeholder has an incentive that can influence which facts '
                                                                         'are emphasized.'],
                                                               'incentive': 'Wants a visible result and has a commitment to defend.',
                                                               'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                          'claims rework, this stakeholder sees a different part of the '
                                                                          'operating problem.',
                                                               'role': 'Executive sponsor'},
                                         'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                       'the other stakeholders.',
                                                                       'The stakeholder has an incentive that can influence which facts '
                                                                       'are emphasized.'],
                                                             'incentive': 'Tests whether improvement becomes a credible economic benefit.',
                                                             'opening': 'Tests whether improvement becomes a credible economic benefit. In '
                                                                        'claims rework, this stakeholder sees a different part of the '
                                                                        'operating problem.',
                                                             'role': 'Finance'},
                                         'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                'constraint than the other stakeholders.',
                                                                                'The stakeholder has an incentive that can influence which '
                                                                                'facts are emphasized.'],
                                                                      'incentive': 'Sees workarounds, exceptions, friction, and practical '
                                                                                   'constraints.',
                                                                      'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                                 'constraints. In claims rework, this stakeholder sees a '
                                                                                 'different part of the operating problem.',
                                                                      'role': 'Frontline employee'},
                                         'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                     'the other stakeholders.',
                                                                     'The stakeholder has an incentive that can influence which facts are '
                                                                     'emphasized.'],
                                                           'incentive': 'Owns service performance and operational continuity.',
                                                           'opening': 'Owns service performance and operational continuity. In claims '
                                                                      'rework, this stakeholder sees a different part of the operating '
                                                                      'problem.',
                                                           'role': 'Process owner'},
                                         'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                       'the other stakeholders.',
                                                                       'The stakeholder has an incentive that can influence which facts '
                                                                       'are emphasized.'],
                                                             'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                          'requirements.',
                                                             'opening': 'Protects policy, regulatory, control, and reputational '
                                                                        'requirements. In claims rework, this stakeholder sees a different '
                                                                        'part of the operating problem.',
                                                             'role': 'Risk / compliance'}}},
 'g-loan-underwriting': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                               'id': 'problem',
                                               'prompt': 'What is the problem in measurable terms, and for whom?',
                                               'requires': ['baseline', 'customer', 'problem']},
                                              {'feedback': 'Turn plausible stories into testable hypotheses.',
                                               'id': 'evidence',
                                               'prompt': 'Which evidence would distinguish competing explanations?',
                                               'requires': ['evidence', 'data', 'variation']},
                                              {'feedback': 'Treat organizational incentives as part of the operating system.',
                                               'id': 'people',
                                               'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                               'requires': ['incentive', 'political', 'social']}],
                         'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                               'id': 'fast',
                                               'label': 'Move quickly on the most visible solution',
                                               'signal': 'speed'},
                                              {'effect': 'Slower up front; improves the quality of the causal decision.',
                                               'id': 'evidence',
                                               'label': 'Collect targeted evidence before committing',
                                               'signal': 'evidence'},
                                              {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                               'id': 'redesign',
                                               'label': 'Redesign the process around the customer requirement',
                                               'signal': 'design'}],
                         'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                         'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                            'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can '
                                                     'be defended responsibly.',
                                            'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                            'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                      'consequences for people.',
                                            'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                         'agendas.',
                                            'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal '
                                                      'work practices.'},
                         'socratic_prompts': ['What do you know versus what are you assuming?',
                                              'Whose definition of the problem are you using?',
                                              'What evidence would change your mind?',
                                              'Who benefits or loses if this recommendation is adopted?',
                                              'What would make a technically correct solution fail organizationally?'],
                         'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                'constraint than the other stakeholders.',
                                                                                'The stakeholder has an incentive that can influence which '
                                                                                'facts are emphasized.'],
                                                                      'incentive': 'Experiences the outcome and defines value differently '
                                                                                   'from internal teams.',
                                                                      'opening': 'Experiences the outcome and defines value differently '
                                                                                 'from internal teams. In mortgage underwriting cycle '
                                                                                 'time, this stakeholder sees a different part of the '
                                                                                 'operating problem.',
                                                                      'role': 'Customer / user'},
                                          'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                          'than the other stakeholders.',
                                                                          'The stakeholder has an incentive that can influence which facts '
                                                                          'are emphasized.'],
                                                                'incentive': 'Wants a visible result and has a commitment to defend.',
                                                                'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                           'mortgage underwriting cycle time, this stakeholder sees a '
                                                                           'different part of the operating problem.',
                                                                'role': 'Executive sponsor'},
                                          'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                        'than the other stakeholders.',
                                                                        'The stakeholder has an incentive that can influence which facts '
                                                                        'are emphasized.'],
                                                              'incentive': 'Tests whether improvement becomes a credible economic benefit.',
                                                              'opening': 'Tests whether improvement becomes a credible economic benefit. '
                                                                         'In mortgage underwriting cycle time, this stakeholder sees a '
                                                                         'different part of the operating problem.',
                                                              'role': 'Finance'},
                                          'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                 'constraint than the other stakeholders.',
                                                                                 'The stakeholder has an incentive that can influence '
                                                                                 'which facts are emphasized.'],
                                                                       'incentive': 'Sees workarounds, exceptions, friction, and practical '
                                                                                    'constraints.',
                                                                       'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                                  'constraints. In mortgage underwriting cycle time, this '
                                                                                  'stakeholder sees a different part of the operating '
                                                                                  'problem.',
                                                                       'role': 'Frontline employee'},
                                          'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                      'the other stakeholders.',
                                                                      'The stakeholder has an incentive that can influence which facts are '
                                                                      'emphasized.'],
                                                            'incentive': 'Owns service performance and operational continuity.',
                                                            'opening': 'Owns service performance and operational continuity. In mortgage '
                                                                       'underwriting cycle time, this stakeholder sees a different part of '
                                                                       'the operating problem.',
                                                            'role': 'Process owner'},
                                          'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                        'than the other stakeholders.',
                                                                        'The stakeholder has an incentive that can influence which facts '
                                                                        'are emphasized.'],
                                                              'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                           'requirements.',
                                                              'opening': 'Protects policy, regulatory, control, and reputational '
                                                                         'requirements. In mortgage underwriting cycle time, this '
                                                                         'stakeholder sees a different part of the operating problem.',
                                                              'role': 'Risk / compliance'}}},
 'w-appointment-scheduling': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                                    'id': 'problem',
                                                    'prompt': 'What is the problem in measurable terms, and for whom?',
                                                    'requires': ['baseline', 'customer', 'problem']},
                                                   {'feedback': 'Turn plausible stories into testable hypotheses.',
                                                    'id': 'evidence',
                                                    'prompt': 'Which evidence would distinguish competing explanations?',
                                                    'requires': ['evidence', 'data', 'variation']},
                                                   {'feedback': 'Treat organizational incentives as part of the operating system.',
                                                    'id': 'people',
                                                    'prompt': 'Which stakeholder incentives could distort the information you are '
                                                              'receiving?',
                                                    'requires': ['incentive', 'political', 'social']}],
                              'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                                    'id': 'fast',
                                                    'label': 'Move quickly on the most visible solution',
                                                    'signal': 'speed'},
                                                   {'effect': 'Slower up front; improves the quality of the causal decision.',
                                                    'id': 'evidence',
                                                    'label': 'Collect targeted evidence before committing',
                                                    'signal': 'evidence'},
                                                   {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                                    'id': 'redesign',
                                                    'label': 'Redesign the process around the customer requirement',
                                                    'signal': 'design'}],
                              'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                              'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity '
                                                             'cost.',
                                                 'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what '
                                                          'can be defended responsibly.',
                                                 'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                                 'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                           'consequences for people.',
                                                 'political': 'Consider power, incentives, commitments, reputation, ownership, and '
                                                              'competing agendas.',
                                                 'social': 'Consider team norms, status, trust, psychological safety, adoption, and '
                                                           'informal work practices.'},
                              'socratic_prompts': ['What do you know versus what are you assuming?',
                                                   'Whose definition of the problem are you using?',
                                                   'What evidence would change your mind?',
                                                   'Who benefits or loses if this recommendation is adopted?',
                                                   'What would make a technically correct solution fail organizationally?'],
                              'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                     'constraint than the other stakeholders.',
                                                                                     'The stakeholder has an incentive that can influence '
                                                                                     'which facts are emphasized.'],
                                                                           'incentive': 'Experiences the outcome and defines value '
                                                                                        'differently from internal teams.',
                                                                           'opening': 'Experiences the outcome and defines value '
                                                                                      'differently from internal teams. In appointment '
                                                                                      'scheduling friction, this stakeholder sees a '
                                                                                      'different part of the operating problem.',
                                                                           'role': 'Customer / user'},
                                               'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or '
                                                                               'constraint than the other stakeholders.',
                                                                               'The stakeholder has an incentive that can influence which '
                                                                               'facts are emphasized.'],
                                                                     'incentive': 'Wants a visible result and has a commitment to defend.',
                                                                     'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                                'appointment scheduling friction, this stakeholder sees a '
                                                                                'different part of the operating problem.',
                                                                     'role': 'Executive sponsor'},
                                               'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or '
                                                                             'constraint than the other stakeholders.',
                                                                             'The stakeholder has an incentive that can influence which '
                                                                             'facts are emphasized.'],
                                                                   'incentive': 'Tests whether improvement becomes a credible economic '
                                                                                'benefit.',
                                                                   'opening': 'Tests whether improvement becomes a credible economic '
                                                                              'benefit. In appointment scheduling friction, this '
                                                                              'stakeholder sees a different part of the operating problem.',
                                                                   'role': 'Finance'},
                                               'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                      'constraint than the other stakeholders.',
                                                                                      'The stakeholder has an incentive that can influence '
                                                                                      'which facts are emphasized.'],
                                                                            'incentive': 'Sees workarounds, exceptions, friction, and '
                                                                                         'practical constraints.',
                                                                            'opening': 'Sees workarounds, exceptions, friction, and '
                                                                                       'practical constraints. In appointment scheduling '
                                                                                       'friction, this stakeholder sees a different part '
                                                                                       'of the operating problem.',
                                                                            'role': 'Frontline employee'},
                                               'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                           'than the other stakeholders.',
                                                                           'The stakeholder has an incentive that can influence which '
                                                                           'facts are emphasized.'],
                                                                 'incentive': 'Owns service performance and operational continuity.',
                                                                 'opening': 'Owns service performance and operational continuity. In '
                                                                            'appointment scheduling friction, this stakeholder sees a '
                                                                            'different part of the operating problem.',
                                                                 'role': 'Process owner'},
                                               'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or '
                                                                             'constraint than the other stakeholders.',
                                                                             'The stakeholder has an incentive that can influence which '
                                                                             'facts are emphasized.'],
                                                                   'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                                'requirements.',
                                                                   'opening': 'Protects policy, regulatory, control, and reputational '
                                                                              'requirements. In appointment scheduling friction, this '
                                                                              'stakeholder sees a different part of the operating problem.',
                                                                   'role': 'Risk / compliance'}}},
 'w-customer-email': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                            'id': 'problem',
                                            'prompt': 'What is the problem in measurable terms, and for whom?',
                                            'requires': ['baseline', 'customer', 'problem']},
                                           {'feedback': 'Turn plausible stories into testable hypotheses.',
                                            'id': 'evidence',
                                            'prompt': 'Which evidence would distinguish competing explanations?',
                                            'requires': ['evidence', 'data', 'variation']},
                                           {'feedback': 'Treat organizational incentives as part of the operating system.',
                                            'id': 'people',
                                            'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                            'requires': ['incentive', 'political', 'social']}],
                      'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                            'id': 'fast',
                                            'label': 'Move quickly on the most visible solution',
                                            'signal': 'speed'},
                                           {'effect': 'Slower up front; improves the quality of the causal decision.',
                                            'id': 'evidence',
                                            'label': 'Collect targeted evidence before committing',
                                            'signal': 'evidence'},
                                           {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                            'id': 'redesign',
                                            'label': 'Redesign the process around the customer requirement',
                                            'signal': 'design'}],
                      'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                      'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                         'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can be '
                                                  'defended responsibly.',
                                         'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                         'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                   'consequences for people.',
                                         'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                      'agendas.',
                                         'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal work '
                                                   'practices.'},
                      'socratic_prompts': ['What do you know versus what are you assuming?',
                                           'Whose definition of the problem are you using?',
                                           'What evidence would change your mind?',
                                           'Who benefits or loses if this recommendation is adopted?',
                                           'What would make a technically correct solution fail organizationally?'],
                      'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                             'constraint than the other stakeholders.',
                                                                             'The stakeholder has an incentive that can influence which '
                                                                             'facts are emphasized.'],
                                                                   'incentive': 'Experiences the outcome and defines value differently '
                                                                                'from internal teams.',
                                                                   'opening': 'Experiences the outcome and defines value differently from '
                                                                              'internal teams. In customer email triage, this stakeholder '
                                                                              'sees a different part of the operating problem.',
                                                                   'role': 'Customer / user'},
                                       'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                       'the other stakeholders.',
                                                                       'The stakeholder has an incentive that can influence which facts '
                                                                       'are emphasized.'],
                                                             'incentive': 'Wants a visible result and has a commitment to defend.',
                                                             'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                        'customer email triage, this stakeholder sees a different part of '
                                                                        'the operating problem.',
                                                             'role': 'Executive sponsor'},
                                       'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                     'the other stakeholders.',
                                                                     'The stakeholder has an incentive that can influence which facts are '
                                                                     'emphasized.'],
                                                           'incentive': 'Tests whether improvement becomes a credible economic benefit.',
                                                           'opening': 'Tests whether improvement becomes a credible economic benefit. In '
                                                                      'customer email triage, this stakeholder sees a different part of '
                                                                      'the operating problem.',
                                                           'role': 'Finance'},
                                       'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                              'constraint than the other stakeholders.',
                                                                              'The stakeholder has an incentive that can influence which '
                                                                              'facts are emphasized.'],
                                                                    'incentive': 'Sees workarounds, exceptions, friction, and practical '
                                                                                 'constraints.',
                                                                    'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                               'constraints. In customer email triage, this stakeholder '
                                                                               'sees a different part of the operating problem.',
                                                                    'role': 'Frontline employee'},
                                       'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than the '
                                                                   'other stakeholders.',
                                                                   'The stakeholder has an incentive that can influence which facts are '
                                                                   'emphasized.'],
                                                         'incentive': 'Owns service performance and operational continuity.',
                                                         'opening': 'Owns service performance and operational continuity. In customer '
                                                                    'email triage, this stakeholder sees a different part of the operating '
                                                                    'problem.',
                                                         'role': 'Process owner'},
                                       'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                     'the other stakeholders.',
                                                                     'The stakeholder has an incentive that can influence which facts are '
                                                                     'emphasized.'],
                                                           'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                        'requirements.',
                                                           'opening': 'Protects policy, regulatory, control, and reputational '
                                                                      'requirements. In customer email triage, this stakeholder sees a '
                                                                      'different part of the operating problem.',
                                                           'role': 'Risk / compliance'}}},
 'w-invoice-correction': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                                'id': 'problem',
                                                'prompt': 'What is the problem in measurable terms, and for whom?',
                                                'requires': ['baseline', 'customer', 'problem']},
                                               {'feedback': 'Turn plausible stories into testable hypotheses.',
                                                'id': 'evidence',
                                                'prompt': 'Which evidence would distinguish competing explanations?',
                                                'requires': ['evidence', 'data', 'variation']},
                                               {'feedback': 'Treat organizational incentives as part of the operating system.',
                                                'id': 'people',
                                                'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                                'requires': ['incentive', 'political', 'social']}],
                          'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                                'id': 'fast',
                                                'label': 'Move quickly on the most visible solution',
                                                'signal': 'speed'},
                                               {'effect': 'Slower up front; improves the quality of the causal decision.',
                                                'id': 'evidence',
                                                'label': 'Collect targeted evidence before committing',
                                                'signal': 'evidence'},
                                               {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                                'id': 'redesign',
                                                'label': 'Redesign the process around the customer requirement',
                                                'signal': 'design'}],
                          'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                          'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                             'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can '
                                                      'be defended responsibly.',
                                             'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                             'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                       'consequences for people.',
                                             'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                          'agendas.',
                                             'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal '
                                                       'work practices.'},
                          'socratic_prompts': ['What do you know versus what are you assuming?',
                                               'Whose definition of the problem are you using?',
                                               'What evidence would change your mind?',
                                               'Who benefits or loses if this recommendation is adopted?',
                                               'What would make a technically correct solution fail organizationally?'],
                          'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                 'constraint than the other stakeholders.',
                                                                                 'The stakeholder has an incentive that can influence '
                                                                                 'which facts are emphasized.'],
                                                                       'incentive': 'Experiences the outcome and defines value differently '
                                                                                    'from internal teams.',
                                                                       'opening': 'Experiences the outcome and defines value differently '
                                                                                  'from internal teams. In invoice correction queue, this '
                                                                                  'stakeholder sees a different part of the operating '
                                                                                  'problem.',
                                                                       'role': 'Customer / user'},
                                           'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                           'than the other stakeholders.',
                                                                           'The stakeholder has an incentive that can influence which '
                                                                           'facts are emphasized.'],
                                                                 'incentive': 'Wants a visible result and has a commitment to defend.',
                                                                 'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                            'invoice correction queue, this stakeholder sees a different '
                                                                            'part of the operating problem.',
                                                                 'role': 'Executive sponsor'},
                                           'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                         'than the other stakeholders.',
                                                                         'The stakeholder has an incentive that can influence which facts '
                                                                         'are emphasized.'],
                                                               'incentive': 'Tests whether improvement becomes a credible economic '
                                                                            'benefit.',
                                                               'opening': 'Tests whether improvement becomes a credible economic benefit. '
                                                                          'In invoice correction queue, this stakeholder sees a different '
                                                                          'part of the operating problem.',
                                                               'role': 'Finance'},
                                           'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                  'constraint than the other stakeholders.',
                                                                                  'The stakeholder has an incentive that can influence '
                                                                                  'which facts are emphasized.'],
                                                                        'incentive': 'Sees workarounds, exceptions, friction, and '
                                                                                     'practical constraints.',
                                                                        'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                                   'constraints. In invoice correction queue, this '
                                                                                   'stakeholder sees a different part of the operating '
                                                                                   'problem.',
                                                                        'role': 'Frontline employee'},
                                           'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                       'the other stakeholders.',
                                                                       'The stakeholder has an incentive that can influence which facts '
                                                                       'are emphasized.'],
                                                             'incentive': 'Owns service performance and operational continuity.',
                                                             'opening': 'Owns service performance and operational continuity. In invoice '
                                                                        'correction queue, this stakeholder sees a different part of the '
                                                                        'operating problem.',
                                                             'role': 'Process owner'},
                                           'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                         'than the other stakeholders.',
                                                                         'The stakeholder has an incentive that can influence which facts '
                                                                         'are emphasized.'],
                                                               'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                            'requirements.',
                                                               'opening': 'Protects policy, regulatory, control, and reputational '
                                                                          'requirements. In invoice correction queue, this stakeholder '
                                                                          'sees a different part of the operating problem.',
                                                               'role': 'Risk / compliance'}}},
 'w-password-reset': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                            'id': 'problem',
                                            'prompt': 'What is the problem in measurable terms, and for whom?',
                                            'requires': ['baseline', 'customer', 'problem']},
                                           {'feedback': 'Turn plausible stories into testable hypotheses.',
                                            'id': 'evidence',
                                            'prompt': 'Which evidence would distinguish competing explanations?',
                                            'requires': ['evidence', 'data', 'variation']},
                                           {'feedback': 'Treat organizational incentives as part of the operating system.',
                                            'id': 'people',
                                            'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                            'requires': ['incentive', 'political', 'social']}],
                      'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                            'id': 'fast',
                                            'label': 'Move quickly on the most visible solution',
                                            'signal': 'speed'},
                                           {'effect': 'Slower up front; improves the quality of the causal decision.',
                                            'id': 'evidence',
                                            'label': 'Collect targeted evidence before committing',
                                            'signal': 'evidence'},
                                           {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                            'id': 'redesign',
                                            'label': 'Redesign the process around the customer requirement',
                                            'signal': 'design'}],
                      'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                      'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                         'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can be '
                                                  'defended responsibly.',
                                         'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                         'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                   'consequences for people.',
                                         'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                      'agendas.',
                                         'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal work '
                                                   'practices.'},
                      'socratic_prompts': ['What do you know versus what are you assuming?',
                                           'Whose definition of the problem are you using?',
                                           'What evidence would change your mind?',
                                           'Who benefits or loses if this recommendation is adopted?',
                                           'What would make a technically correct solution fail organizationally?'],
                      'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                             'constraint than the other stakeholders.',
                                                                             'The stakeholder has an incentive that can influence which '
                                                                             'facts are emphasized.'],
                                                                   'incentive': 'Experiences the outcome and defines value differently '
                                                                                'from internal teams.',
                                                                   'opening': 'Experiences the outcome and defines value differently from '
                                                                              'internal teams. In employee access requests, this '
                                                                              'stakeholder sees a different part of the operating problem.',
                                                                   'role': 'Customer / user'},
                                       'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                       'the other stakeholders.',
                                                                       'The stakeholder has an incentive that can influence which facts '
                                                                       'are emphasized.'],
                                                             'incentive': 'Wants a visible result and has a commitment to defend.',
                                                             'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                        'employee access requests, this stakeholder sees a different part '
                                                                        'of the operating problem.',
                                                             'role': 'Executive sponsor'},
                                       'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                     'the other stakeholders.',
                                                                     'The stakeholder has an incentive that can influence which facts are '
                                                                     'emphasized.'],
                                                           'incentive': 'Tests whether improvement becomes a credible economic benefit.',
                                                           'opening': 'Tests whether improvement becomes a credible economic benefit. In '
                                                                      'employee access requests, this stakeholder sees a different part of '
                                                                      'the operating problem.',
                                                           'role': 'Finance'},
                                       'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                              'constraint than the other stakeholders.',
                                                                              'The stakeholder has an incentive that can influence which '
                                                                              'facts are emphasized.'],
                                                                    'incentive': 'Sees workarounds, exceptions, friction, and practical '
                                                                                 'constraints.',
                                                                    'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                               'constraints. In employee access requests, this stakeholder '
                                                                               'sees a different part of the operating problem.',
                                                                    'role': 'Frontline employee'},
                                       'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than the '
                                                                   'other stakeholders.',
                                                                   'The stakeholder has an incentive that can influence which facts are '
                                                                   'emphasized.'],
                                                         'incentive': 'Owns service performance and operational continuity.',
                                                         'opening': 'Owns service performance and operational continuity. In employee '
                                                                    'access requests, this stakeholder sees a different part of the '
                                                                    'operating problem.',
                                                         'role': 'Process owner'},
                                       'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                     'the other stakeholders.',
                                                                     'The stakeholder has an incentive that can influence which facts are '
                                                                     'emphasized.'],
                                                           'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                        'requirements.',
                                                           'opening': 'Protects policy, regulatory, control, and reputational '
                                                                      'requirements. In employee access requests, this stakeholder sees a '
                                                                      'different part of the operating problem.',
                                                           'role': 'Risk / compliance'}}},
 'w-process-map': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                         'id': 'problem',
                                         'prompt': 'What is the problem in measurable terms, and for whom?',
                                         'requires': ['baseline', 'customer', 'problem']},
                                        {'feedback': 'Turn plausible stories into testable hypotheses.',
                                         'id': 'evidence',
                                         'prompt': 'Which evidence would distinguish competing explanations?',
                                         'requires': ['evidence', 'data', 'variation']},
                                        {'feedback': 'Treat organizational incentives as part of the operating system.',
                                         'id': 'people',
                                         'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                         'requires': ['incentive', 'political', 'social']}],
                   'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                         'id': 'fast',
                                         'label': 'Move quickly on the most visible solution',
                                         'signal': 'speed'},
                                        {'effect': 'Slower up front; improves the quality of the causal decision.',
                                         'id': 'evidence',
                                         'label': 'Collect targeted evidence before committing',
                                         'signal': 'evidence'},
                                        {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                         'id': 'redesign',
                                         'label': 'Redesign the process around the customer requirement',
                                         'signal': 'design'}],
                   'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                   'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                      'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can be '
                                               'defended responsibly.',
                                      'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                      'pathos': 'Consider customer and employee experience, trust, frustration, workload, and consequences '
                                                'for people.',
                                      'political': 'Consider power, incentives, commitments, reputation, ownership, and competing agendas.',
                                      'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal work '
                                                'practices.'},
                   'socratic_prompts': ['What do you know versus what are you assuming?',
                                        'Whose definition of the problem are you using?',
                                        'What evidence would change your mind?',
                                        'Who benefits or loses if this recommendation is adopted?',
                                        'What would make a technically correct solution fail organizationally?'],
                   'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                          'than the other stakeholders.',
                                                                          'The stakeholder has an incentive that can influence which facts '
                                                                          'are emphasized.'],
                                                                'incentive': 'Experiences the outcome and defines value differently from '
                                                                             'internal teams.',
                                                                'opening': 'Experiences the outcome and defines value differently from '
                                                                           'internal teams. In retail returns handoff, this stakeholder '
                                                                           'sees a different part of the operating problem.',
                                                                'role': 'Customer / user'},
                                    'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                    'the other stakeholders.',
                                                                    'The stakeholder has an incentive that can influence which facts are '
                                                                    'emphasized.'],
                                                          'incentive': 'Wants a visible result and has a commitment to defend.',
                                                          'opening': 'Wants a visible result and has a commitment to defend. In retail '
                                                                     'returns handoff, this stakeholder sees a different part of the '
                                                                     'operating problem.',
                                                          'role': 'Executive sponsor'},
                                    'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint than the '
                                                                  'other stakeholders.',
                                                                  'The stakeholder has an incentive that can influence which facts are '
                                                                  'emphasized.'],
                                                        'incentive': 'Tests whether improvement becomes a credible economic benefit.',
                                                        'opening': 'Tests whether improvement becomes a credible economic benefit. In '
                                                                   'retail returns handoff, this stakeholder sees a different part of the '
                                                                   'operating problem.',
                                                        'role': 'Finance'},
                                    'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                           'than the other stakeholders.',
                                                                           'The stakeholder has an incentive that can influence which '
                                                                           'facts are emphasized.'],
                                                                 'incentive': 'Sees workarounds, exceptions, friction, and practical '
                                                                              'constraints.',
                                                                 'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                            'constraints. In retail returns handoff, this stakeholder sees '
                                                                            'a different part of the operating problem.',
                                                                 'role': 'Frontline employee'},
                                    'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than the '
                                                                'other stakeholders.',
                                                                'The stakeholder has an incentive that can influence which facts are '
                                                                'emphasized.'],
                                                      'incentive': 'Owns service performance and operational continuity.',
                                                      'opening': 'Owns service performance and operational continuity. In retail returns '
                                                                 'handoff, this stakeholder sees a different part of the operating '
                                                                 'problem.',
                                                      'role': 'Process owner'},
                                    'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint than the '
                                                                  'other stakeholders.',
                                                                  'The stakeholder has an incentive that can influence which facts are '
                                                                  'emphasized.'],
                                                        'incentive': 'Protects policy, regulatory, control, and reputational requirements.',
                                                        'opening': 'Protects policy, regulatory, control, and reputational requirements. '
                                                                   'In retail returns handoff, this stakeholder sees a different part of '
                                                                   'the operating problem.',
                                                        'role': 'Risk / compliance'}}},
 'y-contact-centre': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                            'id': 'problem',
                                            'prompt': 'What is the problem in measurable terms, and for whom?',
                                            'requires': ['baseline', 'customer', 'problem']},
                                           {'feedback': 'Turn plausible stories into testable hypotheses.',
                                            'id': 'evidence',
                                            'prompt': 'Which evidence would distinguish competing explanations?',
                                            'requires': ['evidence', 'data', 'variation']},
                                           {'feedback': 'Treat organizational incentives as part of the operating system.',
                                            'id': 'people',
                                            'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                            'requires': ['incentive', 'political', 'social']}],
                      'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                            'id': 'fast',
                                            'label': 'Move quickly on the most visible solution',
                                            'signal': 'speed'},
                                           {'effect': 'Slower up front; improves the quality of the causal decision.',
                                            'id': 'evidence',
                                            'label': 'Collect targeted evidence before committing',
                                            'signal': 'evidence'},
                                           {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                            'id': 'redesign',
                                            'label': 'Redesign the process around the customer requirement',
                                            'signal': 'design'}],
                      'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                      'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                         'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can be '
                                                  'defended responsibly.',
                                         'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                         'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                   'consequences for people.',
                                         'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                      'agendas.',
                                         'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal work '
                                                   'practices.'},
                      'socratic_prompts': ['What do you know versus what are you assuming?',
                                           'Whose definition of the problem are you using?',
                                           'What evidence would change your mind?',
                                           'Who benefits or loses if this recommendation is adopted?',
                                           'What would make a technically correct solution fail organizationally?'],
                      'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                             'constraint than the other stakeholders.',
                                                                             'The stakeholder has an incentive that can influence which '
                                                                             'facts are emphasized.'],
                                                                   'incentive': 'Experiences the outcome and defines value differently '
                                                                                'from internal teams.',
                                                                   'opening': 'Experiences the outcome and defines value differently from '
                                                                              'internal teams. In contact centre after-call work, this '
                                                                              'stakeholder sees a different part of the operating problem.',
                                                                   'role': 'Customer / user'},
                                       'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                       'the other stakeholders.',
                                                                       'The stakeholder has an incentive that can influence which facts '
                                                                       'are emphasized.'],
                                                             'incentive': 'Wants a visible result and has a commitment to defend.',
                                                             'opening': 'Wants a visible result and has a commitment to defend. In contact '
                                                                        'centre after-call work, this stakeholder sees a different part of '
                                                                        'the operating problem.',
                                                             'role': 'Executive sponsor'},
                                       'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                     'the other stakeholders.',
                                                                     'The stakeholder has an incentive that can influence which facts are '
                                                                     'emphasized.'],
                                                           'incentive': 'Tests whether improvement becomes a credible economic benefit.',
                                                           'opening': 'Tests whether improvement becomes a credible economic benefit. In '
                                                                      'contact centre after-call work, this stakeholder sees a different '
                                                                      'part of the operating problem.',
                                                           'role': 'Finance'},
                                       'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                              'constraint than the other stakeholders.',
                                                                              'The stakeholder has an incentive that can influence which '
                                                                              'facts are emphasized.'],
                                                                    'incentive': 'Sees workarounds, exceptions, friction, and practical '
                                                                                 'constraints.',
                                                                    'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                               'constraints. In contact centre after-call work, this '
                                                                               'stakeholder sees a different part of the operating '
                                                                               'problem.',
                                                                    'role': 'Frontline employee'},
                                       'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than the '
                                                                   'other stakeholders.',
                                                                   'The stakeholder has an incentive that can influence which facts are '
                                                                   'emphasized.'],
                                                         'incentive': 'Owns service performance and operational continuity.',
                                                         'opening': 'Owns service performance and operational continuity. In contact '
                                                                    'centre after-call work, this stakeholder sees a different part of the '
                                                                    'operating problem.',
                                                         'role': 'Process owner'},
                                       'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                     'the other stakeholders.',
                                                                     'The stakeholder has an incentive that can influence which facts are '
                                                                     'emphasized.'],
                                                           'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                        'requirements.',
                                                           'opening': 'Protects policy, regulatory, control, and reputational '
                                                                      'requirements. In contact centre after-call work, this stakeholder '
                                                                      'sees a different part of the operating problem.',
                                                           'role': 'Risk / compliance'}}},
 'y-maintenance-request': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                                 'id': 'problem',
                                                 'prompt': 'What is the problem in measurable terms, and for whom?',
                                                 'requires': ['baseline', 'customer', 'problem']},
                                                {'feedback': 'Turn plausible stories into testable hypotheses.',
                                                 'id': 'evidence',
                                                 'prompt': 'Which evidence would distinguish competing explanations?',
                                                 'requires': ['evidence', 'data', 'variation']},
                                                {'feedback': 'Treat organizational incentives as part of the operating system.',
                                                 'id': 'people',
                                                 'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                                 'requires': ['incentive', 'political', 'social']}],
                           'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                                 'id': 'fast',
                                                 'label': 'Move quickly on the most visible solution',
                                                 'signal': 'speed'},
                                                {'effect': 'Slower up front; improves the quality of the causal decision.',
                                                 'id': 'evidence',
                                                 'label': 'Collect targeted evidence before committing',
                                                 'signal': 'evidence'},
                                                {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                                 'id': 'redesign',
                                                 'label': 'Redesign the process around the customer requirement',
                                                 'signal': 'design'}],
                           'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                           'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                              'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what '
                                                       'can be defended responsibly.',
                                              'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                              'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                        'consequences for people.',
                                              'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                           'agendas.',
                                              'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal '
                                                        'work practices.'},
                           'socratic_prompts': ['What do you know versus what are you assuming?',
                                                'Whose definition of the problem are you using?',
                                                'What evidence would change your mind?',
                                                'Who benefits or loses if this recommendation is adopted?',
                                                'What would make a technically correct solution fail organizationally?'],
                           'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                  'constraint than the other stakeholders.',
                                                                                  'The stakeholder has an incentive that can influence '
                                                                                  'which facts are emphasized.'],
                                                                        'incentive': 'Experiences the outcome and defines value '
                                                                                     'differently from internal teams.',
                                                                        'opening': 'Experiences the outcome and defines value differently '
                                                                                   'from internal teams. In maintenance work requests, '
                                                                                   'this stakeholder sees a different part of the '
                                                                                   'operating problem.',
                                                                        'role': 'Customer / user'},
                                            'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                            'than the other stakeholders.',
                                                                            'The stakeholder has an incentive that can influence which '
                                                                            'facts are emphasized.'],
                                                                  'incentive': 'Wants a visible result and has a commitment to defend.',
                                                                  'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                             'maintenance work requests, this stakeholder sees a different '
                                                                             'part of the operating problem.',
                                                                  'role': 'Executive sponsor'},
                                            'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                          'than the other stakeholders.',
                                                                          'The stakeholder has an incentive that can influence which facts '
                                                                          'are emphasized.'],
                                                                'incentive': 'Tests whether improvement becomes a credible economic '
                                                                             'benefit.',
                                                                'opening': 'Tests whether improvement becomes a credible economic benefit. '
                                                                           'In maintenance work requests, this stakeholder sees a '
                                                                           'different part of the operating problem.',
                                                                'role': 'Finance'},
                                            'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                   'constraint than the other stakeholders.',
                                                                                   'The stakeholder has an incentive that can influence '
                                                                                   'which facts are emphasized.'],
                                                                         'incentive': 'Sees workarounds, exceptions, friction, and '
                                                                                      'practical constraints.',
                                                                         'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                                    'constraints. In maintenance work requests, this '
                                                                                    'stakeholder sees a different part of the operating '
                                                                                    'problem.',
                                                                         'role': 'Frontline employee'},
                                            'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                        'than the other stakeholders.',
                                                                        'The stakeholder has an incentive that can influence which facts '
                                                                        'are emphasized.'],
                                                              'incentive': 'Owns service performance and operational continuity.',
                                                              'opening': 'Owns service performance and operational continuity. In '
                                                                         'maintenance work requests, this stakeholder sees a different '
                                                                         'part of the operating problem.',
                                                              'role': 'Process owner'},
                                            'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                          'than the other stakeholders.',
                                                                          'The stakeholder has an incentive that can influence which facts '
                                                                          'are emphasized.'],
                                                                'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                             'requirements.',
                                                                'opening': 'Protects policy, regulatory, control, and reputational '
                                                                           'requirements. In maintenance work requests, this stakeholder '
                                                                           'sees a different part of the operating problem.',
                                                                'role': 'Risk / compliance'}}},
 'y-order-fulfillment': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                               'id': 'problem',
                                               'prompt': 'What is the problem in measurable terms, and for whom?',
                                               'requires': ['baseline', 'customer', 'problem']},
                                              {'feedback': 'Turn plausible stories into testable hypotheses.',
                                               'id': 'evidence',
                                               'prompt': 'Which evidence would distinguish competing explanations?',
                                               'requires': ['evidence', 'data', 'variation']},
                                              {'feedback': 'Treat organizational incentives as part of the operating system.',
                                               'id': 'people',
                                               'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                               'requires': ['incentive', 'political', 'social']}],
                         'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                               'id': 'fast',
                                               'label': 'Move quickly on the most visible solution',
                                               'signal': 'speed'},
                                              {'effect': 'Slower up front; improves the quality of the causal decision.',
                                               'id': 'evidence',
                                               'label': 'Collect targeted evidence before committing',
                                               'signal': 'evidence'},
                                              {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                               'id': 'redesign',
                                               'label': 'Redesign the process around the customer requirement',
                                               'signal': 'design'}],
                         'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                         'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                            'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can '
                                                     'be defended responsibly.',
                                            'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                            'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                      'consequences for people.',
                                            'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                         'agendas.',
                                            'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal '
                                                      'work practices.'},
                         'socratic_prompts': ['What do you know versus what are you assuming?',
                                              'Whose definition of the problem are you using?',
                                              'What evidence would change your mind?',
                                              'Who benefits or loses if this recommendation is adopted?',
                                              'What would make a technically correct solution fail organizationally?'],
                         'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                'constraint than the other stakeholders.',
                                                                                'The stakeholder has an incentive that can influence which '
                                                                                'facts are emphasized.'],
                                                                      'incentive': 'Experiences the outcome and defines value differently '
                                                                                   'from internal teams.',
                                                                      'opening': 'Experiences the outcome and defines value differently '
                                                                                 'from internal teams. In order fulfillment handoffs, this '
                                                                                 'stakeholder sees a different part of the operating '
                                                                                 'problem.',
                                                                      'role': 'Customer / user'},
                                          'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                          'than the other stakeholders.',
                                                                          'The stakeholder has an incentive that can influence which facts '
                                                                          'are emphasized.'],
                                                                'incentive': 'Wants a visible result and has a commitment to defend.',
                                                                'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                           'order fulfillment handoffs, this stakeholder sees a different '
                                                                           'part of the operating problem.',
                                                                'role': 'Executive sponsor'},
                                          'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                        'than the other stakeholders.',
                                                                        'The stakeholder has an incentive that can influence which facts '
                                                                        'are emphasized.'],
                                                              'incentive': 'Tests whether improvement becomes a credible economic benefit.',
                                                              'opening': 'Tests whether improvement becomes a credible economic benefit. '
                                                                         'In order fulfillment handoffs, this stakeholder sees a different '
                                                                         'part of the operating problem.',
                                                              'role': 'Finance'},
                                          'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                                 'constraint than the other stakeholders.',
                                                                                 'The stakeholder has an incentive that can influence '
                                                                                 'which facts are emphasized.'],
                                                                       'incentive': 'Sees workarounds, exceptions, friction, and practical '
                                                                                    'constraints.',
                                                                       'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                                  'constraints. In order fulfillment handoffs, this '
                                                                                  'stakeholder sees a different part of the operating '
                                                                                  'problem.',
                                                                       'role': 'Frontline employee'},
                                          'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                      'the other stakeholders.',
                                                                      'The stakeholder has an incentive that can influence which facts are '
                                                                      'emphasized.'],
                                                            'incentive': 'Owns service performance and operational continuity.',
                                                            'opening': 'Owns service performance and operational continuity. In order '
                                                                       'fulfillment handoffs, this stakeholder sees a different part of '
                                                                       'the operating problem.',
                                                            'role': 'Process owner'},
                                          'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                        'than the other stakeholders.',
                                                                        'The stakeholder has an incentive that can influence which facts '
                                                                        'are emphasized.'],
                                                              'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                           'requirements.',
                                                              'opening': 'Protects policy, regulatory, control, and reputational '
                                                                         'requirements. In order fulfillment handoffs, this stakeholder '
                                                                         'sees a different part of the operating problem.',
                                                              'role': 'Risk / compliance'}}},
 'y-policy-intake': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                           'id': 'problem',
                                           'prompt': 'What is the problem in measurable terms, and for whom?',
                                           'requires': ['baseline', 'customer', 'problem']},
                                          {'feedback': 'Turn plausible stories into testable hypotheses.',
                                           'id': 'evidence',
                                           'prompt': 'Which evidence would distinguish competing explanations?',
                                           'requires': ['evidence', 'data', 'variation']},
                                          {'feedback': 'Treat organizational incentives as part of the operating system.',
                                           'id': 'people',
                                           'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                           'requires': ['incentive', 'political', 'social']}],
                     'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                           'id': 'fast',
                                           'label': 'Move quickly on the most visible solution',
                                           'signal': 'speed'},
                                          {'effect': 'Slower up front; improves the quality of the causal decision.',
                                           'id': 'evidence',
                                           'label': 'Collect targeted evidence before committing',
                                           'signal': 'evidence'},
                                          {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                           'id': 'redesign',
                                           'label': 'Redesign the process around the customer requirement',
                                           'signal': 'design'}],
                     'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                     'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                        'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can be '
                                                 'defended responsibly.',
                                        'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                        'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                  'consequences for people.',
                                        'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                     'agendas.',
                                        'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal work '
                                                  'practices.'},
                     'socratic_prompts': ['What do you know versus what are you assuming?',
                                          'Whose definition of the problem are you using?',
                                          'What evidence would change your mind?',
                                          'Who benefits or loses if this recommendation is adopted?',
                                          'What would make a technically correct solution fail organizationally?'],
                     'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                            'than the other stakeholders.',
                                                                            'The stakeholder has an incentive that can influence which '
                                                                            'facts are emphasized.'],
                                                                  'incentive': 'Experiences the outcome and defines value differently from '
                                                                               'internal teams.',
                                                                  'opening': 'Experiences the outcome and defines value differently from '
                                                                             'internal teams. In insurance policy intake, this stakeholder '
                                                                             'sees a different part of the operating problem.',
                                                                  'role': 'Customer / user'},
                                      'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                      'the other stakeholders.',
                                                                      'The stakeholder has an incentive that can influence which facts are '
                                                                      'emphasized.'],
                                                            'incentive': 'Wants a visible result and has a commitment to defend.',
                                                            'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                       'insurance policy intake, this stakeholder sees a different part of '
                                                                       'the operating problem.',
                                                            'role': 'Executive sponsor'},
                                      'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                    'the other stakeholders.',
                                                                    'The stakeholder has an incentive that can influence which facts are '
                                                                    'emphasized.'],
                                                          'incentive': 'Tests whether improvement becomes a credible economic benefit.',
                                                          'opening': 'Tests whether improvement becomes a credible economic benefit. In '
                                                                     'insurance policy intake, this stakeholder sees a different part of '
                                                                     'the operating problem.',
                                                          'role': 'Finance'},
                                      'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                             'constraint than the other stakeholders.',
                                                                             'The stakeholder has an incentive that can influence which '
                                                                             'facts are emphasized.'],
                                                                   'incentive': 'Sees workarounds, exceptions, friction, and practical '
                                                                                'constraints.',
                                                                   'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                              'constraints. In insurance policy intake, this stakeholder '
                                                                              'sees a different part of the operating problem.',
                                                                   'role': 'Frontline employee'},
                                      'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than the '
                                                                  'other stakeholders.',
                                                                  'The stakeholder has an incentive that can influence which facts are '
                                                                  'emphasized.'],
                                                        'incentive': 'Owns service performance and operational continuity.',
                                                        'opening': 'Owns service performance and operational continuity. In insurance '
                                                                   'policy intake, this stakeholder sees a different part of the operating '
                                                                   'problem.',
                                                        'role': 'Process owner'},
                                      'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                    'the other stakeholders.',
                                                                    'The stakeholder has an incentive that can influence which facts are '
                                                                    'emphasized.'],
                                                          'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                       'requirements.',
                                                          'opening': 'Protects policy, regulatory, control, and reputational requirements. '
                                                                     'In insurance policy intake, this stakeholder sees a different part '
                                                                     'of the operating problem.',
                                                          'role': 'Risk / compliance'}}},
 'y-purchase-orders': {'branch_questions': [{'feedback': 'Define the gap before naming a cause.',
                                             'id': 'problem',
                                             'prompt': 'What is the problem in measurable terms, and for whom?',
                                             'requires': ['baseline', 'customer', 'problem']},
                                            {'feedback': 'Turn plausible stories into testable hypotheses.',
                                             'id': 'evidence',
                                             'prompt': 'Which evidence would distinguish competing explanations?',
                                             'requires': ['evidence', 'data', 'variation']},
                                            {'feedback': 'Treat organizational incentives as part of the operating system.',
                                             'id': 'people',
                                             'prompt': 'Which stakeholder incentives could distort the information you are receiving?',
                                             'requires': ['incentive', 'political', 'social']}],
                       'decision_options': [{'effect': 'May create momentum, but risks solving the wrong problem.',
                                             'id': 'fast',
                                             'label': 'Move quickly on the most visible solution',
                                             'signal': 'speed'},
                                            {'effect': 'Slower up front; improves the quality of the causal decision.',
                                             'id': 'evidence',
                                             'label': 'Collect targeted evidence before committing',
                                             'signal': 'evidence'},
                                            {'effect': 'May deliver a stronger outcome but requires broader stakeholder alignment.',
                                             'id': 'redesign',
                                             'label': 'Redesign the process around the customer requirement',
                                             'signal': 'design'}],
                       'phases': ['define', 'measure', 'analyze', 'improve', 'control'],
                       'reasoning_lens': {'economic': 'Consider cost, capacity, revenue, risk, benefits capture, and opportunity cost.',
                                          'ethos': 'Consider professional responsibility, credibility, fairness, controls, and what can be '
                                                   'defended responsibly.',
                                          'logos': 'Use evidence, process data, causal logic, and explicit assumptions.',
                                          'pathos': 'Consider customer and employee experience, trust, frustration, workload, and '
                                                    'consequences for people.',
                                          'political': 'Consider power, incentives, commitments, reputation, ownership, and competing '
                                                       'agendas.',
                                          'social': 'Consider team norms, status, trust, psychological safety, adoption, and informal work '
                                                    'practices.'},
                       'socratic_prompts': ['What do you know versus what are you assuming?',
                                            'Whose definition of the problem are you using?',
                                            'What evidence would change your mind?',
                                            'Who benefits or loses if this recommendation is adopted?',
                                            'What would make a technically correct solution fail organizationally?'],
                       'stakeholders': {'Customer Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                              'constraint than the other stakeholders.',
                                                                              'The stakeholder has an incentive that can influence which '
                                                                              'facts are emphasized.'],
                                                                    'incentive': 'Experiences the outcome and defines value differently '
                                                                                 'from internal teams.',
                                                                    'opening': 'Experiences the outcome and defines value differently from '
                                                                               'internal teams. In purchase order approval, this '
                                                                               'stakeholder sees a different part of the operating '
                                                                               'problem.',
                                                                    'role': 'Customer / user'},
                                        'Executive Sponsor': {'clues': ['This perspective emphasizes a different outcome or constraint '
                                                                        'than the other stakeholders.',
                                                                        'The stakeholder has an incentive that can influence which facts '
                                                                        'are emphasized.'],
                                                              'incentive': 'Wants a visible result and has a commitment to defend.',
                                                              'opening': 'Wants a visible result and has a commitment to defend. In '
                                                                         'purchase order approval, this stakeholder sees a different part '
                                                                         'of the operating problem.',
                                                              'role': 'Executive sponsor'},
                                        'Finance Partner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                      'the other stakeholders.',
                                                                      'The stakeholder has an incentive that can influence which facts are '
                                                                      'emphasized.'],
                                                            'incentive': 'Tests whether improvement becomes a credible economic benefit.',
                                                            'opening': 'Tests whether improvement becomes a credible economic benefit. In '
                                                                       'purchase order approval, this stakeholder sees a different part of '
                                                                       'the operating problem.',
                                                            'role': 'Finance'},
                                        'Frontline Representative': {'clues': ['This perspective emphasizes a different outcome or '
                                                                               'constraint than the other stakeholders.',
                                                                               'The stakeholder has an incentive that can influence which '
                                                                               'facts are emphasized.'],
                                                                     'incentive': 'Sees workarounds, exceptions, friction, and practical '
                                                                                  'constraints.',
                                                                     'opening': 'Sees workarounds, exceptions, friction, and practical '
                                                                                'constraints. In purchase order approval, this stakeholder '
                                                                                'sees a different part of the operating problem.',
                                                                     'role': 'Frontline employee'},
                                        'Process Owner': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                    'the other stakeholders.',
                                                                    'The stakeholder has an incentive that can influence which facts are '
                                                                    'emphasized.'],
                                                          'incentive': 'Owns service performance and operational continuity.',
                                                          'opening': 'Owns service performance and operational continuity. In purchase '
                                                                     'order approval, this stakeholder sees a different part of the '
                                                                     'operating problem.',
                                                          'role': 'Process owner'},
                                        'Risk & Controls': {'clues': ['This perspective emphasizes a different outcome or constraint than '
                                                                      'the other stakeholders.',
                                                                      'The stakeholder has an incentive that can influence which facts are '
                                                                      'emphasized.'],
                                                            'incentive': 'Protects policy, regulatory, control, and reputational '
                                                                         'requirements.',
                                                            'opening': 'Protects policy, regulatory, control, and reputational '
                                                                       'requirements. In purchase order approval, this stakeholder sees a '
                                                                       'different part of the operating problem.',
                                                            'role': 'Risk / compliance'}}}}


# v1.6: Explicit DFSS/DMADV case framing.
_DMADV_IDS = {
    'w-invoice-correction','w-appointment-scheduling','y-purchase-orders','y-maintenance-request',
    'g-hospital-pharmacy','g-factory-changeover','b-digital-onboarding','b-medication-administration'
}
for _case_id in _DMADV_IDS:
    if _case_id in SCENARIO_DETAIL:
        SCENARIO_DETAIL[_case_id]['method'] = 'DMADV / IDOV'
        SCENARIO_DETAIL[_case_id]['phases'] = ['define','measure','analyze','design','verify']
        SCENARIO_DETAIL[_case_id]['socratic_prompts'] = [
            'Who is the customer, and what must the new design accomplish?',
            'What requirements can you measure before choosing a design?',
            'Which risks or constraints could invalidate the design?',
            'Which design trade-off best balances customer, business, and operational needs?',
            'What evidence would verify that the new design works in the real process?',
        ]
        SCENARIO_DETAIL[_case_id]['reasoning_lens']['economic'] += ' For a new design, consider lifecycle cost, capacity and cost of failure.'
        SCENARIO_DETAIL[_case_id]['reasoning_lens']['political'] += ' Consider who owns the design decision and whose priorities shape requirements.'
        SCENARIO_DETAIL[_case_id]['reasoning_lens']['social'] += ' Consider adoption, trust, role changes and how the new design fits real work.'


# Expanded case library: generate a usable interactive case detail for every
# source-based case that does not already have a bespoke detail map.
from content import SCENARIOS as _CONTENT_SCENARIOS

_DEFAULT_STAKEHOLDERS = {
    'Executive Sponsor': {
        'role': 'Executive sponsor',
        'incentive': 'Wants a visible result and has a commitment to defend.',
        'opening': 'Wants a visible result and has a commitment to defend the project. This stakeholder sees the challenge through business priorities and commitments.',
        'clues': ['Emphasizes outcomes, commitments and timing.', 'May selectively emphasize facts that support a preferred direction.'],
    },
    'Process Owner': {
        'role': 'Process owner',
        'incentive': 'Owns performance and operational continuity.',
        'opening': 'Owns day-to-day performance and operational continuity. This stakeholder sees constraints created by the current process and its workarounds.',
        'clues': ['Knows where work gets stuck.', 'May optimize for continuity over redesign.'],
    },
    'Frontline Representative': {
        'role': 'Frontline employee',
        'incentive': 'Sees workarounds, workload and practical constraints.',
        'opening': 'Sees how the work is actually performed, including exceptions and informal workarounds. This stakeholder can reveal where the documented process differs from reality.',
        'clues': ['Knows practical friction and hidden work.', 'May be concerned about role changes or added burden.'],
    },
    'Customer Representative': {
        'role': 'Customer / user',
        'incentive': 'Defines value through the experience and outcome received.',
        'opening': 'Defines value from the customer or user perspective. This stakeholder may judge success differently from internal teams.',
        'clues': ['Can expose a gap between internal metrics and customer value.', 'May prioritize simplicity, reliability or speed.'],
    },
    'Risk & Controls': {
        'role': 'Risk / controls',
        'incentive': 'Protects safety, compliance, policy and reputation.',
        'opening': 'Protects the constraints that must not be traded away for speed or cost. This stakeholder can identify control requirements and unintended consequences.',
        'clues': ['May see risks that other stakeholders discount.', 'Can identify non-negotiable constraints.'],
    },
    'Finance Partner': {
        'role': 'Finance',
        'incentive': 'Tests whether the change creates a credible economic benefit.',
        'opening': 'Tests whether the business case is real and whether benefits can be captured. This stakeholder sees cost, capacity and opportunity cost.',
        'clues': ['Challenges weak benefit calculations.', 'May ask who actually receives the benefit.'],
    },
}

_DEFAULT_LENSES = {
    'logos': 'Use evidence, process data, causal logic and explicit assumptions.',
    'pathos': 'Consider customer and employee experience, trust, frustration, workload and consequences for people.',
    'ethos': 'Consider professional responsibility, credibility, fairness, controls and what can be defended responsibly.',
    'economic': 'Consider cost, capacity, service impact, risk, benefits capture and opportunity cost.',
    'political': 'Consider power, incentives, commitments, reputation, ownership and competing agendas.',
    'social': 'Consider norms, status, trust, psychological safety, adoption and informal work practices.',
}


def _generic_case_detail(case):
    is_dmadv = case.get('method') == 'DMADV / IDOV'
    if is_dmadv:
        phases = ['define', 'measure', 'analyze', 'design', 'verify']
        branch_questions = [
            {'id': 'requirements', 'prompt': 'What must the new design accomplish, and for whom?', 'feedback': 'Start with customer and stakeholder requirements before proposing a design.', 'requires': ['customer', 'requirement', 'problem']},
            {'id': 'evidence', 'prompt': 'Which measures would tell you whether the design is likely to meet those requirements?', 'feedback': 'Define measurable evidence before comparing design options.', 'requires': ['measure', 'data', 'baseline']},
            {'id': 'tradeoffs', 'prompt': 'Which constraints or risks could make an apparently good design fail in the real organization?', 'feedback': 'Bring operational, economic and organizational constraints into the design decision.', 'requires': ['risk', 'political', 'social']},
        ]
        prompts = [
            'Who is the customer, and what must the new design accomplish?',
            'What can you measure before choosing among designs?',
            'Which requirements or constraints could invalidate the design?',
            'Which design trade-off best balances customer, business and operational needs?',
            'What evidence would verify that the design works in real operations?',
        ]
    else:
        phases = ['define', 'measure', 'analyze', 'improve', 'control']
        branch_questions = [
            {'id': 'problem', 'prompt': 'What is the problem in measurable terms, and for whom?', 'feedback': 'Define the gap before naming a cause.', 'requires': ['baseline', 'customer', 'problem']},
            {'id': 'evidence', 'prompt': 'Which evidence would distinguish competing explanations?', 'feedback': 'Turn plausible stories into testable hypotheses.', 'requires': ['evidence', 'data', 'variation']},
            {'id': 'people', 'prompt': 'Which stakeholder incentives could distort the information you are receiving?', 'feedback': 'Treat organizational incentives as part of the operating system.', 'requires': ['incentive', 'political', 'social']},
        ]
        prompts = [
            'What do you know versus what are you assuming?',
            'Whose definition of the problem are you using?',
            'What evidence would change your mind?',
            'Who benefits or loses if this recommendation is adopted?',
            'What would make a technically correct solution fail organizationally?',
        ]
    return {
        'phases': phases,
        'branch_questions': branch_questions,
        'socratic_prompts': prompts,
        'reasoning_lens': dict(_DEFAULT_LENSES),
        'decision_options': [
            {'id': 'fast', 'label': 'Act on the most visible issue', 'effect': 'May create momentum, but risks solving the wrong problem.', 'signal': 'speed'},
            {'id': 'evidence', 'label': 'Collect targeted evidence first', 'effect': 'Slower up front; improves the quality of the decision.', 'signal': 'evidence'},
            {'id': 'alignment', 'label': 'Test the change with affected stakeholders', 'effect': 'Requires more alignment, but improves adoption and reduces implementation risk.', 'signal': 'alignment'},
        ],
        'stakeholders': {name: dict(info, opening=info['opening'] + f" The case concerns {case['title']} in {case['area']}.") for name, info in _DEFAULT_STAKEHOLDERS.items()},
    }

for _case in _CONTENT_SCENARIOS:
    SCENARIO_DETAIL.setdefault(_case['id'], _generic_case_detail(_case))

# Preserve explicit DMADV framing for the expanded source cases.
for _case in _CONTENT_SCENARIOS:
    if _case.get('method') == 'DMADV / IDOV':
        SCENARIO_DETAIL[_case['id']]['phases'] = ['define', 'measure', 'analyze', 'design', 'verify']
