import requests
import time
import json
import sys
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0'
}

print("""
   __ __     __                 __    ______          ___    
  / // /__ _/ /__  ___ ____ ___/ /   / __/ /___ _____/ (_)__ 
 / _  / _ `/ / _ \/ _ `/ -_) _  /   _\ \/ __/ // / _  / / _ |
/_//_/\_,_/_/\___/\_, /\__/\_,_/   /___/\__/\_,_/\_,_/_/\___/
                 /___/
编程猫数据统计
作者：haloged
版本：0.1.3
============================================================                                                            
""")

def main():
   codemao_id=input("请输入您的编程猫ID")
   get=requests.get("https://api.codemao.cn/api/user/info/detail/"+codemao_id,headers=headers)
   #print(get.text)
   user_data = json.loads(get.text)
   user_data_data=json.loads(user_data[data])
   user_data_data_data=json.load(user_data_data[userInfo])
   user_data_data_data_data=json.load(user_data_data_data[user])
   print(user_data_data_data_data[id])
   print(user_data.items())
   #if(user_data[code]=="200"):
      #pass
   #else:
      #print("请求失败，请检查网络。")



def fei():
   login_phonenunber=int(input("请输入注册编程猫的手机号"))
   login_password=input("请输入编程猫密码")
   login_data = {
      'phonenumber': login_phonenunber,
      'password': login_password,
      'pid': 'q2UHWZx5'
   }
   get_cookie=requests.post("https://api.codemao.cn/tiger/v3/web/accounts/login",headers=headers,params=login_data,)
   print(get_cookie.text)
   cookie_test=requests.get("https://api.codemao.cn/api/user/info")
   print(cookie_test.text)

main()
