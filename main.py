#!/usr/bin/env python
# coding: utf-8

# In[4]:


from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from flask import Flask, render_template, request, redirect

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
#since Im using in repl.it, host as 0.0.0.0. 
app.run(host="0.0.0.0")




# In[ ]:




