import requests
import json
from cfg import *
import pymssql
#登录商户APP

class log():
    def __init__(self,username,password,sort):
        self.user=username
        self.password=password
        self.sort=sort

    def login(self):
        data={"phone":self.user,"passWord":self.password}
        js=json.dumps(data)
      #  data="{\"phone\":\""+self.user+"\",\"passWord\":\""+self.password+"\"}"
        header={"Content-Type":"application/json"}
       # respon=requests.post("http://192.168.0.213:58583/api/Auth/login",data=data,headers=header)
        respon=requests.post(self.sort+"/api/Auth/login",data=js,headers=header)
        res=respon.json()
        tokenid=res['data']['Token']
        print(tokenid)
        return tokenid


class goods():
#添加商品
     def __init__(self,tokenid,sort):
         self.tokenid=tokenid
         self.sort=sort
     def addgoods(self,GoodsName,GoodsNorms,PurchasePrice,OfferPrice,GoodsCount,Sort,GoodsImage,GoodsExplain,GoodsDetails):
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
         header = {"Content-Type": "application/json",'Authorization':self.tokenid}
         respon=requests.post(self.sort+"/api/Merchants/addgoods",data=js,headers=header)
         print(respon.json())

#列出商品
     def listgoods(self):
         header = {"Content-Type": "application/json", 'Authorization': self.tokenid}
         respon=requests.get(self.sort+"/api/Merchants/goods",headers=header)
         res=respon.json()
         goodsid=res["data"]["MyGoods"][0]["GoodsId"]
         print(goodsid)
         print(res)
         goodslist=res["data"]["MyGoods"]
  #       count= goodslist.count
    #     newgood=goodslist[count-1]
         #返回商品ID和商品列表
         return goodsid,goodslist

#检查商品是否添加成功
     def checkgoods(self,GoodsName,GoodsNorms,PurchasePrice,OfferPrice,GoodsCount,Sort,GoodsImage,GoodsExplain,GoodsDetails):
         self.addgoods()
         goodsid,goodslist=self.listgoods()

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
         for a in goodslist:
             if data["GoodsName"]==a["GoodsName"] and data["GoodsNorms"]==a["GoodsNorms"] and float(data["PurchasePrice"])==float(a["PurchasePrice"]) and float(data["OfferPrice"])==float(a["OfferPrice"]) and data["GoodsImage"]==a["PicUri"]:
                 print("添加成功")
             else:
                 print("添加失败")



#根据商品ID来更新商品
     def updategoods(self,goodsid):
         data = {
             "GoodsId": goodsid,
             "GoodsName": "updatepythontest",
             "GoodsNorms": "998",
             "PurchasePrice": "53",
             "OfferPrice": "23",
             "GoodsCount": 23,
             "Sort": 4,
             "GoodsImage": "http://qiniu.shenshoukeji.net/1223145628157671970591108c62b58894f2d1f69f1ae9016b94005.jpeg",
             "GoodsExplain": "121212",
             "GoodsDetails": "kok oko kok ok ok o开端"
         }
         js=json.dumps(data)
         header = {"Content-Type": "application/json", 'Authorization': self.tokenid}
         respon=requests.post(self.sort+"/api/Merchants/updategoods",data=js,headers=header)
         print(respon.json())

#删除商品
     def deletegoods(self,goodsid):
         header={"Content-Type":"application/json",'Authorization': self.tokenid}
         data={"id": goodsid}
         js=json.dumps(data)
         respon=requests.get(self.sort+"/api/Merchants/DeleteGood",headers=header,params=data)
         print(respon.json())


#下架商品
     def upgoods(self,goodsid):
         data = {"id": goodsid}
         js = json.dumps(data)
         header = {"Content-Type": "application/json", 'Authorization': self.tokenid}
         requests.post(self.sort+"/api/Merchants/updowngoods",headers=header,data=js)


#判断商品是否下架，如下架，则删除，如上架，则先下架再删除


     def checkdelete(self,goodslist,goodsid):
         if goodslist[0]["Status"]=="已上架":
            self.upgoods(goodsid)
            self.deletegoods(goodsid)
         else:
            self.deletegoods(goodsid)


#
d = log("13262849250", "a123321", APIfa)
tok=d.login()
e=goods(tok,APIfa)
# e.addgoods()
goodsid,goodslist=e.listgoods()
#e.checkgoods()
#e.updategoods(goodid)
#e.upgoods(goodid)
e.deletegoods(goodsid)
#e.checkdelete(goodslist,goodsid)






