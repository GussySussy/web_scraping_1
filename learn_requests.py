import requests
from bs4 import BeautifulSoup
from requests.models import PreparedRequest

base_url = "https://annas-archive.org"
req = PreparedRequest()

def get_search(value):
    params ={"q": "+".join(value.split(" "))}
    search_path = base_url + "/search"
    req.prepare_url(search_path,params)
    response = requests.get(req.url,timeout=1)
    
    soup = BeautifulSoup(response.content, "lxml")
    books = soup.findAll("div", class_ = lambda x : x in ["h-[125] flex flex-col justify-center js-scroll-hidden", "h-[125] flex flex-col justify-center"])
    for book in books:
        try:
            metadata = book.find("div", class_="line-clamp-[2] leading-[1.2] text-[10px] lg:text-xs text-gray-500")
            content = [x for x in metadata.next_siblings if x != "\n"]
            title = content[0]
            year = content[1]
            author = content[2]
            href = book.a["href"]
            print(f"href : {href}\nmetadata : {metadata.string}\ntitle : {title.string}\nyear : {year.string}\nauthor : {author.string}\n\nfile : {metadata.string}\n\n")
        except Exception as E:
            print("Invalid Book")
            print(book["class"])
            
get_search(input("Enter the name of the book : "))