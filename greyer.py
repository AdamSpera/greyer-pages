# pip install requests
# pip install beautifulsoup4
# pip install lxml

from bs4 import BeautifulSoup
import requests, re

url = 'https://searchpeoplefree.com/find/brey-rivera/pa'

response = requests.get(url)

html = response.text

soup = BeautifulSoup(response.content, 'lxml')

# print(soup.prettify())
results = {
    'name': soup.find_all('h2')[0].text.replace("\n", "").split(' in')[0],
    'age': re.sub(' +', ' ', soup.find_all('h3')[0].text.replace("\n", " ")).strip(),
    'address': soup.find_all('address')[0].text.replace("\n", ""),
    'phone': 'No Phone' if soup.find_all('h4')[0].text.replace("\n", "").strip() == 'Email Address' else soup.find_all('h4')[0].text.replace("\n", "").strip().split('-Current')[0],
}

print(results['name'])
print(results['age'])
print(results['address'])
print(results['phone'])


# textContent = []
# the_latest = soup.find_all("h3").text
# textContent.append(the_latest)

# pd.DataFrame(textContent)
