from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def scrape_episode_links(anime_name):
    
    # Set up Selenium webdriver
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Format the anime name for the URL
    formatted_name = anime_name.replace(" ", "%20")

    # Construct the URL of the search page
    search_url = f"https://9animetv.to/search?keyword={formatted_name}"

    print("getting links")

    driver.get(search_url)
    # Find the link of the anime 
    anime_link = driver.find_element(By.CSS_SELECTOR, 'a.dynamic-name[title="' + anime_name + '"]').get_attribute('href')

    # Use the anime_link directly as the anime_url
    anime_url = anime_link

    driver.get(anime_url)

    # Find all the episode links on the anime page
    episode_links = driver.find_elements(By.CSS_SELECTOR, 'a.item.ep-item')

    episode_links = [link.get_attribute('href') for link in episode_links]

    # print(episode_links)
    i= 1
    for link in episode_links:
        print(f"{i}-"+str(link))
        i=i+1

    driver.quit()


anime_name = "Death Note"# Enter exact name of anime 
scrape_episode_links(anime_name)