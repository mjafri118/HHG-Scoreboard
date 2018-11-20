from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
import datetime, requests

url = "https://tianchi.aliyun.com/competition/information.htm?raceId=231692"

def submissionCount():

    #Opening Connection, Grabbing the Page
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    #Parse the HTML
    page_soup = soup(page_html, "html.parser")
    submissionCount = page_soup.findAll("span", {"class":"span-6"})[1].text
    print(submissionCount)
    return submissionCount


def date():
    d = datetime.date.today()
    month = str('%02d' % d.month)
    day = str('%02d' % d.day)
    year = str('%02d' % d.year)
    return month + "/" + day + "/" + year

def submitForm():
    formUrl = "https://docs.google.com/forms/d/e/1FAIpQLSf34oKQNeWO2XwFLgheqAI6y1YPW7i2VxRx8t8AK9YCvka3LQ/formResponse"
    data = {
        "usp": "pp_url",
        "entry.585634914":date(),
        "entry.237934334":submissionCount()
    }
    r = requests.post(url=formUrl, data=data)

submitForm()
