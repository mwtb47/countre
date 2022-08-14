"""Script to create the countre module _regex_dict.py.

The countre _regex_dict.py module contains a dictionary holding all the
data used by the package. The dictionary keys are the regex patterns
used to match the country names and the values are a dictionary of
attributes and their values.

Functions:
"""


import pandas as pd

from regex_dict import regex_dict


df = pd.read_csv(
    "country_data/countries_summary_data.csv", keep_default_na=False, na_values=[""]
)

# This has to be set outside of a function as black removes the
# indentation in the blank rows when it is set in a function.
# This results in the module file being incorrectly formatted.
MODULE_HEADER = '''"""Module with dictionary containing all country data."""


data = '''


def create_dictionary() -> dict[str, dict[str, str | int | float | bool]]:
    """Create the dictionary used by countre from the csv file.

    Returns:
        Dictionary containing all data.
    """
    data = {}

    for country, attributes in regex_dict.items():
        df_country = df[df.iso3 == attributes["iso3"]]
        if len(df_country) == 0:
            print(f"Country data not found - {country}")
            continue
        data[attributes["regex"]] = get_attributes(df_country)
    return data


def get_attributes(df_country: pd.DataFrame) -> dict[str, str | int | float | bool]:
    """Return a dictionary of attributes for a given country.

    Args:
        df_country: Single DataFrame row containing data for
            a single country.

    Returns:
        A dictionary with attributes as keys and attribute
        values as values.
    """
    return {
        col: "" if pd.isna(df_country[col].iloc[0]) else df_country[col].iloc[0]
        for col in df.columns
    }


def create(
    data: dict[str, dict[str, str | int | float | bool]], module_header: str
) -> None:
    """Create the _regex_dict.py module.

    Args:
        data: The dictionary containing all data.
        module_header: String which forms the start of the module.
    """
    module_string = module_header + str(data)

    with open("countre/_regex_dict.py", "w", encoding="utf-8") as file_handle:
        file_handle.write(module_string)


def main(module_header: str) -> None:
    """Main function to run script.

    Args:
        module_header: String which forms the start of the module.
    """
    data = create_dictionary()
    create(data, module_header)


if __name__ == "__main__":
    main(MODULE_HEADER)
