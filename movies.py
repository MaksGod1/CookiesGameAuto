from selenium import webdriver
from selenium.webdriver.common.by import By
import time



chrome_options=webdriver.ChromeOptions()



chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])


chrome_options.add_argument("--log-level=3")


chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)

genre_movies=["action","adventure","animation","biography","comedy","crime","documentary",
              "drama","family","fantasy","film-noir","game-show","history","horror","music",
              "musical","mystery","news","reality-tv","romance","sci-fi","sport","talk-show",
              "thriller","war","western"]

genre=input(f"WRITE THE GENRE OF THE MOVIES FROM THIS VARIANTS {genre_movies}: ")
if genre in genre_movies:
    driver.get(f"https://www.imdb.com/search/title/?title_type=feature&genres={genre}")
while genre not in genre_movies:
    genre=input(f"WRITE THE GENRE OF THE MOVIES FROM THIS VARIANTS {genre_movies}: ")
    if genre in genre_movies:
        driver.get(f"https://www.imdb.com/search/title/?title_type=feature&genres={genre}")





time.sleep(2)
driver.find_element(By.XPATH,value='//*[@id="__next"]/div[1]/div/div[2]/div/button[2]').click()

range1=0
number_of_movies=int(input("WRITE THE NUMBER OF MOVIES: "))
metacritica_rating=float(input("WRITE THE METACRITICA RATING 1-100(YOU SEE THE MOVIES WITH THIS RATING OR MORE): "))
imdb_rating=float(input("WRITE THE IMDB RATING 1.0-10.0(YOU SEE THE MOVIES WITH THIS RATING OR MORE): "))
result_movies=[]
while True:
    time.sleep(2)


    for i in range(range1,len(driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item"))):
        if driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_elements(By.CLASS_NAME,value="metacritic-score-box") and driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_elements(By.CLASS_NAME,value="ipc-rating-star--rating"):
            if len(result_movies)==number_of_movies:
                break
            print(driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="ipc-title-link-wrapper").text,driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="metacritic-score-box").text, driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="ipc-rating-star--rating").text)
            if float(driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="metacritic-score-box").text)>=metacritica_rating and float(driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="ipc-rating-star--rating").text)>=imdb_rating:
                result_movies.append([driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="ipc-title-link-wrapper").text,float(driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="metacritic-score-box").text), float(driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="ipc-rating-star--rating").text)])
                print(f"FOUND OUT: {len(result_movies)} out of {number_of_movies}")
        


        


        elif driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_elements(By.CLASS_NAME,value="metacritic-score-box"):
            if len(result_movies)==number_of_movies:
                break
            print(driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="ipc-title-link-wrapper").text,driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="metacritic-score-box").text)
            if float(driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="metacritic-score-box").text)>=metacritica_rating:
                result_movies.append([driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="ipc-title-link-wrapper").text,float(driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="metacritic-score-box").text),None])
                print(f"FOUND OUT: {len(result_movies)} out of {number_of_movies}")

        



        elif driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_elements(By.CLASS_NAME,value="ipc-rating-star--rating"):
            if len(result_movies)==number_of_movies:
                break
            print(driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="ipc-title-link-wrapper").text, driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="ipc-rating-star--rating").text)
            if float(driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="ipc-rating-star--rating").text)>=imdb_rating:
                result_movies.append([driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="ipc-title-link-wrapper").text,None,float(driver.find_elements(By.CLASS_NAME,value="ipc-metadata-list-summary-item")[i].find_element(By.CLASS_NAME,value="ipc-rating-star--rating").text)])
                print(f"FOUND OUT: {len(result_movies)} out of {number_of_movies}")
        else:
            continue
    
    if number_of_movies==len(result_movies):
        break

    range1+=50







    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1000);")
    time.sleep(2)
    if driver.find_elements(By.XPATH,value='//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/div[2]/div/span/button'):
        driver.find_element(By.XPATH,value='//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/div[2]/div/span/button').click()
    else:
        break



print(f"\n\n\n\t\t.....RESULT.....(METACRITICA AND IMDB RATING YOU DID WRITE: {metacritica_rating}, {imdb_rating})\n\n\n")
for i in result_movies:
    name, metacritica, imdb=tuple(i)
    print(f'{name} || Metacritica rating: {metacritica} || IMDB rating: {imdb}')