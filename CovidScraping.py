import requests
from bs4 import BeautifulSoup
import os
import time


def Pause(n):
    time.sleep(n)


def CLR():
    os.system("CLS")


def CoronaReport():
    a = list()
    print("Search for A Country for CORONA Report - ", end="")
    n = input()
    CLR()
    page = requests.get('https://www.worldometers.info/coronavirus/#countries')
    soup = BeautifulSoup(page.content, 'html.parser')
    for record in soup.findAll('tr'):
        b = list()
        for data in record.findAll('td'):
            if data.text == '' or data.text == ' ':
                b.append(0)
            else:
                b.append(data.text)
        a.append(b)

    # print("Loading Results", end="", flush=True)
    # time.sleep(1)
    # print(".", end="", flush=True)
    # time.sleep(1)
    # print(".", end="", flush=True)
    # time.sleep(1)
    # print(".", end="", flush=True)
    # time.sleep(1)
    CLR()

    for i in range(1, len(a)):
        if a[i][0] == n:
            print(f"Location : {a[i][0]}")
            print(f"Cases Confirmed : {a[i][1]}")
            print(f"Cases Today : {a[i][2]}")
            print(f"Total Death till now : {a[i][3]}")
            print(f"New Deaths : {a[i][4]}")
            print(f"Total Recovered : {a[i][5]}")
            print(f"Active Cases : {a[i][6]}")
            break


def Driver():
    ch = '1'
    while ch == '1':
        CoronaReport()
        print("\r")
        print("Press 1 For More Search")
        print("Press 0 to Exit")
        print("Your Choice - ", end="")
        ch = input()
        CLR()


Driver()
