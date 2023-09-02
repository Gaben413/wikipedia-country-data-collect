from bs4 import BeautifulSoup
import requests

def FetchCountriesLinks():
    URL = 'https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Asia'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    tables = soup.find_all("table")

    links_dict = []

    targets = [1, 2, 3, 4, 5]

    for target in targets:
        for row in tables[target].tbody.find_all('tr'):
            columns = row.find_all('td')

            if(columns != []):
                if '#' not in columns[2].find("a").get("href"):
                    #print(f'LINK: {columns[2].find("a").get("title")} | COUNTRY: {columns[2].find("a").get("href")}')
                    links_dict.append({
                        'country': columns[2].find("a").get("title"),
                        'link': columns[2].find("a").get("href"),
                    })

    return links_dict

dicts = FetchCountriesLinks()

for dict in dicts:
    print(f"COUNTRY: {dict['country']} | LINK: {dict['link']}")