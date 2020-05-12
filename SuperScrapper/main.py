from flask import Flask, render_template, request

app = Flask("PythonScrapper")

#@ = decorator , looks for only a function under it 
@app.route("/")
def home():
  return render_template("templates.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  #flask is rendering the variation in the html file "{{}}"
  return render_template("report.html",searchingBy=word)

@app.route("/<username>")# <> means placeholder
def username(username):
  return "080-0000-0000"
#since Im using in repl.it, host as 0.0.0.0. 
app.run(host="0.0.0.0")