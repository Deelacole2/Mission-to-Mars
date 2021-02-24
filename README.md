# Mission-to-Mars

### Description of the Mission to Mars project

My coworker Robin assisted me in creating a web app that would scrape and then dispaly the latest data regarding Mars. We collected data about the latest new stories, feautured images, as well as a list of facts about Mars and information regarding the 4 hemispheres.

    This particular project incorporated various data analysis methods:
        * Used BeautifulSoup and Splinter to locate and scrape images, text and urls from the various source websites.
        * A Mongo DB was created to store the freshly scraped data, the Mars database.
        * Using the Mars database we created a web app using Flask for the framework.
        * The Flask app, scraped updated data whenever the "Scrape New Data" button was clicked.
        * And finally, the newly compiled data was displayed on a local webpage using html and bootstrap.
