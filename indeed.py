#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup

LIMIT = 50

def get_last_pages(url):  #define extract function of indeed pages
    result = requests.get(url) # request page

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
      
      if company: #some company doesnt have there name...
        company_anchor = company.find("a")
        if company_anchor is not None:
           company = str(company_anchor.string)

        else:
           company = str(company.string)
        company = company.strip() #strip() function removes all space 
      else:
        company = None
      location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
      job_id = html["data-jk"]

      return {'title':title,
              'company':company, 
              'location':location, 
              "link":f"https://jp.indeed.com/viewjob?jk={job_id}"
        }


def extract_jobs(last_page, url):
    
    jobs = []

    for page in range(last_page):

      print(f"Scrapping Page {page}")

      result = requests.get(f"{url}&start={page*LIMIT}") #request whole pages of indeed.com 
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

      for result in results:
        job = extract_job(result)
        jobs.append(job)

    return jobs

def get_jobs(word):
  url = f"https://jp.indeed.com/jobs?q=python&limit={LIMIT}"
  last_page = get_last_pages(url)
  jobs = extract_jobs(last_page, url)
  return jobs
# In[ ]:




