import pandas as pd
import time, requests
from lxml import etree
from Execution import TableModel as TM
headers={'User-Agent':'Hello World'};kkk0=[]
for i0 in range(0,10):
    try:
        aaa0=requests.get("https://anidb.net/tag/2241/chartb/?page="+str(i0),headers=headers)
        aaa0.encoding="UTF-8";xxx0=etree.HTML(aaa0.text);ash0=xxx0.xpath("//*[@class='characterlist']/tbody/tr")
        for x0 in ash0:
            art0={};exec_ad=" y0.xpath(\"@data-label\")[0]==";exec_a1="y0.xpath(\"a/picture/img/@src\")"
            exec_a2="=\"https://anidb.net\"+y0.xpath(\"a/@href\")[0];art0";exec_a3="=y0.xpath(\"a/text()\")[0]"
            exec_a4="\n\t\t\t\tart0[y0.xpath(\"@data-label\")[0]]=";exec_art="for y0 in x0.xpath(\"td\"):\n\ttry:\n\t\tif"
            exec_art+=exec_ad+"\"Image\":\n\t\t\tif "+exec_a1+"!=[]:\n\t\t\t\tart0[\"URL(IMG)\"]="+exec_a1+"[0]\n\t\t\t"
            exec_art+="else:\n\t\t\t\tart0[\"URL(IMG)\"]=\"\"\n\t\telif"+exec_ad+"\"Title\":\n\t\t\tart0[\"URL1\"]"
            exec_art+=exec_a2+"[\"Name\"]"+exec_a3+"\n\t\telif"+exec_ad+"\"From\":\n\t\t\tart0[\"URL2\"]"+exec_a2
            exec_art+="[\"From\"]"+exec_a3+"\n\t\telif"+exec_ad+"\"Action\":\n\t\t\tpass\n\t\telse:\n\t\t\t"
            exec_art+="if y0.xpath(\"text()\")!=[]:"+exec_a4+"y0.xpath(\"text()\")[0].replace(\"\\n\",\"\")"
            exec(exec_art+".replace(\"\\t\",\"\")\n\t\t\telse:"+exec_a4+"\"\"\n\texcept:\n\t\tpass");kkk0.append(art0)
        #print("Finished!")
    except Exception as e:
        print("Error occurred, because "+str(e)+"!")
pddf0=pd.DataFrame(kkk0);pd_len=len(pddf0.columns);pddf_c1=pddf0.pop("URL1");pddf0.insert(pd_len-1,"URL1",pddf_c1)
pddf_c2=pddf0.pop("URL2");pddf0.insert(pd_len-1,"URL2",pddf_c2);pddf_c3=pddf0.pop("URL(IMG)")
pddf0.insert(pd_len-1,"URL(IMG)",pddf_c3);TM(pddf0).TkinterTable('AniDB','750x450',20,15,'n')
#pddf0.to_csv(r"C:\Users\53113\Desktop\anidb0.csv",index=False)
#pddf0.to_excel(r"C:\Users\53113\Desktop\anidb0.xlsx",index=False)
