"""
Use this module for scrapping the links from any webpage.
"""
import requests
from bs4 import BeautifulSoup


class Scrapper:
    """
    Use this class for basic scrapping oin website. 
    """

    def __init__(self, url: str):
        if url.startswith("https://"):
            complete_url = url
        elif url.startswith("//"):
            complete_url = "https:"+url
        elif url.startswith("/"):
            complete_url = "https:/"+url
        else:
            complete_url = "https://"+url
        self.url = complete_url

    def read_page(self):
        """
        read the page layout
        """
        page = requests.get(self.url, timeout=2)

        html = BeautifulSoup(page.content, "html.parser")

        return html

    def read_links(self, read=None):
        """
        reads the links from the webpage.
        enter the attribute you want to read . 
        """
        html = self.read_page()
        body = html.body()
        check_list = ["img", "a","div"]
        output = []
        for tag in body:
            for i in tag.find_all(check_list):
                for link in i.get_attribute_list(read):
                    if link is not None:
                        output.append(link)
        return output

    def cure_links(self, sub_url=""):
        """
        returns the curated links.
        """
        if sub_url.startswith("https://"):
            return sub_url
        url_list = self.url.split("/")
        curated_url = url_list[0]+"//"+url_list[2]+sub_url
        return curated_url

    def read_all_links(self):
        """
        it returns the final curated list of all links
        """
        links = self.read_links(read="src")
        link2 = self.read_links(read="src2")
        try:
            links.append(link2[0])
        except:
            pass
        img_links = []
        for link in links:
            curated_link = self.cure_links(link)
            img_links.append(curated_link)
        return img_links
