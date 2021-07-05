# ScottishCovidOverview.py - Returns details on the current COVID-19 cases and deaths in Scotland.
# Data and API details can be located here:
# https://www.opendata.nhs.scot/dataset/covid-19-in-scotland/resource/e8454cf0-1152-4bcb-b9da-4343f625dfef?inner_span=True

# Imports
import argparse
import os
import sys
import requests
import json


class Covid:
    def __init__(self):
        self.default_loc = ['Aberdeen City', 'Aberdeenshire', 'Angus', 'Argyll & Bute', 'City of Edinburgh',
                            'Clackmannanshire', 'Dumfries & Galloway', 'Dundee City', 'East Ayrshire',
                            'East Dunbartonshire', 'East Lothian', 'East Renfrewshire', 'Falkirk', 'Fife',
                            'Glasgow City', 'Highland', 'Inverclyde', 'Midlothian', 'Moray', 'Na h-Eileanan Siar',
                            'North Ayrshire', 'North Lanarkshire', 'Orkney Islands', 'Perth & Kinross', 'Renfrewshire',
                            'Scottish Borders', 'Shetland Islands', 'South Ayrshire', 'South Lanarkshire', 'Stirling',
                            'West Dunbartonshire', 'West Lothian']
        self.locations = []
        self.positive = []
        self.total_cases = []
        self.deaths = []
        self.total_deaths = []

    def call_api(self):
        """
        Makes a call to the CKAN API to retrieve the most recent COVID-19 data
        """
        try:
            url = 'https://www.opendata.nhs.scot/api/3/action/datastore_search?resource_id=e8454cf0-1152-4bcb-b9da-4343f625dfef'
            raw_data = requests.get(url)  # Downloads the API data results
            data = json.loads(raw_data.content)  # Reads the JSON data from the API results

            # Pull the locations, case numbers and death values from the JSON data and add each to a list
            for area in data["result"]["records"]:
                for k, v in area.items():
                    if k == "CAName":
                        self.locations.append(v)
                    if k == "NewPositive":
                        self.positive.append(v)
                    if k == "TotalCases":
                        self.total_cases.append(v)
                    if k == "NewDeaths":
                        self.deaths.append(v)
                    if k == "TotalDeaths":
                        self.total_deaths.append(v)
        except requests.exceptions.ConnectTimeout:
            print("Error! The connection timed out when attempting to connect to API")
            sys.exit()
        except requests.ConnectionError:
            print("Error! Network error when attempting to connect to API")
            sys.exit()
        except requests.exceptions.RequestException:
            print("Error! There was a network error when attempting to connect to API")
            sys.exit()

    def get_pos(self, area):
        """
        Gets the index position of a given area name from the locations list.
        Used to pull all relevant data using same position, as each list is equal in length.
        :param area: (str) The local authority name
        :return: (int) The list position of the local authority name
        """
        try:
            pos = self.locations.index(area)
            return pos
        except ValueError:
            print("Error! Given local authority could not be found in the API results.".format(name))
            sys.exit()

    def get_area(self, area):
        """
        Returns the COVID-19 data for the given local authority.
        :param area: (str) The user inputted name of the local authority
        """
        pos = self.get_pos(area)
        print("{}\n\tNew Positive cases: {}\n\tTotal cases: {}\n\tNew Deaths: {}\n\tTotal Deaths: {}".format(
            self.locations[pos], self.positive[pos], self.total_cases[pos], self.deaths[pos], self.total_deaths[pos]))

    def get_overview(self):
        """
        Returns an overview of all COVID-19 data for all local authorities to the screen
        """
        for x in range(len(self.locations)):
            print("{}\n\tNew Positive cases: {}\n\tTotal cases: {}\n\tNew Deaths: {}\n\tTotal Deaths: {}".format(
                self.locations[x], self.positive[x], self.total_cases[x], self.deaths[x], self.total_deaths[x]))

    def get_default(self):
        """
        Returns the list of default names for each local authority
        :return: (list) A list of the local authority names that can be used with the -a option
        """
        return self.default_loc


# argparse options that can be called by the user
parser = argparse.ArgumentParser(prog=os.path.basename(__file__), usage='%(prog)s [option]',
                                 description='---- Scottish Covid Data Overview ---- ',
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
group = parser.add_mutually_exclusive_group()
group.add_argument('-o', '--overview', required=False, action='store_true', help='Returns overview of each Local '
                                                                                 'Authority and their cases/deaths.')
group.add_argument('-a', '--area', required=False, nargs='*', help='Get COVID-19 data on a specific local authority. '
                                                                   'Names that are longer than a single word require '
                                                                   'speech marks around them e.g. \"Perth & Kinross\"')
args = parser.parse_args()

# Creates a COVID object that makes use of the API data
covid = Covid()

# Command line options and how they are handled
if args.overview is True:               # Returns an overview of all the API results
    print("Calling API...")
    covid.call_api()
    print("---- Scottish Covid Data Overview ----")
    covid.get_overview()
# Returns a list of details on the specific local authority name
# Any names that are greater that 1 word long require "" around them, due to Windows requirements
elif args.area is not None:
    print("Calling API...")
    covid.call_api()
    print("---- Scottish Covid Data Overview ----")
    # Checks if the given user input is more than 1 word and joins them together
    if len(args.area) > 1:
        name = ' '.join(args.area)
    else:
        name = str(args.area[0])
    # Checks that the given local authority is valid, otherwise informs user of available names
    if name not in covid.get_default():
        print("Error! Given location name '{}' not valid. Must be one of the following:".format(name))
        for name in covid.get_default():
            print("{}, ".format(name), end='')
    else:
        # Return the COVID-19 data for the given local authority
        covid.get_area(name)
else:
    # Defaults to the argparse help options
    parser.print_help()
