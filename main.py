import requests
from bs4 import BeautifulSoup
import json

results = []
url = "https://www.xpress.jobs/jobs?page=1"
num_page = 2

for current_page in range(0, num_page):
   response = requests.get(url)
   soup = BeautifulSoup(response.text, "html.parser")


   titles = soup.find_all('h3', 'job_listing-title')
   companies = soup.find_all('div', 'job_listing-company')
   locations = soup.find_all('div', 'location')
   descriptions = soup.find_all('div', 'job_listing-overview')

   for title, company, location, description in zip(titles, companies, locations, descriptions):
        data_item = {
                     "title": title.text.strip(),
                     "company": company.text.strip(),
                     "location": location.text.strip(),
                     "description": description.text.strip()
        }

        results.append(data_item)

   next_page_url = soup.find('a',class_='page-numbers next').get('href')
   page_url = f'https://www.xpress.jobs{next_page_url}'
   

print(json.dumps(results, indent=2))