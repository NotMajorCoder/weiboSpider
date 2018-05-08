import requests
import re

def get_html_text(url):
	try:
		r = requests.get(url,timeout = 5)
		r.raise_for_status
		r.encoding = 'utf-8'
		return r.text
	except:
		return ""

def get_info_list(url,event_list,href_list):
	html = get_html_text(url)
	pattern1 = re.compile(r'"star_name\\">\\n(.*?)a>', re.S)
	for element in re.findall(pattern1, html):
		keyword = re.split("(<|>)", element)[4]
		href = re.search(r'href=\\"(.*?)\\"', element).group().split('"')[1]
		mature_href = 'http://s.weibo.com'+re.sub('\\\\', '', href)
		event = keyword.encode('latin-1').decode('unicode_escape')
		event_list.append(event)
		href_list.append(mature_href)
	return event_list, href_list

if __name__ == '__main__':
	url = 'http://s.weibo.com/top/summary?cate=realtimehot&c=spr_sinamkt_buy_hyww_weibo_p130#_loginLayer_1525707501591'
	href_list = []
	event_list = []
	get_info_list(url,event_list,href_list)
	print(event_list, href_list)
