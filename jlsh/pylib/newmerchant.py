import requests
import json
from cfg import *
import pymssql
#登录商户APP


def login(username,password,sort):
    data={"phone":username,"passWord":password}
    js=json.dumps(data)
  #  data="{\"phone\":\""+self.user+"\",\"passWord\":\""+self.password+"\"}"
    header={"Content-Type":"application/json"}
   # respon=requests.post("http://192.168.0.213:58583/api/Auth/login",data=data,headers=header)
    respon=requests.post(sort+"/api/Auth/login",data=js,headers=header)
    res=respon.json()
    tokenid=res['data']['Token']
 #   print(tokenid)
    return tokenid



def addgoods(tokenid,sort,GoodsName,GoodsNorms,PurchasePrice,OfferPrice,GoodsCount,Sort,GoodsImage,GoodsExplain,GoodsDetails):
 data={
    "GoodsName": GoodsName,
    "GoodsNorms": GoodsNorms,
    "PurchasePrice": PurchasePrice,
    "OfferPrice": OfferPrice,
    "GoodsCount": GoodsCount,
    "Sort": Sort,
    "GoodsImage": GoodsImage,
    "GoodsExplain": GoodsExplain,
    "GoodsDetails": GoodsDetails
     }
 js=json.dumps(data)
 header = {"Content-Type": "application/json",'Authorization':tokenid}
 respon=requests.post(sort+"/api/Merchants/addgoods",data=js,headers=header)
 print(respon.json())

#列出商品
def listgoods(tokenid,sort):
 header = {"Content-Type": "application/json", 'Authorization':tokenid}
 respon=requests.get(sort+"/api/Merchants/goods",headers=header)
 res=respon.json()
 goodslist=res["data"]["MyGoods"]
 print(goodslist)
 #返回商品ID和商品列表
 return goodslist


#检查商品是否添加成功
def checkgoods(GoodsName,GoodsNorms,PurchasePrice,OfferPrice,GoodsCount,Sort,GoodsImage,GoodsExplain,GoodsDetails):
     data = {
         "GoodsName": GoodsName,
         "GoodsNorms": GoodsNorms,
         "PurchasePrice": PurchasePrice,
         "OfferPrice": OfferPrice,
         "GoodsCount": GoodsCount,
         "Sort": Sort,
         "GoodsImage": GoodsImage,
         "GoodsExplain": GoodsExplain,
         "GoodsDetails": GoodsDetails
     }
     goodslist=listgoods()
     for a in goodslist:
         if data["GoodsName"]==a["GoodsName"] and data["GoodsNorms"]==a["GoodsNorms"] and float(data["PurchasePrice"])==float(a["PurchasePrice"]) and float(data["OfferPrice"])==float(a["OfferPrice"]) and data["GoodsImage"]==a["PicUri"]:
             print("添加成功")
         else:
             print("添加失败")



#根据商品ID来更新商品
def updategoods(tokenid,sort,goodsid,GoodsName,GoodsNorms,PurchasePrice,OfferPrice,GoodsCount,Sort,GoodsImage,GoodsExplain,GoodsDetails):
 data = {
     "GoodsId": goodsid,
     "GoodsName": GoodsName,
     "GoodsNorms": GoodsNorms,
     "PurchasePrice": PurchasePrice,
     "OfferPrice": OfferPrice,
     "GoodsCount": GoodsCount,
     "Sort": Sort,
     "GoodsImage": GoodsImage,
     "GoodsExplain": GoodsExplain,
     "GoodsDetails": GoodsDetails
 }
 js=json.dumps(data)
 header = {"Content-Type": "application/json", 'Authorization': tokenid}
 respon=requests.post(sort+"/api/Merchants/updategoods",data=js,headers=header)
 print(respon.json())

#删除商品
def deletegoods(tokenid,sort,goodsid):
 header={"Content-Type":"application/json",'Authorization': tokenid}
 data={"id": goodsid}
 js=json.dumps(data)
 respon=requests.get(sort+"/api/Merchants/DeleteGood",headers=header,params=data)
 print(respon.json())

#删除所有的商品
def deleteall():
 tokenid = login("13262849250","a123321","http://47.96.83.35:5001")
 goodslist=listgoods(tokenid,"http://47.96.83.35:5001")
 # print(goodslist)
 if goodslist!=[]:
     for goods in goodslist:
         if goods==[]:
             break
         else:
             if goods["Status"] == "已上架":
                 upgoods(tokenid, "http://47.96.83.35:5001", goods["GoodsId"])
                 deletegoods(tokenid, "http://47.96.83.35:5001", goods["GoodsId"])
             else:
                 deletegoods(tokenid, "http://47.96.83.35:5001", goods["GoodsId"])




#下架商品
def upgoods(tokenid,sort,goodsid):
 data = {"id": goodsid}
 js = json.dumps(data)
 header = {"Content-Type": "application/json", 'Authorization': tokenid}
 requests.post(sort+"/api/Merchants/updowngoods",headers=header,data=js)


#判断商品是否下架，如下架，则删除，如上架，则先下架再删除


def checkdelete(tokenid,goodslist,goodsid):
 if goodslist[0]["Status"]=="已上架":
    upgoods(tokenid,"http://47.96.83.35:5001",goodsid)
    deletegoods(tokenid,"http://47.96.83.35:5001",goodsid)
 else:
    deletegoods(tokenid, "http://47.96.83.35:5001", goodsid)


# tokenid=login("13262849250","a123321","http://47.96.83.35:5001")
# addgoods(tokenid,"http://47.96.83.35:5001","4511","454","23","12","6","2","http://qiniu.shenshoukeji.net/1223145628157671970591108c62b58894f2d1f69f1ae9016b94005.jpeg","koiko","jijk")
# listgood=listgoods(tokenid,"http://47.96.83.35:5001")
# updategoods(tokenid,"http://47.96.83.35:5001",listgood[0]["GoodsId"],"451188888","454","23","12","6","2","http://qiniu.shenshoukeji.net/1223145628157671970591108c62b58894f2d1f69f1ae9016b94005.jpeg","koiko","jijk")
# listgoods(tokenid,"http://47.96.83.35:5001")


#if __name__=="__main__":
#     addgoods()
#     listgoods()

