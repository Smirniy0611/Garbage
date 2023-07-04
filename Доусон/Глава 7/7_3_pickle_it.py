# Консервируем
# Демонстрирует консервацию данных и доспут к ним через интерфейс полки
import pickle
import shelve

print('Консервация списков')
variety = ['огурцы', 'помидоры', 'капуста']
shape = ['целые', 'кубиками', 'соломкой']
brand = ['Главпродукт', 'Чумак', 'Бондюэль']
f = open('pickles1.dat', 'wb')
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print('\nРасконсервация списков')
f = open('pickles1.dat', 'rb')
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)

print('\nПомещение списков на полку.')
s = shelve.open('pickles2.dat')
s['variety'] = ['огурцы', 'помидоры', 'капуста']
s['shape'] = ['целые', 'кубиками', 'соломкой']
s['brand'] = ['Главпродукт', 'Чумак', 'Бондюэль']
s.sync()

print('Извлечение списков из файла полки: ')
print('Торговые марки - ', s['brand'])
print('формы - ', s['shape'])
print('виды овощей - ', s['variety'])
s.close()
