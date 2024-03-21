#!/usr/bin/env python3

#Website 1
cookies = '//*[@id="onetrust-accept-btn-handler"]' #Xpath
EN = '//*[@id="language"]/a' #Xpath 
postalCode = '//*[@id="code_postal"]' #Xpath, send H1N 4L2
searchButton = '//*[@id="recherche"]' #Xpath
# wait for everything to load, and grab the next button
#while the next button is still awake, extract all the car details
#click on the next button.
#if next button is not available, then extract all the car details
nextPage = '//*[@id="pagination"]/ul/li[11]/a' #Xpath

