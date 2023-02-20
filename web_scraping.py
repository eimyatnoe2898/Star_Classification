import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup
import requests
import json

url = "https://universe.nasa.gov/stars/types/"

#request a get request to the url and get the content of the page and store it in result
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
mainContent = doc.find("div", class_="wysiwyg_content")
starTitles = mainContent.find_all("h2")
stars = []

#loop over
for starTitle in starTitles[1:]:
    star = {}
    starDetail = starTitle.find_next_sibling("p")
    stargazerDiv = starTitle.find_next_sibling("div", class_="snippet_box_container with_frame_title")
    stargazerCtnr = stargazerDiv.find("fieldset")
    starGazer = stargazerCtnr.find("p")
    # print(starGazer.text)
    star["starName"] = starTitle.text
    star["starDetail"] = starDetail.text
    star["starGazer"] = starGazer.text.strip()
    stars.append(star)

for eachStar in stars:
    print(eachStar)


with open("stars.json", "w") as outfile:
        json.dump(stars, outfile)




