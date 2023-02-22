import os
import socket
import requests
import numpy as np
from bs4 import BeautifulSoup


def myFunc(e):
    return len(e)


def readData(file_path):
    file_data = np.array([])
    if os.path.exists(file_path):
        with open(file_path, "rb") as fp:
            file_data = np.load(fp)
            fp.close()
    return file_data.tolist()
    # return file_data


def saveDataRasathane(file_path, file_datas):
    try:
        print(len(file_datas))
        if len(file_datas) > 0:
            with open(file_path, "wb") as fp:
                file_data_np = np.array(file_datas)
                # sort data by time and date
                file_data_np = file_data_np[file_data_np[:, 1].argsort()]  # sort by hours
                file_data_np = file_data_np[file_data_np[:, 0].argsort(kind='mergesort')]  # sort by date
                # print("file_path: ", file_path, "file_data_np: ", file_data_np)
                np.save(fp, file_data_np)
                fp.close()
        return True
    except Exception as ex:
        print("error: ", ex)
        return False


def saveDataAfad(file_path, file_datas):
    try:
        if len(file_datas) > 0:
            print(file_path)
            print(file_datas)
            with open(file_path, "wb") as fp:
                file_data_np = np.array(file_datas)
                file_data_np = file_data_np[file_data_np[:, 0].argsort()]  # sort by hours
                np.save(fp, file_data_np)
                fp.close()
            return True
        else:
            return False
    except Exception:
        return False


def printCase(checked, file_name):
    if checked:
        print(f"{file_name} dosyası başarıyla kaydedildi.")
    else:
        print(f"{file_name} dosyası kaydedilirken bir sorunla karşılaşıldı.")


def getTableData(url, tag_name, tag_class):
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, "html.parser")
    return soup.find(tag_name, attrs={'class': tag_class})


def getHtmlElementData(url, element_tag):
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, "html.parser")
    return soup.find(element_tag)
