import os,time

os.system('cls||clear')
time.sleep(0.2)

def tambah():
    os.system('cls||clear')
    time.sleep(0.3)
    print('===== PENJUMLAHAN SEDERHANA =====')
    a = int(input('Angka  Pertama => '))
    b = int((input('Angka Kedua => ')))
    result = a + b
    time.sleep(0.3)
    print('\nHasil penjumlahan {} + {} adalah {}'.format(a,b,result))
    print('=================================')
    q = input('ULANG ? (y/n) : ')
    if q == 'y':
        tambah()
    elif q == 'n':
        menu()
def tambah():
    os.system('cls||clear')
    time.sleep(0.3)
    print('===== PENJUMLAHAN SEDERHANA =====')
    a = int(input('Angka Pertama => '))
    b = int((input('Angka Kedua => ')))
    result = a + b
    time.sleep(0.3)
    print('\nHasil penjumlahan {} + {} adalah {}'.format(a,b,result))
    print('=================================')
    q = input('ULANG ? (y/n) : ')
    if q == 'y':
        tambah()
    elif q == 'n':
        menu()
def kurang():
    os.system('cls||clear')
    time.sleep(0.3)
    print('===== PENGURANGAN SEDERHANA =====')
    a = int(input('Angka Pertama => '))
    b = int((input('Angka Kedua => ')))
    result = a - b
    time.sleep(0.3)
    print('\nHasil pengurangan {} - {} adalah {}'.format(a,b,result))
    print('=================================')
    q = input('ULANG ? (y/n) : ')
    if q == 'y':
        kurang()
    elif q == 'n':
        menu()
def kali():
    os.system('cls||clear')
    time.sleep(0.3)
    print('===== PERKALIAN SEDERHANA =====')
    a = int(input('Angka  Pertama => '))
    b = int((input('Angka Kedua => ')))
    result = a * b
    time.sleep(0.3)
    print('\nHasil perkalian {} x {} adalah {}'.format(a,b,result))
    print('=================================')
    q = input('ULANG ? (y/n) : ')
    if q == 'y':
        kali()
    elif q == 'n':
        menu()


def menu():
    os.system('cls||clear')
    time.sleep(0.5)
    print('\n===== APLIKASI PENGHITUNG SEDERHANA ======')
    print('FITUR : \n')
    print('[1] PERTAMBAHAN')
    print('[2] PENGURANGAN')
    print('[3] PERKALIAN')

    menu = int(input('\nPILIH FITUR => '))
    if menu == 1:
        tambah()
    elif menu == 2:
        kurang()
    elif menu == 3:
        kali()

if __name__ == "__main__":
    while(True):
        menu()