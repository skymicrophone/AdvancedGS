import json
import time, requests
from lxml import etree
from Execution import SFOperation as SFO
headers={'User-Agent':'Hello World'};dict0={}
for i0 in range(0,1):
    aaa0=requests.get("https://mbti.fan/ja/persons/ryosuke-yamada/complete/"+str(i0+1),headers=headers)
    aaa0.encoding="UTF-8";xxx0=etree.HTML(aaa0.text);ash0=xxx0.xpath("//*[@class='comment']/div/div[2]/div[1]")
    for art0 in ash0:
        ART=art0.xpath("text()");dict0["コメント"+ART[0]]=ART[2]
print(dict0)#;SFO(r"C:\Users\Administrator\Desktop\mbtifan.json").FWriter([json.dumps(dict0,ensure_ascii=False)],'w','UTF-8')
