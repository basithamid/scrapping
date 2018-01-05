
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.premierleague.com/tables")

c = r.content
soup = BeautifulSoup(c,"html.parser")

tr = soup.find_all("tr")
print(tr)

team_list = []
for item in tr:
    if len(team_list) < 20:
        try:
            team_list.append(item.find("span",{"class":"long"}).text)
        except:
            pass
for team in team_list:
    print(team)

tds = []
for item in tr:
    try:
        tds.append(item.find("td"))
    except:
        pass
print(tds)

for item in tr:
    print(item.find_all("td"))
    print("\n\n\n\n\n\n\n\n\n\n\n")

new_team_list = []
for item in tr:
    if len(new_team_list) < 20:
        try:
            new_team_list.append(item.find("td",{"class":"team"}).find("span",{"class":"long"}).text)
        except:
            pass
print(new_team_list)

