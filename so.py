import requests
from bs4 import BeautifulSoup

LIMIT = 50

def get_last_pages(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)


def extract_job(html):
  title = html.find("div",{"class":"grid--cell fl1"}).find("a")["title"]
  company, location = html.find("h3",{"class":"fc-black-700 fs-body1 mb4"}).find_all("span",recursive=False) 
  # "Unpacking" very comfortable to make to var together 
  # "recursive" only runs first seleced levels
  company = company.get_text(strip=True).strip("•").strip("\r")
  location = location.get_text(strip=True).strip("•").strip("\r")
  job_id = html['data-jobid']

  return {'title':title,'company':company,'location':location,"apply_link":f"https://stackoverflow.com/jobs/{job_id}"}

def extract_jobs(last_page, url):
    
  jobs = []
  for page in range(last_page):
    print(f"Scrapping StackOverFlow with Page: {page}")
    result = requests.get(f"{url}&pg={page+1}")
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("div",{"class":"-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs(word):
  url = f"https://stackoverflow.com/jobs?q={word}"
  last_page = get_last_pages(url)
  jobs = extract_jobs(last_page, url)
  return jobs
