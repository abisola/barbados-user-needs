"""Business, companies, trade, exports and imports."""

from .catalogue import CAFFAIRS, BIDC

CUSTOMS = {
    "agency": "Barbados Customs and Excise Department",
    "address": "Customs House, Bridge Street\nBridgetown, St. Michael",
    "phone": ["(246) 535-1300"],
    "email": "customs@barbados.gov.bb",
    "hours": "Open Monday to Friday: 8:15am to 4:30pm",
}

SERVICES_BUSINESS = [

    # ---------------------------------------------------------------- #
    # BUSINESS AND COMPANIES
    # ---------------------------------------------------------------- #
    {
        "slug": "register-a-domestic-company",
        "title": "Register a domestic company",
        "category": "business-and-companies",
        "description": "Set up a Barbadian company under the Companies Act, Cap. 308.",
        "summary": [
            "If you want to set up a company that operates in Barbados, you must register it with the Corporate Affairs and Intellectual Property Office (CAIPO).",
            "A Barbadian attorney-at-law will need to sign the declaration form on your behalf.",
        ],
        "who_can_apply": [
            "anyone over 18 who wants to set up a company in Barbados",
            "a Barbadian attorney-at-law acting on behalf of the applicant",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the name of the company (and one or two alternatives in case it is taken)",
                "the type of business the company will do",
                "the address of the registered office",
                "the names, addresses and dates of birth of every director",
                "the names and addresses of every shareholder",
                "the share structure of the company",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Articles of incorporation", "note": "Signed by your attorney-at-law."},
                {"name": "Notice of address of registered office (Form 4)"},
                {"name": "Notice of directors (Form 9)"},
                {"name": "Declaration form signed by your attorney-at-law"},
                {"name": "Photo ID for every director"},
                {"name": "Name reservation slip", "note": "Get this first from CAIPO."},
                {"name": "Proof of payment of the registration fee"},
            ],
        },
        "fees": {
            "items": [
                {"label": "Name reservation", "amount": "$25 BBD"},
                {"label": "Incorporation", "amount": "$750 BBD"},
            ],
        },
        "how_long": "A decision usually takes 5 to 10 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Through an attorney-at-law",
                    "content": [
                        "A Barbadian attorney-at-law will prepare the documents and file them with the Corporate Affairs and Intellectual Property Office.",
                    ],
                },
            ],
        },
        "contact": CAFFAIRS,
        "related": [
            {"slug": "register-an-ibc", "title": "Register an International Business Company"},
            {"slug": "register-a-non-profit-company", "title": "Register a non-profit company"},
        ],
    },

    {
        "slug": "register-an-ibc",
        "title": "Register an International Business Company",
        "category": "business-and-companies",
        "description": "Set up an International Business Company (IBC) in Barbados.",
        "summary": [
            "An International Business Company (IBC) does its business outside Barbados. To register one, you need both a declaration from a Barbadian attorney-at-law and a Government Form 1 application.",
            "An IBC must keep its records in Barbados, hold board meetings here and have a local registered office.",
        ],
        "who_can_apply": [
            "anyone who wants to set up an International Business Company in Barbados",
            "a Barbadian attorney-at-law acting on behalf of the applicant",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the proposed name of the company (and alternatives)",
                "the type of international business it will do",
                "the name and address of the proposed registered office in Barbados",
                "the names, addresses and nationalities of every director",
                "the names and addresses of every shareholder",
                "the share structure",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Form 1 Application for a Licence as an International Business Company"},
                {"name": "Articles of incorporation"},
                {"name": "Declaration form signed by your attorney-at-law"},
                {"name": "Police record certificates for every director and shareholder"},
                {"name": "Business plan", "note": "A short summary of the planned activities."},
                {"name": "Photo ID for every director and shareholder"},
                {"name": "Proof of payment of the application fee"},
            ],
        },
        "fees": {
            "items": [
                {"label": "Incorporation", "amount": "$750 BBD"},
                {"label": "Annual IBC licence", "amount": "$1,000 BBD"},
            ],
        },
        "how_long": "A decision usually takes 4 to 8 weeks.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Through an attorney-at-law",
                    "content": [
                        "A Barbadian attorney-at-law will file the documents with the International Business Unit and the Corporate Affairs and Intellectual Property Office.",
                    ],
                },
            ],
        },
        "contact": CAFFAIRS,
    },

    {
        "slug": "register-a-non-profit-company",
        "title": "Register a non-profit company",
        "category": "business-and-companies",
        "description": "Set up a Barbadian non-profit company under the Companies Act, Cap. 308.",
        "summary": [
            "A non-profit company exists for a charitable, religious, educational or other public good purpose. You must register it with the Corporate Affairs and Intellectual Property Office.",
            "Any income or assets a non-profit company has must be used for its stated purpose, not paid out to members.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the proposed name of the company",
                "the charitable or public-good purpose of the company",
                "the address of the registered office",
                "the names, addresses and dates of birth of every director",
                "the names of every founding member",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Articles of incorporation for a non-profit company"},
                {"name": "Declaration form signed by your attorney-at-law"},
                {"name": "Notice of directors and registered office"},
                {"name": "Photo ID for every director"},
                {"name": "Proof of payment of the registration fee"},
            ],
        },
        "fees": "There is a reduced incorporation fee for non-profit companies. Confirm at CAIPO.",
        "how_long": "A decision usually takes 5 to 10 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Through an attorney-at-law",
                    "content": [
                        "A Barbadian attorney-at-law will prepare the documents and file them with CAIPO.",
                    ],
                },
            ],
        },
        "contact": CAFFAIRS,
    },

    {
        "slug": "articles-of-reincorporation",
        "title": "File articles of reincorporation",
        "category": "business-and-companies",
        "description": "Re-state a company under the current Companies Act of Barbados.",
        "summary": [
            "Articles of reincorporation are filed under Section 355.5 of the Companies Act to bring a company under the current Act.",
            "You will need this if your company was set up under an older law and needs to be brought up to date.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the current name and company number",
                "the maximum number of shares the company can issue",
                "any restrictions on issuing or transferring shares",
                "the minimum and maximum number of directors",
                "any restrictions on the business the company can do",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Resolution of directors approving the reincorporation"},
                {"name": "Notice of registered office and directors"},
                {"name": "Updated by-laws"},
                {"name": "Photo ID for the signing officer"},
                {"name": "Proof of payment of the filing fee"},
            ],
        },
        "fees": "Filing fees are set by CAIPO. Confirm before you submit.",
        "how_long": "A decision usually takes 4 to 6 weeks.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Through an attorney-at-law",
                    "content": [
                        "A Barbadian attorney-at-law will file the articles with CAIPO.",
                    ],
                },
            ],
        },
        "contact": CAFFAIRS,
    },

    {
        "slug": "external-company-cancellation",
        "title": "Cancel an external company",
        "category": "business-and-companies",
        "description": "Tell CAIPO that an external (foreign) company is no longer doing business in Barbados.",
        "summary": [
            "Under Section 338 of the Companies Act, an external company must tell the Corporate Affairs and Intellectual Property Office when it stops doing business in Barbados.",
            "The notice of cancellation removes the company from the register of external companies.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the name and company number",
                "the address of the registered office in Barbados",
                "the names and addresses of the directors",
                "the date the company stopped doing business in Barbados",
                "the reason for cancellation",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Resolution of directors approving cancellation"},
                {"name": "Statement of accounts up to the cancellation date"},
                {"name": "Photo ID for the signing officer"},
                {"name": "Proof of payment of the filing fee"},
            ],
        },
        "fees": "Filing fees are set by CAIPO. Confirm before you submit.",
        "how_long": "A decision usually takes 4 to 6 weeks.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "Through an attorney-at-law",
                    "content": [
                        "A Barbadian attorney-at-law will file the notice with CAIPO.",
                    ],
                },
            ],
        },
        "contact": CAFFAIRS,
    },

    {
        "slug": "register-an-agent",
        "title": "Register a corporate agent",
        "category": "business-and-companies",
        "description": "Register or update the details of an agent acting for a Barbadian company.",
        "summary": [
            "Companies can register an agent who will act on their behalf with the Corporate Affairs and Intellectual Property Office.",
            "Use this form to register a new agent, change the details of an existing agent, or update the agent’s address or contact information.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the agent number, if you have one",
                "the agent’s name, address, phone number, fax and email",
                "the name and number of the company the agent is acting for",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Letter of authority from the company"},
                {"name": "Photo ID for the agent"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Updates are usually recorded within 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Registered Agent Application Form to the Corporate Affairs and Intellectual Property Office at Baobab Tower, Warrens.",
                    ],
                },
            ],
        },
        "contact": CAFFAIRS,
    },

    {
        "slug": "geographical-indications-agent",
        "title": "Authorise a geographical indications agent",
        "category": "business-and-companies",
        "description": "Appoint an agent to act for you in a geographical indications matter under Cap. 320.",
        "summary": [
            "If you are bringing or responding to a geographical indications matter under the Geographical Indications Act, Cap. 320, you can appoint an agent to act for you.",
            "The agent will then handle all correspondence with the Intellectual Property Office on your behalf.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name and address (or the name and address of the appointing company)",
                "the name and address of the agent",
                "the matter or proceeding being authorised",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID for the signing party"},
                {"name": "Board resolution", "note": "If the appointing party is a company."},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Authorisations are recorded within 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person or by post",
                    "content": [
                        "Take or send the completed Form of Authorisation of Agent to the Corporate Affairs and Intellectual Property Office.",
                    ],
                },
            ],
        },
        "contact": CAFFAIRS,
    },

    {
        "slug": "url-declaration",
        "title": "Make a URL ownership declaration",
        "category": "business-and-companies",
        "description": "Declare that you legally own a website domain (URL) registered to your company.",
        "summary": [
            "If your business owns a website domain (URL) and you need to prove it, you can make a URL declaration before an attorney-at-law.",
            "The declaration shows that the URL is registered to your business and is legally and beneficially owned by it.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name and address",
                "the URL you are declaring (for example, www.yourbusiness.bb)",
                "the legal name of the company that owns the URL",
                "the date the URL was registered",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID"},
                {"name": "Proof of URL registration", "note": "A WHOIS print-out or registrar receipt."},
            ],
        },
        "fees": "No government fee. Your attorney-at-law may charge for witnessing the declaration.",
        "how_long": "Same day with your attorney-at-law.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "With an attorney-at-law",
                    "content": [
                        "Make the declaration before a Barbadian attorney-at-law, who will witness your signature and stamp the document.",
                    ],
                },
            ],
        },
        "contact": CAFFAIRS,
    },

    {
        "slug": "financial-declaration",
        "title": "Make a financial declaration",
        "category": "business-and-companies",
        "description": "Public officials and other named people must declare their assets, liabilities and income every year.",
        "summary": [
            "Some public officials, directors and senior officers must make a financial declaration each year.",
            "Your declaration covers your assets, your liabilities, your income, the same for your spouse and minor children, and any gifts you received.",
        ],
        "who_can_apply": [
            "people in public office named under the Prevention of Corruption Act",
            "directors and senior officers of state-owned enterprises",
            "other people the law says must declare",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, address and the parish you live in",
                "details of every property you own, in Barbados and overseas",
                "the value and account numbers of your bank, credit union and investment accounts",
                "details of your vehicles and other valuable property",
                "every loan, mortgage and debt you have",
                "your income from every source",
                "the same details for your spouse and any minor children",
                "any gifts of $500 BBD or more you received in the year",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Bank, credit union and investment statements"},
                {"name": "Loan and mortgage statements"},
                {"name": "Payslips or tax records"},
                {"name": "Property valuations or title deeds"},
                {"name": "Photo ID"},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "Submit your declaration by the date in the notice you received.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take your sworn declaration to the Integrity Commission or other office named in the law you are declaring under.",
                    ],
                },
            ],
        },
        "edge_cases": [
            {
                "heading": "If you cannot get all the details in time",
                "content": [
                    "Tell the Commission in writing. Late or incomplete declarations may be referred for investigation.",
                ],
            },
        ],
        "contact": CAFFAIRS,
    },

    # ---------------------------------------------------------------- #
    # TRADE, EXPORTS AND IMPORTS
    # ---------------------------------------------------------------- #
    {
        "slug": "caricom-certificate-of-origin",
        "title": "Apply for a CARICOM certificate of origin",
        "category": "trade-exports-and-imports",
        "description": "Get a certificate showing that your goods qualify for CARICOM Single Market preferential treatment.",
        "summary": [
            "If you are exporting goods to another CARICOM country and you want them to qualify for preferential treatment, you will need a CARICOM Common Market combined declaration by exporter and certificate of origin.",
            "Certificates are issued by the Barbados Investment and Development Corporation (BIDC).",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the exporter’s name and address",
                "the consignee’s name and address",
                "the country of issue, origin and destination",
                "transport information (vessel, aircraft, place of loading)",
                "your exporter reference number",
                "details of the goods (marks, numbers, packages, description)",
                "the HS tariff number, gross weight and value",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Commercial invoice"},
                {"name": "Bill of lading or airway bill"},
                {"name": "Packing list"},
                {"name": "Proof that the goods meet CARICOM rules of origin"},
            ],
        },
        "fees": "Confirm fees with BIDC.",
        "how_long": "Certificates are usually issued within 3 to 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed CARICOM Common Market combined declaration by exporter and certificate of origin to BIDC at Pelican House.",
                    ],
                },
            ],
        },
        "contact": BIDC,
        "related": [
            {"slug": "bidc-certificate-of-origin", "title": "Apply for a BIDC certificate of origin"},
            {"slug": "caricom-colombia-certificate", "title": "Apply for a CARICOM–Colombia certificate of origin"},
            {"slug": "caricom-costa-rica-certificate", "title": "Apply for a CARICOM–Costa Rica certificate of origin"},
            {"slug": "caricom-dominican-republic-certificate", "title": "Apply for a CARICOM–Dominican Republic certificate of origin"},
            {"slug": "eur1-movement-certificate", "title": "Apply for an EUR.1 movement certificate"},
        ],
    },

    {
        "slug": "caricom-colombia-certificate",
        "title": "Apply for a CARICOM–Colombia certificate of origin",
        "category": "trade-exports-and-imports",
        "description": "Get a certificate of origin under the CARICOM–Colombia trade agreement.",
        "summary": [
            "Use this certificate of origin if you are exporting goods to Colombia under the Agreement on Trade, Economic and Technical Cooperation between CARICOM and the Government of the Republic of Colombia.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the exporter’s name and address",
                "the consignee’s name and address in Colombia",
                "the country of origin, country of destination and country of issue",
                "transport information (vessel, aircraft, place of loading)",
                "your exporter reference number",
                "details of the goods, HS tariff number, value and gross weight",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Commercial invoice"},
                {"name": "Bill of lading or airway bill"},
                {"name": "Packing list"},
                {"name": "Proof that the goods meet the CARICOM–Colombia rules of origin"},
            ],
        },
        "fees": "Confirm fees with BIDC.",
        "how_long": "Certificates are usually issued within 3 to 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed CARICOM–Colombia certificate of origin to BIDC at Pelican House.",
                    ],
                },
            ],
        },
        "contact": BIDC,
    },

    {
        "slug": "caricom-costa-rica-certificate",
        "title": "Apply for a CARICOM–Costa Rica certificate of origin",
        "category": "trade-exports-and-imports",
        "description": "Get a certificate of origin under the CARICOM–Costa Rica Free Trade Agreement.",
        "summary": [
            "Use this certificate of origin if you are exporting goods to Costa Rica under the Free Trade Agreement between the Caribbean Community (CARICOM) and Costa Rica.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the exporter’s name and address",
                "the producer’s name and address, if different",
                "the consignee’s name and address",
                "the period the certificate will cover",
                "transport information and route",
                "the goods description, HS tariff code, origin criterion and value",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Commercial invoice"},
                {"name": "Bill of lading or airway bill"},
                {"name": "Packing list"},
                {"name": "Proof that the goods meet the CARICOM–Costa Rica rules of origin"},
            ],
        },
        "fees": "Confirm fees with BIDC.",
        "how_long": "Certificates are usually issued within 3 to 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed CARICOM–Costa Rica certificate of origin to BIDC at Pelican House.",
                    ],
                },
            ],
        },
        "contact": BIDC,
    },

    {
        "slug": "caricom-dominican-republic-certificate",
        "title": "Apply for a CARICOM–Dominican Republic certificate of origin",
        "category": "trade-exports-and-imports",
        "description": "Get a certificate of origin under the CARICOM–Dominican Republic Free Trade Agreement.",
        "summary": [
            "Use this certificate of origin if you are exporting goods to the Dominican Republic under the Free Trade Agreement between the Caribbean Community (CARICOM) and the Dominican Republic.",
            "The form is bilingual – the Spanish version says ‘Certificado de Origen’.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the exporter’s name and address",
                "the importer or consignee’s name and address",
                "the goods description, HS code, value, quantity and country of origin",
                "transport information",
                "the period the certificate covers",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Commercial invoice"},
                {"name": "Bill of lading or airway bill"},
                {"name": "Packing list"},
                {"name": "Proof that the goods meet the CARICOM–Dominican Republic rules of origin"},
            ],
        },
        "fees": "Confirm fees with BIDC.",
        "how_long": "Certificates are usually issued within 3 to 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed CARICOM–Dominican Republic certificate of origin (Certificado de Origen) to BIDC at Pelican House.",
                    ],
                },
            ],
        },
        "contact": BIDC,
    },

    {
        "slug": "eur1-movement-certificate",
        "title": "Apply for an EUR.1 movement certificate",
        "category": "trade-exports-and-imports",
        "description": "Get an EUR.1 certificate to claim preferential treatment when exporting to the European Union.",
        "summary": [
            "An EUR.1 movement certificate proves that goods you are exporting to the European Union (or other partner countries) qualify for preferential customs treatment under a trade agreement.",
            "Certificates are issued by the Barbados Customs and Excise Department.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the exporter’s and consignee’s name, full address and country",
                "the country, group of countries or territory of origin",
                "the country, group of countries or territory of destination",
                "transport details and the route",
                "marks and numbers, description of the goods, packages and HS tariff code",
                "gross weight or other quantity",
                "invoice number and the basis for claiming origin",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Commercial invoice"},
                {"name": "Bill of lading or airway bill"},
                {"name": "Packing list"},
                {"name": "Supplier’s declaration or proof of origin", "note": "Showing that the goods meet the rules of origin."},
            ],
        },
        "fees": "Confirm fees with the Customs and Excise Department.",
        "how_long": "Certificates are usually issued within 3 to 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed EUR.1 movement certificate to the Customs and Excise Department in Bridgetown.",
                    ],
                },
            ],
        },
        "contact": CUSTOMS,
    },

    {
        "slug": "bidc-certificate-of-origin",
        "title": "Apply for a BIDC certificate of origin",
        "category": "trade-exports-and-imports",
        "description": "Apply for a Barbados Investment and Development Corporation certificate of origin for any export.",
        "summary": [
            "The BIDC certificate of origin is the general form for goods exported from Barbados where there is no specific trade-agreement certificate.",
            "Use this form if no other certificate of origin (CARICOM, CARICOM–Colombia, CARICOM–Costa Rica, CARICOM–Dominican Republic, EUR.1) fits.",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "the manufacturer’s name, address, phone and email",
                "the exporter’s details, if different",
                "the consignee’s name and address",
                "details of the goods (description, packages, weight, value)",
                "the country of origin and destination",
                "transport information",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Commercial invoice"},
                {"name": "Bill of lading or airway bill"},
                {"name": "Packing list"},
                {"name": "Proof that the goods were made in Barbados"},
            ],
        },
        "fees": "Confirm fees with BIDC.",
        "how_long": "Certificates are usually issued within 3 to 5 working days.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "In person",
                    "content": [
                        "Take the completed Application for Certificate of Origin (Part A: Manufacturer Information) to BIDC at Pelican House.",
                    ],
                },
            ],
        },
        "contact": BIDC,
    },

    {
        "slug": "csme-complaint",
        "title": "Make a CSME point of entry complaint",
        "category": "trade-exports-and-imports",
        "description": "Tell CARICOM if you were treated unfairly at a port of entry or departure under the CSME.",
        "summary": [
            "If you are a CARICOM national and you were treated unfairly at a port of entry, departure or inland post in any CARICOM country, you can make a complaint under the Caribbean Single Market and Economy (CSME).",
            "The complaint is reviewed by the CSME Unit.",
        ],
        "who_can_apply": [
            "a CARICOM national who was treated unfairly at a port",
            "someone acting on behalf of a CARICOM national",
        ],
        "before_you_start": {
            "intro": "You will need to know:",
            "items": [
                "your full name, nationality and passport number",
                "your address, telephone, email and sex",
                "the date and place of the incident",
                "a short, plain-language account of what happened",
                "the names or badge numbers of any officials, if you have them",
            ],
        },
        "documents": {
            "intro": "Bring with you:",
            "items": [
                {"name": "Photo ID or passport"},
                {"name": "Boarding pass or ticket", "note": "If you have one."},
                {"name": "Any other supporting documents", "note": "Photos, statements from witnesses, etc."},
            ],
        },
        "fees": "There is no fee.",
        "how_long": "An acknowledgement is sent within 10 working days. A full response may take longer if the CSME Unit needs to investigate.",
        "how_to_apply": {
            "options": [
                {
                    "heading": "By post or in person",
                    "content": [
                        "Send the completed CARICOM Point of Entry/Departure/Inland Complaints Form to the CSME Unit, or hand it to an immigration officer at a port.",
                    ],
                },
            ],
        },
        "contact": {
            "agency": "CSME Unit, CARICOM",
            "address": "Tom Adams Financial Centre, Church Village\nSt. Michael",
            "phone": ["(246) 622-0150"],
            "email": "csme@caricom.org",
            "hours": "Open Monday to Friday: 8:30am to 4:30pm",
        },
    },
]
