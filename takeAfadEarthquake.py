from earthQuakeTools import *


if __name__ == '__main__':
    url = "https://deprem.afad.gov.tr/last-earthquakes.html"

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
        row_data = [ele for ele in cols if ele]
        if len(row_data) >= 8:
            if float(row_data[5]) >= 4.0:
                row_data = row_data[0].split(" ") + row_data
                if row_data not in afad_biggerThan4:
                    afad_biggerThan4.append(row_data)
                if "Malatya" in row_data[8]:
                    if row_data not in afad_malatya:
                        afad_malatya.append(row_data)
                elif "Elazığ" in row_data[8]:
                    if row_data not in afad_elazig:
                        afad_elazig.append(row_data)
        else:
            print("row_size: ", len(row_data), "- error: ", row_data)

    # print(afad_biggerThan4)
    printCase(saveDataRasathane("EarthQuakeDatas/afad_malatya.npy",
                       afad_malatya), "afad_malatya.npy")
    printCase(saveDataRasathane("EarthQuakeDatas/afad_elazig.npy",
                       afad_elazig), "afad_elazig.npy")
    printCase(saveDataRasathane("EarthQuakeDatas/afad_biggerThan4.npy",
                       afad_biggerThan4), "afad_biggerThan4.npy")

    print("Finishing Parsing")
