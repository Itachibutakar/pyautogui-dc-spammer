import pyperclip#CODED BY L4V1N14
import pyautogui#CODED BY L4V1N14
import time#CODED BY L4V1N14
from pip._vendor.colorama import Fore#CODED BY L4V1N14
message = input("Spam atmak istiyormusun ? e-h > ")#CODED BY L4V1N14
if message == "e":#CODED BY L4V1N14
    index = input(Fore.GREEN+"Ne yazmak istiyoursunuz ? > "+Fore.RESET)#CODED BY L4V1N14
    repeats = int(input(Fore.GREEN+"Kaç Mesaj Atmak İstiyorsunuz ? > "+Fore.RESET))#CODED BY L4V1N14
    bitis = input("Bitiş mesajını yazınız > ")
    delay = int(input(Fore.RED+"Kaç milisaniye gecikmeli olarak mesaj atılsın ?(kötü bilgisayarlar için yüksek sayılar önerilir) > "+Fore.RESET))#CODED BY L4V1N14
    isLoaded = input(Fore.RED+"ENTER'a BAS VE SPAMI BAŞLAT... ")#CODED BY L4V1N14
    print(Fore.YELLOW+"5 saniye sonra spam başlayacak lütfen discordu tam ekran yap."+Fore.RESET)
    time.sleep(5)#CODED BY L4V1N14
    pyautogui.moveTo(820,680)
    pyautogui.leftClick()
    pyperclip.copy(index)
    for i in range(repeats):#CODED BY L4V1N14
        pyautogui.hotkey("ctrl", "v") 
        pyautogui.press("enter")
        time.sleep(delay/1000)
    pyperclip.copy(bitis)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    print("END")


else:#CODED BY L4V1N14
    print("O zaman burda işin yok 3 saniye sonra program otomatik kapanacaktır!")
    time.sleep(3)
    exit#CODED BY L4V1N14
#CODED BY L4V1N14
