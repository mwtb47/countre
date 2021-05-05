import re

from countre.regex_dict import regex_dict

# Import dictionary of country information named regex_dict which is
# stored in the file regex_dict.py.
regex_dict = regex_dict

regex_dict_index = {
    'country': 0,
    'country_short': 1,
    'sovereign': 2,
    'iso2': 3,
    'iso3': 4,
    'iso_num': 5,
    'ccTLD': 6,
    'calling_code': 7,
    'latitude': 8,
    'longitude': 9,
    'continent': 10,
    'sub_region': 11,
    'flag': 12,
    'total_area': 13,
    'land_area': 14,
    'water_area': 15,
    'capital': 16,
    'capital_latitude_sexa': 17,
    'capital_longitude_sexa': 18,
    'capital_longitude': 19,
    'capital_latitude': 20,
    'population_2019': 21,
    'gdp_2019': 22,
    'gdp_per_capita_2019': 23,
    'gdp_per_capita_ppp_2019': 24,
    'OECD': 25,
    'EU': 26,
    'EU_EEA': 27
}

def country_info(country_list, variables, no_match='no match'):
    '''
    Returns variables for each country in either a list or dictionary.

    Parameters:
        country_list (list) : list of country names, iso2 or iso3
                              codes to get variables for.

        variables (str, list) : choose one or more from the following
            {'country', 'country_short', 'iso2', 'iso3', 'iso_num',
             'calling_code', 'latitude', 'longitude', 'ccTLD', 'flag',
             'capital', 'continent', 'sub_region', 'sovereign',
             'OECD', 'EU', 'EU_EEA', 'flag', 'population_2019', 
             'capital_latitude_sexa', 'capital_longitude_sexa',
             'capital_longitude', 'capital_latitude', 'gdp_2019',
             'gdp_per_capita_2019', 'gdp_per_capita_ppp_2019',
            'total_area', 'land_area', 'water_area'}

        no_match (str) : value returned for a country if there is no
                         match. Default: 'no match'.

    Returns:
        list of values if only one variable given.
        dictionary of values if more than one varibale is given.
    '''

    if type(variables) == str:
        index = regex_dict_index[variables]
        variable_list = []
        for country in country_list:
            match = no_match
            for regex_pattern in regex_dict:
                if bool(re.match(regex_pattern, country, re.IGNORECASE)):
                    match = regex_dict[regex_pattern][index]
                    break
            variable_list.append(match)
        return variable_list

    else:
        indices = [regex_dict_index[v] for v in variables]
        variables_dict = {}
        for i, v in zip(indices, variables):
            variables_dict[v] = []
            for country in country_list:
                match=no_match
                for regex_pattern in regex_dict:
                    if bool(re.match(regex_pattern, country, re.IGNORECASE)):
                        match = regex_dict[regex_pattern][i]
                        break
                variables_dict[v].append(match)
        return variables_dict


eu_members = {}
for c in regex_dict:
    if regex_dict[c][regex_dict_index['EU']] == True:
        eu_members[c] = [regex_dict[c][regex_dict_index['country']],
                         regex_dict[c][regex_dict_index['iso2']],
                         regex_dict[c][regex_dict_index['iso3']]]

eu_member_index = {
    'country': 0,
    'iso2': 1,
    'iso3': 2
}

def eu_27(code='country'):
    """
    Return a list containing the country names, iso2 or iso3 codes for
    the 27 EU members.

    Parameters:
        code (str) : {'country', 'iso2', 'iso3'}

    Returns:
        list of 27 names, iso2 or iso3 codes.
    """
    index = eu_member_index[code]
    variable_list = []
    for country in eu_members:
        variable_list.append(eu_members[country][index])
    return variable_list


oecd_members = {}
oecd_members = {}
for c in regex_dict:
    if regex_dict[c][regex_dict_index['OECD']] == True:
        oecd_members[c] = [regex_dict[c][regex_dict_index['country']],
                           regex_dict[c][regex_dict_index['iso2']],
                           regex_dict[c][regex_dict_index['iso3']]]

oecd_member_index = {
    'country': 0,
    'iso2': 1,
    'iso3': 2
}

def oecd(code='country'):
    """
    Return a list containing the country names, iso2 or iso3 codes for
    the 37 OECD members.

    Parameters:
        code (str) : {'country', 'iso2', 'iso3'}

    Returns:
        list of 37 names, iso2 or iso3 codes.
    """
    index = oecd_member_index[code]
    variable_list = []
    for country in oecd_members:
        variable_list.append(oecd_members[country][index])
    return variable_list
