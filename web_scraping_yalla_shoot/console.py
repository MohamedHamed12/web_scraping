from  main_ import get_page ,get_leagues,standings_of_league,matches_time

# extract the matches from the shoot-yalla website



url = 'https://live.shoot-yalla.tv/'
page = get_page(url)
leagues=get_leagues(page)      
print("hi")
print("choose number of  what you want :")
print("1 : coming matches")
print("2 : standings_of_league")
res=int(input())
if res==1:
    matches_time=matches_time(page)  
    for  i in matches_time:
        print(i)
else:
    print("choose number of  league you want :")
    for i ,j in enumerate(leagues):
        print(i+1," - ",j['team_name'])

    idx=int(input())-1
    league_standing= standings_of_league(leagues[idx]['url'])   
    for i in league_standing:
        print(i) 