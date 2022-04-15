#    in this program we are going to extract data froma github users profile 
#   using beautifulsoup 
#   we are going to import some modules: bs4 and requests

from bs4 import BeautifulSoup as bs
import requests

github_username= input("Enter your github user_name: ")

url = "https://github.com/"+  github_username

req_info = requests.get(url)

soup= bs(req_info.content, "html.parser")

prof_image = soup.find('img', {'alt': 'Avatar'})['src']

print(prof_image)