# ---- Workspace setup instructions: ----
# pip install requests
# pip install beautifulsoup4
# pip install lxml

# ---- Running the program ----
# python greyerTerminal.py

from bs4 import BeautifulSoup
import requests, re, sys

while (1 == 1):
    # Get user input for target
    first = input('Enter First Name: ')
    last = input('Enter Last Name: ')
    state = input('Enter state abbreviation: ')

    # Build URL from user input
    url = 'https://searchpeoplefree.com/find/'+ first +'-'+ last + '/' + state

    # Get response from URL
    response = requests.get(url)

    # Parse response for HTML
    html = response.text

    # Parse HTML for readable data using soup
    soup = BeautifulSoup(response.content, 'lxml')

    # Parse the soup HTML for the top result
    results = {
        'name': soup.find_all('h2')[0].text.replace("\n", "").split(' in')[0],
        'age': re.sub(' +', ' ', soup.find_all('h3')[0].text.replace("\n", " ")).strip(),
        'address': soup.find_all('address')[0].text.replace("\n", ""),
        'phone': 'No Phone' if soup.find_all('h4')[0].text.replace("\n", "").strip() == 'Email Address' else soup.find_all('h4')[0].text.replace("\n", "").strip().split('-Current')[0],
    }
    
    # Print the results
    print()
    print(results['name'])
    print(results['age'])
    print(results['address'])
    print(results['phone'])
    print()
    
    # Ask user if they want to search again
    if (input('Would you like to search again? (Enter anything to continue, 0 to exit) ') == '0'):
        exit()