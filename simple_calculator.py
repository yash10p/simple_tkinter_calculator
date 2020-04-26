
# coding: utf-8

# In[2]:


from tkinter import *
from tkinter import messagebox

calculator = Tk()
calculator.title("Calculator")


class Application(Frame):
    """
    A simple GUI Calculator written using tkinter library.
    """
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.createWidgets()

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def appendToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if self.entryText == "0":
            self.replaceText(text)
        else:
            self.display.insert(self.textLength, text)

    #using inbuilt eval function 
    def calculateExpression(self):
        self.expression = self.display.get()
        self.expression = self.expression.replace("%", "/ 100")

        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
            messagebox.showinfo("ERROR", "Invalid input", icon="warning", parent=calculator)

    #sets input to '0' on pressing AC
    def clearText(self):
        self.replaceText("0")

    def createWidgets(self):
        self.display = Entry(self, font=("Roboto", 16), relief=RAISED, justify=LEFT)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4)


    #First Row        
        self.clearButton = Button(self, font=("Roboto", 11), text="AC", command=lambda: self.clearText())
        self.clearButton.grid(row=1, column=0, columnspan=2,  sticky="NWNESWSE")

        self.percentageButton = Button(self, font=("Roboto", 11), text="%", command=lambda: self.appendToDisplay("%"))
        self.percentageButton.grid(row=1, column=2, sticky="NWNESWSE")

        self.divideButton = Button(self, font=("Roboto", 11), text="/", command=lambda: self.appendToDisplay("/"))
        self.divideButton.grid(row=1, column=3, sticky="NWNESWSE")

    #Second Row
        self.sevenButton = Button(self, font=("Roboto", 11), text="7", command=lambda: self.appendToDisplay("7"))
        self.sevenButton.grid(row=2, column=0, sticky="NWNESWSE")

        self.eightButton = Button(self, font=("Roboto", 11), text="8", command=lambda: self.appendToDisplay("8"))
        self.eightButton.grid(row=2, column=1, sticky="NWNESWSE")

        self.nineButton = Button(self, font=("Roboto", 11), text="9", command=lambda: self.appendToDisplay("9"))
        self.nineButton.grid(row=2, column=2, sticky="NWNESWSE")

        self.timesButton = Button(self, font=("Roboto", 11), text="*", command=lambda: self.appendToDisplay("*"))
        self.timesButton.grid(row=2, column=3, sticky="NWNESWSE")


    #Third Row
        self.fourButton = Button(self, font=("Roboto", 11), text="4", command=lambda: self.appendToDisplay("4"))
        self.fourButton.grid(row=3, column=0, sticky="NWNESWSE")

        self.fiveButton = Button(self, font=("Roboto", 11), text="5", command=lambda: self.appendToDisplay("5"))
        self.fiveButton.grid(row=3, column=1, sticky="NWNESWSE")

        self.sixButton = Button(self, font=("Roboto", 11), text="6", command=lambda: self.appendToDisplay("6"))
        self.sixButton.grid(row=3, column=2, sticky="NWNESWSE")

        self.minusButton = Button(self, font=("Roboto", 11), text="-", command=lambda: self.appendToDisplay("-"))
        self.minusButton.grid(row=3, column=3, sticky="NWNESWSE")


    #Fourth Row
        self.oneButton = Button(self, font=("Roboto", 11), text="1", command=lambda: self.appendToDisplay("1"))
        self.oneButton.grid(row=4, column=0, sticky="NWNESWSE")

        self.twoButton = Button(self, font=("Roboto", 11), text="2", command=lambda: self.appendToDisplay("2"))
        self.twoButton.grid(row=4, column=1, sticky="NWNESWSE")

        self.threeButton = Button(self, font=("Roboto", 11), text="3", command=lambda: self.appendToDisplay("3"))
        self.threeButton.grid(row=4, column=2, sticky="NWNESWSE")

        self.plusButton = Button(self, font=("Roboto", 11), text="+", command=lambda: self.appendToDisplay("+"))
        self.plusButton.grid(row=4, column=3, sticky="NWNESWSE")

    #Fifth Row
        self.zeroButton = Button(self, font=("Roboto", 11), text="0", command=lambda: self.appendToDisplay("0"))
        self.zeroButton.grid(row=5, column=0, columnspan=2, sticky="NWNESWSE")

        self.dotButton = Button(self, font=("Roboto", 11), text=".", command=lambda: self.appendToDisplay("."))
        self.dotButton.grid(row=5, column=2, sticky="NWNESWSE")

        self.equalsButton = Button(self, font=("Roboto", 11), text="=", command=lambda: self.calculateExpression())
        self.equalsButton.grid(row=5, column=3, sticky="NWNESWSE", rowspan=1)


app = Application(calculator).grid()        
calculator.mainloop()

