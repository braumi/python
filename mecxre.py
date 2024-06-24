import mechanicalsoup
import pandas as pd
from sqlalchemy import create_engine

url = "https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions"
# browseris start
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)
#pageis amogheba 
soup = browser.get_current_page()

# header da datas povna
headers = [header.text.strip() for header in soup.select("th.table-rh_")]
rows = soup.select("table.wikitable tbody tr")

data = []
for row in rows:
    cells = row.find_all("td")
    if len(cells) == len(headers):
        data.append([cell.text.strip() for cell in cells])

df = pd.DataFrame(data, columns=headers)
column_names = [
    "Founder",
    "Maintainer",
    "Initial_Release_Year",
    "Current_Stable_Version",
    "Security_Updates",
    "Release_Date",
    "System_Distribution_Commitment",
    "Forked_From",
    "Target_Audience",
    "Cost",
    "Status"
]

# Aaxali column-namebis mititteba 
df.columns = column_names
#bazis sheqmna 
engine = create_engine('sqlite:///linux_distributions.db')
df.to_sql('linux_distributions', engine, index=False, if_exists='replace')

# dbdan wakitxva 
df_from_db = pd.read_sql('linux_distributions', engine)
print(df_from_db)
