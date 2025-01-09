import sys

header = """[background-block=#c30000][hr][center][img]https://i.imgur.com/9J1Rqfs.png[/img][/center][hr][/background-block]
[b][size=150][color=c30000]Granted Embassy Protocols[/color][/size][/b]
[table][tr][td]Grant Index[/td][td]Region[/td][td]Diagnostic Score[/td][td]Ratification Commit[/td][/tr]
"""
footer = f"""
[/table]
[hr]
version: {sys.argv[1]}"""
data = None
with open("../PRIVATE/Embassy Protocols.csv") as file:
    data = file.readlines();
rows = []
for i in range(0, len(data)):
    csvSplit = [i.strip() for i in data[i].split(",")]
    rows.append(f"[tr][td]{i}[/td][td][region]{csvSplit[0]}[/region][/td][td]{csvSplit[1]}[/td][td][color=cyan]{csvSplit[2]}[/color][/td][/tr]")

Dispatch = header + "\n".join(rows) + footer
with open("./PUBLIC/GRANTED_EMBASSY_PROTOCOLS.bb", "w+") as file:
    file.write(Dispatch)