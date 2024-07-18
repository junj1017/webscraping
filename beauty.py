# 1. Fetch the pages (obtained a response object)
#    result = requests.get("www.google.com")
#
# 2. Page content
#    content = result.text
#
# 3. Create soup
#    soup = BeautifulSoup(content, "lxml")

# <article class="main-article">
#     <h1> Titanic (1997) </h1>
#     <p class="plot"> 84 years later ... </p>
#     <div class="full-script"> 13 meters. You ... </div>
# </article>

# soup.find('article', class_= "main_article") --> element
# soup.find('h1')
# soup.find_all("h2") --> list
from bs4 import BeautifulSoup
import requests

# website = "https://subslikescript.com/movie/Titanic-120338"
# result = requests.get(website)
# content = result.text
#
# soup = BeautifulSoup(content, 'lxml')
# # print(soup.prettify())
#
# box = soup.find('article', class_="main-article")
#
# title = box.find('h1').get_text()
#
#
# transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
#
#
# with open('titanic.txt', 'w') as file:
#     file.write(transcript)

root = 'https://subslikescript.com'
website2 = f'{root}/movies'
result2 = requests.get(website2)
content2 = result2.text

soup2 = BeautifulSoup(content2, 'lxml')
box2 = soup2.find('article', class_="main-article")
links = []
for link in box2.find_all('a', href=True):
    links.append(link['href'])

print(links)

for link in links:
    website2 = f'{root}/{link}'
    result2 = requests.get(website2)
    content2 = result2.text
    soup2 = BeautifulSoup(content2, 'lxml')
    box2 = soup2.find('article', class_="main-article")
    title = box2.find('h1').get_text()
    transcript = box2.find('div', class_='full-script').get_text(strip=True, separator=' ')
    with open(f'{title}.txt', 'w') as file:
        file.write(transcript)
