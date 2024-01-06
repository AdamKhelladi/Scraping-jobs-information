# Scrape https://www.foreignhr.com:

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def get_clinic_name(page_number):

  url = f"https://www.foreignhr.com/job-search.php?page={page_number}"

  html = requests.get(url).text 
  soup = bs(html, "html.parser")

  jobs = soup.find_all("div", {"class": "list-item"})
  # print(len(jobs))

  master_list = []

  for job in jobs[:10]: # All Jobs From This Page
    job_title = job.find("h3").text
    # print(job_title)

    job_description = job.find("p", {"class": "job-desc"}).text
    # print(job_description)

    job_contract = job.find("p", {"class": "p-clock"}).text
    # print(job_contract)

    job_salary = job.find("p", {"class": "p-money"}).text
    # print(job_salary)
    
    job_location = job.find("p", {"class": "p-location"}).text
    # print(job_location)

    job_info = {
      "JOb Title": job_title,
      "Job Description": job_description,
      "Job Contract": job_contract,
      "Job Salary": job_salary,
      "Job Location": job_location
    }

    master_list.append(job_info)

  df = pd.DataFrame(master_list)
  df.to_csv("jobs_info.csv", index=False)
  print("File Created.")

page_number = 1
get_clinic_name(page_number)