import sys
import csv
import time
"""
This generates a dispatch upload file using the CSV output of score_embassies.py
The output has two primary sections, the header and content
Headers are formatted with CLRF at the end of each line, similarly to HTTP
The Content is partitioned with two CLRFs, same as HTTP

usage: python embassy_protocol_dispatch.py CHECKSUM DISPATCH_ID
"""
startTiime = time.time()
def log(type: str, message: str):
    runtime = int(time.time() - startTiime)
    print(f'{runtime:05} [{type}] {message}')

log("INFO", f"Generating Embassy Grant SZD for {sys.argv[2]}")
Header = f"[HIGHSEC] S0 Embassy Policy Test\r\n{sys.argv[2]},1,109\r\n\r\n"

Content = """[background-block=#c30000][hr][center][img]https://i.imgur.com/9J1Rqfs.png[/img][/center][hr][/background-block]
[b][size=150][color=c30000]Granted Embassy Protocols[/color][/size][/b]
[table][tr][td]Grant Index[/td][td]Region[/td][td]Diagnostic Score[/td][td]Ratification Commit[/td][/tr]
"""

log("INFO", "Loading Embassy Protocol manifest")
embProto = [Tag for Tag in csv.DictReader(open("PRIVATE/EMBASSY PROTOCOLS.csv", "r"))]
rows = []
for i in range(0, len(embProto)):
    rows.append(f"[tr][td]{i}[/td][td][region]{embProto[i]["embassy"]}[/region][/td][td]{embProto[i]["score"]}[/td][td][color=cyan]{embProto[i]["checksum"]}[/color][/td][/tr]")

Content += "\n".join(rows)

Content += f"""
[/table]
[hr]
version: {sys.argv[1]}"""

log("INFO", "Saving SZD file")
with open("PUBLIC/GRANTED_EMBASSY_PROTOCOLS.SZD", "w+") as file:
    file.write(Header+Content)
log("DONE", "Embassy grant file saved")
print(Header+Content)