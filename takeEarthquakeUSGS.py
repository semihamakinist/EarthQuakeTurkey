import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from earthQuakeTools import *

if __name__ == '__main__':
    usgs_turkey = readData("EarthQuakeDatas/usgs_turkey.npy")
    usgs_allWord = readData("EarthQuakeDatas/usgs_allWord.npy")

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(
        executable_path=r'chromedriver_win32\chromedriver.exe',
        chrome_options=options)
    # &map=false&sort=largest
    url = "https://earthquake.usgs.gov/earthquakes/map/?extent=-87.28641,-121.64063&extent=87.28641,225.70313&map=false"
    driver.get(url)
    page_source = driver.page_source
    time.sleep(3)
    driver.quit()

    soup = BeautifulSoup(page_source, "html.parser")

    usgs_events_list = soup.find("usgs-events-list")
    mat_list_items = usgs_events_list.find_all("mat-list-item")

    for item in mat_list_items:
        div_callout = item.find("usgs-event-item-detail").find("div", attrs={'class': "callout"})
        div_details = item.find("usgs-event-item-detail").find("div", attrs={'class': "details"})

        # if float(div_callout.find("span").text) >= 4.0:
        #     # usgs_turkey -> [date, country, large]
        #     row_data = [div_details.find("span").text,
        #                 div_details.find("h6").text,
        #                 div_callout.find("span").text]
        #
        #     if ('turkey' in div_details.find("h6").text.lower()) and (row_data not in usgs_turkey):
        #         usgs_turkey.append(row_data)
        #     if row_data not in usgs_allWord:
        #         usgs_allWord.append(row_data)

        # usgs_turkey -> [date, country, large]
        row_data = [div_details.find("span").text,
                    div_details.find("h6").text,
                    div_callout.find("span").text]

        # if float(row_data[2]) >= 4.0:
        #     if ('turkey' in row_data[1].lower()) and (row_data not in usgs_turkey):
        #         usgs_turkey.append(row_data)
        #     if row_data not in usgs_allWord:
        #         usgs_allWord.append(row_data)

        if (float(row_data[2]) >= 4.0) and ('turkey' in row_data[1].lower()) and (row_data not in usgs_turkey):
            usgs_turkey.append(row_data)
        if (float(row_data[2]) >= 5.5) and (row_data not in usgs_allWord):
            usgs_allWord.append(row_data)

    # usgs_allWord_temp = []
    # for u in usgs_allWord:
    #     if float(u[2]) >= 5.5:
    #         usgs_allWord_temp.append(u)

    printCase(saveDataRasathane("EarthQuakeDatas/usgs_turkey.npy",
                                usgs_turkey, mode=1),
              f"Data_Sayısı: {len(usgs_turkey)} - usgs_turkey.npy")
    printCase(saveDataRasathane("EarthQuakeDatas/usgs_allWord.npy",
                                usgs_allWord, mode=1),
              f"Data_Sayısı: {len(usgs_allWord)} - usgs_allWord.npy")
    # time.sleep(3)
