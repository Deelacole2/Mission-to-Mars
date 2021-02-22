

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import time
from time import sleep


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': r'C:\Users\DeeLa\.wdm\drivers\chromedriver\win32\88.0.4324.96\chromedriver.exe', headless=True}
browser = Browser('chrome', **executable_path)



# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


slide_elem.find("div", class_='content_title')


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### Featured Images

# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel



# Use the base URL to create an absolute URL
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df

# converts the df back to html-ready code
df.to_html()


# # D1: Scrape High-Resolution Mars' Hemisphere Images and Titles

# In[ ]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[24]:


# 2. Create a list to hold the images and titles.
results = []


# In[ ]:


# 3. Write code to retrieve the image urls and titles for each hemisphere

for i in range(4):
    hemispheres = {}
    
    browser.find_by_css("a.itemLink h3")[i].click()
    
    sample_elem = browser.links.find_by_text("Sample").first
    hemispheres["img_url"] = sample_elem["href"]
    print(sample_elem)
    
    # Get Hemisphere title
    hemispheres["title"] = browser.find_by_css("h2.title").get_text()
    
    print(hemispheres)
    
    # Get hemisphere object to list
    results.append(hemispheres)
    
    #Finally, we navigate backwards
    browser.back()


# In[26]:


# 4. Print the list that holds the dictionary of each image url and title.
results


# In[19]:


browser.quit()

