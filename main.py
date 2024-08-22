from extractors.wanted import extract_wanted_jobs
from file import save_to_file

keyword = input("무슨 직종을 검색 하시겠습니까?\n")

jobs = extract_wanted_jobs(keyword)

save_to_file(keyword, jobs)
