"""
一只抓取微博热点的爬虫
(包括热点名，相应的链接，热度)

"""
import requests
import re

def get_html_text(url):
	"""获取html页面"""
	try:
		r = requests.get(url,timeout = 5)
		r.raise_for_status
		r.encoding = 'utf-8'
		return r.text
	except:
		return ""

def get_info_list(url,event_list,href_list,hots_list):
	"""利用正则表达式获取热点名，链接，热度，并返回相应的列表"""
	html = get_html_text(url)
	pattern1 = re.compile(r'"star_name\\">\\n(.*?)a>', re.S)	#热点名和链接的正则表达式
	pattern2 = re.compile(r'"star_num\\"><span>(.*?)<\\/span>',re.S)	#热度的正则表达式
	for element in re.findall(pattern1, html):		
		keyword = re.split("(<|>)", element)[4]
		href = re.search(r'href=\\"(.*?)\\"', element).group().split('"')[1]
		mature_href = 'http://s.weibo.com'+re.sub('\\\\', '', href)
		event = keyword.encode('latin-1').decode('unicode_escape')
		event_list.append(event)
		href_list.append(mature_href)
	for hot in re.findall(pattern2,html):
		hots_list.append(hot)

	return event_list, href_list,hots_list

if __name__ == '__main__':
	url = 'http://s.weibo.com/top/summary?cate=realtimehot&c=spr_sinamkt_buy_hyww_weibo_p130#_loginLayer_1525707501591'
	href_list = []		#用于储存链接
	event_list = []		#用于储存热点名
	hots_list = [0]		#用于储存热度
	get_info_list(url,event_list,href_list,hots_list)
	print(event_list, href_list,hots_list)

