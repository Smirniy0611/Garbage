graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()  # создание новой очереди
    search_queue += graph['you']  # создание новой очереди
    searched = [ ] # для отслеживания уже проверенных людей
    while search_queue:   # пока очередь не пуста
        person = search_queue.popleft()   # из очереди извлекается первый человек
        if not person is searched:
            if person_is_seller(person):   # проверяем, является ли человек продавцом манго
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person] # все друзья этого человека добавляются в очередь
                searched.append(person)
    return False

search('you')
