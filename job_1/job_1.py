import requests


TOKEN = '2619421814940190'  # Токен
superhero_list = ['Hulk', 'Thanos', 'Captain America']  # Список супергероев для сравнения


def intelligence_compare(hero_list):
    # функция определения и сравнения интелекта супергероес\в
    super_man = []  # Создаем пустой список для храниния профилей супергероев
    for hero in hero_list:  # Перебираем элементы списка
        url = f'https://www.superheroapi.com/api.php/{TOKEN}/search/{hero}'  # Формируем строку запроса
        intelligence = requests.get(url).json()  # Скачиваем профиль супергероя в формате .JSON
        try:
            for power_stats in intelligence['results']:  # Выбираем позазатели интеллекта из всех характеристик

                super_man.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })  # Добавляем имя и уровень интеллекта в созданный ранее список
        except KeyError:  # Выводим сообщение в случае ошибки входных данных
            print(f"Ошибка. Проверьте список супергероев: {hero_list}")

    intelligence_super_hero = 0  # Определяем начальное значение интеллекта
    name = ''  # И переменную для имени
    for intelligence_hero in super_man:  # Выбираем супергероя из заполненного списка
        # Если уровень его интеллекта выше предыдущего, то перезаписыаем переменные имени и интеллекта
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый интелектуальный супергерой: {name}, его интелект: {intelligence_super_hero}")  # Выводим результат


if __name__ == '__main__':

    intelligence_compare(superhero_list)  # Вызываем созданную функцию