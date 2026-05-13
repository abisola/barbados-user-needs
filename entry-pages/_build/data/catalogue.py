"""
Entry-page content for every government form in /forms.

Each service dict produces:
- a JSON file at data/services/<slug>.json
- a rendered HTML page at out/services/<slug>.html

Plain language, British English, written for citizens not civil servants.
"""

def _all_services():
    """Combine services from every catalogue module."""
    from .catalogue_business import SERVICES_BUSINESS
    from .catalogue_youth import SERVICES_YOUTH
    return SERVICES + SERVICES_BUSINESS + SERVICES_YOUTH

CATEGORIES = {
    "driving-and-transport": {
        "name": "Driving and transport",
        "description": "Register, transfer or change a vehicle, import a car, get a vehicle inspection, and other things you do with the Barbados Licensing Authority."
    },
    "national-insurance-and-benefits": {
        "name": "National Insurance and benefits",
        "description": "Apply for pensions and benefits, register with the NIS, set up direct deposit and prove your status to keep payments coming."
    },
    "firearms": {
        "name": "Firearms",
        "description": "Apply for a firearm licence, a dealer or gunsmith licence, a shooting club licence, or to import or export a firearm."
    },
    "safety-and-public-events": {
        "name": "Safety and public events",
        "description": "Get a police accident report, a permit for a march or motorcade, or a loud music permit for an event."
    },
    "business-and-companies": {
        "name": "Business and companies",
        "description": "Register a company, file company changes with Corporate Affairs, appoint a registered agent and other company services."
    },
    "trade-exports-and-imports": {
        "name": "Trade, exports and imports",
        "description": "Apply for a certificate of origin to export goods under a trade agreement, or make a complaint about your treatment at a Caribbean port of entry."
    },
    "youth-and-community": {
        "name": "Youth and community programmes",
        "description": "Apply to a Ministry of Youth programme – BYAC, Get Hired, Pathways, Youth Entrepreneurship Scheme, summer camp and arts programmes."
    },
}


# Common contact records used across multiple services
BLA = {
    "agency": "Barbados Licensing Authority",
    "address": "The Pine, East–West Boulevard\nSt. Michael\nBB11000",
    "phone": [
        "Pine: (246) 536-0264 or (246) 536-0278",
        "Holetown: (246) 535-8168 or (246) 535-5169",
        "Oistins: (246) 535-8147 or (246) 536-8148",
    ],
    "email": "BLASupport@barbados.gov.bb",
    "hours": "Open Monday to Friday: 8:15am to 3:30pm",
}

NIS = {
    "agency": "National Insurance Office",
    "address": "Culloden Road\nSt. Michael",
    "phone": ["(246) 467-4000"],
    "email": "nationalinsurance@nis.gov.bb",
    "hours": "Open Monday to Friday: 8:30am to 4:30pm",
}

POLICE = {
    "agency": "The Royal Barbados Police Force",
    "address": "Police Headquarters\nRoebuck Street\nSt. Michael",
    "phone": ["(246) 430-7100"],
    "email": "police@barbados.gov.bb",
    "hours": "Open Monday to Friday: 8:30am to 4:30pm",
}

CAFFAIRS = {
    "agency": "Corporate Affairs and Intellectual Property Office (CAIPO)",
    "address": "Baobab Tower, Ground Floor\nWarrens\nSt. Michael",
    "phone": ["(246) 535-2401"],
    "email": "caipo@caipo.gov.bb",
    "hours": "Open Monday to Friday: 8:30am to 4:30pm",
}

BIDC = {
    "agency": "Barbados Investment and Development Corporation (BIDC)",
    "address": "Pelican House, Princess Alice Highway\nSt. Michael",
    "phone": ["(246) 427-5350"],
    "email": "info@bidc.com",
    "hours": "Open Monday to Friday: 8:30am to 4:30pm",
}

MOY_BYAC = {
    "agency": "Barbados YouthADVANCE Corps (BYAC), Ministry of Youth, Sports and Community Empowerment",
    "address": "#33 Warrens Industrial Park\nWarrens, St. Michael",
    "phone": ["(246) 535-0180"],
    "email": "info@byac.gov.bb",
    "hours": "Open Monday to Friday: 8:30am to 4:30pm",
}

MOY = {
    "agency": "Ministry of Youth, Sports and Community Empowerment",
    "address": "Sky Mall, Haggatt Hall\nSt. Michael",
    "phone": ["(246) 535-3700"],
    "email": "youth@barbados.gov.bb",
    "hours": "Open Monday to Friday: 8:30am to 4:30pm",
}

YES_DIV = {
    "agency": "Division of Youth and Culture, Office of the Prime Minister",
    "address": "Sky Mall, Haggatt Hall\nSt. Michael",
    "phone": ["(246) 535-3700"],
    "email": "yes@barbados.gov.bb",
    "hours": "Open Monday to Friday: 8:30am to 4:30pm",
}


