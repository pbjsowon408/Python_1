#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://jp.indeed.com/%E6%B1%82%E4%BA%BA?q=python&limit={LIMIT}"

def extract_indeed_pages():  #define extract function of indeed pages
    result = requests.get(URL) # request page

    soup = BeautifulSoup(result.text, "html.parser") 
    #create soup to search page numbers (extract data / whole html file)

    pagination = soup.find("div", {"class":"pagination"})   
    # clasiffy specific data (div - class - pagination)

    links = pagination.find_all('a')            #make pages

                                                #find span of every anchor in the list

    pages = []                                  #create empty array

    for link in links[:-1]:                     # [starting number:ending number(-1/last element)]
        pages.append(int(link.string))              #extract specific data 'span'  //  .string to get only the string // .int change into integers
                                                #link.find("span").string

    max_page = pages[-1]
                                                #list of span
        
    return max_page


def extract_job(html):

      title = html.find("h2", {"class":"title"}).find("a")["title"]
      company = html.find("span",{"class":"company"})
      company_anchor = company.find("a")

      if company_anchor is not None:
        company = str(company_anchor.string)

      else:
        company = str(company.string)
      company = company.strip() #strip() function removes all space 
      location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
      job_id = html["data-jk"]

      return {'title':title,
              'company':company, 
              'location':location, 
              "link":f"https://jp.indeed.com/viewjob?jk={job_id}"
        }


def extract_indeed_jobs(last_page):
    
    jobs = []

    for page in range(last_page):

      print(f"Scrapping Page {page}")

      result = requests.get(f"{URL}&start={page*LIMIT}") #request whole pages of indeed.com 
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

      for result in results:
        job = extract_job(result)
        jobs.append(job)

    return jobs


# In[ ]:




