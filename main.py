# from extractors.wanted import extract_wanted_jobs
# from file import save_to_file

# keyword = input("무슨 직종을 검색 하시겠습니까?\n")

# jobs = extract_wanted_jobs(keyword)

# save_to_file(keyword, jobs)

from flask import Flask, render_template 

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name = "최은석")
    

@app.route("/search")
def a_dir():
    return render_template("search.html")

app.run("0.0.0.0")