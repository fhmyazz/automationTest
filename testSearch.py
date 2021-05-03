#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.bukalapak.com")

keyword = "baju lebaran"
driver.find_element_by_id("v-omnisearch__input").send_keys(keyword + Keys.ENTER)
if driver.find_element_by_class_name("bl-text--subheading-3.bl-text.bl-heading.bl-heading--h6"):
    print("Product searched")
else:
    print("Product not found")
driver.quit()

