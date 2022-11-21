# ---- Workspace setup instructions: ----
# pip install requests
# pip install beautifulsoup4
# pip install lxml

# ---- Running the program ----
# python greyer.py

from bs4 import BeautifulSoup
import requests, re, sys

cont = 1
count = 0
while (cont == 1):
    first = input('Enter First Name: ')
    last = input('Enter Last Name: ')
    state = input('Enter state abbreviation: ')

    url = 'https://searchpeoplefree.com/find/'+ first +'-'+ last + '/' + state

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
    
    
    print()
    print(results['name'])
    print(results['age'])
    print(results['address'])
    print(results['phone'])
    print()
    
    if count != 0:
        previous = input('Do you want to get the previous search? ')
        if previous == 'yes':
            print()
            print(name.pop())
            print(age.pop())
            print(address.pop())
            print(phone.pop())
            print()
    else:
        cont = int(input('Enter a 1 to continue (anything else to quit): '))
        name = []
        name.append(results['name']) 
        age = []
        age.append(results['age']) 
        address = []
        address.append(results['address']) 
        phone = []
        phone.append(results['phone'])
        count += 1
        
