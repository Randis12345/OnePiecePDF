import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from PIL import Image


def digcri(x):
    return "0"*(3-len(str(x))) + str(x)

CLASS_NAME = "mb-3 mx-auto js-page"

# downloads chapters from START to END 
START = 1
END = 10

TIME_START = datetime.now()

for i in range(START,END):
    url = f"https://ww9.readonepiece.com/chapter/one-piece-digital-colored-comics-chapter-{digcri(i)}/"
    html = requests.get(url).text
    soap = BeautifulSoup(html,"html.parser")
    
    urls = [repr(x['src'])[1:-1].removesuffix(r"\r") for x in soap.findAll("img", class_=CLASS_NAME) if x.has_attr('src')]

    images = [Image.open(requests.get(x,stream=True).raw).convert('RGB') for x in urls]
    
    images[0].save(rf'{os.path.dirname(__file__)}\\OnePiece{i}.pdf', save_all=True, append_images=images[1:])
    perc = (i+1 - START)/(END-START)
    print(f"Downloaded Chapter {i} {round(perc*100,2)}%")
    print("ETA:",((datetime.now()-TIME_START)/perc + datetime.now()).strftime("%I:%M %p"))


