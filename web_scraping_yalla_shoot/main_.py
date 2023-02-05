import requests
from bs4 import BeautifulSoup

def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    return soup
    # response.status_code


def get_leagues(soup):
    lst=list()
    leagues = soup.find('div', class_="league-side")
   
    for a in leagues.find_all('a', href=True):
        url= a['href']
        team_name=a.text.strip()
        tmp={
            'team_name':team_name,
            'url':url,
        }
        lst.append(tmp)
    return lst



def matches_time(soup):       
    lst=list()
    result = soup.find(id="matchTable")
    mats = result.find_all('div', class_"match-event")
    # item=mats[0]
    for item in mats:
        firstTeam = item.find('div', class_="first-team").find('div',
                                    class_="team-name team-name-ar").find('span').text

        secondTeam = item.find('div', class_="left-team").find('div',
                                    class_="team-name team-name-ar").find('span').text

        time = item.find(id="result-now").text
        tmp={
            'firstTeam':firstTeam,
            'secondTeam':secondTeam,
            'time':time
        }
        # print(firstTeam, "  vs   ", secondTeam, "   time  ", time)
        lst.append(tmp)
    return lst



def standings_of_league(link):
    lst=[]
    soup = get_page( link)
    standing = soup.find(id='standings').find_all('div', class_="row-standing")
    
    for row in standing:
       
        team_name=row.find('div', class_="standing-team").text.strip()
        points=row.find('div', class_="standing-pt").text.strip()
        num_wins=row.find('div', class_="standing-win").text.strip()
        tmp={
            "team_name":team_name,
            "points":points,
            "num_wins":num_wins
        }
        lst.append(tmp)
    return lst


    