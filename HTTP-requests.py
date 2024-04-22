import requests

class Config():
 r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
 # print(r.status_code)
 # print(r.content)
 # print(r.cookies)
 # print(r.elapsed)
 # print(r.encoding)
 # print(r.headers['content-type'])
 # print(r.text)
 # print(r.json())
 # print(r.history)



if Config.r.status_code == 200:
    print("Success")
else:
    print("Failed")