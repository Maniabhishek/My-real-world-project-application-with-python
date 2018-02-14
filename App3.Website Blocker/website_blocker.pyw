from datetime import datetime as dt
import time
hosts_temp="C:\python_programs\my_application\App3.Website Blocker\hosts"
path_host=r"C:\Windows\System32\drivers\etc\hosts"
redirected="127.0.0.1"
website_list=["www.facebook.com","www.pornhd.com","www.instagram.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,12)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hour")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirected+" "+website+"\n")
    else:
        print("fun hours")
        with open(hosts_temp,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()


    time.sleep(5)
