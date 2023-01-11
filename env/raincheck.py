from bs4 import BeautifulSoup
import requests
def raincheck():
    URL = 'https://weather.gc.ca/city/pages/on-94_metric_e.html'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="mainContent")
    weath = results.find_all('dd', string='Cloudy')
    print(weath)
    if len(weath)>=0:
        return True
    return False


