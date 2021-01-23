from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    celsius = None
    __tempAnterior = ''
    
    def __init__(self):
        Tk.__init__(self)
        self.title('Termómetro')
        self.geometry('210x150')
        self.configure(bg='#DED789')
        self.resizable(0,0)
        
        self.temperatura = StringVar(value='')
        self.temperatura.trace('w',self.validateTemperature)
        self.celsius = BooleanVar()
        self.celsius.set(True)
        self.createLayout()
        
    def createLayout(self):
        self.entrada = ttk.Entry(self,textvariable=self.temperatura).place(x=10,y=10)
        self.lblSistema = ttk.Label(self,text='Grados:').place(x=10,y=44)
        self.C = ttk.Radiobutton(self,text='Celsius',variable=self.celsius,value=True,command=self.switch).place(x=10,y=64)
        self.F = ttk.Radiobutton(self,text='Fahrenheit',variable=self.celsius,value=False,command=self.switch).place(x=10,y=84)
        
    def validateTemperature(self,*args):
        #permitido = ('0','1','2','3','4','5','6','7','8','9','.')
        #lastChar = self.temperatura.get()[-1:]
        #if lastChar == '.' and self.temperatura.get()[:-1].count('.') > 0 or lastChar not in permitido:
            #self.temperatura.set(self.temperatura.get()[:-1])
        tempNueva = self.temperatura.get()
        try:
            float(tempNueva)
            if tempNueva.find(' ') > 0 or tempNueva[:1] == ' ':
                self.temperatura.set(self.__tempAnterior)
            else:
                self.__tempAnterior = tempNueva
        except:
            if tempNueva == '' or tempNueva == '-':
                self.__tempAnterior = tempNueva
            else:
                self.temperatura.set(self.__tempAnterior)
            
    def switch(self):
        resultado = 0
        aCelsius = self.celsius.get()
        if len(self.temperatura.get()) > 0 and self.temperatura.get() != '-':
            grados = float(self.temperatura.get())
            if aCelsius:
                resultado = grados*9/5+32
            elif not aCelsius:
                resultado = (grados-32)*5/9
            else:
                resultado = grados
            self.temperatura.set(resultado)
    
    def start(self):
        while True:
            self.mainloop()
    
if __name__ == '__main__':
    app = mainApp()
    app.start()