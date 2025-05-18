import datetime

from requests import get, post, delete


def main():
    print('get')

    print(get('http://127.0.0.1:5000/api/users').json())  # работает
    print(get('http://127.0.0.1:5000/api/user/1').json())  # работает
    print(get('http://127.0.0.1:5000/api/user/9999999999999999').json())  # ошибка Bad request
    print(get('http://127.0.0.1:5000/api/user/r').json())  # ошибка 404, т.к. передаем строку, а не число

    print('post')

    print(post('http://127.0.0.1:5000/api/user/post', json={}).json())  # ошибка Empty request

    print(post('http://127.0.0.1:5000/api/user/post',
               json={'title': 'Заголовок'}).json())  # ошибка Bad request, левые данные

    print(post('http://127.0.0.1:5000/api/user/post',
               json={'id': 2,}).json())  # ошибка Bad request, недостаточно данных

    print(post('http://127.0.0.1:5000/api/user/post',
               json={'id': 2,
                     'name': 'Ясос',
                     'surname': 'Биб',
                     'age': 24,
                     'position': '1',
                     'speciality': 'философ',
                     'address': '1000000000-05-19 00:00:00',
                     'hashed_password': '1000000000-05-19 00:00:00',
                     'modified_date': '1000000000-05-19 00:00:00',
                     'email': "ne_pishi_mne@sobaka.py"}).json())  # работает.
    print(get('http://127.0.0.1:5000/api/users').json())  # добавили работу, проверка

    print('delete')

    print(delete('http://localhost:5000/api/user/del/999').json())  # пользователя с id = 999 нет в базе
    print(delete('http://localhost:5000/api/user/del').json())  # ошибка 404, т.к. ничего не передаём
    print(delete('http://localhost:5000/api/user/del/r').json())  # ошибка 404, т.к. передаем строку, а не число

    print(get('http://127.0.0.1:5000/api/users').json())  # все работы до удаления пользователя с id 1
    print(delete('http://localhost:5000/api/user/del/1').json())
    print(get('http://127.0.0.1:5000/api/users').json())  # все работы после удаления пользователя с id 1

    print('радакция работ')

    print(post('http://127.0.0.1:5000/api/user/red', json={}).json())  # ошибка Empty request
    print(post('http://127.0.0.1:5000/api/user/red',
               json={'id': 2,
                     'name': 'Ясосочка',
                     'surname': 'Биб',
                     'age': 2444,
                     'position': '121313'}).json())  # ошибка Bad request, недостаточно данных
    print(post('http://127.0.0.1:5000/api/user/red',
               json={'id': 2,
                     'name': 'Ясосочка',
                     'surname': 'Биб',
                     'age': 2444,
                     'position': '121313',
                     'speciality': 'ytфилософ',
                     'address': '1000000000-05-19 00:00:00',
                     'hashed_password': '00:00:00',
                     'modified_date': '00:00:00',
                     'email': "ne_pishi_mne@sobaka.py"}).json())  # Редактируем второго пользователя.
    print(post('http://127.0.0.1:5000/api/user/red',
               json={'title': 'Заголовок'}).json())  # ошибка Bad request, левые данные

    print('вернём сё на круги своя')

    print(post('http://127.0.0.1:5000/api/user/post',
               json={'id': 1,
                     'name': 'Яна',
                     'surname': 'Цист',
                     'age': 666,
                     'position': 'есть',
                     'speciality': 'инженер-пиротехник',
                     'address': 'ул.Ясоса, дом 6',
                     'hashed_password': '123456',
                     'modified_date': '123456',
                     'email': "est@pochta.rossii"}).json())  # Вернем пользователя с id == 1 для будущих поколений.
    print(delete('http://localhost:5000/api/user/del/2').json())  # удалим пользователя 2 для будущих поколений


if __name__ == '__main__':
    main()
