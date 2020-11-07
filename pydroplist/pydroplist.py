# AUTHOUR: CALVIN KINATEDER
import requests, json, bs4

def latest(brand, withDates=False):    
    droplist = list()
    
    if brand == 'supreme':
        base_url = 'https://www.supremecommunity.com/'
        weeks_ext = 'season/fall-winter2020/droplists/'
        weeks_list = requests.get(base_url+weeks_ext)
        soup = bs4.BeautifulSoup(weeks_list.content, 'html.parser')    
        latest_url = base_url+soup.find("div", {"id": "box-latest"}).a['href']

        drop_page = requests.get(latest_url)
        drop_soup = bs4.BeautifulSoup(drop_page.content, 'html.parser')    
        droppy = drop_soup.find_all('h2', 'name item-details item-details-title')        

        for i in droppy:
            droplist.append(i.text)
        
    elif brand == 'nike':
        pass
    return droplist