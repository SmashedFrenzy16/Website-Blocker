import time
from datetime import datetime

adding_websites = True

path = input("Enter in your OS hosts path: ")

redirect = "127.0.0.1"

websites_array = []

while adding_websites:

    website_name = input("Enter in the URL of the website you want to block: ")

    websites_array.append(website_name)

    continue_add = input("Do you want to add another website (y/n)?")

    if continue_add != "Y" or continue_add != "y":

        break

"""
Hosts Paths On Windows, Mac & Linux:

Windows: C:\Windows\System32\drivers\etc

Mac & Linux: /etc/hosts
"""

path = input("Enter in your OS hosts path: ")

redirect = "127.0.0.1"

while True:

    if datetime(datetime.now().year, datetime.now().month, datetime.now().day, 8) < datetime.now() < datetime(datetime.now().year, datetime.now().month, datetime.now().day, 8):

        with open(path, "r+") as web_file:

            contents = web_file.read()

            for i in websites_array:

                if i in contents:

                    pass

                else:

                    web_file.write(f"{redirect} {i}\n")
    
    else:

        with open(path, "r+") as web_file:

            contents = web_file.readlines()

            web_file.seek(0)

            for i in contents:

                if not any(j in i for j in websites_array):

                    web_file.write(i)

            web_file.truncate()

    time.sleep(5)
