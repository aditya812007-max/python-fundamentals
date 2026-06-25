import csv

name=input("whta's ur name? ")
home=input("where's ur home? ")

with open("day9_names.csv","a") as file:
    write = csv.DictWriter(file, fieldnames=["name","home"])
    write.writerow({"name":name, "home":home})