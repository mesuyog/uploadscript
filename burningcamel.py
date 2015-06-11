#!/usr/bin/env python
import requests
import webbrowser
import re

# username and password of the website
username = 'dreamers'
password = 'dreamers'

# respective url or the website
login_url = "http://www.burningcamel.com/login"
final_url = "http://www.burningcamel.com/upload/video"


# This function gives the auth query string hidden in javascript from regex
def query_string():
    video_page = s.get("http://www.burningcamel.com/upload/video")
    auth = re.search("r.*auth=(\d\w.*)',", video_page.content)
    return auth.group(1)


# filename of the video which needs to be uploaded
file_name = 'p240.mp4'
files = {'file': (file_name, open(file_name, 'rb'))}

s = requests.session()

# payload for login

login_payload = {
    '_method': 'POST',
    'data[Member][username]': username,
    'data[Member][password]': password,
    'data[Member][remember_me]': '0',
    'data[Member][remember_me]': '1'
}

# sending login post request
login_page = s.post(login_url, data=login_payload)

# concatenating query string returning from function to upload url
upload_url = ("http://www.burningcamel.com/upload.php?auth=" + query_string())

# payload for upload
upload_payload = {
    'name': "o_19mphdb69kvm17bh1qgkvil3aq7.mp4"
}

# sending upload post request
upload_post = s.post(upload_url, data=upload_payload, files=files)

# payload for upload info
upload_info_payload = {
    '_method': 'POST',
    'data[Item][filename]': 'o_19mphdb69kvm17bh1qgkvil3aq7.mp4',
    'data[Item][title]': 'asa akira',
    'data[Item][descr]': 'hello this is asa',
    'data[Item][terms]': '0',
    'data[Item][terms]': '1'
}

# sending upload info post request
info_post = s.post(final_url, data=upload_info_payload)

# if file is successfully uploaded open in browser
if info_post.ok:
    filename = "burningcamel.html"
    target = open(filename, 'w')
    target.write(info_post.content)
    print "your file has been successfully uploaded!!!"
    webbrowser.open('burningcamel.html', new=2)
