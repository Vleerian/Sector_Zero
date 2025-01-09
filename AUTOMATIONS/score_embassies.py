import requests
import csv
import sys
import re
import time

def canonnicalize(region : str):
    return region.replace(" ", "_").lower()

print("Fetching Embassy Grants from the repository...")
# Fetch all the data needed to construct the manifests
repository = re.findall("(.{7}).*((?:grant)|(?:revoke)) embassy protocol to (.*)", open(".git/logs/HEAD", "r").read(), flags=re.RegexFlag.IGNORECASE)
Embassy_Grants = {}
for entry in repository:
    Embassy_Grants[canonnicalize(entry[2])] = (entry[0], entry[1].lower() == "grant")

print("Reading tag weights...")
Tag_Weights = [Tag for Tag in csv.DictReader(open("PRIVATE/Tag Weights.csv", "r"))]

print("Fetching regions by tag...")
headers = { "User-Agent":f"S0 Scanner/0.1 (by vleerian (discord) vleerian@hotmail.com in use by {sys.argv[1]})" }
tagged_regions = {}
for tag in Tag_Weights:
    print(f"Requesting {tag["tag_name"]} tagged regions...")
    time.sleep(0.7)
    data = requests.get(f"https://www.nationstates.net/cgi-bin/api.cgi?q=regionsbytag;tags={tag["tag_name"]}", headers=headers)
    tagged_regions[tag["tag_name"]] = ([canonnicalize(r) for r in str(data.content)[20:][:-20].split(",")], int(tag['score']))

scanData = []
for region, grant_data in Embassy_Grants.items():
    print(f"Embassy diagnostic scan for {region}...")
    time.sleep(0.7)
    data = requests.get(f"https://www.nationstates.net/cgi-bin/api.cgi?region={region}&q=embassies", headers=headers)
    embassies = [canonnicalize(e) for e in re.findall('<EMBASSY>([^<]*)</EMBASSY>', str(data.content))]
    score = 0
    for embassy in embassies:
        for tag, tagged_data in tagged_regions.items():
            if embassy in tagged_data[0]:
                score += tagged_data[1]
    scanData.append(f"{region}, {grant_data[0]}, {score}, {grant_data[1]}")

print(f"Scan complete. Writing results to CSV")
with open("PRIVATE/EMBASSY PROTOCOLS.csv", "w+") as file:
    file.write("embassy,checksum,score,granted\n")
    file.write("\n".join(scanData))
    