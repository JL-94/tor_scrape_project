import time
from datetime import timedelta
import re
from bs4 import BeautifulSoup
import random
import logging
#CC: I add the "requests" import below to enable line 46 to work
import requests

#Logging configuration settings.
logging.basicConfig(filename='scrape.log', filemode='w', level=logging.INFO, format = '%(asctime)s - %(name) s - %(levelname) s - %(message) s')

def scrape():
    #Get a start time
    startTime = time.time()
    logging.info('Data retrieval started...')
    print('Data retrieval started...')

    #Open a file to read search terms from
    readFile = open("search_terms.txt", "r")

    #Open a file to write search count results to
    writeFile = open("search_results.csv","w") 

    retries = 1

    logging.info('Building TOR Circuit...')

    #Loop through all search terms
    for searchTerm in readFile:
        print(searchTerm)
        #Contstruct the destination url including the specified searchTerm
        #res = requests.get('https://uk.indeed.com/jobs?q=%27' + searchTerm + '%27&l=')
        while True:
            try:
                logging.info('Sending request...')
                
                #CC: The original line is below
                #res = requests.get("https://uk.indeed.com/jobs?q='" + searchTerm + "'&l=")
                
                #CC: The modified version of line 41 is entered on line 46
                #CC: The term "sess" was changed to "requests"
                #CC: It also includes a browser agent entry at the end.
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36', 'Referer': 'https://google.co.uk'}
                res = requests.get("https://uk.indeed.com/jobs?q='" + searchTerm + "'&l=", headers=headers)

            except (Exception) as e:
                wait = retries + 5
                print('Error, waiting %s seconds before retrying...' %wait)
                logging.info('Error, waiting %s seconds before retrying...' %wait)
                time.sleep(wait)
                retries += 1
                logging.info('Building new TOR Circuit...')
                requests.close()
                continue
            break                
        
        print(res)
        #Parse the html results returned from the url request
        soup = BeautifulSoup(res.text, 'html.parser')
        
        #Find a specific <div> element on the specified web page
        searchPage = soup.find('div', id='searchCountPages')  
        
        print(searchPage)

        #Convert the results that are found, to a string
        spString = str(searchPage)

        #valueToo = int(re.sub('[^0-9]', '', spString))
        print(spString)

        #Sanititse step 1, by removing the conent at the beginning of the string (i.e. 'Page 1 of ' )
        spStringRemFront = str(spString.split('Page 1 of ')[1])

        #Sanitise value count (remove remaining markup and non-alphabet characters (i.e. 7,083 jobs</div>), and convert to an integer.  
        value = int(re.sub('[^0-9]', '', spStringRemFront))

        #Sanitise searchTerm string by removing quotations and line breaks. Only keep characters.
        writeTerm = re.sub("[^a-zA-Z/]","",searchTerm)

        #Write sanitised searchTerm concatenated with a colon and the value count returned for the searchTerm
        #writeFile.write(writeTerm + ":" + str(value) + "\n") 
        writeFile.write(str(value) + ",\n")  

        #Create a random number of seconds and store in variable n.
        n = random.randint(10,20)    

        #Pause the script for n seconds after each search iteration.
        #Preventative method against IP blocking.
        time.sleep(n)      

    #Close the file to write result counts to
    writeFile.close()

    #Close the file to read search terms from
    readFile.close()

    #Get am end time
    endTime = time.time()

    print('Data retrieval complete!')
    logging.info('Scraping completed.')
    #Calculate the difference betwee the end time and the strat time
    timeCalc = endTime - startTime

    #Define a duration and format it
    duration = timedelta(seconds=timeCalc)
    logging.info('Scraping completed in %s' %duration)
    print('Scraping completed in %s' %duration)

def main():
    scrape()

if __name__ == "__main__":
    main()


