import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd

url = "https://docs.python.org/3/library/random.html"
response = urllib.request.urlopen(url)
webContent = response.read()
soup = BeautifulSoup(webContent, 'html.parser')

# Find all dt tags with id='random'
dt_tags = soup.find_all('dt', id=re.compile('random'))

data = []
for dt in dt_tags:
    class_name = dt.get_text(strip=True)
    dd = dt.find_next_sibling('dd')
    description = dd.get_text(strip=True) if dd else ''
    data.append((class_name, description))

df = pd.DataFrame(data, columns=['Class Name', 'Description'])
print(df)
