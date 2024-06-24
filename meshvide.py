import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
# response.raise_for_status()  amowmebs monacemebi modis tu araa, anu status-code-it

soup = BeautifulSoup(response.text, 'html.parser')
results_container = soup.find('div', id='ResultsContainer')
job_titles = results_container.find_all('h2', class_='title is-5')

# cikli gadavatarot ro yvela daibewhdos
for job_title in job_titles:
    print(job_title.text.strip())
