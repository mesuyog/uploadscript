import requests
import re
import hashlib
from bs4 import BeautifulSoup
import webbrowser


def LoginToken():
    # using beautifulsoup to parse the login token hidden in the form
    soup = BeautifulSoup(front_page.text)
    login_token = soup.find("input",{'type': '\\"hidden\\"'}).attrs["value"].replace('\\"', '').replace('\\/', "")
    return login_token


def GetUploadToken():
    # using beautiful soup to find the upload token
    soup = BeautifulSoup(user_page.text)
    upload_token = soup.find("input",{'name': "token"}).attrs["value"]
    #uid = soup.find("input",{'id': "uid"}).attrs["value"]
    return upload_token

def GetUid():
    # using beautiful soup to find the upload token
    soup = BeautifulSoup(user_page.text)
    #upload_token = soup.find("input",{'name': "token"}).attrs["value"]
    uid = soup.find("input",{'id': "uid"}).attrs["value"]
    return uid


def GetFileNameHash(filename):
    """hash of the filename is used in the form field in the upload"""
    return hashlib.md5(filename).hexdigest()


# username and password of the website
username = 'mesuyog'
password = 'gentlepornxs123'

# Title and description of the upload form
MovieTitle = "hello this is asa"
Description = "asa akira baby"
Tags = "9"
 
 # filename of the video which needs to be uploaded
filename = 'sunny_leone.mp4'
files = {'files[]': (filename, open(filename, 'rb'))}

# creating session object by using request
s = requests.session()

# post url of login and upload
login_url = "http://pornxs.com/ajax.php?action=create_login_view"
upload_url = "http://encoding.pornxs.com/uploader_test.php"

front_page = s.get(login_url)


# payload for login
login_payload = {"token":LoginToken(),'username': username, "password":password } 

response = s.post("http://pornxs.com/ajax.php?action=check_login",data=login_payload)
 
login_payload = {"token":LoginToken(), 'username':username, "password":password, "login12": "Login"} 
response = s.post("http://pornxs.com/",data=login_payload)
 
user_page = s.get("http://pornxs.com/homepage.php")


# payload for upload
upload_payload = {
    'token': GetUploadToken(),
    'uid': GetUid(),
    'terms': '1',
    "movie_title"+GetFileNameHash(filename): MovieTitle,
    "description"+GetFileNameHash(filename): Description,
    'tagsb15494b8d6ec5fe230b7584fbf91a67b[]': Tags    
    
}

# sending upload post request
upload_post = s.post(upload_url, data=upload_payload, files=files)




filename = "porn.html"
target = open(filename,'w')
target.write(upload_post.content)


webbrowser.open('porn.html', new=2)