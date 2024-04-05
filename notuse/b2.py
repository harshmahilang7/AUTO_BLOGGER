# -*- coding: utf-8 -*-
# @Author: Dastan_Alam
# @Date:   10-03-2024 07:52:54 PM       19:52:54
# @Last Modified by:   Dastan_Alam
# @Last Modified time: 05-04-2024 04:34:28 PM       16:34:28
from googleapiclient.discovery import build

# Your API key
API_KEY = ''

# Your Blogger blog ID
BLOG_ID = ''

# HTML content to post
HTML_CONTENT = """
<!DOCTYPE html>
<html>
<head>
  <title>My HTML Post</title>
</head>
<body>
  <h1>Hello, Blogger!</h1>
  <p>This is a test post created via the Blogger API.</p>
</body>
</html>
"""

def create_blogger_post(api_key, blog_id, content):
    service = build('blogger', 'v3', developerKey=api_key)

    # Create the post
    post_data = {
        'kind': 'blogger#post',
        'blog': {
            'id': blog_id
        },
        'title': 'My HTML Post',
        'content': content,
    }
    post = service.posts().insert(blogId=blog_id, body=post_data).execute()

    print("Post created successfully. Post ID:", post['id'])

if __name__ == "__main__":
    create_blogger_post(API_KEY, BLOG_ID, HTML_CONTENT)
