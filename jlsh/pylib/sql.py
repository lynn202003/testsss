
import pymssql

def sqlconnet():
    connection=pymssql.connect("192.168.0.240",
                        "ceshi",
                        "ceshi@2020!",
                        "Kingsland",
                        "utf8")
    cursor=connection.cursor()
    #查询表里所有的列

    #sql="select colid,name from syscolumns where id=object_id('[dbo].[MerchantGoods]') order by colid"
    sql="select  top 1 * from [dbo].[MerchantGoods] order by id desc"
    cursor.execute(sql)
    a=cursor.fetchall()
#    print(a)
    newlist=[]
    for values in a:
       print("id= ",values[0])
       print("MerchantId= ",values[1])
       print("GoodsName= ",values[2])
       print("GoodsExplain= ",values[3])
       print("GoodsCount= ",values[5])
       print("PurchasePrice= ",values[7])
       print("OfferPrice= ",values[8])
    connection.close()
sqlconnet()

     GoodsName,sqlconnet()
     if a==GoodsName:

