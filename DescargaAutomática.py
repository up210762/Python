import os
import requests
from time import time
from multiprocessing.pool import ThreadPool

def url_response(url):
    path, url = url
    r = requests.get(url, stream = True)

    with open(path, 'wb') as f:
    
        for ch in r:
            f.write(ch)

urls = [("Evento1.pdf", "https://drive.google.com/u/0/uc?id=1AkC4kFoF3zUGJoqP7qtXEwogTnfwvhzd&export=download")]

#https://drive.google.com/file/d/1AkC4kFoF3zUGJoqP7qtXEwogTnfwvhzd/view?usp=sharing

start = time()
for x in urls:
    url_response (x)
print(f"Time to download: {time() - start}")

ThreadPool(9).imap_unordered(url_response, urls)