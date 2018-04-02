import requests
import json
import sys

if(len(sys.argv)==2):
	tag=sys.argv[1]
else:
	print("Numero incorrecto de parametros. Solo debe ser un parámetro; el hashtag")
	sys.exit()
#tag='futbolsinlimite'

url='https://www.instagram.com/explore/tags/' + tag + '/?__a=1'
filename=tag+'.json'
has_next=True

def jsave(data_dict,filename='default.json'):
	with open(filename, 'a+') as outfile:
		json.dump(data_dict,outfile)
		outfile.write("\n")


def get_ig_page(url, session=None):
	session = session or requests.Session()

	r = session.get(url)
	r_code = r.status_code
	print("STATUS: "+str(r_code))
	session.close()
	if r_code ==requests.codes.ok:
		return r
	else:
		return None

while(has_next ):
	ig_dict = get_ig_page(url)
	jsave(ig_dict.json(),filename)
	ig_json=ig_dict.json()
	if(ig_json['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']):
		curzord=ig_json['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
		url='https://www.instagram.com/explore/tags/' + tag + '/?__a=1&max_id='+curzord
		print("Next :"+curzord)
	else:
		has_next=False	
