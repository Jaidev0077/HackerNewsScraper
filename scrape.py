import requests
from bs4 import BeautifulSoup
import pprint

def sort_stories(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True) # sorting by key "votes" in dict

def create_custom_hn(links, subtext):
    hn = []
    for ind, item in enumerate(links):
        title = links[ind].getText()
        href = links[ind].get('href', None)
        votes = subtext[ind].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes':points})
    return sort_stories(hn)


res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
link = soup.select('.storylink')
subtext = soup.select('.subtext')
pprint.pprint(create_custom_hn(link, subtext))
print("\n\n\n\n\n\n")
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2= BeautifulSoup(res2.text, 'html.parser')
link2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')
pprint.pprint(create_custom_hn(link2, subtext2))