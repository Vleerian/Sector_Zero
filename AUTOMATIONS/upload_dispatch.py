import requests
import urllib.parse
import re
import sys
import time

"""
This takes the formatted output from 
"""
startTiime = time.time()
def log(type: str, message: str):
    runtime = int(time.time() - startTiime)
    print(f'{runtime:05} [{type}] {message}')

log("INFO", f"Loading and processing {sys.argv[3]}")
# Split the dispatch file at the CRLFs to get the header and body
header, body, *other = open(sys.argv[3], "rb").read().split(b"\r\n\r\n")
# The header is formatted as: TitleCRLFDispatchID,Section,Subsection
headerSplit = header.split(b"\r\n")
dispatchTitle = str(urllib.parse.quote(headerSplit[0]))
idInfo = headerSplit[1].split(b",")
dispatchID = int(idInfo[0])
category = int(idInfo[1])
subcategory = int(idInfo[2])
# cut out extra whitespace off the body and format it for upload
dispatchText = str(urllib.parse.quote(body.strip().replace(b"\n",b"")))

log("INFO", f"Preparing to upload to discpatch#{dispatchID}@{sys.argv[1]}")
log("INFO", f"Title: {str(headerSplit[0])}")
# Build out the URIs and UserAgent
userAgent = f"Sector_Zero_Dispatch_Uploader (vleerian on discord, vleerian@hotmail.com, in use by {sys.argv[1]})"
baseAPI = f"https://www.nationstates.net/cgi-bin/api.cgi?nation={sys.argv[1]}"

editDispatchPart = f"&c=dispatch&dispatch=edit&dispatchid={dispatchID}&title={dispatchTitle}&category={category}&subcategory={subcategory}"
editDispatchPart += f"&text={dispatchText}"

log("REQX", "Sending prepare request...")
r = requests.get(baseAPI + editDispatchPart + "&mode=prepare",
    headers={ "User-Agent":userAgent, "X-Password":sys.argv[4] })
token = re.findall("S>([^<]*)<", str(r.content))[0]
log("GOOD", "Token acquired.")

log("REQX", "Sending prepare request...")
xPin = r.headers["X-Pin"]
r = requests.get(baseAPI + editDispatchPart + f"&mode=execute&token={token}",
    headers={ "User-Agent":userAgent, "X-Pin":xPin })
log("GOOD", "UPLOAD COMPLETE")