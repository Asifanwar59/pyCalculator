import kivy
kivy.require('1.09.1')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.button import Button
from functools import partial

# Grey color for disbaled buttons
greyRGBA = [211,211,211,2]
blueRGBA = [150,0,51,53]
btnNumSize = [0.25,0.18]
btnNumPos = [[0,0], [50,0],[100,0],[150,0],[200,0],[250,0],[300,0],[350,0],[400.0],[450,0]]
btnNumVal = ["0","1","2","3","4","5","6","7","8","9"]
btnOpVal = ["+", "-"]
#btnNumList = ["btnZero","btnOne","btnTwo","btnThree","btnFour","btnFive","btnSix","btnSeven","btnEight","btnNine"]


class CalciUI(App):
    def initCalci(self, btnInstance, index):
            self.setBtnVals(btnInstance, btnNumVal[index])
            self.colorBlue(btnInstance)
            self.setBtnPosition(btnInstance, btnNumPos[index])
            self.setBtnSize(btnInstance, btnNumSize)


    def setBtnVals(self,btnInstance,btnVal):
        btnInstance.text=(btnVal)

    def disable(self, instance, *args):
        instance.disabled = True

    def update(self, instance, *args):
        instance.text = "I am disabled!"

    def colorGrey(self, instance,*args):
        instance.background_color=(greyRGBA[0], greyRGBA[1],greyRGBA[2],greyRGBA[3])  #Grey background for disabled buttons

    def colorBlue(self, instance,*args):
        instance.background_color=(blueRGBA[0], blueRGBA[1],blueRGBA[2],blueRGBA[3])

    def setBtnPosition(self, btnInstance, btnPos):
        btnInstance.pos=(btnNumPos[0], btnNumPos[1])

    def setBtnSize(self, btnInstance, btnSize):
        btnInstance.size_hint=(btnSize[0],btnSize[1])

    def build(self):
        btnZero = Button()
        self.initCalci(btnZero, 0)

        btnOne = Button()
        self.initCalci(btnOne,1)

        btnTwo = Button()
        self.initCalci(btnTwo,2)

        btnThree = Button()
        self.initCalci(btnThree,3)

        btnFour = Button()
        self.initCalci(btnFour,4)

        btnFive = Button()
        self.initCalci(btnFive,5)

        btnSix = Button()
        self.initCalci(btnSix,6)

        btnSeven = Button()
        self.initCalci(btnSeven,7)

        btnEight = Button()
        self.initCalci(btnEight,8)

        btnNine = Button()
        self.initCalci(btnNine,9)

        btnList = [btnZero, btnOne, btnTwo, btnThree, btnFour, btnFive, btnSix, btnSeven, btnEight, btnNine]

        return btnList[4]

if __name__ == "__main__":
    calc = CalciUI()
    calc.run()
