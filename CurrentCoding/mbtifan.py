import pandas as pd
import time, requests
from lxml import etree
from Execution import TableModel as TM
headers={'User-Agent':'Hello World'};list0=[]
for i0 in range(0,3):
    aaa1=requests.get("https://mbti.fan/ja/tags/athlete/"+str(i0+1),headers=headers)
    aaa1.encoding="UTF-8";xxx1=etree.HTML(aaa1.text);ash1=xxx1.xpath("//*[@class='card__a']")
    for x1 in ash1:
        try:
            list_a={};list_a["Name"]=x1.xpath("div[2]/h2/text()")[0]
            if len(x1.xpath("div[1]/text()"))==0:
                list_a["Rank"]=x1.xpath("div[1]/@class")[0].split('-')[1]
            else:
                list_a["Rank"]=x1.xpath("div[1]/text()")[0]
            person0=x1.xpath("div[3]/img/@src")[0].split('/')[-1].replace("2.jpg","")
            list_a["URL"]="https://mbti.fan/ja/persons/"+person0;list_a["URL(IMG)"]=x1.xpath("div[3]/img/@src")[0]
            aaa2=requests.get("https://mbti.fan/ja/persons/"+person0+"/complete",headers=headers);vote0=0
            aaa2.encoding="UTF-8";xxx2=etree.HTML(aaa2.text);ash2=xxx2.xpath("//*[@class='mbti-info']/span")
            for x2 in ash2:
                list_a[x2.xpath("text()")[0].split(' ')[0]]=x2.xpath("span/text()")[0];vote0=vote0+int(x2.xpath("span/text()")[0])
            list_a["Total"]=vote0;list0.append(list_a)
        except:
            pass
pddf0=pd.DataFrame(list0);pddf0.insert(0,'Rank',pddf0.pop('Rank'));TM(pddf0).TkinterTable('MBTI','750x450',20,15,'n')
#pddf0.to_csv(r"C:\Users\Administrator\Desktop\mbtifan.csv",index=False)
#pddf0.to_excel(r"C:\Users\Administrator\Desktop\mbtifan_base.xlsx",index=False)