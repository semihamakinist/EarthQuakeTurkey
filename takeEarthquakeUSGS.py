import time
from selenium import webdriver
from earthQuakeTools import *

if __name__ == '__main__':
    driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
    driver.get("https://earthquake.usgs.gov/earthquakes/map/?extent=-87.28641,-121.64063&extent=87.28641,225.70313&sort=largest&map=false")
    page_source = driver.page_source
    time.sleep(3)
    driver.quit()

    soup = BeautifulSoup(page_source, "html.parser")

    usgs_events_list = soup.find("usgs-events-list")
    mat_list_items = usgs_events_list.find_all("mat-list-item")

    usgs_turkey = readData("EarthQuakeDatas/usgs_turkey.npy")
    usgs_allWord = readData("EarthQuakeDatas/usgs_allWord.npy")

    for item in mat_list_items:
        div_callout = item.find("usgs-event-item-detail").find("div", attrs={'class': "callout"})
        div_details = item.find("usgs-event-item-detail").find("div", attrs={'class': "details"})

        if float(div_callout.find("span").text) >= 4.0:
            # usgs_turkey -> [date, country, large]
            row_data = [div_details.find("span").text,
                        div_details.find("h6").text,
                        div_callout.find("span").text]

            if 'turkey' in div_details.find("h6").text.lower():
                usgs_turkey.append(row_data)

            usgs_allWord.append(row_data)

    printCase(saveDataRasathane("EarthQuakeDatas/usgs_turkey.npy",
                                usgs_turkey, mode=1), "usgs_turkey.npy")
    printCase(saveDataRasathane("EarthQuakeDatas/usgs_allWord.npy",
                                usgs_allWord, mode=1), "usgs_allWord.npy")
