"""Module containing list of test specifications for regex patterns.

Each country has a list of different versions of its name which should
all return the country's ISO3 code.
"""

test_specifications = [
    {
        "name": "Afghanistan",
        "iso3": "AFG",
        "test_names": ["Afghanistan", "Islamic Emirate of Afghanistan"],
    },
    {
        "name": "Albania",
        "iso3": "ALB",
        "test_names": ["Albania", "Republic of Albania", "Rep. of Albania"],
    },
    {
        "name": "Algeria",
        "iso3": "DZA",
        "test_names": [
            "Algeria",
            "People's Democratic Republic of Algeria",
            "People's Democratic Rep. of Algeria",
        ],
    },
    {
        "name": "American Samoa",
        "iso3": "ASM",
        "test_names": ["American Samoa"],
    },
    {
        "name": "Andorra",
        "iso3": "AND",
        "test_names": ["Andorra"],
    },
    {
        "name": "Angola",
        "iso3": "AGO",
        "test_names": ["Angola", "Republic of Angola", "Rep. of Angola"],
    },
    {
        "name": "Anguilla",
        "iso3": "AIA",
        "test_names": ["Anguilla"],
    },
    {
        "name": "Antarctica",
        "iso3": "ATA",
        "test_names": ["Antarctica"],
    },
    {
        "name": "Antigua",
        "iso3": "ATG",
        "test_names": [
            "Antigua",
            "Barbuda",
            "Antigua & Barbuda",
            "Antigua and Barbuda",
            "Waladli",
            "Wadadli",
        ],
    },
    {
        "name": "Argentina",
        "iso3": "ARG",
        "test_names": [
            "Argentina",
            "Argentine Republic",
            "Argentine Rep.",
            "Argentine Rep",
        ],
    },
    {
        "name": "Armenia",
        "iso3": "ARM",
        "test_names": ["Armenia", "Republic of Armenia", "Rep. of Armenia"],
    },
    {
        "name": "Aruba",
        "iso3": "ABW",
        "test_names": ["Aruba", "Country of Aruba"],
    },
    {
        "name": "Australia",
        "iso3": "AUS",
        "test_names": ["Australia", "Commonwealth of Australia"],
    },
    {
        "name": "Austria",
        "iso3": "AUT",
        "test_names": ["Austria", "Republic of Austria", "Rep. of Austria"],
    },
    {
        "name": "Azerbaijan",
        "iso3": "AZE",
        "test_names": ["Azerbaijan", "Republic of Azerbaijan", "Rep. of Azerbaijan"],
    },
    {
        "name": "Bahamas",
        "iso3": "BHS",
        "test_names": [
            "Bahamas",
            "The Bahamas",
            "Bahamas (the)",
            "Commonwealth of The Bahamas",
        ],
    },
    {
        "name": "Bahrain",
        "iso3": "BHR",
        "test_names": ["Bahrain", "Kingdom of Bahrain"],
    },
    {
        "name": "Bangladesh",
        "iso3": "BGD",
        "test_names": [
            "Bangladesh",
            "People's Republic of Bangladesh",
            "People's Rep. of Bangladesh",
        ],
    },
    {
        "name": "Barbados",
        "iso3": "BRB",
        "test_names": ["Barbados"],
    },
    {
        "name": "Belarus",
        "iso3": "BLR",
        "test_names": ["Belarus", "Republic of Belarus", "Rep. of Belarus"],
    },
    {
        "name": "Belgium",
        "iso3": "BEL",
        "test_names": ["Belgium", "Kingdom of Belgium"],
    },
    {
        "name": "Belize",
        "iso3": "BLZ",
        "test_names": ["Belize"],
    },
    {
        "name": "Benin",
        "iso3": "BEN",
        "test_names": ["Benin", "Republic of Benin", "Rep. of Benin"],
    },
    {
        "name": "Bermuda",
        "iso3": "BMU",
        "test_names": ["Bermuda", "The Bermudas", "Somers Isles"],
    },
    {
        "name": "Bhutan",
        "iso3": "BTN",
        "test_names": ["Bhutan", "Kingdom of Bhutan"],
    },
    {
        "name": "Bolivia",
        "iso3": "BOL",
        "test_names": ["Bolivia", "Plurinational State of Bolivia"],
    },
    {
        "name": "Bosnia and Herzegovina",
        "iso3": "BIH",
        "test_names": ["Bosnia and Herzegovina", "Bosnia-Herzegovina", "bosnia"],
    },
    {
        "name": "Botswana",
        "iso3": "BWA",
        "test_names": ["Botswana", "Republic of Botswana", "Rep. of Botswana"],
    },
    {
        "name": "Bouvet Island",
        "iso3": "BVT",
        "test_names": ["Bouvet Island"],
    },
    {
        "name": "Brazil",
        "iso3": "BRA",
        "test_names": [
            "Brazil",
            "Federative Republic of Brazil",
            "Federative Rep. of Brazil",
        ],
    },
    {
        "name": "British Indian Ocean Territory",
        "iso3": "IOT",
        "test_names": [
            "British Indian Ocean Territory",
            "The British Indian Ocean Territory",
            "BIOT",
        ],
    },
    {
        "name": "Brunei",
        "iso3": "BRN",
        "test_names": ["Brunei", "Brunei Darussalam"],
    },
    {
        "name": "Bulgaria",
        "iso3": "BGR",
        "test_names": ["Bulgaria", "Republic of Bulgaria", "Rep. of Bulgaria"],
    },
    {
        "name": "Burkina Faso",
        "iso3": "BFA",
        "test_names": ["Burkina Faso"],
    },
    {
        "name": "Burundi",
        "iso3": "BDI",
        "test_names": ["Burundi", "Republic of Burundi", "Rep. of Burundi"],
    },
    {
        "name": "Cabo Verde",
        "iso3": "CPV",
        "test_names": [
            "Cabo Verde",
            "Cape Verde",
            "Republic of Cabo Verde",
            "Rep. of Cabo Verde",
        ],
    },
    {
        "name": "Cambodia",
        "iso3": "KHM",
        "test_names": ["Cambodia", "Kampuchea", "Kingdom of Cambodia"],
    },
    {
        "name": "Cameroon",
        "iso3": "CMR",
        "test_names": ["Cameroon", "Republic of Cameroon", "Rep. of Cameroon"],
    },
    {
        "name": "Canada",
        "iso3": "CAN",
        "test_names": ["Canada"],
    },
    {
        "name": "Caribbean Netherlands",
        "iso3": "BES",
        "test_names": [
            "Caribbean Netherlands",
            "Bonaire, Sint Eustatius and Saba",
            "BES Islands",
        ],
    },
    {
        "name": "The Cayman Islands",
        "iso3": "CYM",
        "test_names": ["The Cayman Islands", "Cayman Islands", "Cayman Islands (the)"],
    },
    {
        "name": "The Central African Republic",
        "iso3": "CAF",
        "test_names": [
            "The Central African Republic",
            "Central African Republic",
            "Central African Rep.",
            "Central African Rep",
        ],
    },
    {
        "name": "Chad",
        "iso3": "TCD",
        "test_names": ["Chad", "Republic of Chad", "Rep. of Chad"],
    },
    {
        "name": "Chile",
        "iso3": "CHL",
        "test_names": ["Chile", "Republic of Chile", "Rep. of Chile"],
    },
    {
        "name": "China",
        "iso3": "CHN",
        "test_names": [
            "China",
            "People's Republic of China",
            "People's Rep. of China",
            "PRC",
        ],
    },
    {
        "name": "Christmas Island",
        "iso3": "CXR",
        "test_names": ["Christmas Island", "Territory of Christmas Island"],
    },
    {
        "name": "Cocos Islands",
        "iso3": "CCK",
        "test_names": [
            "Cocos Islands",
            "Cocos (Keeling) Islands",
            "Territory of Cocos (Keeling) Islands",
        ],
    },
    {
        "name": "Colombia",
        "iso3": "COL",
        "test_names": ["Colombia", "Republic of Colombia", "Rep. of Colombia"],
    },
    {
        "name": "The Comoros",
        "iso3": "COM",
        "test_names": ["The Comoros", "Comoros", "Union of the Comoros"],
    },
    {
        "name": "The Democratic Republic of the Congo",
        "iso3": "COD",
        "test_names": [
            "The Democratic Republic of the Congo",
            "Democratic Republic of the Congo",
            "The Democratic Rep. of the Congo",
            "Democratic Rep. of the Congo",
            "Congo-Kinshasa",
            "Kinshasa",
            "DR Congo",
            "DRC",
            "DROC",
            "The DRC",
            "The DROC",
        ],
    },
    {
        "name": "Congo",
        "iso3": "COG",
        "test_names": [
            "Congo",
            "The Congo",
            "The Republic of the Congo",
            "Republic of the Congo",
            "Congo Republic",
            "The Rep. of the Congo",
            "Rep. of the Congo",
            "Congo Rep.",
            "Congo-Brazzaville",
            "Brazzaville",
        ],
    },
    {
        "name": "The Cook Islands",
        "iso3": "COK",
        "test_names": ["The Cook Islands", "Cook Islands", "Cook Islands (the)"],
    },
    {
        "name": "Costa Rica",
        "iso3": "CRI",
        "test_names": ["Costa Rica", "Republic of Costa Rica", "Rep. of Costa Rica"],
    },
    {
        "name": "Croatia",
        "iso3": "HRV",
        "test_names": ["Croatia", "Republic of Croatia", "Rep. of Croatia"],
    },
    {
        "name": "Cuba",
        "iso3": "CUB",
        "test_names": ["Cuba", "Republic of Cuba", "Rep. of Cuba"],
    },
    {
        "name": "Curaçao",
        "iso3": "CUW",
        "test_names": [
            "Curaçao",
            "Curacao",
            "Country of Curaçao",
            "Country of Curacao",
        ],
    },
    {
        "name": "Cyprus",
        "iso3": "CYP",
        "test_names": ["Cyprus", "Republic of Cyprus", "Rep. of Cyprus"],
    },
    {
        "name": "Czechia",
        "iso3": "CZE",
        "test_names": [
            "Czechia",
            "Czech Republic",
            "The Czech Republic",
            "Czech Rep.",
            "The Czech Rep.",
        ],
    },
    {
        "name": "Côte d'Ivoire",
        "iso3": "CIV",
        "test_names": [
            "Côte d'Ivoire",
            "Cote d'Ivoire",
            "Republic of Côte d'Ivoire",
            "Republic of Cote d'Ivoire",
            "Rep. of Côte d'Ivoire",
            "Rep. of Cote d'Ivoire",
            "Ivory Coast",
        ],
    },
    {
        "name": "Denmark",
        "iso3": "DNK",
        "test_names": ["Denmark"],
    },
    {
        "name": "Djibouti",
        "iso3": "DJI",
        "test_names": ["Djibouti", "Republic of Djibouti", "Rep. of Djibouti"],
    },
    {
        "name": "Dominica",
        "iso3": "DMA",
        "test_names": ["Dominica", "Commonwealth of Dominica"],
    },
    {
        "name": "Dominican Republic",
        "iso3": "DOM",
        "test_names": [
            "Dominican Republic",
            "The Dominican Republic",
            "Dominican Rep.",
            "The Dominican Rep.",
        ],
    },
    {
        "name": "Ecuador",
        "iso3": "ECU",
        "test_names": ["Ecuador", "Republic of Ecuador", "Rep. of Ecuador"],
    },
    {
        "name": "Egypt",
        "iso3": "EGY",
        "test_names": ["Egypt", "Arab Republic of Egypt", "Arab Rep. of Egypt"],
    },
    {
        "name": "El Salvador",
        "iso3": "SLV",
        "test_names": ["El Salvador", "Republic of El Salvador", "Rep. of El Salvador"],
    },
    {
        "name": "Equatorial Guinea",
        "iso3": "GNQ",
        "test_names": [
            "Equatorial Guinea",
            "Republic of Equatorial Guinea",
            "Rep. of Equatorial Guinea",
        ],
    },
    {
        "name": "Eritrea",
        "iso3": "ERI",
        "test_names": ["Eritrea", "State of Eritrea"],
    },
    {
        "name": "Estonia",
        "iso3": "EST",
        "test_names": ["Estonia", "Republic of Estonia", "Rep. of Estonia"],
    },
    {
        "name": "Eswatini",
        "iso3": "SWZ",
        "test_names": ["Eswatini", "Kingdom of Eswatini", "Swaziland"],
    },
    {
        "name": "Ethiopia",
        "iso3": "ETH",
        "test_names": [
            "Ethiopia",
            "Federal Democratic Republic of Ethiopia",
            "Federal Democratic Rep. of Ethiopia",
        ],
    },
    {
        "name": "The Falkland Islands",
        "iso3": "FLK",
        "test_names": [
            "The Falkland Islands",
            "Falkland Islands",
            "Isla Malvinas",
            "Malvinas",
        ],
    },
    {
        "name": "The Faroe Islands",
        "iso3": "FRO",
        "test_names": ["The Faroe Islands", "Faroes", "Faeroes"],
    },
    {
        "name": "Fiji",
        "iso3": "FJI",
        "test_names": ["Fiji", "Republic of Fiji", "Rep. of Fiji"],
    },
    {
        "name": "Finland",
        "iso3": "FIN",
        "test_names": ["Finland", "Republic of Finland", "Rep. of Finland"],
    },
    {
        "name": "France",
        "iso3": "FRA",
        "test_names": ["France", "French Republic", "French Rep."],
    },
    {
        "name": "French Guiana",
        "iso3": "GUF",
        "test_names": ["French Guiana"],
    },
    {
        "name": "French Polynesia",
        "iso3": "PYF",
        "test_names": ["French Polynesia"],
    },
    {
        "name": "French Southern and Antarctic Lands",
        "iso3": "ATF",
        "test_names": [
            "French Southern and Antarctic Lands",
            "TAAF",
            "French Southern Territories",
            "French Southern Lands",
        ],
    },
    {
        "name": "Gabon",
        "iso3": "GAB",
        "test_names": ["Gabon", "Gabonese Republic", "Gabonese Rep."],
    },
    {
        "name": "The Gambia",
        "iso3": "GMB",
        "test_names": [
            "The Gambia",
            "Gambia",
            "Republic of the Gambia",
            "Rep. of the Gambia",
        ],
    },
    {
        "name": "Georgia",
        "iso3": "GEO",
        "test_names": ["Georgia"],
    },
    {
        "name": "Germany",
        "iso3": "DEU",
        "test_names": [
            "Germany",
            "Federal Republic of Germany",
            "Federal Rep. of Germany",
        ],
    },
    {
        "name": "Ghana",
        "iso3": "GHA",
        "test_names": ["Ghana", "Republic of Ghana", "Rep. of Ghana"],
    },
    {
        "name": "Gibraltar",
        "iso3": "GIB",
        "test_names": ["Gibraltar"],
    },
    {
        "name": "Greece",
        "iso3": "GRC",
        "test_names": ["Greece", "Hellenic Republic", "Hellenic Rep."],
    },
    {
        "name": "Greenland",
        "iso3": "GRL",
        "test_names": ["Greenland"],
    },
    {
        "name": "Grenada",
        "iso3": "GRD",
        "test_names": ["Grenada"],
    },
    {
        "name": "Guadeloupe",
        "iso3": "GLP",
        "test_names": ["Guadeloupe"],
    },
    {
        "name": "Guam",
        "iso3": "GUM",
        "test_names": ["Guam"],
    },
    {
        "name": "Guatemala",
        "iso3": "GTM",
        "test_names": ["Guatemala", "Republic of Guatemala", "Rep. of Guatemala"],
    },
    {
        "name": "Guernsey",
        "iso3": "GGY",
        "test_names": ["Guernsey"],
    },
    {
        "name": "Guinea",
        "iso3": "GIN",
        "test_names": [
            "Guinea",
            "Republic of Guinea",
            "Rep. of Guinea",
            "Guinea-Conakry",
        ],
    },
    {
        "name": "Guinea-Bissau",
        "iso3": "GNB",
        "test_names": [
            "Guinea-Bissau",
            "Republic of Guinea-Bissau",
            "Rep. of Guinea-Bissau",
            "Guinea Bissau",
        ],
    },
    {
        "name": "Guyana",
        "iso3": "GUY",
        "test_names": [
            "Guyana",
            "Co-operative Republic of Guyana",
            "Co-operative Rep. of Guyana",
        ],
    },
    {
        "name": "Haiti",
        "iso3": "HTI",
        "test_names": ["Haiti", "Republic of Haiti", "Rep. of Haiti"],
    },
    {
        "name": "Heard Island and McDonald Islands",
        "iso3": "HMD",
        "test_names": [
            "Heard Island and McDonald Islands",
            "Territory of Heard Island and McDonald Islands",
            "HIMI",
        ],
    },
    {
        "name": "The Holy See",
        "iso3": "VAT",
        "test_names": [
            "The Holy See",
            "The Vatican",
            "See of Rome",
            "Petrine See",
            "Apostolic See",
        ],
    },
    {
        "name": "Honduras",
        "iso3": "HND",
        "test_names": ["Honduras", "Republic of Honduras", "Rep. of Honduras"],
    },
    {
        "name": "Hong Kong",
        "iso3": "HKG",
        "test_names": [
            "Hong Kong",
            "Hong Kong SAR",
            "HKSAR",
            "Hong Kong Special Administrative Region of the People's Republic of China",
        ],
    },
    {
        "name": "Hungary",
        "iso3": "HUN",
        "test_names": ["Hungary"],
    },
    {
        "name": "Iceland",
        "iso3": "ISL",
        "test_names": ["Iceland"],
    },
    {
        "name": "India",
        "iso3": "IND",
        "test_names": ["India", "Republic of India", "Rep. of India"],
    },
    {
        "name": "Indonesia",
        "iso3": "IDN",
        "test_names": ["Indonesia", "Republic of Indonesia", "Rep. of Indonesia"],
    },
    {
        "name": "Iran",
        "iso3": "IRN",
        "test_names": [
            "Iran",
            "Persia",
            "Islamic Republic of Iran",
            "Islamic Rep. of Iran",
        ],
    },
    {
        "name": "Iraq",
        "iso3": "IRQ",
        "test_names": ["Iraq", "Republic of Iraq", "Rep. of Iraq"],
    },
    {
        "name": "Ireland",
        "iso3": "IRL",
        "test_names": [
            "Ireland",
            "Republic of Ireland",
            "Rep. of Ireland",
            "Eire",
            "Éire",
        ],
    },
    {
        "name": "The Isle of Man",
        "iso3": "IMN",
        "test_names": ["The Isle of Man", "Isle of Man", "Mann"],
    },
    {
        "name": "Israel",
        "iso3": "ISR",
        "test_names": ["Israel", "State of Israel"],
    },
    {
        "name": "Italy",
        "iso3": "ITA",
        "test_names": [
            "Italy",
            "Italian Republic",
            "Italian Rep.",
            "Republic of Italy",
            "Rep. of Italy",
        ],
    },
    {
        "name": "Jamaica",
        "iso3": "JAM",
        "test_names": ["Jamaica"],
    },
    {
        "name": "Japan",
        "iso3": "JPN",
        "test_names": ["Japan"],
    },
    {
        "name": "Jersey",
        "iso3": "JEY",
        "test_names": ["Jersey", "Bailiwick of Jersey"],
    },
    {
        "name": "Jordan",
        "iso3": "JOR",
        "test_names": ["Jordan", "Hashemite Kingdom of Jordan"],
    },
    {
        "name": "Kazakhstan",
        "iso3": "KAZ",
        "test_names": ["Kazakhstan", "Republic of Kazakhstan", "Rep. of Kazakhstan"],
    },
    {
        "name": "Kenya",
        "iso3": "KEN",
        "test_names": ["Kenya", "Republic of Kenya", "Rep. of Kenya"],
    },
    {
        "name": "Kiribati",
        "iso3": "KIR",
        "test_names": ["Kiribati", "Republic of Kiribati", "Rep. of Kiribati"],
    },
    {
        "name": "North Korea",
        "iso3": "PRK",
        "test_names": [
            "North Korea",
            "N. Korea",
            "N Korea",
            "The Democratic People's Republic of Korea",
            "Democratic People's Republic of Korea",
            "The Democratic People's Rep. of Korea",
            "Democratic People's Rep. of Korea",
            "DPRK",
        ],
    },
    {
        "name": "South Korea",
        "iso3": "KOR",
        "test_names": [
            "South Korea",
            "S. Korea",
            "S Korea",
            "The Republic of Korea",
            "Republic or Korea",
            "The Rep. of Korea",
            "Rep. or Korea",
            "ROK",
        ],
    },
    # {
    #    "name": "Kosovo",
    #    "iso3": "XKX",
    #    "test_names": ["Kosovo", "Republic of Kosovo", "Rep. of Kosovo"],
    # },
    {
        "name": "Kuwait",
        "iso3": "KWT",
        "test_names": ["Kuwait", "State of Kuwait", "Kureyn"],
    },
    {
        "name": "Kyrgyzstan",
        "iso3": "KGZ",
        "test_names": ["Kyrgyzstan", "Kyrgyz Republic", "Kyrgyz Rep."],
    },
    {
        "name": "Laos",
        "iso3": "LAO",
        "test_names": [
            "Laos",
            "Lao People's Democratic Republic",
            "Lao People's Democratic Rep.",
        ],
    },
    {
        "name": "Latvia",
        "iso3": "LVA",
        "test_names": ["Latvia", "Republic of Latvia", "Rep. of Latvia"],
    },
    {
        "name": "Lebanon",
        "iso3": "LBN",
        "test_names": [
            "Lebanon",
            "Republic of Lebanon",
            "Rep. of Lebanon",
            "Lebanese Republic",
            "Lebanese Rep.",
        ],
    },
    {
        "name": "Lesotho",
        "iso3": "LSO",
        "test_names": ["Lesotho", "Kingdom of Lesotho"],
    },
    {
        "name": "Liberia",
        "iso3": "LBR",
        "test_names": ["Liberia", "Republic of Liberia", "Rep. of Liberia"],
    },
    {
        "name": "Libya",
        "iso3": "LBY",
        "test_names": ["Libya", "State of Libya"],
    },
    {
        "name": "Liechtenstein",
        "iso3": "LIE",
        "test_names": ["Liechtenstein", "Principality of Liechtenstein"],
    },
    {
        "name": "Lithuania",
        "iso3": "LTU",
        "test_names": ["Lithuania", "Republic of Lithuania", "Rep. of Lithuania"],
    },
    {
        "name": "Luxembourg",
        "iso3": "LUX",
        "test_names": ["Luxembourg", "Grand Duchy of Luxembourg"],
    },
    {
        "name": "Macau",
        "iso3": "MAC",
        "test_names": [
            "Macau",
            "Macao",
            "Macao Special Administrative Region of the People's Republic of China",
            "MSAR",
        ],
    },
    {
        "name": "Madagascar",
        "iso3": "MDG",
        "test_names": ["Madagascar", "Republic of Madagascar", "Rep. of Madagascar"],
    },
    {
        "name": "Malawi",
        "iso3": "MWI",
        "test_names": ["Malawi", "Republic of Malawi", "Rep. of Malawi"],
    },
    {
        "name": "Malaysia",
        "iso3": "MYS",
        "test_names": ["Malaysia"],
    },
    {
        "name": "Maldives",
        "iso3": "MDV",
        "test_names": [
            "Maldives",
            "The Maldives",
            "Republic of Maldives",
            "Rep. of Maldives",
        ],
    },
    {
        "name": "Mali",
        "iso3": "MLI",
        "test_names": ["Mali", "Republic of Mali", "Rep. of Mali"],
    },
    {
        "name": "Malta",
        "iso3": "MLT",
        "test_names": ["Malta", "Republic of Malta", "Rep. of Malta"],
    },
    {
        "name": "Marshall Islands",
        "iso3": "MHL",
        "test_names": [
            "Marshall Islands",
            "Republic of the Marshall Islands",
            "Rep. of the Marshall Islands",
        ],
    },
    {
        "name": "Martinique",
        "iso3": "MTQ",
        "test_names": ["Martinique"],
    },
    {
        "name": "Mauritania",
        "iso3": "MRT",
        "test_names": [
            "Mauritania",
            "Islamic Republic of Mauritania",
            "Islamic Rep. of Mauritania",
        ],
    },
    {
        "name": "Mauritius",
        "iso3": "MUS",
        "test_names": ["Mauritius", "Republic of Mauritius", "Rep. of Mauritius"],
    },
    {
        "name": "Mayotte",
        "iso3": "MYT",
        "test_names": ["Mayotte", "Department of Mayotte"],
    },
    {
        "name": "Mexico",
        "iso3": "MEX",
        "test_names": ["Mexico", "United Mexican States"],
    },
    {
        "name": "Micronesia",
        "iso3": "FSM",
        "test_names": ["Micronesia", "Federated States of Micronesia", "FSM"],
    },
    {
        "name": "Moldova",
        "iso3": "MDA",
        "test_names": ["Moldova", "Republic of Moldova", "Rep. of Moldova"],
    },
    {
        "name": "Monaco",
        "iso3": "MCO",
        "test_names": ["Monaco", "Principality of Monaco"],
    },
    {
        "name": "Mongolia",
        "iso3": "MNG",
        "test_names": ["Mongolia"],
    },
    {
        "name": "Montenegro",
        "iso3": "MNE",
        "test_names": ["Montenegro"],
    },
    {
        "name": "Montserrat",
        "iso3": "MSR",
        "test_names": ["Montserrat"],
    },
    {
        "name": "Morocco",
        "iso3": "MAR",
        "test_names": ["Morocco", "Kingdom of Morocco"],
    },
    {
        "name": "Mozambique",
        "iso3": "MOZ",
        "test_names": ["Mozambique", "Republic of Mozambique", "Rep. of Mozambique"],
    },
    {
        "name": "Myanmar",
        "iso3": "MMR",
        "test_names": [
            "Myanmar",
            "Republic of the Union of Myanmar",
            "Rep. of the Union of Myanmar",
            "Burma",
        ],
    },
    {
        "name": "Namibia",
        "iso3": "NAM",
        "test_names": ["Namibia", "Republic of Namibia", "Rep. of Namibia"],
    },
    {
        "name": "Nauru",
        "iso3": "NRU",
        "test_names": [
            "Nauru",
            "Republic of Nauru",
            "Rep. of Nauru",
            "Pleasant Island",
        ],
    },
    {
        "name": "Nepal",
        "iso3": "NPL",
        "test_names": [
            "Nepal",
            "Federal Democratic Republic of Nepal",
            "Federal Democratic Rep. of Nepal",
        ],
    },
    {
        "name": "The Netherlands",
        "iso3": "NLD",
        "test_names": ["The Netherlands", "Netherlands", "Holland"],
    },
    {
        "name": "New Caledonia",
        "iso3": "NCL",
        "test_names": ["New Caledonia"],
    },
    {
        "name": "New Zealand",
        "iso3": "NZL",
        "test_names": ["New Zealand", "N. Zealand", "N Zealand"],
    },
    {
        "name": "Nicaragua",
        "iso3": "NIC",
        "test_names": ["Nicaragua", "Republic of Nicaragua", "Rep. of Nicaragua"],
    },
    {
        "name": "Niger",
        "iso3": "NER",
        "test_names": ["Niger", "The Niger", "Republic of Niger", "Rep. of Niger"],
    },
    {
        "name": "Nigeria",
        "iso3": "NGA",
        "test_names": [
            "Nigeria",
            "Federal Republic of Nigeria",
            "Federal Rep. of Nigeria",
        ],
    },
    {
        "name": "Niue",
        "iso3": "NIU",
        "test_names": ["Niue"],
    },
    {
        "name": "Norfolk Island",
        "iso3": "NFK",
        "test_names": ["Norfolk Island", "Territory of Norfolk Island"],
    },
    {
        "name": "North Macedonia",
        "iso3": "MKD",
        "test_names": [
            "North Macedonia",
            "N. Macedonia",
            "N Macedonia",
            "Macedonia",
            "Republic of North Macedonia",
            "Rep. of North Macedonia",
        ],
    },
    {
        "name": "The Northern Mariana Islands",
        "iso3": "MNP",
        "test_names": [
            "The Northern Mariana Islands",
            "Commonwealth of the Northern Mariana Islands",
            "CNMI",
        ],
    },
    {
        "name": "Norway",
        "iso3": "NOR",
        "test_names": ["Norway", "Kingdom of Norway"],
    },
    {
        "name": "Oman",
        "iso3": "OMN",
        "test_names": ["Oman", "Sultanate of Oman"],
    },
    {
        "name": "Pakistan",
        "iso3": "PAK",
        "test_names": [
            "Pakistan",
            "Islamic Republic of Pakistan",
            "Islamic Rep. of Pakistan",
        ],
    },
    {
        "name": "Palau",
        "iso3": "PLW",
        "test_names": [
            "Palau",
            "Republic of Palau",
            "Rep. of Palau",
            "Belau",
            "Palaos",
            "Pelew",
        ],
    },
    {
        "name": "Palestine",
        "iso3": "PSE",
        "test_names": ["Palestine", "State of Palestine"],
    },
    {
        "name": "Panama",
        "iso3": "PAN",
        "test_names": ["Panama", "Republic of Panama", "Rep. of Panama"],
    },
    {
        "name": "Papua New Guinea",
        "iso3": "PNG",
        "test_names": [
            "Papua New Guinea",
            "Independent State of Papua New Guinea",
            "PNG",
        ],
    },
    {
        "name": "Paraguay",
        "iso3": "PRY",
        "test_names": ["Paraguay", "Republic of Paraguay", "Rep. of Paraguay"],
    },
    {
        "name": "Peru",
        "iso3": "PER",
        "test_names": ["Peru", "Republic of Peru", "Rep. of Peru"],
    },
    {
        "name": "Philippines",
        "iso3": "PHL",
        "test_names": [
            "Philippines",
            "The Philippines",
            "Republic of Philippines",
            "Rep. of Philippines",
        ],
    },
    {
        "name": "The Pitcairn Islands",
        "iso3": "PCN",
        "test_names": [
            "The Pitcairn Islands",
            "Pitcairn, Henderson, Ducie and Oeno Islands",
        ],
    },
    {
        "name": "Poland",
        "iso3": "POL",
        "test_names": ["Poland", "Republic of Poland", "Rep. of Poland"],
    },
    {
        "name": "Portugal",
        "iso3": "PRT",
        "test_names": ["Portugal", "Portuguese Republic", "Portuguese Rep."],
    },
    {
        "name": "Puerto Rico",
        "iso3": "PRI",
        "test_names": ["Puerto Rico", "Commonwealth of Puerto Rico", "PR"],
    },
    {
        "name": "Qatar",
        "iso3": "QAT",
        "test_names": ["Qatar", "State of Qatar"],
    },
    {
        "name": "Romania",
        "iso3": "ROU",
        "test_names": ["Romania"],
    },
    {
        "name": "Russia",
        "iso3": "RUS",
        "test_names": ["Russia", "Russian Federation", "Russian Fed."],
    },
    {
        "name": "Rwanda",
        "iso3": "RWA",
        "test_names": ["Rwanda", "Republic of Rwanda", "Rep. of Rwanda"],
    },
    {
        "name": "Réunion",
        "iso3": "REU",
        "test_names": ["Réunion", "Reunion", "La Réunion"],
    },
    {
        "name": "Saint Barthélemy",
        "iso3": "BLM",
        "test_names": [
            "Saint Barthélemy",
            "Saint-Barthélemy",
            "Saint Barthelemy",
            "Saint-Barthelemy",
            "Collectivité territoriale de Saint-Barthélemy",
            "St-Barth",
            "St. Barts",
        ],
    },
    {
        "name": "Saint Helena, Ascension and Tristan da Cunha",
        "iso3": "SHN",
        "test_names": [
            "Saint Helena, Ascension and Tristan da Cunha",
            "St. Helena, Ascension and Tristan da Cunha",
        ],
    },
    {
        "name": "Saint Kitts and Nevis",
        "iso3": "KNA",
        "test_names": [
            "Saint Kitts and Nevis",
            "St. Kitts and Nevis",
            "St Kitts and Nevis",
            "Federation of Saint Christopher and Nevis",
            "Fed. of Saint Christopher and Nevis",
        ],
    },
    {
        "name": "Saint Lucia",
        "iso3": "LCA",
        "test_names": ["Saint Lucia", "St. Lucia", "St Lucia"],
    },
    {
        "name": "Saint Martin",
        "iso3": "MAF",
        "test_names": [
            "Saint Martin",
            "Saint-Martin",
            "St. Martin",
            "St Martin",
            "Collectivity of Saint Martin",
        ],
    },
    {
        "name": "Saint Pierre and Miquelon",
        "iso3": "SPM",
        "test_names": [
            "Saint Pierre and Miquelon",
            "St. Pierre and Miquelon",
            "Territorial Collectivity of Saint-Pierre and Miquelon",
        ],
    },
    {
        "name": "Saint Vincent and the Grenadines",
        "iso3": "VCT",
        "test_names": [
            "Saint Vincent and the Grenadines",
            "St. Vincent and the Grenadines",
        ],
    },
    {
        "name": "Samoa",
        "iso3": "WSM",
        "test_names": ["Samoa", "Independent State of Samoa", "Western Samoa"],
    },
    {
        "name": "San Marino",
        "iso3": "SMR",
        "test_names": ["San Marino", "Republic of San Marino", "Rep. of San Marino"],
    },
    {
        "name": "São Tomé and Príncipe",
        "iso3": "STP",
        "test_names": [
            "São Tomé and Príncipe",
            "Sao Tome and Principe",
            "Democratic Republic of São Tomé and Príncipe",
            "Democratic Rep. of São Tomé and Príncipe",
        ],
    },
    {
        "name": "Saudi Arabia",
        "iso3": "SAU",
        "test_names": ["Saudi Arabia", "Kingdom of Saudi Arabia", "KSA"],
    },
    {
        "name": "Senegal",
        "iso3": "SEN",
        "test_names": ["Senegal", "Republic of Senegal", "Rep. of Senegal"],
    },
    {
        "name": "Serbia",
        "iso3": "SRB",
        "test_names": ["Serbia", "Republic of Serbia", "Rep. of Serbia"],
    },
    {
        "name": "Seychelles",
        "iso3": "SYC",
        "test_names": ["Seychelles", "Republic of Seychelles", "Rep. of Seychelles"],
    },
    {
        "name": "Sierra Leone",
        "iso3": "SLE",
        "test_names": [
            "Sierra Leone",
            "Republic of Sierra Leone",
            "Rep. of Sierra Leone",
            "Salone",
        ],
    },
    {
        "name": "Singapore",
        "iso3": "SGP",
        "test_names": ["Singapore", "Republic of Singapore", "Rep. of Singapore"],
    },
    {
        "name": "Sint Maarten",
        "iso3": "SXM",
        "test_names": ["Sint Maarten"],
    },
    {
        "name": "Slovakia",
        "iso3": "SVK",
        "test_names": ["Slovakia", "Slovak Republic", "Slovak Rep."],
    },
    {
        "name": "Slovenia",
        "iso3": "SVN",
        "test_names": ["Slovenia", "Republic of Slovenia", "Rep. of Slovenia"],
    },
    {
        "name": "Solomon Islands",
        "iso3": "SLB",
        "test_names": ["Solomon Islands"],
    },
    {
        "name": "Somalia",
        "iso3": "SOM",
        "test_names": [
            "Somalia",
            "Federal Republic of Somalia",
            "Federal Rep. of Somalia",
        ],
    },
    {
        "name": "South Africa",
        "iso3": "ZAF",
        "test_names": [
            "South Africa",
            "S. Africa",
            "S Africa",
            "Republic of South Africa",
            "Rep. of South Africa",
            "RSA",
        ],
    },
    {
        "name": "South Georgia and the South Sandwich Islands",
        "iso3": "SGS",
        "test_names": ["South Georgia and the South Sandwich Islands", "SGSSI"],
    },
    {
        "name": "South Sudan",
        "iso3": "SSD",
        "test_names": [
            "South Sudan",
            "S. Sudan",
            "S Sudan",
            "Republic of South Sudan",
            "Rep. of South Sudan",
            "Nilotic Republic",
            "Nilotic Rep.",
        ],
    },
    {
        "name": "Spain",
        "iso3": "ESP",
        "test_names": ["Spain", "Kingdom of Spain"],
    },
    {
        "name": "Sri Lanka",
        "iso3": "LKA",
        "test_names": [
            "Sri Lanka",
            "Democratic Socialist Republic of Sri Lanka",
            "Democratic Socialist Rep. of Sri Lanka",
        ],
    },
    {
        "name": "Sudan",
        "iso3": "SDN",
        "test_names": ["Sudan", "Republic of the Sudan", "Rep. of the Sudan"],
    },
    {
        "name": "Suriname",
        "iso3": "SUR",
        "test_names": ["Suriname", "Republic of Suriname", "Rep. of Suriname"],
    },
    {
        "name": "Svalbard and Jan Mayen",
        "iso3": "SJM",
        "test_names": ["Svalbard and Jan Mayen"],
    },
    {
        "name": "Sweden",
        "iso3": "SWE",
        "test_names": ["Sweden", "Kingdom of Sweden"],
    },
    {
        "name": "Switzerland",
        "iso3": "CHE",
        "test_names": ["Switzerland", "Swiss Confederation"],
    },
    {
        "name": "Syria",
        "iso3": "SYR",
        "test_names": ["Syria", "Syrian Arab Republic", "Syrian Arab Rep."],
    },
    {
        "name": "Taiwan",
        "iso3": "TWN",
        "test_names": ["Taiwan"],
    },
    {
        "name": "Tajikistan",
        "iso3": "TJK",
        "test_names": ["Tajikistan", "Republic of Tajikistan", "Rep. of Tajikistan"],
    },
    {
        "name": "Tanzania",
        "iso3": "TZA",
        "test_names": [
            "Tanzania",
            "United Republic of Tanzania",
            "United Rep. of Tanzania",
        ],
    },
    {
        "name": "Thailand",
        "iso3": "THA",
        "test_names": ["Thailand", "Kingdom of Thailand"],
    },
    {
        "name": "Timor-Leste",
        "iso3": "TLS",
        "test_names": [
            "Timor-Leste",
            "East Timor",
            "Democratic Republic of Timor-Leste",
            "Democratic Rep. of Timor-Leste",
        ],
    },
    {
        "name": "Togo",
        "iso3": "TGO",
        "test_names": ["Togo", "Togolese Republic", "Togolese Rep."],
    },
    {
        "name": "Tokelau",
        "iso3": "TKL",
        "test_names": ["Tokelau", "Tokelau Islands", "Union Islands"],
    },
    {
        "name": "Tonga",
        "iso3": "TON",
        "test_names": ["Tonga", "Kingdom of Tonga"],
    },
    {
        "name": "Trinidad and Tobago",
        "iso3": "TTO",
        "test_names": [
            "Trinidad and Tobago",
            "Republic of Trinidad and Tobago",
            "Rep. of Trinidad and Tobago",
        ],
    },
    {
        "name": "Tunisia",
        "iso3": "TUN",
        "test_names": ["Tunisia", "Republic of Tunisia", "Rep. of Tunisia"],
    },
    {
        "name": "Turkey",
        "iso3": "TUR",
        "test_names": [
            "Turkey",
            "Republic of Turkey",
            "Rep. of Turkey",
            "Republic of Türkiye",
            "Rep. of Türkiye",
        ],
    },
    {
        "name": "Turkmenistan",
        "iso3": "TKM",
        "test_names": ["Turkmenistan", "Turkmenia"],
    },
    {
        "name": "The Turks and Caicos Islands",
        "iso3": "TCA",
        "test_names": ["The Turks and Caicos Islands", "The Turks & Caicos Islands"],
    },
    {
        "name": "Tuvalu",
        "iso3": "TUV",
        "test_names": ["Tuvalu", "Ellice Islands"],
    },
    {
        "name": "Uganda",
        "iso3": "UGA",
        "test_names": ["Uganda", "Republic of Uganda", "Rep. of Uganda"],
    },
    {
        "name": "Ukraine",
        "iso3": "UKR",
        "test_names": ["Ukraine"],
    },
    {
        "name": "United Arab Emirates",
        "iso3": "ARE",
        "test_names": ["United Arab Emirates", "UAE", "Emirates"],
    },
    {
        "name": "The United Kingdom of Great Britain and Northern Ireland",
        "iso3": "GBR",
        "test_names": [
            "The United Kingdom of Great Britain and Northern Ireland",
            "The United Kingdom of Great Britain and N. Ireland",
            "The United Kingdom",
            "Great Britain and Northern Ireland",
            "Great Britain and N. Ireland",
            "Great Britain",
            "The U.K.",
            "The UK",
            "U.K.",
            "UK",
        ],
    },
    {
        "name": "United States Minor Outlying Islands",
        "iso3": "UMI",
        "test_names": [
            "United States Minor Outlying Islands",
            "U.S. Minor Outlying Islands",
            "US Minor Outlying Islands",
            "US Outlying Islands",
            "U.S. Outlying Islands",
        ],
    },
    {
        "name": "The United States of America",
        "iso3": "USA",
        "test_names": [
            "The United States of America",
            "The United States",
            "United States",
            "U.S.",
            "US",
            "U.S.A.",
            "USA",
            "The U.S.",
            "The US",
            "The U.S.A.",
            "The USA",
        ],
    },
    {
        "name": "Uruguay",
        "iso3": "URY",
        "test_names": [
            "Uruguay",
            "Oriental Republic of Uruguay",
            "Oriental Rep. of Uruguay",
        ],
    },
    {
        "name": "Uzbekistan",
        "iso3": "UZB",
        "test_names": ["Uzbekistan", "Republic of Uzbekistan", "Rep. of Uzbekistan"],
    },
    {
        "name": "Vanuatu",
        "iso3": "VUT",
        "test_names": ["Vanuatu", "Republic of Vanuatu", "Rep. of Vanuatu"],
    },
    {
        "name": "Venezuela",
        "iso3": "VEN",
        "test_names": [
            "Venezuela",
            "Bolivarian Republic of Venezuela",
            "Bolivarian Rep. of Venezuela",
        ],
    },
    {
        "name": "Vietnam",
        "iso3": "VNM",
        "test_names": [
            "Vietnam",
            "Viet Nam",
            "Socialist Republic of Vietnam",
            "Socialist Rep. of Vietnam",
        ],
    },
    {
        "name": "British Virgin Islands",
        "iso3": "VGB",
        "test_names": [
            "British Virgin Islands",
            "Virgin Islands U.K.",
            "Virgin Islands UK",
            "Virgin Islands (U.K.)",
            "Virgin Islands (UK)",
            "BVI",
        ],
    },
    {
        "name": "United States Virgin Islands",
        "iso3": "VIR",
        "test_names": [
            "United States Virgin Islands",
            "The United States Virgin Islands",
            "U.S. Virgin Islands",
            "US Virgin Islands",
            "Virgin Islands of the United States",
            "Virgin Islands (U.S.)",
            "Virgin Islands (US)",
        ],
    },
    {
        "name": "Wallis and Futuna",
        "iso3": "WLF",
        "test_names": [
            "Wallis and Futuna",
            "Wallis & Futuna",
            "Territory of the Wallis and Futuna Islands",
        ],
    },
    {
        "name": "Western Sahara",
        "iso3": "ESH",
        "test_names": ["Western Sahara"],
    },
    {
        "name": "Yemen",
        "iso3": "YEM",
        "test_names": ["Yemen", "Republic of Yemen", "Rep. of Yemen"],
    },
    {
        "name": "Zambia",
        "iso3": "ZMB",
        "test_names": ["Zambia", "Republic of Zambia", "Rep. of Zambia"],
    },
    {
        "name": "Zimbabwe",
        "iso3": "ZWE",
        "test_names": ["Zimbabwe", "Republic of Zimbabwe", "Rep. of Zimbabwe"],
    },
    {
        "name": "Åland",
        "iso3": "ALA",
        "test_names": ["Åland", "Åland Islands", "Aland", "Aland Islands"],
    },
]
