import requests
from bs4 import BeautifulSoup
import urllib
import ConfigParser
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Read username and password from config file

configFile = "/home/hridoy/Work/youlikehits-scraper/config.txt"
config = ConfigParser.ConfigParser()
config.readfp(open(configFile))

# Fill in your details here to be posted to the login form.
datas = {
    'username': config.get('Credentials', 'username'),
    'pass': config.get('Credentials', 'password')
}
content = None

print "****** YOULIKEHITS PARSER WORKING ******"


# Use 'with' to ensure the session context is closed after use.

with requests.Session() as s:
    # login to youlikehits using payload parameters
        p = s.post('https://youlikehits.com/login.php', data=datas, verify=False)
        
        PageContent = s.get("https://youlikehits.com/newaddtwitter.php" + str(count)).content

      
        # Find all iframes in the web page
        soup = BeautifulSoup(PageContent, 'html.parser')
        tag = soup.find_all('a')


        # Get URLs of retweets
        URLs = []
        for items in tag:
            soup = BeautifulSoup(str(items), 'html.parser')
            tag1 = soup.find_all('a')[0]
            URLs.append(tag1['href'])
