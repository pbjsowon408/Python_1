#!/usr/bin/env python
# coding: utf-8

# In[4]:


from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file
from flask import Flask, render_template, request, redirect, send_file

app = Flask("PythonScrapper")

db = {}

#@ = decorator , looks for only a function under it 
@app.route("/")
def home():
  return render_template("templates.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_so_jobs(word) + get_indeed_jobs(word)
      db[word] = jobs

  else:
    return redirect("/")
  #flask is rendering the variation in the html file "{{}}"
  return render_template("report.html",searchingBy=word, resultsNumber=len(jobs))

@app.route("/<username>")# <> means placeholder
def username(username):
  return "080-0000-0000"


@app.route("/export")
def export():
    try: # try every commit(?)
      word = request.args.get('word') 
      if not word:
        raise Exception() #throw an error.  Exception() == Error
      word = word.lower()
      jobs = db.get(word)
      if not jobs:
        raise Exception()
      save_to_file(jobs)
      return send_file(f"{word}.csv")
    except: # if any error occurs go to /
      return redirect("/")

    
app.run(host="0.0.0.0")




# In[ ]:




