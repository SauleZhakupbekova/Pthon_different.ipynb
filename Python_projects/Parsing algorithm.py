from bs4 import BeautifulSoup as bs # beautiful soap understands html files.
# make query to needed website
import requests as rq  #request - get info from website
site = rq.get('https://afisha.yandex.ru/moscow/selections/cinema-today')
# response[200] means that site is opened for parsing.
# we have some sites which don`t exist or prohibitted.
# They have another number like 404...
# find all needed texts. We use module bs (beautiful soap). We give it required text and gives it extends lxml (special format of parsing)
res = bs(site.text, "lxml")
#find element h2 with class
res.find_all('h2', class_ = 'Title-sc-5meihc-3 eOlfER')
film_names = res.find_all('h2', class_ = 'Title-sc-5meihc-3 eOlfER')
film_names[0].text
film_names = [i.text for i in film_names]
film_places = res.find_all('li', class_ = 'DetailsItem-sc-5meihc-1 gzFGVO')
film_places[1].text
film_places = [i.text for i in film_places]
print(film_places)
dates = film_places[::2]
print(dates)
places = film_places[1::2]
print(places)
dates_places = [dates[i] + '|' + places[i] for i in range (len(dates))
score = res.find_all('span', class_ = 'Inner-sc-10iay7v-1 jhANBY')
#transfer to text from beautiful soap format
score = [i.text for i in score]
print (score)
score.insert(8, "N/A")
score.insert(16, "N/A")
print (score)
hasScore = score[::2]
print(hasScore)
hasTickets = score[1::2]
print(hasTickets)
film_names
dates
places
hasScore
hasTickets
print(len(film_names))
print(len(dates))
print(len(places))
print(len(hasScore))
print(len(hasTickets))
info = [hasScore, places, dates, hasTickets]
info
films = {}
for names in range(len(film_names)):
    films[film_names[names]] = []
    for i in info: #i is small arrays in info
        films[film_names[names]].append(i[names])
for i in films:
    print(i)
    print('-' * len(i)) # --- has length as i
    print(*films[i])# * means show all i in films
    print()
for i in films:
    print(i)
    print('-' * len(i)) # --- has length as i
    print('|'.join(films[i]))
    print()