SERVICES = [

    # ---------------------------------------------------------------- #
    # DRIVING AND TRANSPORT
    # ---------------------------------------------------------------- #
    {
        "slug": "register-or-renew-a-vehicle",
        "title": "Register or renew a vehicle",
        "category": "driving-and-transport",
        "description": "Register a vehicle for the first time, or renew its registration each year.",
        "summary": [
            "You must register your vehicle with the Barbados Licensing Authority before you can drive it on the road. You must also renew the registration every year.",
            "If you are renewing, you only need to fill in the first two lines of the form plus anything that has changed since the last registration.",
        ],
        "who_can_apply": [
            "the registered owner of the vehicle",
            "a partnership, company or sole trader that owns the vehicle (you will need to bring a Barbados Licensing Authority declaration form)",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address and parish",
                "your National Registration Number",
                "the vehicle’s registration number (or previous registration if it has one)",
                "the make, model, year, colour, body type and seating capacity of the vehicle",
                "the chassis number and engine number",
                "where the vehicle is normally kept",
                "what you will use the vehicle for (private, hire, goods, etc.)",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID", "note": "Barbados ID card or passport."},
                {"name": "Proof of insurance", "note": "A current certificate of insurance from a Barbados-registered insurer."},
                {"name": "Bill of sale or proof of ownership", "note": "Needed for first-time registration."},
                {"name": "Vehicle inspection certificate", "note": "Needed for vehicles over a certain age – see ‘Get a vehicle inspection’."},
                {"name": "Previous registration card or disc", "note": "Needed if you are renewing."},
            ],
        },
        "fees": {
            "summary": ["Fees depend on the class and weight of the vehicle. Pay at the Barbados Revenue Authority."],
            "items": [
                {"label": "Private car (annual)", "amount": "From $400 BBD"},
                {"label": "Goods or commercial vehicle", "amount": "From $1,000 BBD"},
                {"label": "Motorcycle", "amount": "From $200 BBD"},
            ],
            "notes": ["Final fees are confirmed at the Licensing Authority."],
        },
        "how_long": "Registration is usually issued the same day if all your documents are in order.",
        "how_to_apply": {
            "intro": "Complete the LA.33 Application for Registration or Renewal of Licence for Motor Vehicle form.",
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Go to the Barbados Licensing Authority in the Pine, Holetown or Oistins.",
                        "Hand in your completed form and supporting documents at the front desk.",
                    ],
                },
            ],
        },
        "edge_cases": [
            {
                "heading": "If your vehicle is owned by a business",
                "content": [
                    "A sole trader, partnership or company must also submit a Barbados Licensing Authority declaration form for that business type. See ‘Make a business declaration for vehicle ownership’ for the form you need."
                ],
            },
        ],
        "contact": BLA,
    },

    {
        "slug": "import-a-vehicle",
        "title": "Apply to import a vehicle",
        "category": "driving-and-transport",
        "description": "Get permission to bring a car, truck or motorcycle into Barbados.",
        "summary": [
            "You must apply to the Barbados Licensing Authority before you bring a vehicle into Barbados.",
            "You will need to give details about you, the vehicle, where it is coming from and how it will be used.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address and contact details",
                "your National Registration Number",
                "the country the vehicle is coming from",
                "the make, model and year of the vehicle",
                "the chassis number, engine number and cubic capacity",
                "the body type, colour and seating capacity",
                "how you will use the vehicle (private, public service, goods, etc.)",
                "the name of the shipping company and the expected date of arrival",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Bill of sale", "note": "From the seller or dealership."},
                {"name": "Export certificate from the country of origin"},
                {"name": "Bill of lading", "note": "From the shipping company."},
                {"name": "Photo ID", "note": "Barbados ID card or passport."},
            ],
        },
        "fees": "An import permit application fee is payable to the Barbados Licensing Authority. You will also need to pay customs duties to the Barbados Revenue Authority when the vehicle arrives.",
        "how_long": "An import permit decision takes around 2 to 4 weeks.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the Application for the Importation of Vehicles into Barbados form, plus your supporting documents, to the Barbados Licensing Authority.",
                    ],
                },
            ],
        },
        "contact": BLA,
        "related": [
            {"slug": "vehicle-inspection", "title": "Get a vehicle inspection"},
            {"slug": "register-or-renew-a-vehicle", "title": "Register or renew a vehicle"},
        ],
    },

    {
        "slug": "vehicle-inspection",
        "title": "Get a vehicle inspection",
        "category": "driving-and-transport",
        "description": "Book a Barbados Licensing Authority inspection to check that a vehicle is roadworthy.",
        "summary": [
            "You must have your vehicle inspected by the Barbados Licensing Authority before it can be registered, and from time to time after that.",
            "The form is called the LA.36R Application for Inspection of a Motor Vehicle.",
        ],
        "who_can_apply": [
            "the registered owner of the vehicle",
            "an authorised agent acting on behalf of the owner",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the registration number of the vehicle",
                "your full name and address",
                "the manufacturer, model and year of the vehicle",
                "the primary and secondary colours",
                "the engine number, chassis number, engine capacity and number of cylinders",
                "the number of axles and the type of body",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Proof of vehicle ownership", "note": "Bill of sale or current registration card."},
                {"name": "Proof of insurance"},
            ],
        },
        "fees": {
            "items": [
                {"label": "Inspection fee", "amount": "From $50 BBD"},
            ],
            "notes": ["Pay at the Barbados Revenue Authority before you are inspected."],
        },
        "how_long": "Inspections normally take less than an hour. You will get the certificate the same day if your vehicle passes.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed LA.36R form and your vehicle to the Barbados Licensing Authority.",
                    ],
                },
            ],
        },
        "edge_cases": [
            {
                "heading": "If your vehicle fails",
                "content": [
                    "You will get a list of the problems that need to be fixed. Once you have done the repairs, book another inspection."
                ],
            },
        ],
        "contact": BLA,
    },

    {
        "slug": "sell-a-vehicle",
        "title": "Tell us you have sold a vehicle",
        "category": "driving-and-transport",
        "description": "Inform the Barbados Licensing Authority when you sell a vehicle, on your own or with co-owners.",
        "summary": [
            "If you sell a vehicle (where money is exchanged), the Road Traffic Act says you must tell the Barbados Licensing Authority.",
            "There is one form for a single owner and one for joint owners. You will choose the right one at the Licensing Authority.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address, ID number, telephone number and email",
                "if there is more than one owner, the names and details of every owner",
                "the registration number, engine number and chassis number of the vehicle",
                "the make and model of the vehicle",
                "the full name and address of the person you sold it to",
                "whether you want to keep your registration number",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Registration card or disc", "note": "From the vehicle you have sold."},
                {"name": "Receipt of sale or bill of sale"},
                {"name": "Photo ID for each owner"},
            ],
        },
        "fees": "There is no fee for telling the Licensing Authority you have sold a vehicle.",
        "how_long": "The change is recorded the same day.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Sale of Vehicle form (single owner or joint owner version) to the Barbados Licensing Authority.",
                    ],
                },
            ],
        },
        "contact": BLA,
        "related": [
            {"slug": "transfer-a-vehicle", "title": "Transfer a vehicle (no money exchanged)"},
            {"slug": "retain-registration-number", "title": "Keep your registration number"},
        ],
    },

    {
        "slug": "transfer-a-vehicle",
        "title": "Transfer a vehicle (no money exchanged)",
        "category": "driving-and-transport",
        "description": "Tell the Barbados Licensing Authority you have transferred ownership of a vehicle without money changing hands.",
        "summary": [
            "Use this service if you are giving a vehicle to someone, for example a family member, with no money exchanged.",
            "There is one form for a single owner and one for joint owners.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address, ID number, telephone number and email",
                "if there is more than one owner, the details of every owner",
                "the registration number, engine number and chassis number",
                "the full name and address of the person taking the vehicle",
                "whether you want to keep your registration number",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Registration card or disc"},
                {"name": "Photo ID for each owner"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "The transfer is recorded the same day.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Transfer of Vehicle form (single owner or joint owner version) to the Barbados Licensing Authority.",
                    ],
                },
            ],
        },
        "contact": BLA,
        "related": [
            {"slug": "sell-a-vehicle", "title": "Tell us you have sold a vehicle"},
        ],
    },

    {
        "slug": "change-vehicle-colour",
        "title": "Change the colour of your vehicle",
        "category": "driving-and-transport",
        "description": "Tell the Barbados Licensing Authority before you change the colour of your vehicle.",
        "summary": [
            "If you change the colour of your vehicle, you must tell the Barbados Licensing Authority so they can update your registration.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name and address",
                "the registration number of the vehicle",
                "the current colour and the new colour",
                "the date you plan to make the change",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Registration card or disc"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Approval is given the same day.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Request to Change the Colour of Vehicle form to the Barbados Licensing Authority.",
                    ],
                },
            ],
        },
        "contact": BLA,
    },

    {
        "slug": "change-vehicle-engine",
        "title": "Change the engine in your vehicle",
        "category": "driving-and-transport",
        "description": "Tell the Barbados Licensing Authority after you change the engine in your vehicle.",
        "summary": [
            "You must tell the Barbados Licensing Authority within 30 days of changing the engine in your vehicle.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address, phone number and date of the change",
                "the registration number, chassis number and old engine number",
                "the new engine number",
                "where you got the new engine from",
                "what happened to the old engine (sold, transferred, disposed of, or kept by you)",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Receipt or proof of where the new engine came from"},
                {"name": "Registration card or disc"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Approval is given the same day.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Change of Engine form to the Barbados Licensing Authority.",
                    ],
                },
            ],
        },
        "contact": BLA,
    },

    {
        "slug": "change-vehicle-use",
        "title": "Change how you use your vehicle",
        "category": "driving-and-transport",
        "description": "Tell the Barbados Licensing Authority if you change how your vehicle is used – for example, from private to commercial.",
        "summary": [
            "If you start using your vehicle for a different purpose, for example from private to commercial use, you must apply to the Barbados Licensing Authority for the change to be approved.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name and address",
                "the registration number",
                "the chassis and engine numbers",
                "what the vehicle is being used for now and what it will be used for",
                "a short description of the vehicle",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Registration card or disc"},
                {"name": "Updated insurance certificate", "note": "Your insurance must match the new use."},
            ],
        },
        "fees": "A fee may apply depending on the new vehicle class. Confirm at the Licensing Authority.",
        "how_long": "A decision is usually given within 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person or by post",
                    "content": [
                        "Take the completed Change of Use of Vehicle letter to the Barbados Licensing Authority, or send it to The Pine, East–West Boulevard, St. Michael.",
                    ],
                },
            ],
        },
        "contact": BLA,
    },

    {
        "slug": "vehicle-investigation",
        "title": "Apply for a vehicle investigation",
        "category": "driving-and-transport",
        "description": "Ask the Barbados Licensing Authority to investigate a vehicle that is off the road.",
        "summary": [
            "You can ask the Barbados Licensing Authority to investigate a vehicle that is currently off the road, for example to confirm details for insurance, a sale or a transfer.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address, parish and phone numbers",
                "the registration number, make, model, engine number and chassis number",
                "where the vehicle is being kept",
                "the name and phone numbers of the person to contact at that location",
                "your reason for the investigation",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Proof of ownership", "note": "Registration card or bill of sale."},
                {"name": "Receipt of payment for the investigation fee"},
            ],
        },
        "fees": {
            "items": [
                {"label": "Investigation fee", "amount": "$50 BBD"},
            ],
            "notes": ["Pay at the Barbados Revenue Authority before you apply."],
        },
        "how_long": "An investigation is usually completed within 10 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Application for Vehicle Investigation form to the Barbados Licensing Authority.",
                    ],
                },
            ],
        },
        "contact": BLA,
    },

    {
        "slug": "vanity-plate",
        "title": "Apply for a vanity plate",
        "category": "driving-and-transport",
        "description": "Apply for a personalised vanity number plate for your vehicle.",
        "summary": [
            "You can apply for a personalised number plate (a vanity plate). The Advisory Committee will decide whether to approve your request.",
            "Plates must not be offensive, contentious, of a sensitive or sexual nature, or breach any trademarks.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address, phone and email",
                "your current registration number, if you have one",
                "the wording or numbers you want on the vanity plate",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Proof of payment for the registration fee"},
            ],
        },
        "fees": {
            "items": [
                {"label": "First-time registration", "amount": "$3,000 BBD"},
                {"label": "Annual renewal", "amount": "$1,000 BBD"},
            ],
        },
        "how_long": "The Advisory Committee usually decides within 4 to 6 weeks.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Application for an Approved Vanity Plate form to the Barbados Licensing Authority.",
                    ],
                },
            ],
        },
        "edge_cases": [
            {
                "heading": "If your application is rejected",
                "content": [
                    "The Advisory Committee will give a reason. You can amend your request and apply again."
                ],
            },
        ],
        "contact": BLA,
    },

    {
        "slug": "retain-registration-number",
        "title": "Keep your registration number",
        "category": "driving-and-transport",
        "description": "Ask to keep your vehicle’s registration number after the vehicle is off the road.",
        "summary": [
            "You can ask to keep your registration number for up to one year after the expiry date if your vehicle has been written off, is being repaired or has changed from private to commercial use.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address, phone numbers and email",
                "the registration number you want to keep",
                "the reason: total loss, under repair, or changed from private to commercial",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Proof of the reason", "note": "For example, an insurance write-off letter or a workshop estimate."},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Approval is usually given within 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person or by post",
                    "content": [
                        "Take the completed Retention of Vehicle Registration Number letter to the Barbados Licensing Authority, or send it to The Pine, East–West Boulevard, St. Michael.",
                    ],
                },
            ],
        },
        "contact": BLA,
    },

    {
        "slug": "scrap-or-sell-vehicle-in-parts",
        "title": "Scrap or sell a vehicle in parts",
        "category": "driving-and-transport",
        "description": "Tell the Barbados Licensing Authority that your vehicle has been permanently taken off the road.",
        "summary": [
            "If your vehicle is no longer roadworthy and you plan to scrap it or sell it in parts, you must tell the Barbados Licensing Authority.",
            "Scrapping a vehicle means it has been permanently taken off the road.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address, phone number and email",
                "a short description of the vehicle",
                "the chassis number, engine number and registration number",
                "whether the vehicle will be scrapped or sold in parts",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Registration card or disc"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Confirmation is usually given within 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person or by post",
                    "content": [
                        "Take the completed Scrapping of Vehicle / Selling Vehicle in Parts letter to the Barbados Licensing Authority, or send it to The Pine, East–West Boulevard, St. Michael.",
                    ],
                },
            ],
        },
        "contact": BLA,
    },

    {
        "slug": "graphics-on-vehicle",
        "title": "Request graphics or lettering on a vehicle",
        "category": "driving-and-transport",
        "description": "Get permission before you put graphics or lettering on a vehicle.",
        "summary": [
            "You must get permission from the Barbados Licensing Authority before you put graphics or lettering on a vehicle.",
            "You cannot put graphics on the windows or windscreen.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your name, your business name (if any), address and phone number",
                "exactly what you want to put on the front, rear and sides of the vehicle",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Image of the proposed graphics", "note": "A photograph or drawing."},
                {"name": "Photo ID"},
                {"name": "Registration card or disc"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "A decision is usually given within 10 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Request for Graphics and/or Lettering on Vehicle letter and your image to the Barbados Licensing Authority.",
                    ],
                },
            ],
        },
        "edge_cases": [
            {
                "heading": "What you must not do",
                "content": [
                    "Do not put any graphics or lettering on your vehicle before you get approval."
                ],
            },
        ],
        "contact": BLA,
    },

    {
        "slug": "duty-free-vehicle-concession",
        "title": "Apply for a duty-free vehicle concession",
        "category": "driving-and-transport",
        "description": "Ask to bring in a vehicle without paying customs duty. Available for some individuals and businesses.",
        "summary": [
            "Some people and businesses can bring in a vehicle without paying customs duty. There is one form for individuals and one for businesses.",
            "The Barbados Licensing Authority will let you know once your concession is ready.",
        ],
        "who_can_apply": [
            "an individual who meets the conditions for a duty-free concession (for example, returning national, government employee, person with a disability)",
            "a business authorised by the Government to receive a duty-free concession",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your name and ID number (or your business name)",
                "your address, phone number and email",
                "the registration number, engine number and chassis number of the vehicle",
                "the year and vehicle type",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Approval letter from the relevant ministry or authority"},
                {"name": "Bill of sale for the vehicle"},
                {"name": "Business stamp", "note": "Businesses only."},
            ],
        },
        "fees": "There is no application fee. Duty-free status removes customs duties; other fees may still apply.",
        "how_long": "You will receive a phone call or email when your document is ready to collect.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Request for Duty Free Concession letter (individual or business version) to the Barbados Licensing Authority.",
                    ],
                },
            ],
        },
        "contact": BLA,
    },

    {
        "slug": "alternate-fuel-levy",
        "title": "Pay the Alternate Fuel Levy",
        "category": "driving-and-transport",
        "description": "Pay the monthly or annual levy for vehicles that are not powered by petrol or diesel.",
        "summary": [
            "If your vehicle is not powered by petrol or diesel – for example, an electric or hybrid car – you must pay the Alternate Fuel Levy.",
            "The levy is $25 BBD per month or $300 BBD per year. It has been in place since April 2023.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your vehicle’s registration number",
                "whether you want to pay monthly or annually",
            ],
        },
        "fees": {
            "items": [
                {"label": "Monthly", "amount": "$25 BBD"},
                {"label": "Annually", "amount": "$300 BBD"},
            ],
        },
        "how_long": "Payment is processed the same day.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Pay at the Barbados Revenue Authority. The Licensing Authority will record the payment against your vehicle.",
                    ],
                },
            ],
        },
        "contact": BLA,
    },

    {
        "slug": "international-circulation-permit",
        "title": "Register a vehicle for a temporary stay in Barbados",
        "category": "driving-and-transport",
        "description": "Apply for an International Circulation Permit if you are bringing a vehicle into Barbados for a short stay.",
        "summary": [
            "If you are bringing a vehicle into Barbados temporarily, you must register it for the length of your stay. The Licensing Authority will issue an International Circulation Permit.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address, phone number and email",
                "the length of your planned stay",
                "the registration number, make, model and year of the vehicle",
                "the engine number and chassis number",
                "details of your overseas insurance",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID or passport"},
                {"name": "Overseas registration document for the vehicle"},
                {"name": "Overseas insurance certificate"},
                {"name": "Carnet de Passage or shipping documents", "note": "If applicable."},
            ],
        },
        "fees": "Fees depend on the length of stay and the vehicle class. Confirm at the Licensing Authority.",
        "how_long": "Permits are usually issued within 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Registration of Vehicle for Temporary Stay form and your documents to the Barbados Licensing Authority.",
                    ],
                },
            ],
        },
        "contact": BLA,
    },

    {
        "slug": "business-vehicle-declaration",
        "title": "Make a business declaration for vehicle ownership",
        "category": "driving-and-transport",
        "description": "Companies, partnerships and sole traders must declare who controls a business-owned vehicle.",
        "summary": [
            "Under Section 2 of the Road Traffic (Amendment) Act, 2018-31, every business that owns a vehicle must complete a Barbados Licensing Authority declaration form.",
            "There is one version for each type of business: sole trader, partnership and company.",
        ],
        "who_can_apply": [
            "a sole trader who owns one or more vehicles in the name of the business",
            "a partnership where one or more partners own a vehicle",
            "a company that owns one or more vehicles",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the legal name of the business",
                "the names, addresses and ID numbers of every owner, partner or director",
                "the registration numbers of every vehicle covered",
                "the date of declaration",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Certificate of incorporation or business registration"},
                {"name": "Photo ID for every signatory"},
                {"name": "Business stamp or seal"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "The declaration is recorded the same day.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Declaration Form (sole trader, partnership or company version) to the Barbados Licensing Authority.",
                    ],
                },
            ],
        },
        "contact": BLA,
        "related": [
            {"slug": "register-or-renew-a-vehicle", "title": "Register or renew a vehicle"},
        ],
    },

    {
        "slug": "vehicle-registration-summary",
        "title": "Get a vehicle registration summary",
        "category": "driving-and-transport",
        "description": "Get a one-page summary of a vehicle’s registration status for a sale or import.",
        "summary": [
            "A vehicle registration summary sheet is a one-page document the Barbados Licensing Authority uses to record the registration details of an imported or newly registered vehicle.",
            "You will need one when you import a vehicle, transfer ownership or update key registration details.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the registration type (new import with new number, new or used import with existing number, transfer or other change)",
                "your full name, address and contact details",
                "the make, model, year, chassis number and engine number",
            ],
        },
        "fees": "There is no separate fee, but you may need to pay related registration or import fees.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Vehicle Registration Summary Sheet to the Barbados Licensing Authority along with your other registration documents.",
                    ],
                },
            ],
        },
        "contact": BLA,
    },

    # ---------------------------------------------------------------- #
    # NATIONAL INSURANCE AND BENEFITS
    # ---------------------------------------------------------------- #
    {
        "slug": "old-age-contributory-pension",
        "title": "Claim Old Age Contributory Pension",
        "category": "national-insurance-and-benefits",
        "description": "Claim a pension from the National Insurance Office once you reach pension age.",
        "summary": [
            "If you are 67 or over and have paid enough National Insurance contributions, you can claim the Old Age Contributory Pension.",
            "You can also claim from age 60 at a reduced rate, if you have stopped working.",
        ],
        "who_can_apply": {
            "intro": "You can claim if:",
            "items": [
                "you are 67 or over (full rate)",
                "you are between 60 and 66, are no longer working and choose to claim early at a reduced rate",
                "you have paid the minimum number of NIS contributions",
            ],
        },
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your National Insurance Number",
                "your National Registration Number",
                "your date of birth and address",
                "details of your work history",
                "the bank or credit union account where you want your pension paid",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "National ID card or passport"},
                {"name": "Birth certificate"},
                {"name": "Marriage certificate", "note": "Only if your surname is different from your birth certificate."},
                {"name": "Bank or credit union account header", "note": "So payments can be deposited."},
                {"name": "Most recent payslips", "note": "If you are still working."},
            ],
        },
        "fees": "There is no fee to claim.",
        "how_long": "A first decision usually takes 6 to 12 weeks. Payments are then made every month.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Claim for Old Age Contributory Pension form to the National Insurance Office on Culloden Road.",
                    ],
                },
                {
                    "heading": "If you live overseas",
                    "content": [
                        "Contact the National Insurance Office. They will tell you how to claim from where you live.",
                    ],
                },
            ],
        },
        "edge_cases": [
            {
                "heading": "If your claim is approved",
                "content": [
                    "You will get a letter telling you how much you will be paid and when. Most people are paid by direct deposit – see ‘Set up direct deposit for NIS payments’.",
                    "You will also need to send a Life Certificate every June and December to keep your pension active.",
                ],
            },
        ],
        "contact": NIS,
        "related": [
            {"slug": "nis-direct-deposit", "title": "Set up direct deposit for NIS payments"},
            {"slug": "nis-life-certificate", "title": "Send a life certificate"},
        ],
    },

    {
        "slug": "unemployment-benefit",
        "title": "Claim unemployment benefit",
        "category": "national-insurance-and-benefits",
        "description": "Claim a weekly payment from the National Insurance Office while you look for work.",
        "summary": [
            "If you have lost your job or been laid off, you may be able to claim unemployment benefit from the National Insurance Office.",
            "You must apply within 21 days of your last day at work.",
        ],
        "who_can_apply": {
            "intro": "You can claim if:",
            "items": [
                "you have stopped working for reasons other than misconduct or your own choice",
                "you have made at least 20 weeks of contributions in the 3 years before you stopped working",
                "you are willing and able to take a suitable new job",
                "you are not getting another NIS benefit at the same time",
            ],
        },
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your National Insurance Number and National Registration Number",
                "your last day of work and the reason you stopped working",
                "the name and address of your last employer",
                "your bank or credit union account details",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "National ID card or passport"},
                {"name": "Termination of Services or Layoff Certificate", "note": "Your former employer will give you this. See ‘Get a termination of services or layoff certificate’."},
                {"name": "Your last payslip"},
                {"name": "Bank or credit union account header"},
            ],
        },
        "fees": "There is no fee to claim.",
        "how_long": "A first decision usually takes 4 to 6 weeks. Payments are weekly while you are unemployed, for up to 26 weeks.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Claim for Unemployment Benefit form to the Unemployment Section at the National Insurance Office.",
                    ],
                },
            ],
        },
        "edge_cases": [
            {
                "heading": "If you find work while claiming",
                "content": [
                    "You must tell the National Insurance Office straight away. Payments will stop on the day you start working."
                ],
            },
        ],
        "contact": NIS,
        "related": [
            {"slug": "termination-of-services-certificate", "title": "Get a termination of services or layoff certificate"},
            {"slug": "nis-direct-deposit", "title": "Set up direct deposit for NIS payments"},
        ],
    },

    {
        "slug": "termination-of-services-certificate",
        "title": "Get a termination of services or layoff certificate",
        "category": "national-insurance-and-benefits",
        "description": "Employers complete this form to give to a worker who has stopped working.",
        "summary": [
            "Employers must complete a Termination of Services or Layoff Certificate when an employee stops working, under Regulation 47 of the National Insurance and Social Security Act.",
            "The worker uses this certificate to claim unemployment benefit.",
        ],
        "who_can_apply": [
            "the employer of someone who has stopped working",
            "a worker can ask their former employer for the certificate",
        ],
        "before_you_start": {
            "intro": "The employer will need:",
            "items": [
                "the worker’s name, address, National Insurance Number and National Registration Number",
                "the worker’s date of birth",
                "the dates of employment",
                "the reason the worker stopped working",
                "the worker’s earnings for the last 12 weeks of work",
            ],
        },
        "documents": {
            "intro": "The employer will need to provide:",
            "items": [
                {"name": "Employer’s NIS registration number"},
                {"name": "Payroll records for the last 12 weeks"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Most employers can complete the certificate within a week.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "By post or in person",
                    "content": [
                        "The completed certificate must be returned to the National Insurance Office, or given to the worker to take with them.",
                    ],
                },
            ],
        },
        "contact": NIS,
        "related": [
            {"slug": "unemployment-benefit", "title": "Claim unemployment benefit"},
        ],
    },

    {
        "slug": "nis-direct-deposit",
        "title": "Set up direct deposit for NIS payments",
        "category": "national-insurance-and-benefits",
        "description": "Have your National Insurance benefit paid directly into your bank or credit union account.",
        "summary": [
            "You can have your National Insurance benefit paid directly into your bank or credit union account.",
            "You will need to give us a copy of the header from your account so we know your account number and name match.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your National Insurance Number and claim number (if you have one)",
                "your full name, address and phone number",
                "the name of your bank or credit union",
                "your account number and branch",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "National ID card or passport"},
                {"name": "Bank or credit union account header", "note": "Showing your name and account number. You can usually get this from your branch or from online banking."},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Direct deposit is usually active within 1 to 2 payment cycles.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Direct Deposit Form to the National Insurance Office.",
                    ],
                },
            ],
        },
        "contact": NIS,
    },

    {
        "slug": "nis-educational-status",
        "title": "Confirm a student’s educational status for NIS",
        "category": "national-insurance-and-benefits",
        "description": "Used to keep paying a Survivors’ or Death Benefit to a student aged 16 to 25.",
        "summary": [
            "If you are getting a Survivors’ or Death Benefit and the person under 25 is still in full-time education, you must send an Educational Status Form so payments continue.",
        ],
        "before_you_start": {
            "intro": "You will need:",
            "items": [
                "the student’s name, NIS number and date of birth",
                "the name and address of the school, college or university",
                "the course the student is on and when it ends",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "A signed and stamped letter from the school", "note": "Confirming the student is enrolled in full-time education."},
                {"name": "National ID for the parent or guardian"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Confirmation is recorded within 2 weeks. You should send a new form for each new academic year.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person or by post",
                    "content": [
                        "Take or send the completed Educational Status Form to the National Insurance Office.",
                    ],
                },
            ],
        },
        "contact": NIS,
    },

    {
        "slug": "nis-life-certificate",
        "title": "Send a life certificate",
        "category": "national-insurance-and-benefits",
        "description": "People claiming an NIS pension must confirm they are alive every six months.",
        "summary": [
            "If you are claiming a pension from the National Insurance Office, you must send a Life Certificate every June and December.",
            "This is how the National Insurance Office knows to keep paying you.",
        ],
        "before_you_start": {
            "intro": "You will need:",
            "items": [
                "your full name and NIS number",
                "your address",
                "an approved witness who can confirm you are alive",
            ],
        },
        "documents": {
            "intro": "The form must be signed by you and stamped or signed by an approved witness, for example:",
            "items": [
                "a Justice of the Peace",
                "a Notary Public",
                "a Minister of Religion",
                "a Permanent Secretary",
                "an officer at the Barbados Consulate or High Commission",
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Send the certificate by 30 June and 31 December each year. Payments may pause if it does not arrive in time.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "By post or in person",
                    "content": [
                        "Take or send the completed Life Certificate to the National Insurance Office, Culloden Road, St. Michael.",
                    ],
                },
            ],
        },
        "contact": NIS,
    },

    {
        "slug": "self-employed-contributions-certificate",
        "title": "Get a Contributions Payment Certificate (self-employed)",
        "category": "national-insurance-and-benefits",
        "description": "Self-employed people can ask for a certificate showing the NIS contributions they have paid.",
        "summary": [
            "If you are self-employed and you need proof of the National Insurance contributions you have paid, you can ask for a Contributions Payment Certificate.",
            "You might need it for a loan, a visa or a tax return.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your National Insurance Number and National Registration Number",
                "your full name and address",
                "the period the certificate should cover",
                "what you need it for (so the right wording is used)",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Past NIS payment receipts", "note": "If you have them, to help us match your records."},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Certificates are usually ready within 10 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person or by post",
                    "content": [
                        "Take or send the completed Contributions Payment Certificate form to the National Insurance Office.",
                    ],
                },
            ],
        },
        "contact": NIS,
    },

    {
        "slug": "nis-online-employee",
        "title": "Register for Online Social Security (employee)",
        "category": "national-insurance-and-benefits",
        "description": "Open an online account with the NIS so you can check your record, change your details and apply for benefits.",
        "summary": [
            "You can use the NIS Online Social Security Service to check your contributions, update your details and apply for some benefits online.",
            "You only need to register once.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name and date of birth",
                "your National Insurance Number",
                "your National Registration Number",
                "your home address and parish",
                "an email address and phone number",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Valid photo ID", "note": "Barbados ID card or passport."},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Your account is usually active within 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Online Social Security Service Registration form and your ID to the National Insurance Office.",
                    ],
                },
            ],
        },
        "contact": NIS,
        "related": [
            {"slug": "nis-online-employer", "title": "Register for Online Social Security (employer)"},
        ],
    },

    {
        "slug": "nis-online-employer",
        "title": "Register for Online Social Security (employer)",
        "category": "national-insurance-and-benefits",
        "description": "Open an online employer account with the NIS so you can pay contributions and report new hires.",
        "summary": [
            "Employers can use the NIS Online Social Security Service to pay contributions, submit returns and report new hires online.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your business name",
                "your employer’s NIS number",
                "your business registration number",
                "the address and parish of the business",
                "an email address and phone number for an authorised contact",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Certificate of incorporation or business registration"},
                {"name": "Photo ID for the authorised contact"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Your account is usually active within 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Online Social Security Service Registration (Employer) form to the National Insurance Office.",
                    ],
                },
            ],
        },
        "contact": NIS,
    },

    {
        "slug": "dp10-contributions-certificate",
        "title": "Get a DP-10 contributions certificate",
        "category": "national-insurance-and-benefits",
        "description": "A summary of the National Insurance contributions paid for an employee during a tax year.",
        "summary": [
            "The DP-10 is a National Insurance Contributions Certificate. Employers issue one to each employee at the end of the tax year so the employee can use it for their tax return.",
            "If you have lost a DP-10, you can ask your employer or the NIS for a replacement.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the employer’s registration number and business name",
                "the employee’s National Insurance Number",
                "the tax year the certificate covers",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Your last payslip", "note": "If you have one."},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Replacements are usually ready within 10 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Through your employer",
                    "content": [
                        "Ask your employer for a DP-10. Employers must issue one for each employee every tax year.",
                    ],
                },
                {
                    "heading": "Directly from the NIS",
                    "content": [
                        "If you cannot get a copy from your employer, ask the National Insurance Office for a replacement.",
                    ],
                },
            ],
        },
        "contact": NIS,
    },

    # ---------------------------------------------------------------- #
    # FIREARMS
    # ---------------------------------------------------------------- #
    {
        "slug": "firearm-licence",
        "title": "Apply for a firearm licence",
        "category": "firearms",
        "description": "Apply for a licence to have, use or carry a firearm in Barbados.",
        "summary": [
            "Under the Firearms Act, you must have a licence before you can have, use or carry a firearm in Barbados.",
            "Applications are reviewed by the Commissioner of Police.",
        ],
        "who_can_apply": [
            "anyone over 18 who is not legally barred from holding a firearm licence",
            "people who can show a clear reason for needing a firearm – for example, sport, hunting, or work",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address, date of birth and place of birth",
                "your nationality and occupation",
                "your reason for needing a firearm",
                "the type of firearm you want, including make, model and calibre",
                "where you will store the firearm",
                "the names and addresses of two referees",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Two passport-size photographs"},
                {"name": "Photo ID", "note": "Barbados ID card or passport."},
                {"name": "Police record certificate", "note": "Recent (within 6 months)."},
                {"name": "Proof of safe storage", "note": "For example, a photograph of an approved gun safe."},
                {"name": "Two character references", "note": "From people who have known you for at least 5 years."},
                {"name": "Proof of payment of the application fee"},
            ],
        },
        "fees": "Fees vary by firearm type. Pay at the Barbados Revenue Authority before you apply.",
        "how_long": "A decision usually takes 8 to 12 weeks.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Hand the completed Form A Application for a Licence to Have, Use or Carry a Firearm in to Police Headquarters, Roebuck Street, St. Michael.",
                    ],
                },
            ],
        },
        "edge_cases": [
            {
                "heading": "If you have a criminal record",
                "content": [
                    "The Commissioner of Police will consider every application on its merits. A criminal record does not always mean your application will be refused.",
                ],
            },
            {
                "heading": "Renewals",
                "content": [
                    "A firearm licence is valid for one year. You will need to renew it before the expiry date.",
                ],
            },
        ],
        "contact": POLICE,
    },

    {
        "slug": "firearm-import-export-licence",
        "title": "Apply for a licence to import or export a firearm",
        "category": "firearms",
        "description": "Apply to bring a firearm into Barbados or send one out of the country.",
        "summary": [
            "Under the Firearms Act, you must have a licence before you can import a firearm into Barbados or export one out of the country.",
        ],
        "who_can_apply": [
            "an individual with a current firearm licence",
            "a registered firearms dealer or gunsmith",
            "a shooting club with a club licence",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name and address",
                "the firearm’s make, model, calibre and serial number",
                "the country it is coming from or going to",
                "the name and address of the supplier or receiver",
                "the date you plan to bring it in or send it out",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Your existing firearm licence"},
                {"name": "Bill of sale or invoice for the firearm"},
                {"name": "Two passport-size photographs"},
                {"name": "Proof of payment of the application fee"},
            ],
        },
        "fees": "Fees depend on the firearm type. Pay at the Barbados Revenue Authority.",
        "how_long": "A decision usually takes 6 to 10 weeks.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Hand the completed Form B Application for a Licence to Import or Export a Firearm in to Police Headquarters, Roebuck Street, St. Michael.",
                    ],
                },
            ],
        },
        "contact": POLICE,
        "related": [
            {"slug": "firearm-licence", "title": "Apply for a firearm licence"},
        ],
    },

    {
        "slug": "firearms-dealer-licence",
        "title": "Apply for a firearms dealer, gunsmith or collector’s licence",
        "category": "firearms",
        "description": "Apply for a licence to operate as a firearms dealer, a gunsmith or a collector.",
        "summary": [
            "Under the Firearms Act, you must have a special licence to sell firearms, repair them as a gunsmith or hold a collection.",
            "There are different parts of the form for individuals and companies.",
        ],
        "who_can_apply": [
            "an individual over 21 who wants to be a registered dealer, gunsmith or collector",
            "a company that wants to deal in firearms",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name (or the company’s name)",
                "your business address and storage location",
                "the type of activity (dealer, gunsmith or collector)",
                "the names of every director or partner of the company",
                "the address of every place you will store firearms",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Two passport-size photographs of every applicant"},
                {"name": "Photo ID for every applicant"},
                {"name": "Police record certificate for every applicant"},
                {"name": "Certificate of incorporation", "note": "For company applications."},
                {"name": "Proof of approved storage"},
                {"name": "Proof of payment of the application fee"},
            ],
        },
        "fees": "Fees vary by category. Pay at the Barbados Revenue Authority.",
        "how_long": "A decision usually takes 10 to 14 weeks.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Hand the completed Form C Application for a Firearms Dealer, Gunsmith or Collector’s Licence in to Police Headquarters, Roebuck Street, St. Michael.",
                    ],
                },
            ],
        },
        "contact": POLICE,
    },

    {
        "slug": "shooting-club-licence",
        "title": "Apply for a shooting club licence",
        "category": "firearms",
        "description": "Apply for a licence so a shooting club can operate in Barbados.",
        "summary": [
            "Under Section 12 of the Firearms Act, every shooting club must hold a current licence.",
        ],
        "who_can_apply": [
            "a registered shooting club with at least one approved range",
            "the secretary or chairperson of the club",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the full name of the club",
                "the address of the club and every range",
                "the names of every officer and committee member",
                "the names of every member who will use firearms at the club",
                "the types of firearms the club uses",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Club constitution"},
                {"name": "List of members with their firearm licence details"},
                {"name": "Range safety plan and inspection report"},
                {"name": "Two passport-size photographs of the club secretary"},
                {"name": "Proof of payment of the application fee"},
            ],
        },
        "fees": "Pay the licence fee at the Barbados Revenue Authority before you apply.",
        "how_long": "A decision usually takes 10 to 14 weeks.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Hand the completed Form D Application for a Shooting Club Licence in to Police Headquarters, Roebuck Street, St. Michael.",
                    ],
                },
            ],
        },
        "contact": POLICE,
    },

    # ---------------------------------------------------------------- #
    # SAFETY AND PUBLIC EVENTS
    # ---------------------------------------------------------------- #
    {
        "slug": "march-or-motorcade-permit",
        "title": "Apply for a march, walk, run or motorcade permit",
        "category": "safety-and-public-events",
        "description": "Get police permission to hold a march, walk, run or motorcade on public roads.",
        "summary": [
            "If you want to hold a march, walk, run or motorcade on a public road in Barbados, you must apply to The Royal Barbados Police Force for permission.",
            "Apply at least 4 weeks before the event so the police can plan road closures and traffic management.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the name and address of the applicant or organisation",
                "the type of event (march, walk, run or motorcade)",
                "the date and start and end times",
                "the planned route, including assembly and dispersal points",
                "the expected number of participants and vehicles",
                "the names of the marshals or organisers",
                "the reason for the event",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID for the lead applicant"},
                {"name": "A map of the route"},
                {"name": "Letter of support from the organising body", "note": "If the applicant is acting on behalf of an organisation."},
            ],
        },
        "fees": "There is no application fee.",
        "how_long": "A decision usually takes 2 to 3 weeks. Apply at least 4 weeks before the event.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Hand the completed Application for March, Walk, Run or Motorcade form in to Police Headquarters, Roebuck Street, St. Michael.",
                    ],
                },
            ],
        },
        "edge_cases": [
            {
                "heading": "If your route changes",
                "content": [
                    "Tell the Police Headquarters as soon as you know. A new approval may be needed.",
                ],
            },
        ],
        "contact": POLICE,
    },

    {
        "slug": "police-accident-report",
        "title": "Get a police accident report",
        "category": "safety-and-public-events",
        "description": "Get a copy of the police report for a road traffic accident.",
        "summary": [
            "If you were involved in a road traffic accident in Barbados, you can ask for a copy of the police report. You will usually need it for an insurance claim.",
        ],
        "who_can_apply": [
            "the driver, owner or named insured of a vehicle involved in the accident",
            "an insurance company or attorney acting for someone involved",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your name, address, phone number and email",
                "the date and time of the accident",
                "the place of the accident",
                "the registration numbers of the vehicles involved",
                "your reason for asking for the report",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Proof of relationship", "note": "For example, the registration card if you are the owner, or a letter of authority if you are acting for someone else."},
                {"name": "Receipt of payment of the fee"},
            ],
        },
        "fees": {
            "items": [
                {"label": "Police accident report fee", "amount": "$50 BBD"},
            ],
            "notes": ["Pay at the Barbados Revenue Authority before you apply."],
        },
        "how_long": "Reports are usually ready within 4 to 6 weeks.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Hand the completed Application for Police Accident Report form in to Police Headquarters, James Street, St. Michael.",
                    ],
                },
            ],
        },
        "contact": POLICE,
    },

    {
        "slug": "loud-music-permit",
        "title": "Apply for a loud music permit",
        "category": "safety-and-public-events",
        "description": "Get police permission to play loud music at an event or in a public place.",
        "summary": [
            "If you want to play loud music at an event, you must apply to The Royal Barbados Police Force for a permit.",
            "Apply at least 2 weeks before the event.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your name, address and phone number",
                "the date and start and end times of the event",
                "the address where the music will be played",
                "the type of event",
                "the expected number of people",
                "what you have done to limit noise to neighbours",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Proof of permission from the property owner", "note": "If you do not own the property."},
            ],
        },
        "fees": "Fees may apply. Confirm at the Police Headquarters.",
        "how_long": "A decision usually takes 5 to 10 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Hand the completed Application for Police Loud Music Permit in to Police Headquarters, Roebuck Street, St. Michael.",
                    ],
                },
            ],
        },
        "edge_cases": [
            {
                "heading": "If your event runs after midnight",
                "content": [
                    "You will need to say what time the music will end and how you will let your neighbours know about the event."
                ],
            },
        ],
        "contact": POLICE,
    },
]
