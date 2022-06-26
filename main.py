import urllib.request
import lxml
import bs4
from torpy.http.requests import tor_requests_session

def get_ip():
    # Pulls your public IP address from https://www.ident.me.

    pub_ip = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
    return pub_ip

def tor_check():
    # Runs a test http request through the TOR network, and returns the public IP address of the TOR exit node used. 
    # TOR network is slow and can be temperamental, be patient if it does not work first time. 

    url = "https://v4.ident.me"
    with tor_requests_session() as tor:
        try:
            res = tor.get(url)
        except:
            print('Something went wrong with the http request.')
    data = bs4.BeautifulSoup(res.text, "lxml")
    tag = data.select('body')
    exit_node = tag[0].get_text()
    return exit_node

def scrape():
    # Self explanatory, runs a scraping task against targets specified in the url variable.
    url = ''
    with tor_requests_session() as tor:
        res = tor.get(url)
    pass

def main():
    pub_ip = get_ip()
    exit_node = tor_check()
    if pub_ip == exit_node:
        print('TOR inactive. Ending scrape.')
        exit()
    elif pub_ip != exit_node:
        print('TOR active. Your IP address will be hidden.')
        print('Using TOR exit node: ' + exit_node)

if __name__ == "__main__":
    main()


