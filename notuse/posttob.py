# -*- coding: utf-8 -*-
# @Author: Dastan_Alam
# @Date:   24-03-2024 07:11:03 PM       19:11:03
# @Last Modified by:   Dastan_Alam
# @Last Modified time: 26-03-2024 12:11:03 AM       00:11:03
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def post_to_blogger(title, content):
    # URL for Blogger
    blogger_url = "https://www.blogger.com/blog/posts/2639175137865167217"
    
    # Configure Firefox profile
    firefox_profile = webdriver.FirefoxProfile("user1")
    
    
    # Configure browser options for Firefox
    firefox_options = Options()
    firefox_options.add_argument("--log-level=3")  # suppress logging
    
    # Initialize WebDriver with Firefox
    driver = webdriver.Firefox(firefox_profile=firefox_profile, options=firefox_options)
    
    # Open Blogger
    driver.get(blogger_url)
    
    try:
        # Click on "New post"
        new_post_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='New post']")))
        new_post_button.click()
        
        # Fill in post title
        title_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Post title']")))
        title_input.send_keys(title)
        
        # Fill in post content
        content_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='editable']")))
        content_input.send_keys(content)
        
        # Click on "Publish"
        publish_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Publish']")))
        publish_button.click()
        
        print("Blog post published successfully!")
    
    except Exception as e:
        print("An error occurred:", str(e))
    
    finally:
        # Close the browser
        driver.quit()

# title = heading
# content = all
# post_to_blogger(title, content)

