"""Module containing dictionary with regex patterns for each country."""


regex_dict = {
    "Afghanistan": {
        "regex": "afghanistan|^AF$|^AFG$",
        "iso3": "AFG",
    },
    "Albania": {
        "regex": "albania|^AL$|^ALB$",
        "iso3": "ALB",
    },
    "Algeria": {
        "regex": "algeria|^DZ$|^DZA$",
        "iso3": "DZA",
    },
    "American Samoa": {
        "regex": "^(?=.*america).*samoa.*|^AS$|^ASM$",
        "iso3": "ASM",
    },
    "Andorra": {
        "regex": "andorra|^AD$|^AND$",
        "iso3": "AND",
    },
    "Angola": {
        "regex": "angola|^AO$|^AGO$",
        "iso3": "AGO",
    },
    "Anguilla": {
        "regex": "anguilla|^AI$|^AIA$",
        "iso3": "AIA",
    },
    "Antarctica": {
        "regex": "antarctic|^AQ$|^ATA$",
        "iso3": "ATA",
    },
    "Antigua and Barbuda": {
        "regex": "antigua|barbuda|^AG$|^ATG$",
        "iso3": "ATG",
    },
    "Argentina": {
        "regex": "argentina|^AR$|^ARG$",
        "iso3": "ARG",
    },
    "Armenia": {
        "regex": "armenia|^AM$|^ARM$",
        "iso3": "ARM",
    },
    "Aruba": {
        "regex": "aruba|^AW$|^ABW$",
        "iso3": "ABW",
    },
    "Australia": {
        "regex": "australia|^AU$|^AUS$",
        "iso3": "AUS",
    },
    "Austria": {
        "regex": "austria|^AT$|^AUT$",
        "iso3": "AUT",
    },
    "Azerbaijan": {
        "regex": "azerbaijan|^AZ$|^AZE$",
        "iso3": "AZE",
    },
    "Bahamas (the)": {
        "regex": ".*bahamas|^BS$|^BHS$",
        "iso3": "BHS",
    },
    "Bahrain": {
        "regex": "bahrain|^BH$|^BHR$",
        "iso3": "BHR",
    },
    "Bangladesh": {
        "regex": "bangladesh|^BD$|^BGD$",
        "iso3": "BGD",
    },
    "Barbados": {
        "regex": "barbados|^BB$|^BRB$",
        "iso3": "BRB",
    },
    "Belarus": {
        "regex": "belarus|^BY$|^BLR$",
        "iso3": "BLR",
    },
    "Belgium": {
        "regex": "belgium|^BE$|^BEL$",
        "iso3": "BEL",
    },
    "Belize": {
        "regex": "belize|^BZ$|^BLZ$",
        "iso3": "BLZ",
    },
    "Benin": {
        "regex": "benin|^BJ$|^BEN$",
        "iso3": "BEN",
    },
    "Bermuda": {
        "regex": "bermuda|^BM$|^BMU$",
        "iso3": "BMU",
    },
    "Bhutan": {
        "regex": "bhutan|^BT$|^BTN$",
        "iso3": "BTN",
    },
    "Bolivia (Plurinational State of)": {
        "regex": ".*bolivia|^BO$|^BOL$",
        "iso3": "BOL",
    },
    "Bonaire, Sint Eustatius and Saba": {
        "regex": ".*bonaire|^BQ$|^BES$",
        "iso3": "BES",
    },
    "Bosnia and Herzegovina": {
        "regex": "bosnia|herzegovina|^BA$|^BIH$",
        "iso3": "BIH",
    },
    "Botswana": {
        "regex": "botswana|^BW$|^BWA$",
        "iso3": "BWA",
    },
    "Bouvet Island": {
        "regex": "bouvet|^BV$|^BVT$",
        "iso3": "BVT",
    },
    "Brazil": {
        "regex": "brazil|^BR$|^BRA$",
        "iso3": "BRA",
    },
    "British Indian Ocean Territory (the)": {
        "regex": ".*british indian|^IO$|^IOT$",
        "iso3": "IOT",
    },
    "Brunei Darussalam": {
        "regex": ".*brunei|^BN$|^BRN$",
        "iso3": "BRN",
    },
    "Bulgaria": {
        "regex": "bulgaria|^BG$|^BGR$",
        "iso3": "BGR",
    },
    "Burkina Faso": {
        "regex": "burkina|^BF$|^BFA$",
        "iso3": "BFA",
    },
    "Burundi": {
        "regex": "burundi|^BI$|^BDI$",
        "iso3": "BDI",
    },
    "Cabo Verde": {
        "regex": "cape verde|cabo verde|^CV$|^CPV$",
        "iso3": "CPV",
    },
    "Cambodia": {
        "regex": "cambodia|^KH$|^KHM$",
        "iso3": "KHM",
    },
    "Cameroon": {
        "regex": "cameroon|cameroun|^CM$|^CMR$",
        "iso3": "CMR",
    },
    "Canada": {
        "regex": "canada|^CA$|^CAN$",
        "iso3": "CAN",
    },
    "Cayman Islands (the)": {
        "regex": ".*cayman islands|^KY$|^CYM$",
        "iso3": "CYM",
    },
    "Central African Republic (the)": {
        "regex": ".*central african rep|car$|^CF$|^CAF$",
        "iso3": "CAF",
    },
    "Chad": {
        "regex": "chad|^TD$|^TCD$",
        "iso3": "TCD",
    },
    "Chile": {
        "regex": "chile|^CL$|^CHL$",
        "iso3": "CHL",
    },
    "China": {
        "regex": "(?!.*hong kong|.*taiwan|.*macau|.*macao).*china|^CN$|^CHN$",
        "iso3": "CHN",
    },
    "Christmas Island": {
        "regex": "christmas|^CX$|^CXR$",
        "iso3": "CXR",
    },
    "Cocos (Keeling) Islands (the)": {
        "regex": ".*cocos|^CC$|^CCK$",
        "iso3": "CCK",
    },
    "Colombia": {
        "regex": "colombia|^CO$|^COL$",
        "iso3": "COL",
    },
    "Comoros (the)": {
        "regex": ".*comoros|^KM$|^COM$",
        "iso3": "COM",
    },
    "Congo (the Democratic Republic of the)": {
        "regex": "(?!,*brazzaville).*(?=.*dem|DR|.*kinshasa).*congo|kinshasa|DRC|DROC|^CD$|^COD$",
        "iso3": "COD",
    },
    "Congo (the)": {
        "regex": "(?!.*kinshasa|DR|.*dem).*(congo|brazzaville)|^CG$|^COG$",
        "iso3": "COG",
    },
    "Cook Islands (the)": {
        "regex": ".*cook|^CK$|^COK$",
        "iso3": "COK",
    },
    "Costa Rica": {
        "regex": "costa rica|^CR$|^CRI$",
        "iso3": "CRI",
    },
    "Croatia": {
        "regex": "croatia|^HR$|^HRV$",
        "iso3": "HRV",
    },
    "Cuba": {
        "regex": "cuba|^CU$|^CUB$",
        "iso3": "CUB",
    },
    "Curaçao": {
        "regex": "curaçao|curacao|^CW$|^CUW$",
        "iso3": "CUW",
    },
    "Cyprus": {
        "regex": "cyprus|^CY$|^CYP$",
        "iso3": "CYP",
    },
    "Czechia": {
        "regex": "czech|^CZ$|^CZE$",
        "iso3": "CZE",
    },
    "Côte d'Ivoire": {
        "regex": "côte d.*ivoire|cote d.*ivoire|ivory coast|^CI$|^CIV$",
        "iso3": "CIV",
    },
    "Denmark": {
        "regex": "denmark|^DK$|^DNK$",
        "iso3": "DNK",
    },
    "Djibouti": {
        "regex": "djibouti|^DJ$|^DJI$",
        "iso3": "DJI",
    },
    "Dominica": {
        "regex": "(?!.*rep).*dominica|.*dominique|^DM$|^DMA$",
        "iso3": "DMA",
    },
    "Dominican Republic (the)": {
        "regex": ".*dominican republic|^DO$|^DOM$",
        "iso3": "DOM",
    },
    "Ecuador": {
        "regex": "ecuador|^EC$|^ECU$",
        "iso3": "ECU",
    },
    "Egypt": {
        "regex": "egypt|^EG$|^EGY$",
        "iso3": "EGY",
    },
    "El Salvador": {
        "regex": ".*salvador|^SV$|^SLV$",
        "iso3": "SLV",
    },
    "Equatorial Guinea": {
        "regex": ".*equatorial guinea|^GQ$|^GNQ$",
        "iso3": "GNQ",
    },
    "Eritrea": {
        "regex": "eritrea|^ER$|^ERI$",
        "iso3": "ERI",
    },
    "Estonia": {
        "regex": "estonia|^EE$|^EST$",
        "iso3": "EST",
    },
    "Eswatini": {
        "regex": "eswatini|swaziland|^SZ$|^SWZ$",
        "iso3": "SWZ",
    },
    "Ethiopia": {
        "regex": "ethiopia|^ET$|^ETH$",
        "iso3": "ETH",
    },
    "Falkland Islands (the) [Malvinas]": {
        "regex": ".*falkland|^FK$|^FLK$",
        "iso3": "FLK",
    },
    "Faroe Islands (the)": {
        "regex": ".*faroe|^FO$|^FRO$",
        "iso3": "FRO",
    },
    "Fiji": {
        "regex": "fiji|^FJ$|^FJI$",
        "iso3": "FJI",
    },
    "Finland": {
        "regex": "finland|^FI$|^FIN$",
        "iso3": "FIN",
    },
    "France": {
        "regex": "france|^FR$|^FRA$",
        "iso3": "FRA",
    },
    "French Guiana": {
        "regex": "french guiana|^GF$|^GUF$",
        "iso3": "GUF",
    },
    "French Polynesia": {
        "regex": "french polynesia|^PF$|^PYF$",
        "iso3": "PYF",
    },
    "French Southern Territories (the)": {
        "regex": ".*french southern|^TF$|^ATF$",
        "iso3": "ATF",
    },
    "Gabon": {
        "regex": ".*gabon|^GA$|^GAB$",
        "iso3": "GAB",
    },
    "Gambia (the)": {
        "regex": ".*gambia|^GM$|^GMB$",
        "iso3": "GMB",
    },
    "Georgia": {
        "regex": "georgia|^GE$|^GEO$",
        "iso3": "GEO",
    },
    "Germany": {
        "regex": "germany|^DE$|^DEU$",
        "iso3": "DEU",
    },
    "Ghana": {
        "regex": ".*ghana|^GH$|^GHA$",
        "iso3": "GHA",
    },
    "Gibraltar": {
        "regex": "gibraltar|^GI$|^GIB$",
        "iso3": "GIB",
    },
    "Greece": {
        "regex": "greece|^GR$|^GRC$",
        "iso3": "GRC",
    },
    "Greenland": {
        "regex": "greenland|^GL$|^GRL$",
        "iso3": "GRL",
    },
    "Grenada": {
        "regex": "grenada|^GD$|^GRD$",
        "iso3": "GRD",
    },
    "Guadeloupe": {
        "regex": "guadeloupe|^GP$|^GLP$",
        "iso3": "GLP",
    },
    "Guam": {
        "regex": "guam|^GU$|^GUM$",
        "iso3": "GUM",
    },
    "Guatemala": {
        "regex": "guatemala|^GT$|^GTM$",
        "iso3": "GTM",
    },
    "Guernsey": {
        "regex": "guernsey|^GG$|^GGY$",
        "iso3": "GGY",
    },
    "Guinea": {
        "regex": "(?!.*bissau|.*new|.*equatorial).*guinea|^GN$|^GIN$",
        "iso3": "GIN",
    },
    "Guinea-Bissau": {
        "regex": "guinea.*bissau|^GW$|^GNB$",
        "iso3": "GNB",
    },
    "Guyana": {
        "regex": "guyana|^GY$|^GUY$",
        "iso3": "GUY",
    },
    "Haiti": {
        "regex": "haiti|^HT$|^HTI$",
        "iso3": "HTI",
    },
    "Heard Island and McDonald Islands": {
        "regex": ".*heard|^HM$|^HMD$",
        "iso3": "HMD",
    },
    "Holy See (the)": {
        "regex": ".*holy see|.*vatican|^VA$|^VAT$",
        "iso3": "VAT",
    },
    "Honduras": {
        "regex": "honduras|^HN$|^HND$",
        "iso3": "HND",
    },
    "Hong Kong": {
        "regex": "hong kong|^HK$|^HKG$",
        "iso3": "HKG",
    },
    "Hungary": {
        "regex": "hungary|^HU$|^HUN$",
        "iso3": "HUN",
    },
    "Iceland": {
        "regex": "iceland|^IS$|^ISL$",
        "iso3": "ISL",
    },
    "India": {
        "regex": "india$|^IN$|^IND$",
        "iso3": "IND",
    },
    "Indonesia": {
        "regex": "indonesia|^ID$|^IDN$",
        "iso3": "IDN",
    },
    "Iran (Islamic Republic of)": {
        "regex": ".*iran|^IR$|^IRN$",
        "iso3": "IRN",
    },
    "Iraq": {
        "regex": ".*iraq|^IQ$|^IRQ$",
        "iso3": "IRQ",
    },
    "Ireland": {
        "regex": "(?!.*north).*ireland|^IE$|^IRL$",
        "iso3": "IRL",
    },
    "Isle of Man": {
        "regex": ".*isle of man|^IM$|^IMN$",
        "iso3": "IMN",
    },
    "Israel": {
        "regex": "israel|^IL$|^ISR$",
        "iso3": "ISR",
    },
    "Italy": {
        "regex": "italy|^IT$|^ITA$",
        "iso3": "ITA",
    },
    "Jamaica": {
        "regex": "jamaica|^JM$|^JAM$",
        "iso3": "JAM",
    },
    "Japan": {
        "regex": "japan|^JP$|^JPN$",
        "iso3": "JPN",
    },
    "Jersey": {
        "regex": "jersey|^JE$|^JEY$",
        "iso3": "JEY",
    },
    "Jordan": {
        "regex": "jordan|^JO$|^JOR$",
        "iso3": "JOR",
    },
    "Kazakhstan": {
        "regex": "kazakhstan|^KZ$|^KAZ$",
        "iso3": "KAZ",
    },
    "Kenya": {
        "regex": "kenya|^KE$|^KEN$",
        "iso3": "KEN",
    },
    "Kiribati": {
        "regex": ".*kiribati|^KI$|^KIR$",
        "iso3": "KIR",
    },
    "Korea (the Democratic People's Republic of)": {
        "regex": "(?=.*korea).*(north|dem|n[\\. ]*)|^KP$|^PRK$",
        "iso3": "PRK",
    },
    "Korea (the Republic of)": {
        "regex": "(?!.*dem|.*people|.*north|.*n[\\., ]|DPR).*korea|^KR$|^KOR$",
        "iso3": "KOR",
    },
    "Kosovo (the Republic of)": {
        "regex": ".*kosovo|^XK$|^XKX$",
        "iso3": "XKX",
    },
    "Kuwait": {
        "regex": "kuwait|^KW$|^KWT$",
        "iso3": "KWT",
    },
    "Kyrgyzstan": {
        "regex": ".*kyrgyz|^KG$|^KGZ$",
        "iso3": "KGZ",
    },
    "Lao People's Democratic Republic (the)": {
        "regex": ".*lao|^LA$|^LAO$",
        "iso3": "LAO",
    },
    "Latvia": {
        "regex": "latvia|^LV$|^LVA$",
        "iso3": "LVA",
    },
    "Lebanon": {
        "regex": "lebanon|^LB$|^LBN$",
        "iso3": "LBN",
    },
    "Lesotho": {
        "regex": "lesotho|^LS$|^LSO$",
        "iso3": "LSO",
    },
    "Liberia": {
        "regex": "liberia|^LR$|^LBR$",
        "iso3": "LBR",
    },
    "Libya": {
        "regex": "libya|^LY$|^LBY$",
        "iso3": "LBY",
    },
    "Liechtenstein": {
        "regex": "liechtenstein|^LI$|^LIE$",
        "iso3": "LIE",
    },
    "Lithuania": {
        "regex": "lithuania|^LT$|^LTU$",
        "iso3": "LTU",
    },
    "Luxembourg": {
        "regex": "luxembourg|^LU$|^LUX$",
        "iso3": "LUX",
    },
    "Macao": {
        "regex": ".*macao|.*macau|^MO$|^MAC$",
        "iso3": "MAC",
    },
    "Madagascar": {
        "regex": "madagascar|^MG$|^MDG$",
        "iso3": "MDG",
    },
    "Malawi": {
        "regex": "malawi|^MW$|^MWI$",
        "iso3": "MWI",
    },
    "Malaysia": {
        "regex": "malaysia|^MY$|^MYS$",
        "iso3": "MYS",
    },
    "Maldives": {
        "regex": "maldives|^MV$|^MDV$",
        "iso3": "MDV",
    },
    "Mali": {
        "regex": "mali$|^ML$|^MLI$",
        "iso3": "MLI",
    },
    "Malta": {
        "regex": "malta|^MT$|^MLT$",
        "iso3": "MLT",
    },
    "Marshall Islands (the)": {
        "regex": ".*marshall|^MH$|^MHL$",
        "iso3": "MHL",
    },
    "Martinique": {
        "regex": "martinique|^MQ$|^MTQ$",
        "iso3": "MTQ",
    },
    "Mauritania": {
        "regex": "mauritania|^MR$|^MRT$",
        "iso3": "MRT",
    },
    "Mauritius": {
        "regex": "mauritius|^MU$|^MUS$",
        "iso3": "MUS",
    },
    "Mayotte": {
        "regex": ".*mayotte|^YT$|^MYT$",
        "iso3": "MYT",
    },
    "Mexico": {
        "regex": "mexico|^MX$|^MEX$",
        "iso3": "MEX",
    },
    "Micronesia (Federated States of)": {
        "regex": ".*micronesia|^FM$|^FSM$",
        "iso3": "FSM",
    },
    "Moldova (the Republic of)": {
        "regex": ".*moldova|^MD$|^MDA$",
        "iso3": "MDA",
    },
    "Monaco": {
        "regex": "monaco|^MC$|^MCO$",
        "iso3": "MCO",
    },
    "Mongolia": {
        "regex": "mongolia|^MN$|^MNG$",
        "iso3": "MNG",
    },
    "Montenegro": {
        "regex": "(?!.*serbia).*montenegro|^ME$|^MNE$",
        "iso3": "MNE",
    },
    "Montserrat": {
        "regex": "montserrat|^MS$|^MSR$",
        "iso3": "MSR",
    },
    "Morocco": {
        "regex": "morocco|^MA$|^MAR$",
        "iso3": "MAR",
    },
    "Mozambique": {
        "regex": "mozambique|^MZ$|^MOZ$",
        "iso3": "MOZ",
    },
    "Myanmar": {
        "regex": "myanmar|burma|^MM$|^MMR$",
        "iso3": "MMR",
    },
    "Namibia": {
        "regex": "namibia|^NA$|^NAM$",
        "iso3": "NAM",
    },
    "Nauru": {
        "regex": "nauru|^NR$|^NRU$",
        "iso3": "NRU",
    },
    "Nepal": {
        "regex": "nepal|^NP$|^NPL$",
        "iso3": "NPL",
    },
    "Netherlands (the)": {
        "regex": "(?!.*antilles).*netherlands|^NL$|^NLD$",
        "iso3": "NLD",
    },
    "New Caledonia": {
        "regex": "new caledonia|^NC$|^NCL$",
        "iso3": "NCL",
    },
    "New Zealand": {
        "regex": "new zealand|NZ|n[\\., ] zealand|^NZ$|^NZL$",
        "iso3": "NZL",
    },
    "Nicaragua": {
        "regex": ".*nicaragua|^NI$|^NIC$",
        "iso3": "NIC",
    },
    "Niger (the)": {
        "regex": "(?!.*nigeria).*niger|^NE$|^NER$",
        "iso3": "NER",
    },
    "Nigeria": {
        "regex": "nigeria|^NG$|^NGA$",
        "iso3": "NGA",
    },
    "Niue": {
        "regex": "niue|^NU$|^NIU$",
        "iso3": "NIU",
    },
    "Norfolk Island": {
        "regex": "norfolk|^NF$|^NFK$",
        "iso3": "NFK",
    },
    "North Macedonia": {
        "regex": ".*macedonia|^MK$|^MKD$",
        "iso3": "MKD",
    },
    "Northern Mariana Islands (the)": {
        "regex": ".*mariana|^MP$|^MNP$",
        "iso3": "MNP",
    },
    "Norway": {
        "regex": "norway|^NO$|^NOR$",
        "iso3": "NOR",
    },
    "Oman": {
        "regex": "oman|^OM$|^OMN$",
        "iso3": "OMN",
    },
    "Pakistan": {
        "regex": "pakistan|^PK$|^PAK$",
        "iso3": "PAK",
    },
    "Palau": {
        "regex": "palau|^PW$|^PLW$",
        "iso3": "PLW",
    },
    "Palestine, State of": {
        "regex": ".*palestine|^PS$|^PSE$",
        "iso3": "PSE",
    },
    "Panama": {
        "regex": "panama|^PA$|^PAN$",
        "iso3": "PAN",
    },
    "Papua New Guinea": {
        "regex": ".*papua new guinea|^PG$|^PNG$",
        "iso3": "PNG",
    },
    "Paraguay": {
        "regex": "paraguay|^PY$|^PRY$",
        "iso3": "PRY",
    },
    "Peru": {
        "regex": "peru|^PE$|^PER$",
        "iso3": "PER",
    },
    "Philippines (the)": {
        "regex": ".*philippines|^PH$|^PHL$",
        "iso3": "PHL",
    },
    "Pitcairn": {
        "regex": ".*pitcairn|^PN$|^PCN$",
        "iso3": "PCN",
    },
    "Poland": {
        "regex": "poland|^PL$|^POL$",
        "iso3": "POL",
    },
    "Portugal": {
        "regex": "portugal|^PT$|^PRT$",
        "iso3": "PRT",
    },
    "Puerto Rico": {
        "regex": ".*puerto rico|^PR$|^PRI$",
        "iso3": "PRI",
    },
    "Qatar": {
        "regex": "qatar|^QA$|^QAT$",
        "iso3": "QAT",
    },
    "Romania": {
        "regex": "romania|^RO$|^ROU$",
        "iso3": "ROU",
    },
    "Russian Federation (the)": {
        "regex": ".*russia|^RU$|^RUS$",
        "iso3": "RUS",
    },
    "Rwanda": {
        "regex": "rwanda|^RW$|^RWA$",
        "iso3": "RWA",
    },
    "Réunion": {
        "regex": "réunion|reunion|^RE$|^REU$",
        "iso3": "REU",
    },
    "Saint Barthélemy": {
        "regex": ".*barthélemy|.*barthelemy|.*barths|.*barts|^BL$|^BLM$",
        "iso3": "BLM",
    },
    "Saint Helena, Ascension and Tristan da Cunha": {
        "regex": ".*helena|.*ascension|^SH$|^SHN$",
        "iso3": "SHN",
    },
    "Saint Kitts and Nevis": {
        "regex": ".*kitts|^KN$|^KNA$",
        "iso3": "KNA",
    },
    "Saint Lucia": {
        "regex": ".*lucia|^LC$|^LCA$",
        "iso3": "LCA",
    },
    "Saint Martin (French part)": {
        "regex": "(?=.*saint|.*st).*martin|^MF$|^MAF$",
        "iso3": "MAF",
    },
    "Saint Pierre and Miquelon": {
        "regex": ".*miquelon|^PM$|^SPM$",
        "iso3": "SPM",
    },
    "Saint Vincent and the Grenadines": {
        "regex": ".*vincent|.*grenadines|^VC$|^VCT$",
        "iso3": "VCT",
    },
    "Samoa": {
        "regex": "samoa|^WS$|^WSM$",
        "iso3": "WSM",
    },
    "San Marino": {
        "regex": "san marino|^SM$|^SMR$",
        "iso3": "SMR",
    },
    "Sao Tome and Principe": {
        "regex": ".*tome|.*tomé|^ST$|^STP$",
        "iso3": "STP",
    },
    "Saudi Arabia": {
        "regex": "saudi|^SA$|^SAU$",
        "iso3": "SAU",
    },
    "Senegal": {
        "regex": "senegal|^SN$|^SEN$",
        "iso3": "SEN",
    },
    "Serbia": {
        "regex": "(?!.*montenegro).*serbia|^RS$|^SRB$",
        "iso3": "SRB",
    },
    "Seychelles": {
        "regex": ".*seychelles|^SC$|^SYC$",
        "iso3": "SYC",
    },
    "Sierra Leone": {
        "regex": ".*sierra leone|selone|^SL$|^SLE$",
        "iso3": "SLE",
    },
    "Singapore": {
        "regex": "singapore|^SG$|^SGP$",
        "iso3": "SGP",
    },
    "Sint Maarten (Dutch part)": {
        "regex": "(?=.*sint|.*st).*maarten|^SX$|^SXM$",
        "iso3": "SXM",
    },
    "Slovakia": {
        "regex": ".*slovak|^SK$|^SVK$",
        "iso3": "SVK",
    },
    "Slovenia": {
        "regex": "slovenia|^SI$|^SVN$",
        "iso3": "SVN",
    },
    "Solomon Islands": {
        "regex": "solomon|^SB$|^SLB$",
        "iso3": "SLB",
    },
    "Somalia": {
        "regex": "somalia|^SO$|^SOM$",
        "iso3": "SOM",
    },
    "South Africa": {
        "regex": "(?=.*africa).*south|s[\\., ]|^ZA$|^ZAF$",
        "iso3": "ZAF",
    },
    "South Georgia and the South Sandwich Islands": {
        "regex": ".*sandwich|^GS$|^SGS$",
        "iso3": "SGS",
    },
    "South Sudan": {
        "regex": "(?=.*south).*sudan|^SS$|^SSD$",
        "iso3": "SSD",
    },
    "Spain": {
        "regex": "spain|^ES$|^ESP$",
        "iso3": "ESP",
    },
    "Sri Lanka": {
        "regex": "sri lanka|^LK$|^LKA$",
        "iso3": "LKA",
    },
    "Sudan (the)": {
        "regex": "(?!.*south).*sudan|^SD$|^SDN$",
        "iso3": "SDN",
    },
    "Suriname": {
        "regex": "surinam|^SR$|^SUR$",
        "iso3": "SUR",
    },
    "Svalbard and Jan Mayen": {
        "regex": "(?=.*svalbard).*jan mayen|^SJ$|^SJM$",
        "iso3": "SJM",
    },
    "Sweden": {
        "regex": "sweden|^SE$|^SWE$",
        "iso3": "SWE",
    },
    "Switzerland": {
        "regex": "switzerland|^CH$|^CHE$",
        "iso3": "CHE",
    },
    "Syrian Arab Republic (the)": {
        "regex": ".*syria|^SY$|^SYR$",
        "iso3": "SYR",
    },
    "Taiwan (Province of China)": {
        "regex": "taiwan|^TW$|^TWN$",
        "iso3": "TWN",
    },
    "Tajikistan": {
        "regex": "tajikistan|^TJ$|^TJK$",
        "iso3": "TJK",
    },
    "Tanzania, the United Republic of": {
        "regex": ".*tanzania|^TZ$|^TZA$",
        "iso3": "TZA",
    },
    "Thailand": {
        "regex": "thailand|^TH$|^THA$",
        "iso3": "THA",
    },
    "Timor-Leste": {
        "regex": "timor.*lest|east timor|^TL$|^TLS$",
        "iso3": "TLS",
    },
    "Togo": {
        "regex": "togo|^TG$|^TGO$",
        "iso3": "TGO",
    },
    "Tokelau": {
        "regex": "tokelau|^TK$|^TKL$",
        "iso3": "TKL",
    },
    "Tonga": {
        "regex": "tonga|^TO$|^TON$",
        "iso3": "TON",
    },
    "Trinidad and Tobago": {
        "regex": ".*trinidad|.*tobago|^TT$|^TTO$",
        "iso3": "TTO",
    },
    "Tunisia": {
        "regex": "tunisia|^TN$|^TUN$",
        "iso3": "TUN",
    },
    "Turkey": {
        "regex": "turkey|^TR$|^TUR$",
        "iso3": "TUR",
    },
    "Turkmenistan": {
        "regex": "turkmenistan|^TM$|^TKM$",
        "iso3": "TKM",
    },
    "Turks and Caicos Islands (the)": {
        "regex": "(?=.*turks).*caicos|^TC$|^TCA$",
        "iso3": "TCA",
    },
    "Tuvalu": {
        "regex": "tuvalu|^TV$|^TUV$",
        "iso3": "TUV",
    },
    "Uganda": {
        "regex": "uganda|^UG$|^UGA$",
        "iso3": "UGA",
    },
    "Ukraine": {
        "regex": "ukraine|^UA$|^UKR$",
        "iso3": "UKR",
    },
    "United Arab Emirates (the)": {
        "regex": ".*united arab emirates|UAE|^AE$|^ARE$",
        "iso3": "ARE",
    },
    "United Kingdom of Great Britain and Northern Ireland (the)": {
        "regex": "u\\.k\\.|united kingdom|gb$|g\\.b\\.|great britain|^GB$|^GBR$",
        "iso3": "GBR",
    },
    "United States Minor Outlying Islands (the)": {
        "regex": "(?=.*minor outlying).*(united states|u\\.s\\.|us$)|^UM$|^UMI$",
        "iso3": "UMI",
    },
    "United States of America (the)": {
        "regex": "u[\\.]*s[\\.]*a[\\.]*$|u[\\.]*s[\\.]*$|.*united states of america|(?!.*minor).*united states$|^US$|^USA$",
        "iso3": "USA",
    },
    "Uruguay": {
        "regex": "uruguay|^UY$|^URY$",
        "iso3": "URY",
    },
    "Uzbekistan": {
        "regex": "uzbekistan|^UZ$|^UZB$",
        "iso3": "UZB",
    },
    "Vanuatu": {
        "regex": "vanuatu|^VU$|^VUT$",
        "iso3": "VUT",
    },
    "Venezuela (Bolivarian Republic of)": {
        "regex": "venezuela|^VE$|^VEN$",
        "iso3": "VEN",
    },
    "Viet Nam": {
        "regex": "vietnam|viet nam|^VN$|^VNM$",
        "iso3": "VNM",
    },
    "Virgin Islands (British)": {
        "regex": "(?=.*virgin).*(u\\.k\\.|uk$|\\(uk\\)|british)|^VG$|^VGB$",
        "iso3": "VGB",
    },
    "Virgin Islands (U.S.)": {
        "regex": "(?=.*virgin).*(u\\.s\\.|us$|\\(us\\)|united states)|^VI$|^VIR$",
        "iso3": "VIR",
    },
    "Wallis and Futuna": {
        "regex": "(?=.*wallis).*futuna|^WF$|^WLF$",
        "iso3": "WLF",
    },
    "Western Sahara*": {
        "regex": "(?=.*western).*sahara|^EH$|^ESH$",
        "iso3": "ESH",
    },
    "Yemen": {
        "regex": "yemen|^YE$|^YEM$",
        "iso3": "YEM",
    },
    "Zambia": {
        "regex": "zambia|^ZM$|^ZMB$",
        "iso3": "ZMB",
    },
    "Zimbabwe": {
        "regex": "zimbabwe|^ZW$|^ZWE$",
        "iso3": "ZWE",
    },
    "Åland Islands": {
        "regex": "(?!.*[z]).*(a|å)land|^AX$|^ALA$",
        "iso3": "ALA",
    },
}
