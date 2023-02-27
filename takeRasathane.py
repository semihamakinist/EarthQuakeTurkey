# import argparse
from earthQuakeTools import *


if __name__ == '__main__':

    url = "http://www.koeri.boun.edu.tr/scripts/lst9.asp"

    # pulling data saved before
    rasathane_elazig = readData("EarthQuakeDatas/rasathane_elazig.npy")
    rasathane_malatya = readData("EarthQuakeDatas/rasathane_malatya.npy")
    rasathane_biggerThan4 = readData("EarthQuakeDatas/rasathane_biggerThan4.npy")

    # while True:
    pre_attr = getHtmlElementData(url, "pre")
    pre_texts = pre_attr.text.split("\r\n")
    print(type(rasathane_biggerThan4))
    for i in range(7, len(pre_texts)):
        # .split(" ")
        row_data = pre_texts[i].replace("İlksel", "") \
            .replace(" (", "-(") \
            .split()
        # .split()  # parsing the string and removing the empty items in the string
        if (len(row_data) > 9) and (float(row_data[6]) >= 4.0):
            row_data[8] = "-".join(row_data[8:len(row_data)])
            [row_data.remove(item) for item in row_data[9:len(row_data)]]
            # for item in row_data[9:len(row_data)]:
            #     row_data.remove(item)

        if len(row_data) >= 9:
            # Taking if the intensity of more than 4 of the earthquake
            if float(row_data[6]) >= 4.0:
                # Adding just the list of earthquakes' intensity of more than 4 in Turkey
                if row_data not in rasathane_biggerThan4:
                    rasathane_biggerThan4.append(row_data)

                # Adding just the list of earthquakes' intensity of more than 4 in Malatya
                if "MALATYA" in row_data[8]:
                    if row_data not in rasathane_malatya:
                        rasathane_malatya.append(row_data)

                # Adding just the list of earthquakes' intensity of more than 4 in Elazig
                elif "ELAZIG" in row_data[8]:
                    if row_data not in rasathane_elazig:
                        rasathane_elazig.append(row_data)
        else:
            print("index_size: ", len(pre_texts),
                  "index: ", i, "size: ", len(row_data),
                  "- error_data: ", row_data)

    # saving new data after data changed
    printCase(saveDataRasathane("EarthQuakeDatas/rasathane_malatya.npy",
                       rasathane_malatya),
              f"Data_Sayısı: {len(rasathane_malatya)} - rasathane_malatya.npy")
    printCase(saveDataRasathane("EarthQuakeDatas/rasathane_elazig.npy",
                       rasathane_elazig),
              f"Data_Sayısı: {len(rasathane_elazig)} - rasathane_elazig.npy")
    printCase(saveDataRasathane("EarthQuakeDatas/rasathane_biggerThan4.npy",
                       rasathane_biggerThan4),
              f"Data_Sayısı: {len(rasathane_biggerThan4)} - rasathane_biggerThan4.npy")

    print("Finishing Parsing")
    # time.sleep(3)
