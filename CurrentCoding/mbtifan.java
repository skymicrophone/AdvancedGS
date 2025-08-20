package NNN;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.util.*;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.jsoup.*;
import com.alibaba.fastjson.*;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class SSS {
	public static void main(String[] args){
		try {
			JSONArray KKK0=new JSONArray();String Path0="C:\\Users\\Administrator\\Desktop\\mbtifan.json";
			for(int i0=0;i0<10;i0++) {
				try {
					Document doc_B0=Jsoup.connect("https://mbti.fan/ja/tags/kpop-idol/"+String.valueOf(i0+1)).get();
					Elements ele_B0=doc_B0.select(".card__a");int rank0=1+i0*20;
					for(Element attr_B0 : ele_B0){
						try {
							int total0=0;LinkedHashMap<String,String> MAP_M=new LinkedHashMap<>();
							MAP_M.put("Rank",String.valueOf(rank0));MAP_M.put("Name",attr_B0.select("h2").text());
							String[] AAA0=attr_B0.select(".profile-img").select("img").attr("src").replaceAll("2.jpg","").split("/");
							MAP_M.put("URL","https://mbti.fan/ja/persons/"+AAA0[5]);
							//MAP_M.put("URL(IMG)",attr_B0.select(".profile-img").select("img").attr("src"));
							Document doc_B=Jsoup.connect("https://mbti.fan/ja/persons/"+AAA0[5]+"/complete").get();
							Elements ele_B=doc_B.select(".mbti-info");
							for(Element attr_B : ele_B){
								//String[] AAA=attr_B.select("span").text().split(" ");MAP_M.put(AAA[0],attr_B.select(".mbti-num").text());
								total0+=Integer.valueOf(attr_B.select(".mbti-num").text());
							}
							MAP_M.put("Total",String.valueOf(total0));KKK0.add(JSONObject.toJSON(MAP_M));
							System.out.println(JSONObject.toJSON(MAP_M));rank0+=1;total0=0;
						} catch (Exception e) {System.out.println(e);rank0+=1;}
					}
				} catch (Exception e) {System.out.println(e);}
			}
			//File file_M=new File(Path0);OutputStreamWriter wri_M=new OutputStreamWriter(new FileOutputStream(file_M),"UTF-8");
			//wri_M.append(JSON.toJSONString(KKK0,SerializerFeature.PrettyFormat,SerializerFeature.WriteMapNullValue));wri_M.close();
		} catch (Exception e) {e.printStackTrace();}
	}
}