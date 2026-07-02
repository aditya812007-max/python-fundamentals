import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?x\.com/([0-9a-z_]+)", url, re.IGNORECASE):

    print(f"USERNAME: {matches.group(1)}")