import requests
import re

LOGIN_URL = "https://portal.dhivehinet.net.mv/adsls/login_api"
HOME_URL = "https://portal.dhivehinet.net.mv/home"

#The creds
DHIRAAGU_USERNAME=""
DHIRAAGU_PASSWORD=""
NOIP_USERNAME=""
NOIP_PASSWORD=""
NOIP_DOMAIN=""

def login(username= DHIRAAGU_USERNAME, password=DHIRAAGU_PASSWORD):

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    form_data = {"data[adsl][username]": username, "data[adsl][password]": password}

    login_req = requests.post(LOGIN_URL,headers=headers, data=form_data)

    # 200 means the creds are correct
    if login_req.status_code == 200:
        cookie = login_req.cookies
        home_page = requests.get(HOME_URL,cookies=cookie) #get the home page with the returned cookie
        return home_page.text
    else:
        return False

#tries to find ip address from the homepage with regex

def getIp(string):
    #tries to filter so it will work if two ip matches are found
    results = re.findall('<td colspan="2">(.*)</td>', string)
    result = ' '.join(result for result in results)
    #finds the ip in the new string
    ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", result)
    if len(ip_candidates) == 1:
        return ip_candidates[0]
    else:
        return "NULL"

page = login()
DHIRAAGU_IPADDRESS = getIp(page)

print("IP Adress: {}".format(DHIRAAGU_IPADDRESS))

#Send IP to no-ip.com for DNS update
requests.get("http://"+(NOIP_USERNAME)+":"+(NOIP_PASSWORD)+"@dynupdate.no-ip.com/nic/update?hostname="+(NOIP_DOMAIN)+"&myip="+(DHIRAAGU_IPADDRESS))
