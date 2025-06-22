import requests
from bs4 import BeautifulSoup
import csv

URL = "https://github.com/trending"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

repo_data = []
repos = soup.find_all("article", class_="Box-row")[:5]  # Top 5 repos

for repo in repos:
    anchor = repo.find("h2").find("a")  # Updated this part
    full_name = anchor.get_text(strip=True).replace(" ", "")
    link = "https://github.com" + anchor["href"]
    repo_data.append([full_name, link])

# Save to CSV
with open("trending_repos.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Repository Name", "Link"])
    writer.writerows(repo_data)

print("Top 5 trending repositories saved to 'trending_repos.csv'")
