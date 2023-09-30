import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_live_scores():
    url = 'https://www.espncricinfo.com/live-cricket-score'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    date = datetime.now().strftime('%Y-%m-%d ')

    if response.status_code == 200:
        livescore = soup.find('div', class_="ds-px-4 ds-py-3").text.strip()
        team1 = soup.find('div', class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1').text.strip()
        team2 = soup.find('div', class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-opacity-50 ds-my-1').text.strip()

        live_score_message = print(f"Fetching the live scores...\n{team1}\n= {team2}\n=\n{date}")
        
        with open('liveScores.csv', 'a', newline='') as csvfile:
            csv= csv.writer(csvfile)
            csv.writerow([date, team1, team2, livescore])
        return live_score_message
    else:
        return "No live scores available! Try again later."
