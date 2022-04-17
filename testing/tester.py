import chatbot
import filewriter

ParaphraseDict = {10: ['Is it necessary for my child to be evaluated for special education?',
                        'Should I get my kid evaluated for special education?',
                        'Do I need to screen my child for special education?',
                        'Should I have my children seen for special education?',
                        'How do I know if I need to screen my child for special education?'
                        ],

                        3: ['What is an Individualized Education Plan?',
                        'What exactly is an IEP?',
                        'I’m not sure what an IEP is.',
                        'Define IEP.',
                        'Please tell me what IEP is.',
                        ],

                        14: ['Is it possible for the school to use my confidential evaluation to speed up the review process?',
                        'Is it possible for the school to use my private evaluation to speed the evaluation process?',
                        'Can the school use my own assessment to expedite the evaluation process?',
                        'Would the school be able to utilize my own appraisal to speed up the assessment interaction?',
                        'Is the school able to make the evaluation process quicker by using my private evaluation?',
                        ],

                        18: ['How long will it take for my kid to be assessed?',
                        'Does the evaluation process take a long time?',
                        'What amount of time does it require to get my kid assessed?',
                        'What is the wait time to get my child evaluated?',
                        'If my child is evaluated, how long will we wait for the results?'
                        ],

                        20: ['What if the parent disagrees with the assessment?',
                        'What should I do if I disagree with the evaluation?',
                        'Am I able to disagree with the evaluation?',
                        'Is the evaluation definitive, or can the parent disagree with the evaluation?',
                        'Are parents allowed to disagree with their child’s evaluation?'
                        ],

                        23: ['Is it necessary for the school to inform me of who will be attending the meeting?',
                        'Does the school need to let me know who will go to the meeting?',
                        'How will I know who is attending the IEP meeting?',
                        'Will I know who is attending the meeting?',
                        'Will the school inform me who is attending the meeting?'
                        ],

                        46: ['Are there age restrictions for different age groups in the same special education class?',
                        'Are there any age restrictions in a special education class for different age groups?',
                        'Are there age restrictions in the same special education class for different age groups?',
                        'What are the age limits on different ages in the same class?',
                        'How far apart are the ages in a special education class?'
                        ],

                        51: ['At what age does a child typically receive special education services?',
                        'When can a child receive special education services?',
                        'At what age can children receive special education services?',
                        'What age do children usually go into special education?',
                        'What is the minimum age for a child to be eligible for special education services?'
                        ],

                        53: ['If my child was in Early Steps, will they go on to special education at their school?',
                        'What comes after Early Steps?',
                        'Are students leaving Early Steps automatically eligible for special education services?',
                        'When students graduate from Early Steps, will they automatically be eligible for special education services?',
                        'Does Early steps lead directly to special education after?'
                        ],

                        29: ['What happens if my child’s teacher misses an IEP meeting?',
                        'Is it okay for a team member to miss a meeting?',
                        'What should I do if a team member is late to the meeting?',
                        'My child’s teacher arrived late to our IEP meeting. Is that OK?',
                        'What are the rules regarding missing an IEP meeting?'
                        ]}

questions = chatbot.read_file("questions.txt")

results = [[], [], [], [], [], [], [], [], [], []]

counter = 0
for question in ParaphraseDict:
    correct_index = question
    amtCorrect = 0

    for variation in ParaphraseDict[question]:
        ranks= chatbot.find_similarity(questions, variation)
        a_index = chatbot.answer(ranks)

        if a_index == question:
            amtCorrect += 1

        idx_list = [x[0] for x in ranks]
        results[counter].append(idx_list.index(question)+1)

    results[counter].append(amtCorrect)
    counter += 1

for row in results:
    print(row)
