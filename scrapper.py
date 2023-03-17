import os
import requests
from bs4 import BeautifulSoup

class Scrapper:
    
    def __init__(self, url:str):
        
        
        self.url=url