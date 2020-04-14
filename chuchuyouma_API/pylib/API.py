#encoding=utf8
import requests
import json
class Api_web:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"   #解决初始化生成的实例和用例生成的实例是同一个实例

    #url="http://www.ccym88.com"
    #url="http://47.96.83.35:3002/api"
    url="http://192.168.0.241:3002/api"
    def login(self,phone,password):
        paybody={
            "phone":phone,
            "password":password
        }

        URL=f'{self.url}/auth/login'
        jsoninfo=json.dumps(paybody)
        resp=requests.post(URL,headers={'Content-Type': 'application/json'},data=jsoninfo)
        restojb=resp.json()
        tokens = "Bearer " + restojb["result"]["token"]
        self.token = tokens
        return restojb



    #创建一个群聊码
    def createAdminCode(self,id,adminType,adminTitle,adminShowType,InvalidDate,modes,adminRemark=None):
        URL=f'{self.url}/code/createAdminCode'
        paybody={
            "Id":int(id),
            "adminType":int(adminType),#因为这些参数必须传int，但是robot中会自动作为字符串传入，所以在此加入int强制转化为int，也可在rf中写成${0}
            "adminTitle":adminTitle,
            "modes":modes,
            "adminShowType":int(adminShowType),
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
            "AdminId":int(AdminId),
            "ChildsImages":[{"ChildId":int(ChildId),"ChildType":int(ChildType),"ChildTitle":ChildTitle,"ChildImageType":int(ChildImageType),"ChildImageName":ChildImageName,"ChildImageUrl":ChildImageUrl,"ChildLogo":ChildLogo
                            ,"ChildFrequency":int(ChildFrequency)}]
                              }
        resp=requests.post(URL,data=json.dumps(data),headers={"Authorization":self.token,"Content-Type":"application/json"})
        return resp.json()

#列出活码下的子码列表
    def getChildList(self,id):
        URL=f'{self.url}/code/getChildCodeList'
        data={"Id":int(id)}
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


#获取所有活码列表，找出活码ID，再创建子码,用于初始化环境下创建子码
    def suitesetup(self,ChildId,ChildType,ChildTitle,ChildImageType,ChildImageName,ChildImageUrl,ChildLogo,ChildFrequency):
        getcode=self.getcodelist()
        addcode=self.addChildCode(getcode["result"][0]["id"],int(ChildId),int(ChildType),ChildTitle,int(ChildImageType),ChildImageName,ChildImageUrl,ChildLogo,int(ChildFrequency))
        print(addcode)


 #获取某个活码的子码展示模式
    def getAdminShowType(self,id):
        URL=f'{self.url}/code/getAdminShowType'
        data={"Id":id}
        resp=requests.post(URL,data=json.dumps(data),headers={"Authorization":self.token,"Content-Type":"application/json"})
        return resp.json()
#修改某个活码的子码展示模式
    def setAdminShowType(self,id):
        URL=f'{self.url}/code/setAdminShowType'
        data={"Id":id}
        resp=requests.post(URL,data=json.dumps(data),headers={"Authorization":self.token,"Content-Type":"application/json"})
        return resp.json()

 #获取某个活码分日数据
    def getAdminCodeCounts(self,id):
        URL=f'{self.url}/code/getAdminCodeCounts'
        data={"Id":id}
        resp=requests.post(URL,data=json.dumps(data),headers={"Authorization":self.token,"Content-Type":"application/json"})
        return resp.json()
    #结果页-获取某个子码
    def getTargetCode(self,id):
        URL = f'{self.url}/code/getTargetCode'
        data = {"Id": id}
        resp = requests.post(URL, data=json.dumps(data),headers={"Authorization": self.token, "Content-Type": "application/json"})
        return resp.json()
#结果页-长按某个子码
    def scanTargetCode(self):
        URL = f'{self.url}/code/scanTargetCode'
        data = {"Id": id}
        resp = requests.post(URL, data=json.dumps(data),headers={"Authorization": self.token, "Content-Type": "application/json"})
        return resp.json()

 #获取页面所有等级
    def GetSetMealList(self):
        URL = f'{self.url}/global/GetSetMealList'
        resp = requests.post(URL,headers={"Authorization": self.token, "Content-Type": "application/json"})
        return resp.json()

#获取用户会员信息
    def GetUserVipInfo(self):
        URL = f'{self.url}/auth/GetUserVipInfo'
        resp = requests.get(URL,headers={"Authorization": self.token, "Content-Type": "application/json"})
        return resp.json()
#立即开通
    def Calculation(self,id): #id: 1免费 2基础月付 3基础年付 4旗舰月付 5旗舰年付,cycle: 1为月付，2为年付
        URL=f'{self.url}/pay/Calculation'
        data={"id":int(id)}
        resp = requests.post(URL, data=json.dumps(data),headers={"Authorization": self.token, "Content-Type": "application/json"})
     #   self.money=resp["result"]["money"]
        return resp.json()

#支付方式
    def GetPayOrder(self,cycle,money,type,setMealId):  #type:1支付宝，2微信
        URL = f'{self.url}/pay/GetPayOrder'
       # money=(self.Calculation(int(id)))["result"]["money"]
        data={"cycle": int(cycle), "money":int(money), "type":int(type), "setMealId":int(setMealId)}
        resp = requests.post(URL, data=json.dumps(data),headers={"Authorization": self.token, "Content-Type": "application/json"})
        # self.orderNo=resp["result"]["orderNo"]
        return resp.json()
#点击已成功支付
    def PayBack(self,type,orderNo):
        URL = f'{self.url}/pay/PayBack'

        data = {"type":int(type),"orderNo":orderNo}
        resp = requests.post(URL, data=json.dumps(data),headers={"Authorization": self.token, "Content-Type": "application/json"})
        return resp.json()



if __name__ == '__main__':
    apiweb=Api_web()
    print(apiweb.login("13774351025","test123456"))
    # modesinf={"noRepeat":False, "administrator": False, "safeTip":True, "customerService": ""}
  #  createcode=apiweb.createAdminCode(-1,0,"我在用创建活码，能成功吗11",0,"2020-03-29",modesinf)
  #  print(apiweb.getcodelist())
   # print(apiweb.deletecode(224))
   # print(apiweb.delete_all_code())
  #  print(apiweb.addChildCode(createcode["result"]["id"],-1,0,"ji12512",0,"yttt","http://qiniu.shenshoukeji.net/0326113958timg.jpg","http://qiniu.shenshoukeji.net/0305163619group-default.png",23))
    #print(apiweb.getChildList(225))
   # apiweb.delete_childcode(255,654)
   #  apiweb.suitesetup(-1,0,"ji1251266",0,"yttt66","http://qiniu.shenshoukeji.net/0326113958timg.jpg","http://qiniu.shenshoukeji.net/0305163619group-default.png",28)
 #   getCode=apiweb.getTargetCode()
    idinfo=apiweb.Calculation(4)
    getpay=apiweb.GetPayOrder(1,idinfo["result"]["money"],1,4)
    print(apiweb. PayBack(1,getpay["result"]["orderNo"]))


