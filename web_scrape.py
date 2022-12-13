import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

basic = HTTPBasicAuth('test1@gmail.com', '123456')
job_title="software+engineer"
location="San+Francisco%2C+CA"
URL = "https://www.indeed.com/jobs?q="+job_title+"&l="+location+"&from=searchOnHP&vjk=d72dc3a273ac3665"
page = requests.get(URL, auth=basic)
# print(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("div", {"class": "job_seen_beacon"})

# Look for Python jobs
# print(results)
python_jobs = results.find(
    "span", string=lambda text: "software" in text.lower()
)
python_job_elements = [
    span_element.parent.parent.parent for span_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("span", class_="jobTitle-954e4fb20788c34f")
    company_element = job_element.find("a", class_="turnstileLink companyOverviewLink")
    location_element = job_element.find("div", class_="companyLocation")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    link_url = job_element.find_all("a", {"class":"jcs-JobTitle css-jspxzf eu4oa1w0"})[1]["href"]
    print(f"Apply here: {link_url}\n")
    print()
