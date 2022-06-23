import json

# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.
file_path = 'C:\Programming Language\Programming\Python'
file_path += r'\python_work\text_files\\'
filename = 'username.json'
def get_stored_username():
    """Получает имя пользователя, если оно существует."""
    try:
        with open(file_path + filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input('What is your name? ')
    with open(file_path + filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username

def greet_user():
    """Приветствуем пользователя по имени."""
    username = get_stored_username()
    if username:
        print('Welcome back, ' + username + '!')
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " +
              username + "!")

greet_user()
