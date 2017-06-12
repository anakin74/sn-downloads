

#python tool to download Security now transcripts from the GRC website

#import dependencies


import requests
import time

#initialize counters
#this needs to change in V2, want to make it configurable by user input


#counter = 350
#x=348

#start loop, loop will start at the beginning (x) and loop until it reaches the last document requested (counter)
x = input("What is the first transcript you want to download ? ")
counter = input("what is the last transcript you want to download ?")
start_time = time.time()

while int(x) <= int(counter):
   url="https://grc.com/sn/sn-" + str(x) + ".pdf"
   r= requests.get(url)
   with open("sn-" + str(x) + ".pdf", "wb") as code:
       code.write(r.content)
       print(str(r.status_code) + " I downloaded episode " + str(x) + " and saved it to disk")
       x=int(x)+1
print('this action took exactly '  + str(round(time.time() - start_time,2)) + " seconds")


