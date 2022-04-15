from cgitb import html
import requests
from bs4 import BeautifulSoup

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')

# description = jobs.find('ul', class_='list-job-dtl clearfix').find('li')

for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name').text
    experience = job.find('ul', {'class': 'top-jd-dtl clearfix'}).find('li').text[11:]
    skills = job.find('span', {'class': 'srp-skills'}).text.replace(' ', '')

    print(f'Company Name: {company_name}\nExperience: {experience}\nSkills: {skills}')

    print('')