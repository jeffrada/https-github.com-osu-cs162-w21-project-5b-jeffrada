# Author: Adam Jeffries
# Date: 2/3/2021
# Description: Reads a JSON file containing data on Nobel Prizes and allows the user to search that data.

import json


class NobelData:
    """
    Represents an object that retrieves information from a JSON file
    """
    def __init__(self, json_file):
        self.json_file = json_file

        with open(self.json_file, 'r') as infile:
            self.restored_list = json.load(infile)

    def search_nobel(self, year, category):
        sorted_result = []
        for obj in self.restored_list["prizes"]:
            if obj["year"] == year and obj["category"] == category:
                for laureate in obj["laureates"]:
                    sorted_result.append(laureate["surname"])
        sorted_result.sort()
        return sorted_result
