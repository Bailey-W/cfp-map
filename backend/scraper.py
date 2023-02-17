import requests
from bs4 import BeautifulSoup

conferenceList = []

for i in range(1,4):
    # Fetches the first page of the list of conferences
    r = requests.get(f'http://www.wikicfp.com/cfp/call?conference=robotics&page={i}')

    # Parses the previously fetched html
    soup = BeautifulSoup(r.content, 'html.parser')

    # find the div containing the page contents
    div = soup.find('div', class_ = 'contsec')

    # Find a list of all rows containing conference information
    ## Note: Each conference is spread across 2 rows
    table = div.findChild("table").findChildren('tr', recursive=False)[2]
    ## Note: removes the first 'tr' entry since it acts as a header row
    conferenceHTML = table.findChild("table").findChildren('tr', recursive=False)[1:]


    # parses every other row of the table
    for conf in range(0, len(conferenceHTML), 2):
        row1_columns = conferenceHTML[conf].findChildren('td')
        row2_columns = conferenceHTML[conf + 1].findChildren('td')
        currentConference = {'name': row1_columns[0].text, 
                            'link': 'http://www.wikicfp.com' + row1_columns[0].findChild('a').get('href'),
                            'location': row2_columns[1].text,
                            'deadline': row2_columns[2].text}
        conferenceList.append(currentConference)
    
for conf in conferenceList:
    print(conf)