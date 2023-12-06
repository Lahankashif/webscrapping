import requests
from bs4 import BeautifulSoup

def insta_followers():
    user = input("Enter an existing username: ").lower()
    url = 'https://www.instagram.com/' + user
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    fllwr_count_tag = soup.find('meta', {'name': 'description'})['content']
    start_idx = fllwr_count_tag.find('Followers') - 5
    end_idx = fllwr_count_tag.find(' Following', start_idx)-4
    followers = fllwr_count_tag[start_idx:end_idx]
    
    print(f"\nFollowers Count: {followers}")

insta_followers()
