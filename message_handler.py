# message_handler.py
import requests
import json
from config import PAGE_ACCESS_TOKEN

def post_facebook_message(fbid, recevied_message):      
    # ... 消息處理邏輯 ...
    if recevied_message == None:
        recevied_message = '作者外出取材中...下回休刊'
        with open('./cannotDefined.txt','a+') as rc:
                    rc.write('rd: '+csentence.encode('utf-8')+'\n')

    post_message_url = "https://graph.facebook.com/v2.6/me/messages?access_token=%s"%PAGE_ACCESS_TOKEN 
    response_msg = json.dumps({
                                "recipient":{"id":fbid}, 
                                "message":{"text":recevied_message}
                                })
    status = requests.post(post_message_url, headers={"Content-Type":"application/json"},data=response_msg)
    client.close()
	print(status.json())