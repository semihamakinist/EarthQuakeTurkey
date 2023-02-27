from earthQuakeTools import readData


if __name__ == '__main__':
    # AFAD -- pulling data saved before
    afad_elazig = readData("EarthQuakeDatas/afad_elazig.npy")
    afad_malatya = readData("EarthQuakeDatas/afad_malatya.npy")
    afad_biggerThan4 = readData("EarthQuakeDatas/afad_biggerThan4.npy")

    # Rasathane -- pulling data saved before
    rasathane_elazig = readData("EarthQuakeDatas/rasathane_elazig.npy")
    rasathane_malatya = readData("EarthQuakeDatas/rasathane_malatya.npy")
    rasathane_biggerThan4 = readData("EarthQuakeDatas/rasathane_biggerThan4.npy")

    # earthquake.usgs -- pulling data saved before
    usgs_turkey = readData("EarthQuakeDatas/usgs_turkey.npy")
    usgs_allWord = readData("EarthQuakeDatas/usgs_allWord.npy")
