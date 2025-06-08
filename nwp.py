import sys
import time

# Dummy colors class als voorbeeld, pas aan naar jouw eigen kleurenmodule
class colors:
    CRED2 = ''
    CBLUE2 = ''
    ENDC = ''

def nmap():
    banner = (""" 
 █████╗ ███╗███╗███████╗███████╗██╗   ██╗██╗   ██╗
██╔══██╗████╗████║██╔════╝██╔════╝╚██╗ ██╔╝╚██╗ ██╔╝
███████║██╔████╔██║█████╗  █████╗   ╚████╔╝  ╚████╔╝ 
██╔══██║██║╚██╔╝██║██╔══╝  ██╔══╝    ╚██╔╝    ╚██╔╝  
██║  ██║██║ ╚═╝ ██║███████╗███████╗   ██║      ██║   
╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝   ╚═╝      ╚═╝   
             A  M   S   2   Y   0
""")
    # Banner in blauwe kleur tonen
    for col in banner:
        print(colors.CBLUE2 + col, end="")
        sys.stdout.flush()
        time.sleep(0.0025)

    x = ("""
                Auteur:  ams2y0
                Github:  https://github.com/ams2y0""")
    for col in x:
        print(colors.CBLUE2 + col, end="")
        sys.stdout.flush()
        time.sleep(0.0040)

    y = "\n\t\t[:)]: I hope you like it ! \n"
    for col in y:
        print(colors.CRED2 + col, end="")
        sys.stdout.flush()
        time.sleep(0.0040)

    z = "\n"
    for col in z:
        print(colors.ENDC + col, end="")
        sys.stdout.flush()
        time.sleep(0.4)
        
    print("You chose nmap scanner")
    import os
    target = input("Enter the target IP or domain: ")
    print("Running nmap scan...")
    result = os.system(f"nmap {target}")
    if result != 0:
        print("Nmap scan failed or nmap is not installed.")
    else:
        print("Nmap scan completed.")

def webscraper():
    banner = (""" 
 █████╗ ███╗███╗███████╗███████╗██╗   ██╗██╗   ██╗
██╔══██╗████╗████║██╔════╝██╔════╝╚██╗ ██╔╝╚██╗ ██╔╝
███████║██╔████╔██║█████╗  █████╗   ╚████╔╝  ╚████╔╝ 
██╔══██║██║╚██╔╝██║██╔══╝  ██╔══╝    ╚██╔╝    ╚██╔╝  
██║  ██║██║ ╚═╝ ██║███████╗███████╗   ██║      ██║   
╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝   ╚═╝      ╚═╝   
             A  M   S   2   Y   0
""")
    # Banner in blauwe kleur tonen
    for col in banner:
        print(colors.CBLUE2 + col, end="")
        sys.stdout.flush()
        time.sleep(0.0025)

    x = ("""
                Auteur:  ams2y0
                Github:  https://github.com/ams2y0""")
    for col in x:
        print(colors.CBLUE2 + col, end="")
        sys.stdout.flush()
        time.sleep(0.0040)

    y = "\n\t\t[:)]: I hope you like it ! \n"
    for col in y:
        print(colors.CRED2 + col, end="")
        sys.stdout.flush()
        time.sleep(0.0040)

    z = "\n"
    for col in z:
        print(colors.ENDC + col, end="")
        sys.stdout.flush()
        time.sleep(0.4)
    print("You chose webscraper")
    import requests
    from bs4 import BeautifulSoup

    url = input("Enter the URL to scrape: ")
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        print("Title of the page:", title)
    except Exception as e:
        print("An error occurred:", e)

def password_generator():
    banner = (""" 
 █████╗ ███╗███╗███████╗███████╗██╗   ██╗██╗   ██╗
██╔══██╗████╗████║██╔════╝██╔════╝╚██╗ ██╔╝╚██╗ ██╔╝
███████║██╔████╔██║█████╗  █████╗   ╚████╔╝  ╚████╔╝ 
██╔══██║██║╚██╔╝██║██╔══╝  ██╔══╝    ╚██╔╝    ╚██╔╝  
██║  ██║██║ ╚═╝ ██║███████╗███████╗   ██║      ██║   
╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝   ╚═╝      ╚═╝   
             A  M   S   2   Y   0
""")
    # Banner in blauwe kleur tonen
    for col in banner:
        print(colors.CBLUE2 + col, end="")
        sys.stdout.flush()
        time.sleep(0.0025)

    x = ("""
                Auteur:  ams2y0
                Github:  https://github.com/ams2y0""")
    for col in x:
        print(colors.CBLUE2 + col, end="")
        sys.stdout.flush()
        time.sleep(0.0040)

    y = "\n\t\t[:)]: I hope you like it ! \n"
    for col in y:
        print(colors.CRED2 + col, end="")
        sys.stdout.flush()
        time.sleep(0.0040)

    z = "\n"
    for col in z:
        print(colors.ENDC + col, end="")
        sys.stdout.flush()
        time.sleep(0.4)
    print(banner)
    print("You chose password generator")
    import random
    import string
    def generate_password(length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    length = int(input("How long should your password be? "))
    print("Generated password:", generate_password(length))

# -------------------- main program --------------------

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Welcome", name)
print("You are", age, "years old!")
choice = int(input("Choose a number from 1 to 10: "))
if choice < 2:
    print("cool")
else:
    print("cool")

print("But we're not done yet, let's continue")

serious = input("Do you want to be serious now? ")

if serious == "no":
    print("We're stopping here")
    exit()
elif serious == "yes":
    print("Let's continue")
    
print("Choose an option")
print("1. nmap")
print("2. webscraper")
print("3. password generator")

choice2 = input("Enter a number: ")
if choice2 == "1":
    nmap()
elif choice2 == "2":
    webscraper()
elif choice2 == "3":
    password_generator()
else:
    print("You didn't choose anything, LOSER!")
    
liked = input("Did you like it? ")

if liked == "yes":
    print("Alright, follow me on github")
elif liked == "no":
    print("Too bad, I hope you don't make anything in your life")