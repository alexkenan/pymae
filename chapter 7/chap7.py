# !/usr/bin/env python3
"""
Get aluminum properties from Engineering Toolbox and write them to excel

"""
import requests
from bs4 import BeautifulSoup
import openpyxl


def scrape_website(address: str) -> str:
    """
    Scrape the properties website and return the response text
    :param address: URL of website to scrape
    :return: str as response.text
    """
    headers = {'user-agent':
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0"}

    r = requests.get(address, headers=headers)
    return r.text


def extract_properties_from_response(response: str) -> list:
    """
    Use BeautifulSoup to extract the table and build it as a list that contains lists of the properties

    Example: 1100 	  	10.0 	3.75 	3.5 	11 from the website becomes [1100, 10.0, 3.75, 3.5, 11]
     inside the list

    :param response: str of the website HTML from requests.get().text
    :return: list of properties
    """
    toreturn = []
    soup = BeautifulSoup(response, features="lxml")
    tag_id = ".large"

    # table = soup.find('table', class_="large tablesorter")
    table = soup.select(tag_id)[0]
    for thead in table:
        for tr in thead:
            if len(tr) == 6:
                # this means we have the header row of the table
                internal_list = []
                for td in tr:
                    if td:
                        internal_list.append(td.text)
                toreturn.append(internal_list)
            elif len(tr) == 13:
                # this means we have the material row
                internal_list = []
                for td in tr:
                    if td and td.string != ' ':
                        if str(td.string) == '\xa0':
                            value = 'None'
                        else:
                            value = str(td.string)
                        internal_list.append(value)
                toreturn.append(internal_list)
    return toreturn


def create_spreadsheet(info: list) -> None:
    """
    Create a spreadsheet with the info list. Assumes that info[0] is a list of column headers

    :param info: All info to be written to the spreadsheet
    :return: None
    """
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = 'aluminum'
    destination = '/Users/Alex/Desktop/aluminum_properties.xlsx'

    row_counter = 1
    column_counter = 1
    for row in info:
        # row represents each "line" or "row" of the table we scraped
        for cell in row:
            # cell represents each column or cell in the row
            try:
                text = float(cell)
            except ValueError:
                text = cell
            worksheet.cell(row=row_counter, column=column_counter, value=text)
            column_counter += 1
        column_counter = 1
        row_counter += 1

    workbook.save(filename=destination)


if __name__ == "__main__":
    url = "https://www.engineeringtoolbox.com/properties-aluminum-pipe-d_1340.html"
    website_text = scrape_website(url)
    results = extract_properties_from_response(website_text)
    create_spreadsheet(results)
