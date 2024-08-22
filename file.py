def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w") 
    file.write("link, title, company, reward\n")

    for job in jobs:
        file.write(f"{job['link']},{job['title']},{job['company']},{job['reward']}\n")

    file.close()  
