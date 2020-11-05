# This program will fetch data like number of followers and following
# from the specified instagram account using beautifulSoup Module

import requests
from bs4 import BeautifulSoup

# respective website url
URL = "https://www.instagram.com/{}/"

# function to scrape the data
def scrape(username):
    # .format is used to form url with username
    full_url = URL.format(username)
    # print(full_url)

    # using requests to get data from url
    r = requests.get(full_url)

    # to fetch content from the webpage
    s = BeautifulSoup(r.text,"lxml")

    # getting only the followers and following content from the content
    tag = s.find("meta",attrs = {"name":"description"})
    text = tag.attrs['content']
    main_text = text.split("-")[0]

    # returning the required output
    return main_text

# input the username of the account you need to fetch
USERNAME = "sivakarthikeyan"

# storing the scraped data into a variable
data = scrape(USERNAME)

# printing the required output
print(data)
