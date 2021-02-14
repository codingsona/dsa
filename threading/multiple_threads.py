# import requests module to visit the websites
import requests
# import the threading module to be able to create threads
import threading

# Step 1: List of Websites to visit
websites = [
    'http://en.kremlin.ru/',
    'http://mfa.go.th/main/',
    'http://www.mofa.gov.la/',
    'http://www.presidency.gov.gh/',
    'https://www.aph.gov.au/',
    'https://www.argentina.gob.ar/',
    'https://www.fmprc.gov.cn/mfa_eng/',
    'https://www.gcis.gov.za/',
    'https://www.gov.ro/en',
    'https://www.government.se/',
    'https://www.india.gov.in/',
    'https://www.jpf.go.jp/e/',
    'https://www.oreilly.com/',
    'https://www.parliament.nz/en/',
    'https://www.peru.gob.pe/',
    'https://www.premier.gov.pl/en.html',
    'https://www.saskatchewan.ca/'
]

# Step 2: Create a function to retrieve Information about each website (pre-req import requests)
def visit_website(url):
    try:
        """
        Makes a GET request to a website URL and prints response information
        """
        response = requests.get(url)
        print(f'URL {url} returned {response.status_code} after {response.elapsed} seconds')
    except:
        print(f'Failed for URL {url}')


# Step3 : Visit Website using Threads
if __name__ == '__main__':
    urlCount = 1
    for website in websites:
        print(f'url: {urlCount}')
        urlCount += 1
        t = threading.Thread(target=visit_website, args=[website])
        t.start()

""" Notes:

Step1:
First, let's generate a list of websites to visit.

Step2:
Next, let's make a function that will visit a website and print information
 about the response. This function will use the the requests module, so 
 let's import that first.

Step3:
Now that you have a list of websites and a function to visit them, let's 
 create some threads to run the function! Before you create threads, you 
 need to import the threading module.

Notice how we are not directly calling visit_website(url), but creating
 a thread and setting the function as the target parameter. Then passing 
 the arguments—in this case websites—to the args parameter. Then we are
 using start() to run the function using the thread object.
  
"""