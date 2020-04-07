#encoding=utf8
import requests
import json
class Api_web:
    #url="http://www.ccym88.com"
    url="http://47.96.83.35:3002/api"
    #url="http://192.168.0.241:3002/api"
    def login(self,phone,password):
        paybody={
            "phone":phone,
            "password":password
        }

        URL=f'{self.url}/auth/login'
        jsoninfo=json.dumps(paybody)
        resp=requests.post(URL,headers={'Content-Type': 'application/json'},data=jsoninfo)
        restojb=resp.json()
    #    print(restojb)
        return restojb
        token="Bearer "+restojb["result"]["token"]
        self.token=token


    #创建一个群聊码
    def createAdminCode(self,adminType,adminTitle,adminShowType,InvalidDate,modes,adminRemark=None):
        URL=f'{self.url}/code/createAdminCode'
        paybody={
            "Id":-1,
            "adminType":adminType,
            "adminTitle":adminTitle,
            "modes":modes,
            "adminShowType":adminShowType,
            "InvalidDate":InvalidDate
        }
        resp=requests.post(URL,data=json.dumps(paybody),headers={'Content-Type': 'application/json',"Authorization":self.token})#如果请求参数是json格式，一定要放请求头里面
     #   print(resp.json())
        return resp.json()
#获取活码列表
    def getcodelist(self):
        header={"Authorization":self.token}
        URL=f'{self.url}/code/getAdminCodeList'
        resp=requests.get(URL,headers=header)
        return resp.json()
    #删除单个活码
    def deletecode(self,id):
        URL=f'{self.url}/code/deleteAdminCode'
        databody={"id":id}
        resp=requests.post(URL,data=json.dumps(databody),headers={"Authorization":self.token,"Content-Type":"application/json"})
        return resp.json()
   #删除所有的活码列表
    def delete_all_code(self):
        beforelist=self.getcodelist()
        for one in beforelist["result"]:
            self.deletecode(one["id"])
        afterlist=self.getcodelist()
        if afterlist["result"]!=[]:#如果条件满足就会抛出下面的异常，停止运行
            raise Exception("没有删除干净")

#新增子码
    def addChildCode(self,AdminId,ChildId,ChildType,ChildTitle,ChildImageType,ChildImageName,ChildImageUrl,ChildLogo,ChildFrequency,ChildTip=None):
        URL=f'{self.url}/code/editChildCode'
        data={
            "AdminId":AdminId,
            "ChildsImages":[{"ChildId":ChildId,"ChildType":ChildType,"ChildTitle":ChildTitle,"ChildImageType":ChildImageType,"ChildImageName":ChildImageName,"ChildImageUrl":ChildImageUrl,"ChildLogo":ChildLogo
                            ,"ChildFrequency":ChildFrequency}]
                              }
        resp=requests.post(URL,data=json.dumps(data),headers={"Authorization":self.token,"Content-Type":"application/json"})
        return resp.json()

#列出活码下的子码列表
    def getChildList(self,id):
        URL=f'{self.url}/code/getChildCodeList'
        data={"Id":id}
        resp=requests.post(URL,data=json.dumps(data),headers={"Authorization":self.token,"Content-Type":"application/json"})
        return resp.json()

    #删除一个子码
    def delete_childcode(self,AdminId,ChildId):
        URL=f'{self.url}/code/deleteChildCode'
        data={"AdminId":AdminId,
              "ChildId":ChildId}
        resp=requests.post(URL,data=json.dumps(data),headers={"Authorization":self.token,"Content-Type":"application/json"})
        return resp.json()

    #删除一个活码下的所有的子码
    def delete_all_childcode(self,AdminId,ChildId):
        childlist=self.getChildList()
        for one in childlist["result"]:
            self.delete_childcode(AdminId,one["id"])
        afterlist=self.getChildList()
        if afterlist["result"]!=[]:
            raise Exception("子码没有删除干净")


#初始化环境下创建一个子码
    def suitesetup(self,adminType,adminTitle,modes,adminShowType,InvalidDate,ChildId,ChildType,ChildTitle,ChildImageType,ChildImageName,ChildImageUrl,ChildLogo,ChildFrequency,ChildTip=None,adminRemark=None):
        addadmincode=self.createAdminCode(adminType,adminTitle,modes,adminShowType,InvalidDate)
        addchild=self.addChildCode(addadmincode["result"]["id"],ChildId,ChildType,ChildTitle,ChildImageType,ChildImageName,ChildImageUrl,ChildLogo,ChildFrequency)
        return addchild

 #获取某个活码的子码展示模式
    def getAdminShowType(self,id):
        URL=f'{self.url}/code/getAdminShowType'
        data={"Id":id}
        resp=requests.get(URL,data=json.dumps(data),headers={"Authorization":self.token,"Content-Type":"application/json"})
        return resp.json()
#修改某个活码的子码展示模式
    def setAdminShowType(self,id):
        URL=f'{self.url}/code/setAdminShowType'
        data={"Id":id}
        resp=requests.post(URL,data=json.dumps(data),headers={"Authorization":self.token,"Content-Type":"application/json"})
        return resp.json()

if __name__ == '__main__':
    apiweb=Api_web()
    print(apiweb.login("*&……**....","test123456"))
    #modesinf={"noRepeat":False, "administrator": False, "safeTip":True, "customerService": ""}
   # apiweb.createAdminCode(0,"我在用创建活码，能成功吗11",0,"2020-03-29",modesinf)
  #  print(apiweb.getcodelist())
   # print(apiweb.deletecode(224))
   # print(apiweb.delete_all_code())
    #print(apiweb.addChildCode( 225,-1,0,"ji12512",0,"yttt","http://qiniu.shenshoukeji.net/0326113958timg.jpg","http://qiniu.shenshoukeji.net/0305163619group-default.png",23))
    #print(apiweb.getChildList(225))
   # apiweb.delete_childcode(255,654)


