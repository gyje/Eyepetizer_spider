import json
import requests
import time
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/42.0'}
date=time.strftime("%Y%M%D",time.localtime(time.time()))
url="http://baobab.kaiyanapp.com/api/v1/feed?date="+date
json_text=requests.get(url,headers=headers).text
json_dict=json.loads(json_text)
s=time.clock()
fob=open("0.txt","w+")
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
e=time.clock()
print ("{}S".format(e-s))
'''
说明:尝试了用字典和列表的形式减少磁盘I/O,在2天的数据获取测试中,虽然时间差距较大(39倍),但是整体花费时间并没有比较大的影响,这种方式时间为:0.0396258597025203秒,而用字典存储时间为:0.0014271225123327833秒,而且字典是无序的还需要更多的代码实现排序,所以,还是选择这种方式.
'''
