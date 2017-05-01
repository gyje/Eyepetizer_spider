import json
import requests
import time
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/42.0'}
date=time.strftime("%Y%M%D",time.localtime(time.time()))
url="http://baobab.kaiyanapp.com/api/v1/feed?date="+date
json_text=requests.get(url,headers=headers).text
json_dict=json.loads(json_text)
fob=open("1.txt","w+")
video_num=int(json_dict["dailyList"][0]["total"])
all_video_list=json_dict["dailyList"][0]["videoList"]
for i in range(video_num):
	fob.write("标题:"+all_video_list[i]["title"]+"\n")
	fob.write("标签:"+all_video_list[i]["category"]+"\n")
	fob.write("视频ID:"+str(all_video_list[i]["id"])+"\n")
	fob.write("描述:"+all_video_list[i]["description"]+"\n")
	fob.write("播放地址(又拍云):"+all_video_list[i]["playUrl"]+"\n")
	fob.write("播放地址(七牛云):"+all_video_list[i]["playUrl"].strip("ucloud")+"qcloud"+"\n")
	fob.write("视频时长:"+str(all_video_list[i]["duration"])+"秒\n\n\n")
fob.close()
