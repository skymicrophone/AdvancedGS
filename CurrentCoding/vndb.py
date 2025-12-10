import pandas as pd
import time, requests
from lxml import etree
from Execution import TableModel as TM
headers={'User-Agent':'Hello World'};kkk0=[]
for i0 in range(0,10):
    try:
        aaa0=requests.get("https://vndb.org/g140?p="+str(i0),headers=headers)
        aaa0.encoding="UTF-8";xxx0=etree.HTML(aaa0.text);ash0=xxx0.xpath("//*[@class='browse vnbrowse']/table/tr")
        for x0 in ash0:
            art0={};exe_v1="\"]=x0.xpath(\"td[";exe_v2="\"]=\", \".join(x0.xpath(\"td[";exe_v3="]/abbr/@title\"));art0[\""
            exe_v4="]\")[0].xpath(\"string(.)\")";exec_art="try:\n\tart0[\"Title"+exe_v1+"2]/a/text()\")[0];art0[\"Platforms"
            exec_art+=exe_v2+"3"+exe_v3+"Languages"+exe_v2+"4"+exe_v3+"Released"+exe_v1+"5"+exe_v4+";art0[\"Score"+exe_v1
            exec_art+="1]/div/span/text()\")[0];art0[\"Rating"+exe_v1+"6"+exe_v4+";art0[\"URL\"]=\"https://vndb.org\"+"
            exec(exec_art+"x0.xpath(\"td[2]/a/@href\")[0]\nexcept:\n\tpass");kkk0.append(art0)
        #print("Finished!")
    except Exception as e:
        print("Error occurred, because "+str(e)+"!")
pddf0=pd.DataFrame(kkk0);TM(pddf0).TkinterTable('VNDB','750x450',20,15,'n')
#pddf0.to_csv(r"C:\Users\53113\Desktop\vndb0.csv",index=False)
#pddf0.to_excel(r"C:\Users\53113\Desktop\vndb0.xlsx",index=False)
