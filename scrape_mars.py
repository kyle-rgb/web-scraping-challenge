import pandas as pd
import numpy as np
import bs4, requests

def scrape():
    final_dict = {}
    #Mars News
    mars_news_url = r"https://mars.nasa.gov/news/8744/nasa-engineers-checking-insights-weather-sensors/"
    response = requests.get(mars_news_url, "lxml")
    soup = bs4.BeautifulSoup(response.text)
    news_title = soup.select("h1")[0].text
    news_title = news_title.strip()
    blurb_text = soup.select("p > i")[1].text

    final_dict["Planet_News"] = {}
    final_dict["Planet_News"]["title"] = news_title
    final_dict["Planet_News"]["blurb"] = blurb_text

    #### JPL Mars Space Images
    images_url = r"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    base_url = r"https://www.jpl.nasa.gov"
    response_img = requests.get(images_url, "lxml")
    soupier = bs4.BeautifulSoup(response_img.text)
    soupier.select(".img")
    mars_image_src = soupier.select(".img")[0].img["src"]
    featured_image_url = base_url + mars_image_src

    final_dict["Planet_Image"] = {}
    final_dict["Planet_Image"]["featured_image_url"] = featured_image_url

    # the featured image of the mars search was of Saturn not Mars

    ### Mars Facts

    facts_response = requests.get(r"https://space-facts.com/mars/")
    table = pd.read_html(r"https://space-facts.com/mars/")
    table[0]
    table = table[0]
    table.rename({0: "Facts", 1:"Mars"}, axis=1, inplace=True)
    table.to_html("table.html")
    
    final_dict["Planet_Facts"] = {}
    final_dict["Planet_Facts"]["table"] = table.to_html()
    

    # Hemisphere Requests
    response_4 = requests.get(r"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
    soupabc = bs4.BeautifulSoup(response_4.text, "lxml")
    soupabc.select("h3")

    hemisphere_dict = [{"img_url": r"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
                         {"img_url": r"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
                         {"img_url": r"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
                         {"img_url": r"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"}]

    for i, hemisphere in enumerate(soupabc.select('h3')):
        hemisphere_dict[i]["title"] = hemisphere.text

    final_dict["Hemispheres"] = hemisphere_dict

    return final_dict
