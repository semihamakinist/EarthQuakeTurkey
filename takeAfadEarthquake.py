from earthQuakeTools import *


if __name__ == '__main__':
    url = "https://deprem.afad.gov.tr/last-earthquakes.html"

    # pulling data saved before
    afad_elazig = readData("EarthQuakeDatas/afad_elazig.npy")
    afad_malatya = readData("EarthQuakeDatas/afad_malatya.npy")
    afad_biggerThan4 = readData("EarthQuakeDatas/afad_biggerThan4.npy")

    table_attr = getTableData(url, 'table', 'content-table')
    table_body = table_attr.find('tbody')

    datas = []
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        # remove emty item
        row_data = [ele for ele in cols if ele]
        if len(row_data) >= 8:
            # Taking if the intensity of more than 4 of the earthquake
            # row_data = ['2023-02-23 14:41:42', '38.074', '37.764',
            #             '6.97', 'MW', '4.4', 'Doğanşehir (Malatya)', '552941']
            if float(row_data[5]) >= 4.0:
                # Adding just the list of earthquakes' intensity of more than 4 in Turkey
                row_data_first = row_data[0].split(" ")
                row_data.remove(row_data[0])
                # row_data = ['2023-02-23', '14:41:42', '38.074', '37.764',
                #             '6.97', 'MW', '4.4', 'Doğanşehir (Malatya)', '552941']
                row_data = row_data_first + row_data

                if row_data not in afad_biggerThan4:
                    afad_biggerThan4.append(row_data)

                # Adding just the list of earthquakes' intensity of more than 4 in Malatya
                if "Malatya" in row_data[7]:
                    if row_data not in afad_malatya:
                        afad_malatya.append(row_data)
                # Adding just the list of earthquakes' intensity of more than 4 in Elazig
                elif "Elazığ" in row_data[7]:
                    if row_data not in afad_elazig:
                        afad_elazig.append(row_data)
        else:
            print("row_size: ", len(row_data), "- error_data: ", row_data)

    # saving new data after data changed
    # printCase(saveDataRasathane("EarthQuakeDatas/afad_malatya.npy",
    #                    afad_malatya), "afad_malatya.npy")
    # printCase(saveDataRasathane("EarthQuakeDatas/afad_elazig.npy",
    #                    afad_elazig), "afad_elazig.npy")
    # printCase(saveDataRasathane("EarthQuakeDatas/afad_biggerThan4.npy",
    #                    afad_biggerThan4), "afad_biggerThan4.npy")

    print("Finishing Parsing")
