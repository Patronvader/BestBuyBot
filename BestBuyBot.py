import threading
import time
from CardScrapper import *

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
url = "/site/searchpage.jsp?st=3080"
avail = False

scraper = CardScrapper()

#while avail == False:
#Retreives html from URL
scraper.prepareSoup(url, headers)

#Clears the startup status messages
scraper.clearScreen()

#Create a dictionary of GPUs from the site
scraper.createGPUList()

# Create worker threads and start them
scraper.makeWorkers()

#Traverses GPU dictionary and checks whether the product is available
#avail = scraper.checkGPUList()

#Waits until all threads have completed their task
#scraper.listQueue.join()
main_thread = threading.current_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    print("joining %s", t.getName())
    t.join()

#Print the in stock GPUs
scraper.printInstock()

#Wait to reqeust data again
scraper.sleep()
