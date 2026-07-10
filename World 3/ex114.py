from requests import get,exceptions

try:
    Re = get('http://www.pudim.com.br/')
except exceptions.ConnectionError:
    print('\033[31mO site pudim não esta acessivel!\033[m')
else:
    print('\033[32mO site pudim esta acessivel!\033[m')