# query_processor.py
import re
from database import get_text_mining_news_collection

def querySlayer1(question):
    # ... 查詢處理邏輯 ...
    with open('conversation.json', 'r',encoding='utf-8') as f:
        tmpY = []
        tmpN = []
        conDict = json.load(f)
        cutQuestion = jieba.cut(question, cut_all=False)
        ### 這邊要先作分流，把可以回答的字先裝起來
        for word in cutQuestion:
            if word in conDict.keys():
                tmpY.append(word)
            else:
                tmpN.append(word)
        
        if tmpY:
            ### 這邊是針對問句中的最先抓到的關鍵字回覆，嘿~
            return conDict[tmpY[0]]
        else:
            return 'nodata4u'

def querySlayer2(question):
    # ... 查詢處理邏輯 ...
    answerList = []
    keyWord = question[1::].lower()
    result = collection.find().sort('Date',-1)
    for oneResult in result:
        if keyWord in oneResult['Tag'] or keyWord in  oneResult['TagByName'] :
            answerList.append(oneResult)
    ### 如果有資料就給前三比，沒有就給default
    if answerList:
        return answerList[0:3]
    else:
        return 'nodata4u'