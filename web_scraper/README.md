# Indeed Web Scraper

A **selenium** web-scraper specialized in scraping Job Listings from Indeed

## What can it scrape?
1. 🧑‍💼 Job Title
2. 🔗 Job Link (indeed link)
3. 🪪 Job ID (indeed ID)
4. 🏢 Company Name
5. 🗺️ Location
6. ⌚ Since (x days ago)
7. 💵 Salary
8. 📜 Job Description

## Capabilities
- ✅ can bypass Cloudfare bot blocker
- ✅ can automatically close pop-up windows
- ✅ can export scraped result into an Excel
- ✅ average scraping speed at 7s/job

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following:

```bash
pip install selenium
pip install numpy
pip install webdriver-manager
pip install pandas
pip install openpyxl
pip install lxml
pip install fsspec
```

## Configuration
1. change these **two variables** to suit your search
```python
# change these two variables ONLY
job_ = 'Technician+Aircond'
location = 'Selangor'
```
2. ensure that you use **plus symbol (+)** in places where you'd normally space( ), example below:
```python
# example (must use '+' as 'space')
job_ = 'Software+Engineer'
location = 'Kuala+Lumpur'
```
3. (additional) enable **filter=0** to show more results (**not recommended**)
```python
# you can change the 'filter=0' to show more result, but it MAY contain DUPES!
pagination_url = 'https://malaysia.indeed.com/jobs?q={}&l={}&radius=15&filter=1&sort=date&start={}' #filter=0
pagination_url = 'https://malaysia.indeed.com/jobs?q={}&l={}&radius=15&filter=0&sort=date&start={}' #filter=1
```
4. (additional) you can **increase the search radius** to show more results (**not recommended**)
```python
# you can increase radius to show more result, but it may be produce inaccurate result
pagination_url = 'https://malaysia.indeed.com/jobs?q={}&l={}&radius=15&filter=1&sort=date&start={}' #radius=15
pagination_url = 'https://malaysia.indeed.com/jobs?q={}&l={}&radius=25&filter=0&sort=date&start={}' #filter=25
```

## Contributors

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This project is protected under the [MIT](https://choosealicense.com/licenses/mit/) License