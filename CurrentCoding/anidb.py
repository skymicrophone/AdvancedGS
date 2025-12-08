import pandas as pd
import time, requests
from lxml import etree
from Execution import TableModel as TM
headers={'User-Agent':'Hello World'};kkk0=[]
for i0 in range(0,10):
    aaa0=requests.get("https://anidb.net/tag/2626/animetb/?page="+str(i0),headers=headers)
    aaa0.encoding="UTF-8";xxx0=etree.HTML(aaa0.text);ash0=xxx0.xpath("//*[@class='animelist']/tbody/tr")
    for x0 in ash0:
        art0={};exec_ad="y0.xpath(\"@data-label\")[0]==";exec_art="for y0 in x0.xpath(\"td\"):"
        exec_art+="\n\ttry:\n\t\tif "+exec_ad+"\"Image\":\n\t\t\tart0[\"URL(IMG)\"]=y0.xpath(\"a/picture/img/@src\")[0]"
        exec_art+="\n\t\telif "+exec_ad+"\"Title\":\n\t\t\tart0[\"URL\"]=\"https://anidb.net\"+y0.xpath(\"a/@href\")[0];"
        exec_art+="art0[\"Title\"]=y0.xpath(\"a/text()\")[0]\n\t\telif "+exec_ad+"\"Award\":\n\t\t\tif "
        exec_art+="y0.xpath(\"span/span/text()\")!=[]:\n\t\t\t\tart0[\"Awards\"]=\", \".join(y0.xpath(\"span/span/text()\"))"
        exec_art+="\n\t\t\telse:\n\t\t\t\tart0[\"Awards\"]=\"\"\n\t\telif "+exec_ad+"\"Eps\":\n\t\t\tart0[\"Eps\"]="
        exec_art+="y0.xpath(\"string(.)\").replace(\"\\n\",\"\").replace(\"\\t\",\"\")\n\t\telif "+exec_ad+"\"Weight\":\n\t\t\t"
        exec_art+="art0[\"Weight\"]=y0.xpath(\"span/@title\")[0]\n\t\telse:\n\t\t\tart0[y0.xpath(\"@data-label\")[0]]="
        exec(exec_art+"y0.xpath(\"text()\")[0].replace(\"\\n\",\"\").replace(\"\\t\",\"\")\n\texcept:\n\t\tpass");kkk0.append(art0)
    #print("Finished!")
pddf0=pd.DataFrame(kkk0);TM(pddf0).TkinterTable('AniDB','750x450',20,15,'n')
#pddf0.to_csv(r"C:\Users\53113\Desktop\anidb0.csv",index=False)
#pddf0.to_excel(r"C:\Users\53113\Desktop\anidb0.xlsx",index=False)

