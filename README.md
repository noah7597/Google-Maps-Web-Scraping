# Google-Maps-Web-Scraping

## General info
This is a Python script I made that uses beautiful soup and selenium to scrape data from Google Maps.

## Installations
### Beautiful Soup
To install beautiful soup onto your computer, open terminal and type "pip install beautifulsoup4"

### Selenium
To install selenium onto your computer, open terminal and type "pip install selenium"

### Chrome Driver
1. Begin by checking your version of chrome
2. Go to https://chromedriver.chromium.org/downloads
3. Download the Chrome Driver corresponding to your Chrom version and OS
4. Unzip the file in a location on your computer (Mine is kept in downloads)

## Running
1. In the repository home page, click on "Code" -> "Download Zip"
2. Unzip somewhere on easily accessible on your computer
3. Open "GoogleMapsWebScraping.py" in an IDE (I use Jupyter Notebooks)
4. Go to line 84, and replace what is in quotation marks with the path name of your chromedriver
5. Go to line 127, and replace what is currently in the preset path to the path of where you want to store the data in a csv on your computer
6. Finally, on a new line outside of any functions copy the following format:
  
  main(search_term)
  
7. Run the program
