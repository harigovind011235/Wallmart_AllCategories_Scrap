from bs4 import BeautifulSoup
from requests_html import HTMLSession
import json

session = HTMLSession()

response  = session.get('https://www.walmart.com/all-departments')
response.html.render(sleep=1, keep_page=True,scrolldown=4)

all_a_tags = response.html.find('a')
categorylist = []

for data in all_a_tags:
    categoryname = data.text
    categorylink = str(data.absolute_links)

    if categoryname and categorylink is None:
        continue

    else:
        mydict = {'categoryname':categoryname,
                 'categorylink':categorylink}

        categorylist.append(mydict)

        json_text = json.dumps(categorylist,indent=8,sort_keys=True)
        with open('wallmartcategories2.json', 'w') as json_file:
            json_file.write(json_text)
