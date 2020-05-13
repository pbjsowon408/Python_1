#!/usr/bin/env python
# coding: utf-8

# In[4]:


from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
#from save import save_to_file

from flask import Flask, render_template, request, redirect

app = Flask("PythonScrapper")

db = {}#############

#@ = decorator , looks for only a function under it 
@app.route("/")
def home():
  return render_template("templates.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  
  so_jobs = get_so_jobs(word)
  indeed_jobs = get_indeed_jobs(word)
  material = so_jobs + indeed_jobs
  #save_to_file(jobs)
  if word:
    word = word.lower()
    fromDb = db.get(word)########## from here
    if fromDb:
      jobs = fromDb
    else:
      jobs = material
      db[word] = jobs####### to here

  else:
    return redirect("/")
  #flask is rendering the variation in the html file "{{}}"
  return render_template("report.html",searchingBy=word, resultsNumber=len(jobs))##########  , resultsNumber=len(jobs)

@app.route("/<username>")# <> means placeholder
def username(username):
  return "080-0000-0000"
#since Im using in repl.it, host as 0.0.0.0. 
app.run(host="0.0.0.0")


##CSV = Comma Separated Values



# In[ ]:




