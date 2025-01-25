import requests
from bs4 import BeautifulSoup
import lxml
import csv
from itertools import zip_longest

job_title = []
company_name = []
location_name = []
date = []

result = requests.get("https://wuzzuf.net/search/jobs?q=html")
src = result.content
soup = BeautifulSoup(src, "lxml")


job_titles = soup.find_all("h2", {"class" : "css-m604qf"} )
company_names = soup.find_all("a", {"class" : "css-17s97q8"})
location_names = soup.find_all("span", {"class" :"css-5wys0k" })
date_old = soup.find_all("div", {"class" : "css-do6t5g"})
date_new = soup.find_all("div", {"class" : "css-4c4ojb"})
dates = [*date_old, *date_new]

# معالجة البيانات
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text.strip())  # إضافة عنوان الوظيفة
    company_name.append(company_names[i].text.strip())  # إضافة اسم الشركة
    location_name.append(location_names[i].text.strip())  # إضافة الموقع
    if i < len(dates):  # التحقق من وجود تاريخ مطابق
        date.append(dates[i].text.strip())  # إضافة التاريخ بعد استخلاص النصوص
    else:
        date.append("None") # إذا لم يكن هناك تاريخ، يتم تعيين "None"

# تصدير البيانات إلى ملف CSV
file_list = [job_title, company_name, location_name, date]
exported = zip_longest(*file_list)

with open("htmls.csv", "w", encoding="utf-8", newline="") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job Title", "Company Name", "Location", "Date"])  # كتابة العناوين
    wr.writerows(exported)  # كتابة الصفوف