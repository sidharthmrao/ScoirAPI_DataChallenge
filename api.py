import requests
import time
import sys

load_displays = False
if "--load" in sys.argv or "--l" in sys.argv:
    load_displays = True

responses = {}

for i in range(1, 13):
    responses[i] = []

amount = 1000
starttime = time.time()

for i in range(amount):
    if load_displays:
        print(f"Processing Request: {i}/{amount}. | Time Elapsed: {time.time()-starttime}", end="\r")
    r = requests.get("https://randomuser.me/api/").json()
    name = r['results'][0]['name']['first']
    dmonth = int(r['results'][0]['dob']['date'].split('-')[1])
    responses[dmonth].append(name)
    
if load_displays:
    print("\033[K")
    print(f"\nRequests Complete: {amount}/{amount}. | Time Elapsed: {time.time()-starttime}", end="\r\n")

best_month = 1
for i in responses.keys():
    if len(responses[i]) > len(responses[best_month]):
        best_month = i
        
common = max(set(responses[best_month]), key = responses[best_month].count)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print(f"The most popular birth month was {months[best_month-1]} with {len(responses[best_month])} users")
print(f"The most popular first name of users born in {months[best_month-1]} was {common}")
