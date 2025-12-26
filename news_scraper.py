"""I HAVE LEARNED WEB SCRAPİNG. I was busy because of christmas for these days. Happy new years for everyone."""

import requests
from bs4 import BeautifulSoup


url = "https://news.ycombinator.com/"
response = requests.get(url, timeout=10)
soup = BeautifulSoup(response.text, 'html.parser')


headlines = soup.find_all('span', class_='titleline')

print("--- 🕵️‍♂️ DAILY INTELLIGENCE REPORT ---")

for rank, item in enumerate(headlines, 1):
    title = item.a.text      
    link = item.a['href']
    print(f"{rank}. {title}")
    if rank == 15: break 
