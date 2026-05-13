"""Youth and community programmes – Ministry of Youth, Sports and Community Empowerment."""

from .catalogue import MOY_BYAC, MOY, YES_DIV

SERVICES_YOUTH = [

    {
        "slug": "byac-recruitment",
        "title": "Apply for the Barbados YouthADVANCE Corps (BYAC)",
        "category": "youth-and-community",
        "description": "Apply to join the Barbados YouthADVANCE Corps, a Ministry of Youth training and service programme.",
        "summary": [
            "The Barbados YouthADVANCE Corps (BYAC) is a Ministry of Youth, Sports and Community Empowerment programme that gives young people training, work experience and community service.",
            "Apply, send in a health assessment and have two referees send in their forms. You will then be invited to an interview.",
        ],
        "who_can_apply": [
            "Barbadian nationals aged 16 to 30",
            "people in good health who can take part in physical training and community work",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address and date of birth",
                "your National Registration Number",
                "your phone number and email address",
                "the highest level of education you have completed",
                "your work history, if any",
                "your areas of interest (for example, the trade you want training in)",
                "the names and contact details of two referees",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "National ID card or passport"},
                {"name": "Birth certificate"},
                {"name": "Most recent school report or certificates"},
                {"name": "Health Assessment Form", "note": "Completed and stamped by a doctor – see ‘Submit a BYAC health assessment’."},
                {"name": "Two completed Reference Forms", "note": "One from each of your referees – see ‘Submit a BYAC reference form’."},
                {"name": "Recent passport-size photograph"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Recruitment intakes happen at set times each year. You will get a reply within 6 to 8 weeks of the closing date.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "By email or in person",
                    "content": [
                        "Send the completed Recruitment Form and your supporting documents to BYAC at #33 Warrens Industrial Park, Warrens, St. Michael. You can also email it.",
                    ],
                },
            ],
        },
        "edge_cases": [
            {
                "heading": "If you are under 18",
                "content": [
                    "You will need a parent or guardian to sign your application and your health assessment form.",
                ],
            },
        ],
        "contact": MOY_BYAC,
        "related": [
            {"slug": "byac-health-assessment", "title": "Submit a BYAC health assessment"},
            {"slug": "byac-reference-form", "title": "Submit a BYAC reference form"},
        ],
    },

    {
        "slug": "byac-health-assessment",
        "title": "Submit a BYAC health assessment",
        "category": "youth-and-community",
        "description": "A doctor must complete a health assessment for everyone applying to BYAC.",
        "summary": [
            "Everyone applying to the Barbados YouthADVANCE Corps must have a doctor confirm that they are in good enough health to take part in the programme.",
            "You will need to make an appointment with a doctor and take the form with you.",
        ],
        "who_can_apply": [
            "anyone applying to BYAC",
        ],
        "before_you_start": {
            "intro": "Before you see your doctor, fill in:",
            "items": [
                "your last name, first and middle names",
                "your address and date of birth",
                "your phone number and email",
                "any allergies or long-term conditions you have",
                "any medication you take",
            ],
        },
        "documents": {
            "intro": "Bring to your appointment:",
            "items": [
                {"name": "The Health Assessment Form"},
                {"name": "Photo ID"},
                {"name": "Health card or polyclinic record", "note": "If you have one."},
            ],
        },
        "fees": "Your doctor may charge a fee for the assessment. The Ministry does not charge.",
        "how_long": "Most assessments are completed in one appointment.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Through your doctor",
                    "content": [
                        "Make an appointment, take the form with you and ask your doctor to complete and stamp it.",
                    ],
                },
                {
                    "heading": "Return the completed form to BYAC",
                    "content": [
                        "Once your doctor has signed and stamped it, send the form to BYAC by post or by email, or hand it in at #33 Warrens Industrial Park.",
                    ],
                },
            ],
        },
        "contact": MOY_BYAC,
        "related": [
            {"slug": "byac-recruitment", "title": "Apply for the Barbados YouthADVANCE Corps"},
        ],
    },

    {
        "slug": "byac-reference-form",
        "title": "Submit a BYAC reference form",
        "category": "youth-and-community",
        "description": "Referees complete a reference form for someone applying to BYAC.",
        "summary": [
            "If a friend, mentor or former teacher has asked you to be their referee for the Barbados YouthADVANCE Corps, you will need to fill in a reference form for them.",
            "You should know the applicant well enough to comment on their character and suitability for the programme.",
        ],
        "who_can_apply": [
            "people who have known the applicant for at least 2 years",
            "you should not be a relative of the applicant",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the applicant’s full name",
                "how long you have known the applicant",
                "in what capacity you have known them (for example, teacher, employer, pastor)",
                "your honest view of their character, attitude and ability",
                "your full name, address, phone number and email",
            ],
        },
        "documents": {
            "intro": "You will need:",
            "items": [
                {"name": "Your own photo ID"},
                {"name": "Letterhead", "note": "If you are giving the reference in your professional capacity."},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Fill in the form as soon as possible so the applicant’s application is not held up.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Return the completed form to BYAC",
                    "content": [
                        "Send the completed Reference Form to BYAC by post or email, or give it to the applicant in a sealed envelope to hand in.",
                    ],
                },
            ],
        },
        "contact": MOY_BYAC,
    },

    {
        "slug": "get-hired-programme",
        "title": "Apply for the Get Hired Programme",
        "category": "youth-and-community",
        "description": "Apply for the 2026 Get Hired Programme – a Ministry of Youth jobs and employability programme.",
        "summary": [
            "Get Hired is a Ministry of Youth, Sports and Community Empowerment programme that helps young Barbadians prepare for and find work.",
            "You will get training in workplace skills, help with your CV and an interview, and a placement with an employer.",
        ],
        "who_can_apply": [
            "Barbadian nationals aged 18 to 35",
            "people who are out of work or looking to change careers",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address and date of birth",
                "your National Registration Number",
                "your email address and phone number",
                "your highest level of education and any qualifications",
                "your work history, including dates and roles",
                "the area of work you want to go into",
            ],
        },
        "documents": {
            "intro": "Bring with you (or upload):",
            "items": [
                {"name": "National ID card"},
                {"name": "Birth certificate"},
                {"name": "Most recent CV"},
                {"name": "Certificates for your qualifications"},
                {"name": "Recent passport-size photograph"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Applications are usually open for several weeks. You will get a reply within 4 to 6 weeks of the closing date.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Online",
                    "content": [
                        "Complete the Get Hired Programme: Application Form (2026) on the Ministry website.",
                    ],
                },
            ],
        },
        "contact": MOY,
    },

    {
        "slug": "pathways-employability-programme",
        "title": "Apply for the Pathways Employability Programme",
        "category": "youth-and-community",
        "description": "Apply for the 2026 Pathways Employability Programme – a Ministry of Youth scheme that helps young people get ready for work.",
        "summary": [
            "Pathways is a Ministry of Youth, Sports and Community Empowerment programme that helps young Barbadians build the skills, confidence and contacts they need to find work.",
            "You will take part in classroom training, a work placement and mentoring.",
        ],
        "who_can_apply": [
            "Barbadian nationals aged 17 to 30",
            "people who are not in school, training or full-time work",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address and date of birth",
                "your National Registration Number",
                "your email address and phone number",
                "your highest level of education",
                "your work history, if any",
                "the type of training or work you are interested in",
            ],
        },
        "documents": {
            "intro": "Bring with you (or upload):",
            "items": [
                {"name": "National ID card"},
                {"name": "Birth certificate"},
                {"name": "Most recent school report or certificates"},
                {"name": "CV", "note": "If you have one."},
                {"name": "Recent passport-size photograph"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "You will get a reply within 4 to 6 weeks of the closing date.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Online",
                    "content": [
                        "Complete the Pathways Employability Programme: Application Form (2026) on the Ministry website.",
                    ],
                },
            ],
        },
        "contact": MOY,
    },

    {
        "slug": "yes-first-contact",
        "title": "Make first contact with the Youth Entrepreneurship Scheme",
        "category": "youth-and-community",
        "description": "Tell the Youth Entrepreneurship Scheme (YES) about your business idea so they can offer support.",
        "summary": [
            "The Youth Entrepreneurship Scheme (YES) helps young Barbadians turn ideas into businesses. The First Contact form is the first step.",
            "You will be invited to a one-to-one meeting with a YES officer to talk through your idea and next steps.",
        ],
        "who_can_apply": [
            "Barbadian nationals aged 18 to 35",
            "people with a business idea, or an existing business that is under 3 years old",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address and date of birth",
                "your contact details",
                "a short summary of your business idea or current business",
                "what stage your idea is at",
                "the kind of support you are looking for (training, funding, mentoring)",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Business plan or pitch deck", "note": "If you already have one."},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "You will be contacted within 2 weeks to arrange your first meeting.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Youth Entrepreneurship Scheme First Contact Form to the Division of Youth and Culture, Prime Minister’s Office.",
                    ],
                },
            ],
        },
        "contact": YES_DIV,
    },

    {
        "slug": "nscp-camper-registration",
        "title": "Register a camper for the National Summer Camp Programme",
        "category": "youth-and-community",
        "description": "Register a child aged 7 to 12 for the National Summer Camp Programme.",
        "summary": [
            "The National Summer Camp Programme (NSCP) is the Ministry of Youth, Sports and Community Empowerment’s annual summer camp. It runs across parishes during the school holidays.",
            "The 2025 programme is not currently open – check back when registration opens.",
        ],
        "who_can_apply": [
            "parents and guardians of children aged 7 to 12",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the child’s full name, date of birth and age",
                "the child’s school and parish",
                "the parent or guardian’s name, address, phone and email",
                "the camp location you prefer",
                "the child’s emergency contact",
                "any allergies, medical conditions or dietary needs",
            ],
        },
        "documents": {
            "intro": "Bring with you (or upload):",
            "items": [
                {"name": "The child’s birth certificate"},
                {"name": "Photo ID for the parent or guardian"},
                {"name": "The child’s most recent school report"},
                {"name": "A recent passport-size photograph of the child"},
            ],
        },
        "fees": "Confirm fees when registration opens. The Ministry tries to keep costs low so every child can take part.",
        "how_long": "Places are usually offered within 2 to 4 weeks of the closing date.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Online when registration opens",
                    "content": [
                        "Complete the NSCP Camper Registration form on the Ministry website during the registration window.",
                    ],
                },
            ],
        },
        "edge_cases": [
            {
                "heading": "If the programme is full",
                "content": [
                    "You will be put on a waiting list. The Ministry will let you know if a place opens up.",
                ],
            },
        ],
        "contact": MOY,
    },

    {
        "slug": "national-community-cultural-training",
        "title": "Register for the National Community Cultural Training Programme",
        "category": "youth-and-community",
        "description": "Register for a 2025 community-based cultural training course.",
        "summary": [
            "The National Community Cultural Training Programme offers free training in community-based cultural activities, including drumming, dance, drama and visual arts.",
            "Classes run after school and at weekends across the parishes.",
        ],
        "who_can_apply": [
            "Barbadian nationals aged 10 to 25",
            "parents or guardians registering a child under 16",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the participant’s full name, address and date of birth",
                "their National Registration Number",
                "their phone number and email",
                "the cultural area they want to train in",
                "their level of experience",
                "for under-16s, the parent or guardian’s details",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Birth certificate", "note": "For participants under 18."},
                {"name": "Parental consent form", "note": "For participants under 16."},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Places are usually confirmed within 2 weeks of the closing date.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Online",
                    "content": [
                        "Complete the National Community Cultural Training Programme 2025: Registration Form on the Ministry website.",
                    ],
                },
            ],
        },
        "contact": MOY,
    },

    {
        "slug": "yar-performing-arts",
        "title": "Register for Youth Achieving Results (Performing Arts)",
        "category": "youth-and-community",
        "description": "Register a young performer for the Youth Achieving Results performing arts programme.",
        "summary": [
            "Youth Achieving Results (Performing Arts) is a Ministry of Youth programme that supports young Barbadians in music, dance, theatre and spoken word.",
            "You will get classes, mentoring and performance opportunities.",
        ],
        "who_can_apply": [
            "Barbadian nationals aged 12 to 30",
            "parents or guardians registering a child under 16",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the participant’s full name, address and date of birth",
                "their National Registration Number",
                "their phone number and email",
                "the performing art they want to focus on (music, dance, theatre, spoken word)",
                "their level of experience and any past performances",
                "for under-16s, the parent or guardian’s details",
            ],
        },
        "documents": {
            "intro": "Bring with you (or upload):",
            "items": [
                {"name": "Photo ID"},
                {"name": "Birth certificate", "note": "For participants under 18."},
                {"name": "Parental consent form", "note": "For participants under 16."},
                {"name": "Performance reel or sample", "note": "Optional but helpful."},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Places are usually confirmed within 2 weeks of the closing date.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Online",
                    "content": [
                        "Complete the Youth Achieving Results (Performing Arts): Registration Form on the Ministry website.",
                    ],
                },
            ],
        },
        "contact": MOY,
        "related": [
            {"slug": "yar-visual-arts", "title": "Register for Youth Achieving Results (Visual Arts)"},
        ],
    },

    {
        "slug": "yar-visual-arts",
        "title": "Register for Youth Achieving Results (Visual Arts)",
        "category": "youth-and-community",
        "description": "Register a young visual artist for the Youth Achieving Results visual arts programme.",
        "summary": [
            "Youth Achieving Results (Visual Arts) is a Ministry of Youth programme that supports young Barbadians in painting, drawing, photography, sculpture and digital art.",
            "You will get classes, mentoring and a chance to show your work at end-of-programme exhibitions.",
        ],
        "who_can_apply": [
            "Barbadian nationals aged 12 to 30",
            "parents or guardians registering a child under 16",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the participant’s full name, address and date of birth",
                "their National Registration Number",
                "their phone number and email",
                "the visual art they want to focus on (painting, drawing, photography, sculpture, digital art)",
                "their level of experience",
                "for under-16s, the parent or guardian’s details",
            ],
        },
        "documents": {
            "intro": "Bring with you (or upload):",
            "items": [
                {"name": "Photo ID"},
                {"name": "Birth certificate", "note": "For participants under 18."},
                {"name": "Parental consent form", "note": "For participants under 16."},
                {"name": "Portfolio or sample of recent work", "note": "Optional but helpful."},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Places are usually confirmed within 2 weeks of the closing date.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Online",
                    "content": [
                        "Complete the Youth Achieving Results (Visual Arts): Registration Form on the Ministry website.",
                    ],
                },
            ],
        },
        "contact": MOY,
    },

    {
        "slug": "youth-mc-training",
        "title": "Register for the Youth MC Training Programme",
        "category": "youth-and-community",
        "description": "Apply to train as an MC, presenter or radio host on the Youth MC Training Programme.",
        "summary": [
            "The Youth MC Training Programme trains young Barbadians to MC, present and host events on stage, radio and online.",
            "The programme is not currently open – check back when registration opens.",
        ],
        "who_can_apply": [
            "Barbadian nationals aged 14 to 25",
            "parents or guardians registering a young person under 16",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the participant’s full name, address and date of birth",
                "their National Registration Number",
                "their phone number and email",
                "their level of experience with public speaking or hosting",
                "for under-16s, the parent or guardian’s details",
            ],
        },
        "documents": {
            "intro": "Bring with you (or upload):",
            "items": [
                {"name": "Photo ID"},
                {"name": "Birth certificate", "note": "For participants under 18."},
                {"name": "Parental consent form", "note": "For participants under 16."},
                {"name": "Short voice or video clip", "note": "Optional – introducing yourself."},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Places are usually confirmed within 2 weeks of the closing date.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Online when registration opens",
                    "content": [
                        "Complete the Youth MC Training Programme Registration Form on the Ministry website during the registration window.",
                    ],
                },
            ],
        },
        "contact": MOY,
    },
]
