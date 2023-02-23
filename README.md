## Pulling Earthquake data in Turkey on the website of AFAD and Rasathane
### The List of Website Addresses
* https://deprem.afad.gov.tr/last-earthquakes.html
* http://www.koeri.boun.edu.tr/scripts/lst9.asp
* https://earthquake.usgs.gov/earthquakes/map/?extent=-87.28641,-121.64063&extent=87.28641,225.70313&sort=largest&map=false&sort=largest

### Technologies Used in the Program 
* Python - 3.6.10
* requests - 2.24.0
* numpy - 1.16.6
* bs4 (BeautifulSoup) - 4.9.1
* selenium - 3.141.0

### Running The Programs
* python takeAfadEarthquake.py
* python takeRasathane.py
* python takeEarthquakeUSGS.py
* Adding tasks to run them hourly in the System (cronjob)