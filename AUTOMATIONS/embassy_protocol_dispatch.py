import sys
import csv

header = """[background-block=#c30000][hr][center][img]https://i.imgur.com/9J1Rqfs.png[/img][/center][hr][/background-block]
[b][size=150][color=c30000]Granted Embassy Protocols[/color][/size][/b]
[table][tr][td]Grant Index[/td][td]Region[/td][td]Diagnostic Score[/td][td]Ratification Commit[/td][/tr]
"""
footer = f"""
[/table]
[hr]
version: {sys.argv[1]}"""
embProto = [Tag for Tag in csv.DictReader(open("PRIVATE/EMBASSY PROTOCOLS.csv", "r"))]
rows = []
for i in range(0, len(embProto)):
    rows.append(f"[tr][td]{i}[/td][td][region]{embProto[i]["embassy"]}[/region][/td][td]{embProto[i]["score"]}[/td][td][color=cyan]{embProto[i]["checksum"]}[/color][/td][/tr]")

Dispatch = header + "\n".join(rows) + footer
with open("PUBLIC/GRANTED_EMBASSY_PROTOCOLS.bb", "w+") as file:
    file.write(Dispatch)