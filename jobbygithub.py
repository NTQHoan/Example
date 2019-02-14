
import requests
from bs4 import BeautifulSoup as bs
import sqlite3

url = "https://github.com/awesome-jobs/vietnam/issues"
conn = sqlite3.connect("example.db")
def solve():
    c = conn.cursor()
    c.execute('''CREATE TABLE jobs (company name)''')
    req = requests.get(url)
    soup = bs(req.text, 'html.parser')
    a = soup.findAll('a', {'class':'link-gray-dark v-align-middle no-underline h4 js-navigation-open'})
    for txt in a:
        c.execute('''INSERT INTO jobs VALUES'''+"(" + "'" +(txt.text)+"'"+")")
    conn.commit()
    conn.close()

def main():
    print(solve())

if __name__ == 'main':
    main()