from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

def extract_wanted_jobs(keyword):
  p = sync_playwright().start()
  browser = p.chromium.launch(headless=False)
  page = browser.new_page()
  page.goto("https://www.wanted.co.kr/")
  time.sleep(3.0)
  # page.screenshot(path="screenshot.png")

  page.click("button.Aside_searchButton__rajGo")
  time.sleep(3.0)

  page.get_by_placeholder("검색어를 입력해 주세요.").fill(keyword)
  page.keyboard.down("Enter")
  time.sleep(3.0)

  page.click("a#search_tab_position")
  time.sleep(3.0)

  for i in range(4):
    page.keyboard.down("End")
    time.sleep(3.0)

  contents = page.content()

  soup = BeautifulSoup(contents,"html.parser")

  jobs_db = []

  jobs = soup.find_all("div", class_ = "JobCard_container__REty8")

  for job in jobs: 
    link = f"https://www.wanted.co.kr/{job.find('a')['href']}"     # .get("href")
    title = job.find("strong", class_ ="JobCard_title__HBpZf").text
    company = job.find("span", "JobCard_companyName__N1YrF").text
    reward = job.find("span", "JobCard_reward__cNlG5").text

    job = {"link":link,
          "title":title,
          "company":company,
          "reward":reward}
    
    jobs_db.append(job)
  
  p.stop()
    
  return jobs_db 

# file = open("jobs.csv", "w") 
# writter = csv.writer(file)

# writter.writerow(["link", "title", "company", "reward"])
# for job in extract_wanted_jobs(keyword):
#   writter.writerow(job.values())

# file.close()/  
