import requests
import json

tag='semanasanta'
url='https://www.instagram.com/explore/tags/' + tag + '/?__a=1'

def jprint(data_dict):
	print(json.dumps(data_dict,indent=4))


def get_ig_page(url, session=None):
	print(url)
	session = session or requests.Session()

	r = session.get(url)
	r_code = r.status_code
	#print(r_code)
	if r_code ==requests.codes.ok:
		return r
	else:
		return None


ig_dict = get_ig_page(url)
if ig_dict is not None:
	#jprint(ig_dict.json())
	#print("####################")
	jprint(ig_dict.text)
else:
	print("Ooops ERRRRRR")
		
