# import requests module to visit the websites
import requests
# We will use the ThreadPoolExecutor to create some threads
from concurrent.futures import ThreadPoolExecutor

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

# Step3 : Visit Website using ThreadPoolExecutor
if __name__ == '__main__':
    urlCount = 1
    with ThreadPoolExecutor(max_workers=2) as cook:
        for website in websites:
            print(f'url: {urlCount}')
            urlCount +=1
            cook.submit(visit_website, website)

""" Notes:

Step1:
First, let's generate a list of websites to visit.

Step2:
Next, let's make a function that will visit a website and print information
 about the response. This function will use the the requests module, so 
 let's import that first.

Step3: 
Now that you have a list of websites and a function to visit them, let's 
use the ThreadPoolExecutor to create some threads to run the function! 
Before you can use the ThreadPoolExecutor class, you need to import the 
concurrent.futures module
 
As you can see, ThreadPoolExecutor takes a parameter called max_workers. 
This is the number of worker threads you want to use within the context 
of the executor. Play around with adjusting this number.

The submit() method takes a target callable and an argument. It's very 
similar to Thread.start() from the threading module. In this example, 
the function that each thread will run is visit_website and the argument 
to that function will be the website as it loops through the list of 
websites you have defined.

"""