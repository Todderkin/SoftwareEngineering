room_number = int(input('Введите номер кабинета: '))

rooms = {
    101: {'code': 1234, 'access': True},
    102: {'code': 1337, 'access': True},
    103: {'code': 8943, 'access': True},
    104: {'code': 5555, 'access': False},
    None: {'code': None, 'access': False},
}

room_info = rooms.get(room_number)
if not room_info:
    room_info = rooms[None]

code = room_info.get('code')
access = room_info.get('access')
print(code, access)