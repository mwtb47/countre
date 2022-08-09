# Codebook

The table below provides a summary of the variables included in ```countries_summary_data.csv```.

| Column | Variable | Data type | Source | Description |
| :- | :- | :- | :- | :- |
| 1 | ```calling_code``` | str | [countrycode.org](https://www.countrycode.org) | Country calling code. |
| 2 | ```capital_city``` | str | Wikipedia | Capital city of each country. In order for there to be only one entry per country, there are only coordinates for one of the cities. In South Africa, the coordinates for Pretoria are given. In Eswatini, the coordinates for Lobamba are given. |
| 3 | ```capital_latitude``` | float | Wikipedia | Decimal latitude of the capital city. |
| 4 | ```capital_latitude_sexa``` | str | Wikipedia | Sexagesimal latitude of the capital city. |
| 5 | ```capital_longitude``` | float | Wikipedia | Decimal longitude of the capital city. |
| 6 | ```capital_longitude_sexa``` | str | Wikipedia | Sexagesimal longitude of the capital city. |
| 7 | ```ccTLD``` | str | [Internet Assigned Numbers Authority](https://www.iana.org/domains/root/db) | Country code top-level domain. Countries without ccTLDs have 'Not assigned'. |
| 8 | ```continent``` | str | [United Nations Statistics Division](https://unstats.un.org/unsd/methodology/m49/overview/) | Continent which the country is a part of. Antartica and some islands are not allocated a continent. |
| 9 | ```country``` | str | [International Organization for Standardization](https://www.iso.org/iso-3166-country-codes.html) | Country name. |
| 10 | ```country_short``` | str | Collected manually | Short version of country name that is often seen in the news, on charts etc. |
| 11 | ```country_sv``` | str | [Wikipedia](https://sv.wikipedia.org/wiki/ISO_3166) | Country names in Swedish. |
| 12 | ```currency_iso``` | str | [International Organization for Standardization](https://www.iso.org/iso-4217-currency-codes.html) and manual collection | Currency ISO code. The offcial ISO code is used when assigned, otherwise the commercially used three letter code is used.  |
| 13 | ```currency_name``` | str | [International Organization for Standardization](https://www.iso.org/iso-4217-currency-codes.html) and manual collection | Currency name. |
| 14 | ```currency_symbol``` | str | [International Organization for Standardization](https://www.iso.org/iso-4217-currency-codes.html) and manual collection | Currency symbol. |
| 15 | ```EU``` | Boolean | [European Union](https://europa.eu/european-union/about-eu/countries_en) | True/False as to whether the country is a member of the EU. |
| 16 | ```EU_EEA``` | Boolean | [European Union](https://europa.eu/european-union/about-eu/countries_en), [Eurostat](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:European_Economic_Area_(EEA)) | True/False as to whether the country is a member of the EU or EEA. |
| 17 | ```flag``` | str |  | Emoji of the country's flag. |
| 18 | ```gdp_2021``` | float | [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD) | GDP (current USD) in 2021. |
| 19 | ```gdp_capita_2021``` | float | [World Bank](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD) | GDP per capita (current USD) in 2021. |
| 20 | ```gdp_capita_ppp_2021``` | float | [World Bank](https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.CD) | GDP per capita at purchasing power parity (current international \$) in 2021. |
| 21 | ```gini``` | float | [World Bank](https://data.worldbank.org/indicator/SI.POV.GINI) | Gini coefficient from the most recently calculated year. |
| 22 | ```hci``` | float | [World Bank](https://data.worldbank.org/indicator/HD.HCI.OVRL) | Human Capital Index. |
| 23 | ```hdi``` | float | [United Nations Development Programme](http://hdr.undp.org/en/content/human-development-index-hdi) | Human Development Index from the 2020 report. |
| 24 | ```iso2``` | str | [International Organization for Standardization](https://www.iso.org/iso-3166-country-codes.html) | Alpha-2 code. |
| 25 | ```iso3``` | str | [International Organization for Standardization](https://www.iso.org/iso-3166-country-codes.html) | Alpha-3 code. |
| 26 | ```iso_numeric``` | int | [International Organization for Standardization](https://www.iso.org/iso-3166-country-codes.html) | ISO 3166-1 numeric code. |
| 27 | ```land_area``` | float | [CIA World Factbook](https://www.cia.gov/library/publications/download/) | Land area of the country (km<sup>2</sup>). |
| 28 | ```latitude``` | float | Collected manually | Decimal latitude of an approximate centre point for the country (location based on desired point for country marker on map plots). |
| 29 | ```latitude_sexa``` | str | Collected manually | Sexagesimal latitude of an approximate centre point for the country (location based on desired point for country marker on map plots). |
| 30 | ```longitude``` | float | Collected manually | Decimal longitude for the approximate centre point for the country (location based on desired point for country marker on map plots). |
| 31 | ```longitude_sexa``` | str | Collected manually | Sexagesimal longitude for the approximate centre point for the country (location based on desired point for country marker on map plots). |
| 32 | ```NATO``` | Boolean | [NATO](https://www.nato.int/cps/en/natolive/nato_countries.htm) | True/False as to whether the country is a NATO member. |
| 33 | ```OECD``` | Boolean | [OECD](https://www.oecd.org/about/members-and-partners/) | True/False as to whether the country is an OECD member. |
| 34 | ```OPEC``` | Boolean | [OPEC](https://www.opec.org/opec_web/en/about_us/25.htm) | True/False as to whether the country is an OPEC member. |
| 35 | ```population``` | float | [World Bank](https://data.worldbank.org/indicator/SP.POP.TOTL) | Population from the most recently estimated year. |
| 36 | ```sub_region``` | str | [United Nations Statistics Division](https://unstats.un.org/unsd/methodology/m49/overview/) | Sub-regions are: Southern Asia, Southern Europe, Northern Africa, Polynesia, Middle Africa, Caribbean, South America, Western Asia, Australia and New Zealand, Western Europe, Eastern Europe, Central America, Western Africa, Northern America, Southern Africa, South-Eastern Asia, Eastern Africa, Eastern Asia, Northern Europe, Melanesia, Micronesia, Central Asia. Some islands are not allocated a sub region. |
| 37 | ```total_area``` | float | [CIA World Factbook](https://www.cia.gov/library/publications/download/) | Total land and water area of the country (km<sup>2</sup>). |
| 38 | ```water_area``` | float | [CIA World Factbook](https://www.cia.gov/library/publications/download/) | Water area of the country (km<sup>2</sup>). |