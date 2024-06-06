import requests
from bs4 import BeautifulSoup

url = "https://dining.purdue.edu/menus/"

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142 Safari/537.36',  # Replace with actual Chrome version
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',  # Add Brotli compression support (optional)
  'Connection': 'keep-alive',
}

request = requests.get(url=url, headers=headers)
print(request.text)
soup = BeautifulSoup(request.text, 'html.parser')

# text_diningcourt = soup.find('div', style
# print(len(text_diningcourt))
# for element in text_diningcourt:
#     print(element)
#     print("/n/n/n/n/n/n/n/n/n/n")




