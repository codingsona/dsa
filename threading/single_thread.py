# import requests module to visit the websites
import requests


# Step1: List of Websites to visit
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
        print(f'Failed for URL: {url}')


if __name__ == '__main__':
    urlCount = 1
    print(f'Main thread started')
    for website in websites:
        print(f'url: {urlCount}')
        urlCount += 1
        visit_website(website)
    print(f'Main thread ended')

""" Notes:

Before you implement multi-threading into your programs, it is important
 to understand when and why it will be helpful. We will create a program 
 that visits websites and prints a report on the responses. 

One of the best use cases for multi-threading is when your program spends
 time waiting for a response from a user or a remote server. If you want 
 to create fast and efficient programs, you should aim to take advantage 
 of your computer's resources as much as possible. Multi-threading allows 
 your program to execute code during idle time where you are waiting for 
 a response. You usually end up with a faster overall runtime and better 
 user experience!

Step1:
First, let's generate a list of websites to visit.

Step2:
Next, let's make a function that will visit a website and print information
 about the response. This function will use the the requests module, so 
 let's import that first.

Step3:
Now that you have a list of websites and a function to visit them, let's run 
it! You will create an entry point to the program, and visit each website in a 
loop.

Conclusion:
Notice how we must wait for each website to return a response before the next 
request is made. This program might be spending a lot of time waiting for a 
response from a server. Is there a way to take advantage of that idle time? 
Yes, there is! We can use threads.
"""