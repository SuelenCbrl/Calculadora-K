from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (300, 650)

class Aplicativo(App):
    def build(self):
        layout = BoxLayout(orientation='vertical') 
        header = BoxLayout(orientation='horizontal') 
        header.size_hint = (1.0, 0.3)

        main = BoxLayout(orientation='horizontal')  
        num_grid = GridLayout(cols=3) 
        op_grid = GridLayout(cols=1, size_hint=(0.3, 1.0)) 

        footer = BoxLayout()  
        footer.size_hint = (1.0, 0.2)

        self.display = Label(text='', font_size='35px')

        # Botões numéricos
        self.bot1 = Button(text='1')
        self.bot2 = Button(text='2')
        self.bot3 = Button(text='3')
        self.bot4 = Button(text='4')
        self.bot5 = Button(text='5')
        self.bot6 = Button(text='6')
        self.bot7 = Button(text='7')
        self.bot8 = Button(text='8')
        self.bot9 = Button(text='9')
        self.bot0 = Button(text='0')
        ## cor dos operadores 
        cor_operadores = (64/255, 224/255, 208/255, 1)
        # Botões de operação
        self.botSom = Button(text='+',background_color=cor_operadores)
        self.botSub = Button(text='-',background_color=cor_operadores)
        self.botMult = Button(text='*',background_color=cor_operadores)
        self.botDiv = Button(text='/',background_color=cor_operadores)
        self.botPot = Button(text='^',background_color=cor_operadores)
        self.botM = Button(text='=',color='blue')
        self.botC = Button(text='C',color='red')  
        self.botDel = Button(text='x',color='red')  

        devs = Label(text='Develop by @Fabrica32')

        ####################### EVENTOS #######################
        self.botC.bind(on_press=self.apagar)
        self.botDel.bind(on_press=self.apagar_um)

        self.bot1.bind(on_press=self.armazenar)
        self.bot2.bind(on_press=self.armazenar)
        self.bot3.bind(on_press=self.armazenar)
        self.bot4.bind(on_press=self.armazenar)
        self.bot5.bind(on_press=self.armazenar)
        self.bot6.bind(on_press=self.armazenar)
        self.bot7.bind(on_press=self.armazenar)
        self.bot8.bind(on_press=self.armazenar)
        self.bot9.bind(on_press=self.armazenar)
        self.bot0.bind(on_press=self.armazenar)

        self.botSom.bind(on_press=self.armazenar)
        self.botSub.bind(on_press=self.armazenar)
        self.botMult.bind(on_press=self.armazenar)
        self.botPot.bind(on_press=self.armazenar)
        self.botDiv.bind(on_press=self.armazenar)

        self.botM.bind(on_press=self.calcular)

        header.add_widget(self.display)

        
        num_grid.add_widget(self.bot1)
        num_grid.add_widget(self.bot2)
        num_grid.add_widget(self.bot3)
        num_grid.add_widget(self.bot4)
        num_grid.add_widget(self.bot5)
        num_grid.add_widget(self.bot6)
        num_grid.add_widget(self.bot7)
        num_grid.add_widget(self.bot8)
        num_grid.add_widget(self.bot9)
        num_grid.add_widget(self.bot0)
        num_grid.add_widget(self.botC)
        num_grid.add_widget(self.botDel)  

        
        op_grid.add_widget(self.botSom)
        op_grid.add_widget(self.botSub)
        op_grid.add_widget(self.botMult)
        op_grid.add_widget(self.botDiv)
        op_grid.add_widget(self.botPot)
        op_grid.add_widget(self.botM)

        main.add_widget(num_grid)
        main.add_widget(op_grid)

        footer.add_widget(devs)

        layout.add_widget(header)
        layout.add_widget(main)
        layout.add_widget(footer)

        return layout

    def armazenar(self, event):
        self.display.text += event.text

    def apagar(self, event):
        self.display.text = ''

    def apagar_um(self, event):
        self.display.text = self.display.text[:-1]  
    def calcular(self, event):
         if '+' in self.display.text:
            number= self.display.text.split('+')
            soma=float(number[0])+float(number[1])
            self.display.text=str(soma)

         elif '-' in self.display.text:
            number1= self.display.text.split('-')
            sub=float(number1[0])-float(number1[1])
            self.display.text=str(sub)
        
         elif '*' in self.display.text:
            number2= self.display.text.split('*')
            mult=float(number2[0])*float(number2[1])
            self.display.text=str(mult)
            
         elif '^' in self.display.text:
            number4 = self.display.text.split('^')
            expoente = float(number4[0]) ** float(number4[1])
            self.display.text = str(expoente)


         elif '/' in self.display.text:
            number3= self.display.text.split('/')
            div=float(number3[0])/float(number3[1])
            self.display.text=str(div)

if __name__ == "__main__":
    Aplicativo().run()
