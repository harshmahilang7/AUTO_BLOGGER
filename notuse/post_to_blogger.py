# -*- coding: utf-8 -*-
# @Author: Dastan_Alam
# @Date:   10-03-2024 04:41:35 PM       16:41:35
# @Last Modified by:   Dastan_Alam
# @Last Modified time: 11-03-2024 01:41:46 AM       01:41:46
import httplib2
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from googleapiclient import discovery

def a(all,heading):
    u=all
    h=heading
    # Start the OAuth flow to retrieve credentials
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
        insert=post.insert(blogId='2639175137865167217',body=payload).execute()
        print("Done post!")
        return insert
    
    def buildHtml():
        html = "heloo"
        return html
    
    title = h
    
    # print(htmlData)
    
    customMetaData = "This is meta data"
    payload={
            "content": buildHtml(u),
            "title": title,
            'labels': ['Udemy'],
            'customMetaData': customMetaData
        }
    postToBlogger(payload)