import requests
from bs4 import BeautifulSoup
import lxml
import csv
from itertools import zip_longest
page = requests.get("https://wuzzuf.net/search/jobs/?q=teacher&a=hpb")
scr = page.content
soup = BeautifulSoup(scr, "lxml")

job_title = []
company_name = []
location_name = []
date_new = []
date_old = []

job_titles = soup.find_all("h2", {"class" : "css-m604qf" } )
company_names = soup.find_all("a", {"class" : "css-17s97q8" } )
location_names = soup.find_all("span", {"class" : "css-5wys0k" } )
dates_new = soup.find_all("div", {"class" : "css-4c4ojb" } )
dates_old = soup.find_all("div", {"class" : "css-do6t5g" } )

for i in range(len(job_titles)):
  job_title.append(job_titles[i].text.strip())  # إضافة عنوان الوظيفة
  company_name.append(company_names[i].text.strip())  # إضافة اسم الشركة
  location_name.append(location_names[i].text.strip())
  if i < len(dates_new):
    date_new.append(dates_new[i].text.strip())
  else:
    date_new.append("N/A") 


  if i < len(dates_old):
    date_old.append(dates_old[i].text.strip())
  else:
    date_old.append("N/A")


file_list = [job_title, company_name, location_name, date_new , date_old ]
exported = zip_longest(*file_list)
with open("teaching", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job_title", "company_name", "location_name", "date_new" , "date_old"])
    wr.writerows(exported)