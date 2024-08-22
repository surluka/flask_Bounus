# from extractors.wanted import extract_wanted_jobs
# from file import save_to_file

# keyword = input("무슨 직종을 검색 하시겠습니까?\n")

# jobs = extract_wanted_jobs(keyword)

# save_to_file(keyword, jobs)

from flask import Flask, render_template, request, redirect , send_file
from extractors.wanted import extract_wanted_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = {}  # 딕셔너리의 구조를 모르면 헤깔릴 수 있음

@app.route("/")
def home():
    return render_template("home.html", name = "최은석")


@app.route("/search")
def search():
    
    keyword = request.args.get("keyword")
    
    if keyword == None:
        return redirect("/")
    
    if keyword in db:                          # db 의 키값에서 키워드가 있다면
        jobs = db[keyword]                     # 그 키의 밸류를 jobs 로 한다 가 된다 밸류값이 리스트로 엄청 길겠지?
    else:
        jobs = extract_wanted_jobs(keyword)
        db[keyword] = jobs
        print(db) # 요렇게 해 보면 키워드키값에 대한 밸류값을 볼 수 있다....밸류는 당연하게 리스트안에 딕셔너리가 들어가 있는 형태가 됨
    return render_template("search.html", keyword = keyword, jobs = jobs)

@app.route("/export")
def export():

    keyword = request.args.get("keyword")

    if keyword == None:
        return redirect("/")

    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")

    save_to_file(keyword, db[keyword])

    return send_file(f"{keyword}.csv", as_attachment=True)

app.run("0.0.0.0")