import pyautogui as pag
import keyboard as key


pag.FAILSAFE = True


def main():
    pag.PAUSE = 0.3
    i = 0
    try:
        if pag.confirm('''Откройте окно "Ведомости"''') == 'OK':
            pag.sleep(1)
            pag.leftClick(x=615, y=105)  # Верхняя строка
            while i < 100:
                key.send('enter')
                pag.sleep(0.5)
                key.send('right + enter')
                pag.sleep(0.5)
                pag.leftClick(x=182, y=295)  # Недоставленный заказ
                pag.leftClick(x=501, y=322)  # Заполнить без даты звонка
                key.send('enter')
                pag.leftClick(x=139, y=989)  # OK
                pag.sleep(6)
                # key.send('enter')       #Ок ошибки
                key.send('down')
                pag.sleep(0.5)
                i += 1
    except:
        pag.alert('Программа принудительно завершена')
    print('END')
    pag.alert('Программа завершена')


if __name__ == "__main__":
    main()
