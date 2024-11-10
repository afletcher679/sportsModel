import requests
from bs4 import BeautifulSoup

def get_table_element(html):
    # Get the table element
    table = html.find('table', class_='stats_table')
    return table

def get_table_rows(table_html):
    # Get the table rows
    rows = table_html.find_all('tr')
    return rows

def get_table_headers(table):
    # Get the table headers
    header = table.find('thead')
    headers = header.find_all('th')
    # Print the headers
    for title in headers:
        print(title.text)
    return headers

def get_table_data(table):
    # Get the table data
    body = table.find('tbody')
    table_rows = get_table_rows(body)
    for row in table_rows:
        # Get the data
        data = body.find_all('td')

        # Print the data
        for d in data:
            print(d.text)

# Making a GET request
r = requests.get('https://www.pro-football-reference.com/years/2024/passing.htm')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Find the table
s = soup.find('table', class_='stats_table')
get_table_data(s)

#print(h)

