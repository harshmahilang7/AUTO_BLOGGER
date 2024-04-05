# -*- coding: utf-8 -*-
# @Author: Dastan_Alam
# @Date:   24-03-2024 07:09:49 PM       19:09:49
# @Last Modified by:   Dastan_Alam
# @Last Modified time: 05-04-2024 04:34:47 PM       16:34:47
# -*- ding: utf-8 -*-
# @Autr: Dastan_Alam
# @Dat   24-03-2024 07:09:49 PM       19:09:49
# @LasModified by:   Dastan_Alam
# @LasModified time: 24-03-2024 07:09:51 PM       19:09:51
# Starthe OAuth flow to retrieve credentials

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from googleapiclient import discovery
import httplib2

def authorize_credentials():
    CLIENT_SECRET = 'content.com.json'
    SCOPE = 'https://www.googleapis.com/auth/blogger'
    STORAGE = Storage('credentials.storage')
    # Fetch credentials from storage
    credentials = STORAGE.get()
    # If the credentials doesn't exist in the storage location then run the flow
    if credentials is None or credentials.invalid:
        flow = flow_from_clientsecrets(CLIENT_SECRET, scope=SCOPE)
        http = httplib2.Http()
        credentials = run_flow(flow, STORAGE, http=http)
    return credentials

# print(credentials)
def getBloggerService():
    credentials = authorize_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://blogger.googleapis.com/$discovery/rest?version=v3')
    service = discovery.build('blogger', 'v3', http=http, discoveryServiceUrl=discoveryUrl)
    return service

def postToBlogger(payload):
    service = getBloggerService()
    post=service.posts()
    insert=post.insert(blogId='',body=payload).execute()
    print("Done post!")
    return insert

def buildHtml():
    html = all
    return html

# title = heading

# print(htmlData)

customMetaData = "This is meta data"
payload={
        "content": buildHtml(),
        # "title": title,
        'labels': ['Udemy'],
        'customMetaData': customMetaData
    }
postToBlogger(payload)
