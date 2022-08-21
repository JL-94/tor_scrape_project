# webscrape_project

# WEB SCRAPING CAN BE ABUSED TO NEGATIVELY AFFECT SERVICES. PLEASE ADHERE TO ETHICAL WEB SCRAPING PRACTICES WHEN USING THIS SCRIPT. SCRAPE INFREQUENTLY, AND ENSURE TARGET WEB SERVICES / PAGES CONSENT TO BEING SCRAPED. 

## !!! AS OF 12/08/22 THIS SCRIPT IS CURRENTLY NOT WORKING DUE TO UNKNOWN ISSUES WHEN COMMUNICATING WITH INDEED WEBSERVERS. !!!

This script can be used to return the amount of jobs associated with certain keywords on uk.indeed.com.

Requirements:
Make sure pip3 is installed.

pip install torpy
pip install bs4

Input: 
Data is read from search_terms.txt. Add or remove terms as needed.

Logging:
This script will create a log file inside the project directory. The default name for this file is scrape.log. It will display info regarding the TOR nodes that the requests are sent through.

Results:
search_results.csv will populate when script is run. 
