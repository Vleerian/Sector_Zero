import sys
import time
import re
"""
This generates a changelog, starting from a specified commit
git_log.txt must be generated prior to running, generate it using
`git --no-pager log --pretty=format:"%H%x09%an%x09%x09%s" > git_log.txt`

usage: python generate_changelog.py CHECKSUM
"""
startTiime = time.time()
def log(type: str, message: str):
    runtime = int(time.time() - startTiime)
    print(f'{runtime:05} [{type}] {message}')

Target_Checksum = sys.argv[1]
# Fetch all the data needed to construct the manifests
repository = re.findall("^([^ ]*)\t.*\t(.*)$", open("git_log.txt", "r").read(), flags=re.RegexFlag.IGNORECASE | re.RegexFlag.MULTILINE)
# Find the correct commit to start on
StartIndex = [i for i in range(len(repository)) if Target_Checksum in repository[i][0]][0]
NewCommits = repository[:StartIndex]

print(f"[b]Changelog[/b] for {NewCommits[-1][0][:7]} -> {NewCommits[0][0][:7]}")
print(f"[i]More recent changes are at the top[/i]")
for entry in NewCommits:
    print(f"{entry[0][:7]} - {entry[1]}")