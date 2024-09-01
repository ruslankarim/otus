import re
def main():
    normalize_release_jira = ['R' + r.strip() if 'r' not in r.lower() and r != 'develop' else r.strip() for r in re.split(
        r"\s+|\s*\(\s*|\s*\)\s*|\s*/\s*|\s*\\\s*", 'R4.1.6\R4.1.7') if r != '' and re.search(r"R*\d+.\d+|develop", r)]
    print(normalize_release_jira)


main()