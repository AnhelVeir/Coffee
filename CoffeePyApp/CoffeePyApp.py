from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from datetime import datetime
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

Builder.load_string("""
#:import SlideTransition kivy.uix.screenmanager.FadeTransition

<LoginScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//fon.png'
    FloatLayout:
        Label:
            id: title_label
            text: "[b][color=#A6622B]Coffee Company[/color][/b]"
            markup: True
            font_size: '24sp'
            size_hint: (.6, .1)
            pos_hint: {'x':.2, 'y':.8}

        Label:
            text: "[i][color=#3E3A37]Учебная практика - Гайдомак Мария (ИСП-925)[/color][/i]"
            markup: True
            font_size: '14sp'
            size_hint: (.5, .1)
            pos_hint: {'x':.25, 'y':.1}
        
        Label:
            id: info_label
            text: ''
            markup: True
            font_size: '18sp'
            size_hint: (.6, .1)
            pos_hint: {'x':.2, 'y':.15} 

        Button:
            id: enter_button
            size_hint: (.22, .08)
            pos_hint: {'x':.24, 'y':.3}
            text: 'Войти'
            background_color: (.94, .66, .39, 1)
            background_normal: ''
            background_down: ''
            on_press: 
                root.btn_press()
            on_release:
                root.btn_release()
            
        Button:
            id: register_button
            size_hint: (.3, .08)
            pos_hint: {'x':.47, 'y':.3}
            text: 'Зарегистироваться'
            background_color: (.94, .66, .39, 1)
            background_normal: ''
            background_down: ''
            on_press: 
                root.register()
            on_release:
                root.btn_release()
            
        Label:
            text:'[color=#231C0B]Имя пользователя[/color]'
            markup : True
            font_size : '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint:{'x':.25, 'y':.67}
            
        TextInput:
            id: login_enter
            text: ''
            size_hint:(.5, .06)
            pos_hint:{'x':.25, 'y':.6}
            multiline:False
            
        Label:
            text:'[color=#231C0B]Пароль[/color]'
            markup : True
            font_size : '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.25, 'y':.52}
            
        TextInput:
            id: passw_enter
            text: ''
            size_hint: (.5, .06)
            pos_hint: {'x':.25, 'y':.45}
            multiline: False
            password : True

<MainScreen>:

    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//fon2.png'

    FloatLayout:
        Button:
            id: addnote_button
            text: 'Добавить запись'
            font_size : '20sp'
            size_hint: (.25, .1)
            pos_hint: {'x':.2, 'y':.6}
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: ''
            on_press:
                root.goto_addnote()

        Button:
            id: editnote_button
            text: 'Изменить запись'
            font_size : '20sp'
            size_hint: (.25, .1)
            pos_hint: {'x':.2, 'y':.4}
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: ''
            on_press:
                root.goto_edit()

        Button:
            id: report_button
            pos_hint: {'x':.2, 'y':.6}
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            text: 'Посмотреть отчёт'
            font_size : '20sp'
            size_hint: (.25, .1)
            pos_hint: {'x':.55, 'y':.6}
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: ''
            on_press:
                root.goto_report()

        Button:
            id: delete_button
            pos_hint: {'x':.2, 'y':.6}
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            text: 'Удалить аккаунт'
            font_size : '20sp'
            size_hint: (.25, .1)
            pos_hint: {'x':.55, 'y':.4}
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: ''
            on_press:
                root.goto_del()
        
        Button:
            text: 'Выйти'
            on_press:
                root.manager.current = 'login'
            size_hint: (.1, .05)
            pos_hint: {'x':.85, 'y':.1}

        Label:
            text: "[i][color=#3E3A37]Учебная практика - Гайдомак Мария (ИСП-925)[/color][/i]"
            markup: True
            font_size: '14sp'
            size_hint: (.5, .05)
            pos_hint: {'x':.25, 'y':.1}
            bcolor: .94, .9, .87, 1
            canvas.before:
                Color:
                    rgba: self.bcolor
                Rectangle:
                    pos: self.pos
                    size: self.size

        Label:
            id: username_label
            text: "[b]Пользователь: [/b]"
            markup: True
            font_size: '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.75, 'y':.9}
            color: (.25, .22, .19, 1)
            bcolor: .94, .9, .87, 1
            canvas.before:
                Color:
                    rgba: self.bcolor
                Rectangle:
                    pos: self.pos
                    size: self.size

<AddnoteScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//fon3.png'
    FloatLayout:
        Label:
            text: '[color=#A6622B]Для добавления записи необходимо ввести дату и обьем проданного кофе[/color]'
            markup : True
            font_size : '20sp'
            size_hint: (1, .1)
            halign: 'left'
            pos_hint: {'x':0, 'y':.8}

        Label:
            text: '[color=#A6622B]Дата в формате дд/мм/гг:[/color]'
            markup : True
            font_size : '18sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.2, 'y':.65}
            
        DataInput:
            id: date
            text: '01/01/20'
            size_hint:(.6, .05)
            pos_hint:{'x':.2, 'y':.6}
            multiline:False
            
        Label:
            text: '[color=#A6622B]Обьем:[/color]'
            markup : True
            font_size : '18sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.2, 'y':.55}
            
        FloatInput:
            id: liters
            text: '0.0'
            size_hint:(.6, .05)
            pos_hint:{'x':.2, 'y':.5}
            multiline:False
            
        Button:
            id: confirm_button
            size_hint: (.5, .1)
            pos_hint: {'x':.25, 'y':.3}
            text: 'Подтвердить'
            on_press: 
                root.confirm()
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: ''
            
        Button:
            text: 'Назад'
            size_hint: (.1, .05)
            pos_hint: {'x':.8, 'y':.1} 
            on_press:
                root.manager.current = 'main'
        
        Label:
            id: info_label
            text: ''
            markup : True
            font_size : '16sp'
            size_hint: (1, .1)
            pos_hint: {'x':0, 'y':.15}    
            
        Label:
            text: "[i][color=#3E3A37]Учебная практика - Гайдомак Мария (ИСП-925)[/color][/i]"
            markup: True
            font_size: '14sp'
            size_hint: (.5, .05)
            pos_hint: {'x':.25, 'y':.1}

        Label:
            id: username_label
            text: "[b]Пользователь: [/b]"
            markup: True
            font_size: '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.75, 'y':.9}
            color: (.25, .22, .19, 1)

<ReportScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//fon3.png'
    FloatLayout:
        Label:
            text: '[color=#A6622B]Отчёт[/color]'
            markup : True
            font_size : '20sp'
            size_hint: (1, .1)
            pos_hint: {'x':0, 'y':.85}
            
        Label:
            text: "[color=#A6622B]Введите начальную дату[/color]"
            markup : True
            size_hint: (.25, .1)
            pos_hint: {'x':.25, 'y':.78}            
            
        Label:
            text: "[color=#A6622B]Введите конечную дату[/color]"
            markup : True
            size_hint: (.25, .1)
            pos_hint: {'x':.52, 'y':.78}            
            
        DataInput:
            id:start_date
            text: '01/01/20'
            size_hint: (.25, .05)
            pos_hint: {'x':.25, 'y':.75}
            multiline: False
        
        DataInput:
            id:end_date
            text: '01/12/20'
            size_hint: (.25, .05)
            pos_hint: {'x':.52, 'y':.75}  
            multiline: False
            
        Button:
            id: confirm_report
            text: "Подтвердить"
            size_hint: (.25, .05)
            pos_hint: {'x':.25, 'y':.69}   
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: '' 
            on_press:
                root.give_report()  
            on_release:
                root.restore_buttons() 

        Button:
            id: clean_button
            text: 'Очистить'
            size_hint: (.25, .05)
            pos_hint: {'x':.52, 'y':.69}
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: ''
            on_press:
                root.clean()
            on_release:
                root.restore_buttons()

        Label:
            id: report_text
            text: '...'
            size_hint: (1, .1)
            pos_hint: {'x':0, 'y':.61} 
            color: (.25, .22, .19, 1)
            
        Button:
            text: 'Назад'
            size_hint: (.1, .05)
            pos_hint: {'x':.8, 'y':.05} 
            on_press:
                root.manager.current = 'main'

        Image:
            id: plot
            source: '.data\\partplot.png'
            size_hint: (1, .48)
            pos_hint: {'x':0, 'y':.15} 
            color: .84, .8, .79, 1
            opacity: 0

        Label:
            text: "[i][color=#3E3A37]Учебная практика - Гайдомак Мария (ИСП-925)[/color][/i]"
            markup: True
            font_size: '14sp'
            size_hint: (.5, .05)
            pos_hint: {'x':.25, 'y':.1}

        Label:
            id: username_label
            text: "[b]Пользователь: [/b]"
            markup: True
            font_size: '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.75, 'y':.9}
            color: (.25, .22, .19, 1)

<EditScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//fon3.png'

    FloatLayout:

        Label:
            text: "[i][color=#3E3A37]Учебная практика - Гайдомак Мария (ИСП-925)[/color][/i]"
            markup: True
            font_size: '14sp'
            size_hint: (.5, .05)
            pos_hint: {'x':.25, 'y':.06}

        Label:
            id: username_label
            text: "[b]Пользователь: [/b]"
            markup: True
            font_size: '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.75, 'y':.9}
            color: (.25, .22, .19, 1)
            bcolor: .94, .9, .87, 1

        Label:
            text: '[color=#A6622B]Здесь можно изменить существующую запись[/color]'
            markup : True
            font_size : '20sp'
            size_hint: (1, .1)
            pos_hint: {'x':0, 'y':.8}

        Label:
            text: "[color=#A6622B]Дата[/color]"
            markup : True
            size_hint: (.175, .1)
            pos_hint: {'x':.2, 'y':.72}            
            
        DataInput:
            id:date
            text: '01/01/20'
            size_hint: (.175, .05)
            pos_hint: {'x':.2, 'y':.7}
            multiline: False
           
        Label:
            text: "[color=#A6622B]Текущий обьём[/color]"
            markup : True
            size_hint: (.175, .1)
            pos_hint: {'x':.4, 'y':.72}            

        Label:
            id: liters_info
            text: "0.0"
            color: (.2, .22, .19, 1)
            markup : True
            size_hint: (.175, .05)
            pos_hint: {'x':.4, 'y':.7}   
            bcolor: .95, .95, .95, 1
            canvas.before:
                Color:
                    rgba: self.bcolor
                Rectangle:
                    pos: self.pos
                    size: self.size
            
        Label:
            text: "[color=#A6622B]Новый обьём[/color]"
            markup : True
            size_hint: (.25, .1)
            pos_hint: {'x':.6, 'y':.72}  

        FloatInput:
            id:liters
            text: '0.0'
            size_hint: (.25, .05)
            pos_hint: {'x':.6, 'y':.7}  
            multiline: False

        Button:
            id: view
            text: 'Посмотреть'
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: '' 
            size_hint: (.175, .05)
            pos_hint: {'x':.2, 'y':.65}  
            on_press:
                root.view()
            on_release:
                root.release()

        Button:
            id: confirm_edit
            text: 'Изменить'
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: '' 
            size_hint: (.175, .05)
            pos_hint: {'x':.4, 'y':.65}  
            on_press:
                root.confirm_edit()
            on_release:
                root.release()

        Button:
            id: delete
            text: 'Удалить данную запись'
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: '' 
            size_hint: (.25, .05)
            pos_hint: {'x':.6, 'y':.65}  
            on_press:
                root.delete()
            on_release:
                root.release()

        Image:
            id: plot
            source: '.data\\plot.png'
            size_hint: (1, .5)
            pos_hint: {'x':0, 'y':.12} 
            color: .84, .8, .79, 1
            opacity: 0
        
        Label:
            id: info_label
            text: ''
            markup: True
            font_size: '16sp'
            size_hint: (.6, .1)
            pos_hint: {'x':.2, 'y':.05} 
        
        Button:
            text: 'Назад'
            size_hint: (.1, .05)
            pos_hint: {'x':.8, 'y':.05} 
            on_press:
                root.manager.current = 'main'

<DeleteScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//fon3.png'

    FloatLayout:
        
        Label:
            text: "[i][color=#3E3A37]Учебная практика - Гайдомак Мария (ИСП-925)[/color][/i]"
            markup: True
            font_size: '14sp'
            size_hint: (.5, .05)
            pos_hint: {'x':.25, 'y':.1}

        Label:
            id: username_label
            text: "[b]Пользователь: [/b]"
            markup: True
            font_size: '18sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.3, 'y':.7}
            color: (.25, .22, .19, 1)
            bcolor: .94, .9, .87, 1

        Label:
            text: '[color=#A6622B]Здесь вы можете удалить аккаунт и все данные в нём[/color]'
            markup : True
            font_size : '20sp'
            size_hint: (1, .1)
            pos_hint: {'x':0, 'y':.8}

        Label:
            text:'[color=#231C0B]Введите пароль:[/color]'
            markup : True
            font_size : '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.3, 'y':.65}
            
        TextInput:
            id: passw_enter
            text: ''
            size_hint: (.4, .05)
            pos_hint: {'x':.3, 'y':.6}
            multiline: False
            password : True

        Button:
            id: delete_acc
            text: 'Удалить аккаунт'
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: '' 
            size_hint: (.25, .05)
            pos_hint: {'x':.25, 'y':.5}  
            on_press:
                root.delete_acc()
            on_release:
                root.release()

        Button:
            id: delete_info
            text: 'Удалить всю информацию'
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: '' 
            size_hint: (.25, .05)
            pos_hint: {'x':.52, 'y':.5}  
            on_press:
                root.delete_info()
            on_release:
                root.release()

        Label:
            id: info_label
            text: ''
            markup: True
            font_size: '18sp'
            size_hint: (.6, .1)
            pos_hint: {'x':.2, 'y':.4} 

        Button:
            text: 'Назад'
            size_hint: (.1, .05)
            pos_hint: {'x':.8, 'y':.1} 
            on_press:
                root.manager.current = 'main'
        
""")

user = ''
users = pd.read_csv('.data\\users.csv', sep=';', index_col=[0])
info = pd.read_csv('.data\\info.csv', sep=';', index_col=[0])

class LoginScreen(Screen):

    def on_enter(self):
        self.ids.login_enter.text = ''
        self.ids.passw_enter.text = ''
        self.ids.info_label.text = ''

    def btn_press(self):
        global users
        self.ids.enter_button.text = 'Проверка'
        self.ids.enter_button.background_normal = ''
        self.ids.enter_button.background_color = (.82, .6, .38, 1.0)

        try:
            temp_passw = users[users.user == self.ids.login_enter.text]['pass'].tolist()[0]
            
            if temp_passw == self.ids.passw_enter.text:
                self.ids.enter_button.text = 'Войти'
                self.ids.enter_button.background_normal = ''
                self.ids.enter_button.background_color = (.94, .66, .39, 1)
                global user
                user = self.ids.login_enter.text
                self.manager.current = 'main'

            else:
                self.ids.info_label.text = '[color=#DD1B07]Неверный пароль[/color]'

        except KeyError:
            self.ids.info_label.text = '[color=#DD1B07]Неверный пароль[/color]'

        except IndexError:
            self.ids.info_label.text = '[color=#DD1B07]Пользователь не найден[/color]'

    def btn_release(self):
        self.ids.enter_button.text = 'Войти'
        self.ids.enter_button.background_normal = ''
        self.ids.enter_button.background_color = (.94, .66, .39, 1)

        self.ids.register_button.text = 'Зарегистироваться'
        self.ids.register_button.background_normal = ''
        self.ids.register_button.background_color = (.94, .66, .39, 1)

    def register(self):
        global users
        self.ids.register_button.text = 'Проверка'
        self.ids.register_button.background_normal = ''
        self.ids.register_button.background_color = (.82, .6, .38, 1.0)

        try:
            users[users.user == self.ids.login_enter.text]['pass'].tolist()[0]

        except IndexError:

            if len(self.ids.login_enter.text) <4 or len(self.ids.passw_enter.text) < 4:
                self.ids.info_label.text = '[color=#DD1B07]Имя пользователя и пароль должны быть не меньше 4 символов[/color]'

            else:
                self.last_index = users.count()[0]
                users.loc[self.last_index] = {'user': self.ids.login_enter.text, 'pass': self.ids.passw_enter.text}
                self.ids.info_label.text = '[color=#DD1B07]Вы зарегистрированы. Нажмите "Войти"[/color]'
                users.to_csv('.data\\users.csv', sep=';')
        else:

            self.ids.info_label.text = '[color=#DD1B07]Пользователь с таким именем уже зарегистрирован[/color]'

class MainScreen(Screen):

    def on_enter(self):
        self.ids.addnote_button.background_color = (.69, .49, .33, 1)
        self.ids.addnote_button.background_normal = ''
        self.ids.report_button.background_color = (.69, .49, .33, 1)
        self.ids.report_button.background_normal = ''
        self.ids.editnote_button.background_color = (.69, .49, .33, 1)
        self.ids.editnote_button.background_normal = ''
        self.ids.delete_button.background_color = (.69, .49, .33, 1)
        self.ids.delete_button.background_normal = ''
        global user
        self.ids. username_label.text = f"[b]Пользователь: {user}[/b]"

    def goto_addnote(self):
        self.ids.addnote_button.background_normal = ''
        self.ids.addnote_button.background_color = (.82, .6, .38, 1.0)
        self.manager.current = 'add'

    def goto_report(self):
        self.ids.report_button.background_normal = ''
        self.ids.report_button.background_color = (.82, .6, .38, 1.0)
        self.manager.current = 'report'

    def goto_edit(self):
        self.ids.editnote_button.background_normal = ''
        self.ids.editnote_button.background_color = (.82, .6, .38, 1.0)
        self.manager.current = 'edit'

    def goto_del(self):
        self.ids.delete_button.background_normal = ''
        self.ids.delete_button.background_color = (.82, .6, .38, 1.0)
        self.manager.current = 'del'


class AddnoteScreen(Screen):

    def on_enter(self):
        global user
        self.ids.username_label.text = f"[b]Пользователь: {user}[/b]"
        self.ids.info_label.text = ""

    def confirm(self):
        global user
        global info
        try:
            self.date = datetime.strptime(self.ids.date.text, "%d/%m/%y")
        except:
            self.ids.info_label.text = '[color=#DD1B07]Некорректно введена дата[/color]'
        else:
            self.ids.info_label.text = ''
            self.date = self.date.strftime("%d/%m/%y")
            if self.ids.liters.text == "":

                self.ids.info_label.text = '[color=#DD1B07]Введите объем[/color]'
            else:
                try:
                    self.index = info[(info['user'] == user) & (info['date'] == self.date)].index[0]
                    self.ids.info_label.text = '[color=#DD1B07]Запись с данной датой уже существует\nНовый объем будет прибавлен к записанному ранее[/color]'

                except IndexError:
                    self.last_index = info.count()[0]
                    info.loc[self.last_index] = {'user': user, 'date': self.date, 'liters': float(self.ids.liters.text)}
                    info['date'] = info['date'].apply(lambda x: datetime.strptime(x, "%d/%m/%y"))
                    info = info.sort_values(by = ['date'])
                    info['date'] = info['date'].apply(lambda x: x.strftime("%d/%m/%y"))
                    info = info.reset_index()
                    del info['index']
                    info.index.name= 'index'
                    info.to_csv('.data\\info.csv', sep=';')
                    self.ids.info_label.text = ""

                else:
                    self.liters = float(info.loc[self.index, 'liters'])
                    self.liters += float(self.ids.liters.text)
                    info.loc[self.index, 'liters'] = self.liters
                    info.to_csv('.data\\info.csv', sep=';')
                    
        finally:
            self.ids.date.text = '01/01/20'
            self.ids.liters.text = '0.0'

class ReportScreen(Screen):

    def on_enter(self):
        global user
        self.ids.username_label.text = f"[b]Пользователь: {user}[/b]"
        self.ids.report_text.text = "..."
        
    def give_report(self):
        global user
        global info
        try:
            self.dt_s = datetime.strptime(self.ids.start_date.text, "%d/%m/%y")
            self.dt_e = datetime.strptime(self.ids.end_date.text, "%d/%m/%y")
        except ValueError:
            self.ids.report_text.text = "Некорректно введена дата"
            self.ids.report_text.color = (.87, .08, 0, 1)
        else:

            self.info_part = info.copy()
            self.info_part.date = self.info_part.date.apply(lambda x: datetime.strptime(x, "%d/%m/%y"))
            self.info_part = self.info_part[(self.info_part.user == user) & (self.info_part.date >= self.dt_s) & (self.info_part.date <= self.dt_e)]
            self.summ = self.info_part['liters'].sum()
            self.info_part.date = self.info_part.date.apply(lambda x: x.strftime("%d/%m/%y"))
            self.ids.report_text.text = f"С {self.ids.start_date.text} по {self.ids.end_date.text} было продано {round(self.summ, 4)} л кофе"
            self.ids.confirm_report.background_color= (.59, .39, .23, 1)
            plt.figure(figsize=(10,5), tight_layout=True)
            sns.set(style="darkgrid")
            plt.plot(self.info_part['date'].values,
                     self.info_part['liters'].values)
            #chart = sns.lineplot(x="date", y="liters", data=self.info_part)
            x_ticks = self.info_part['date'].values
            x_labels = list(self.info_part['date'].values)
            plt.xticks(x_ticks, rotation='90', labels=x_labels)
            plt.savefig('.data\\partplot.png', optimize=True, quality=100)
            self.ids.plot.reload()
            self.ids.plot.source = ".data\\partplot.png"
            self.ids.plot.opacity= 1

        finally:
            info = pd.read_csv('.data\\info.csv', sep=';', index_col=[0])

    def clean(self):
        self.ids.start_date.text = '01/01/20'
        self.ids.end_date.text = '01/12/20'
        self.ids.report_text.text = "..."
        self.ids.clean_button.background_color= (.59, .39, .23, 1)
        self.ids.report_text.color = (.25, .22, .19, 1)
        self.ids.plot.source = ""
        self.ids.plot.opacity= 0

    def restore_buttons(self):
        self.ids.confirm_report.background_color= (.69, .49, .33, 1)
        self.ids.clean_button.background_color= (.69, .49, .33, 1)


class EditScreen(Screen):

    def on_enter(self):
        global user
        global info
        self.ids.username_label.text = f"[b]Пользователь: {user}[/b]"
        self.dates = ""
        self.n = 0
        self.ids.info_label.text = ""
        plt.figure(figsize=(10,5), tight_layout=True)
        ax = plt.subplot(111) 
        sns.set(style="darkgrid")
        #chart = sns.lineplot(x="date", y="liters", data=info[info['user'] == user])
        plt.plot(info[info['user'] == user]['date'].values,
                 info[info['user'] == user]['liters'].values)
        plt.xticks(rotation=90)
        ax.set_title('Статистика по продаже кофе со временем')
        plt.savefig('.data\\plot.png', optimize=True, quality=100)
        self.ids.plot.reload()
        self.ids.plot.source = ".data\\plot.png"
        self.ids.plot.opacity = 1
        
    def confirm_edit(self):
        global info
        self.ids.confirm_edit.background_normal = ''
        self.ids.confirm_edit.background_color = (.82, .6, .38, 1.0)
        try:
            datetime.strptime(self.ids.date.text, "%d/%m/%y")
        except:
            self.ids.info_label.text = '[color=#DD1B07]Некорректно введена дата[/color]'
        else:
            self.ids.info_label.text = ''
            try:
                self.index = info[(info['user'] == user) & (info['date'] == self.ids.date.text)].index[0]

            except IndexError:
                self.ids.info_label.text = '[color=#DD1B07]Записи с такой датой нет[/color]'

            else:
                info.loc[self.index, 'liters'] = float(self.ids.liters.text)
                self.ids.liters_info.text =  self.ids.liters.text
                info.to_csv('.data\\info.csv', sep=';')
                self.ids.info_label.text = ''
                plt.figure(figsize=(10,5), tight_layout=True)
                ax = plt.subplot(111) 
                sns.set(style="darkgrid")
                #chart = sns.lineplot(x="date", y="liters", data=info[info['user'] == user])
                plt.plot(info[info['user'] == user]['date'].values,
                         info[info['user'] == user]['liters'].values)
                plt.xticks(rotation=90)
                ax.set_title('Статистика по продаже кофе со временем')
                plt.savefig('.data\\plot.png', optimize=True, quality=100)
                self.ids.plot.reload()
                self.ids.plot.source = ".data\\plot.png"
                self.ids.plot.opacity = 1

    def view(self):
        self.ids.view.background_normal = ''
        self.ids.view.background_color = (.82, .6, .38, 1.0)
        global info

        try:
            datetime.strptime(self.ids.date.text, "%d/%m/%y")

        except:
            self.ids.info_label.text = '[color=#DD1B07]Некорректно введена дата[/color]'
        else:
            try:
                self.index = info[(info['user'] == user) & (info['date'] == self.ids.date.text)].index[0]

            except IndexError:
                self.ids.info_label.text = '[color=#DD1B07]Записи с такой датой нет[/color]'

            else:
                self.ids.liters_info.text =  str(info.loc[self.index, 'liters'])



    def delete(self):
        self.ids.delete.background_normal = ''
        self.ids.delete.background_color = (.82, .6, .38, 1.0)
        global info
        try:
            datetime.strptime(self.ids.date.text, "%d/%m/%y")
        except:
            self.ids.info_label.text = '[color=#DD1B07]Некорректно введена дата[/color]'
        else:
            self.ids.info_label.text = ''
            try:
                self.index = info[(info['user'] == user) & (info['date'] == self.ids.date.text)].index[0]

            except IndexError:
                self.ids.info_label.text = '[color=#DD1B07]Записи с такой датой нет[/color]'

            else:
                self.ids.info_label.text = ''
                info.drop(self.index, inplace=True)
                info.index = range(0, info.count()[0])
                info.index.name = 'index'
                self.ids.liters_info.text =  '0.0'
                info.to_csv('.data\\info.csv', sep=';')
                plt.figure(figsize=(10,5), tight_layout=True)
                sns.set(style="darkgrid")
                chart = sns.lineplot(x="date", y="liters", data=info[info['user'] == user])
                plt.xticks(rotation=90)
                chart.set_title('Статистика по продаже кофе со временем')
                plt.savefig('.data\\plot.png', optimize=True, quality=100)
                self.ids.plot.reload()
                self.ids.plot.source = ".data\\plot.png"
                self.ids.plot.opacity = 1



    def release(self):
        self.ids.confirm_edit.background_color = (.69, .49, .33, 1)
        self.ids.confirm_edit.background_normal = ''
        self.ids.view.background_color = (.69, .49, .33, 1)
        self.ids.view.background_normal = ''
        self.ids.delete.background_color = (.69, .49, .33, 1)
        self.ids.delete.background_normal = ''

class DeleteScreen(Screen):
    def on_enter(self):
        global user
        self.ids.username_label.text = f"[b]Пользователь: {user}[/b]"
        self.ids.delete_info.background_color = (.69, .49, .33, 1)
        self.ids.delete_info.background_normal = ''
        self.ids.delete_acc.background_color = (.69, .49, .33, 1)
        self.ids.delete_acc.background_normal = ''
        self.ids.info_label.text = ''
        self.ids.passw_enter.text = ''

    def delete_acc(self):
        global users
        global info
        self.ids.delete_acc.background_normal = ''
        self.ids.delete_acc.background_color = (.82, .6, .38, 1.0)

        temp_passw = users[users.user == user]['pass'].tolist()[0]
        self.index = users[users.user == user].index[0]
        if temp_passw == self.ids.passw_enter.text:

            users.drop(self.index, inplace=True)
            users.to_csv('.data\\users.csv', sep=';')
            info = pd.read_csv('.data\\info.csv', sep=';', index_col=[0])
            for i in info[info['user'] == user].index:
                info.drop(i, inplace=True)
            info.index = range(0, info.count()[0])
            info.index.name = 'index'
            info.to_csv('.data\\info.csv', sep=';')
            self.manager.current = 'login'

        else:
            self.ids.info_label.text = '[color=#DD1B07]Неверный пароль[/color]'

    def delete_info(self):
        global user
        global users
        global info
        self.ids.delete_info.background_normal = ''
        self.ids.delete_info.background_color = (.82, .6, .38, 1.0)

        temp_passw = users[users.user == user]['pass'].tolist()[0]
        self.index = users[users.user == user].index[0]

        if temp_passw == self.ids.passw_enter.text:

            for i in info[info['user'] == user].index:
                info.drop(i, inplace=True)
            info.index = range(0, info.count()[0])
            info.index.name = 'index'
            info.to_csv('.data\\info.csv', sep=';')
            self.ids.info_label.text = '[color=#DD1B07]Информация удалена[/color]'

        else:
            self.ids.info_label.text = '[color=#DD1B07]Неверный пароль[/color]'


    def release(self):
        self.ids.delete_info.background_color = (.69, .49, .33, 1)
        self.ids.delete_info.background_normal = ''
        self.ids.delete_acc.background_color = (.69, .49, .33, 1)
        self.ids.delete_acc.background_normal = ''


"""
Поля с ограничением ввода:
FloatInput - только цифры и . (точка один раз)
DataInput - только цифры и / (косых - сколько угодно, 
проверка на корректность происходит в классе AddnoteScreen)
"""
class FloatInput(TextInput):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)


class DataInput(TextInput):
    pat = re.compile('[^0-9//]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        s = re.sub(pat, '', substring)
        return super(DataInput, self).insert_text(s, from_undo=from_undo)

sm = ScreenManager(transition=FadeTransition(duration=.4))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(AddnoteScreen(name='add'))
sm.add_widget(ReportScreen(name='report'))
sm.add_widget(EditScreen(name='edit'))
sm.add_widget(DeleteScreen(name='del'))


class CoffeeApp(App):

    def build(self):
        self.title = 'Coffee Company'
        self.icon = '.data\\myicon.png'
        Window.clearcolor = (.94, .82, .75, 1)
        Window.size = (800, 600)

        return sm

        
if __name__ == "__main__":
    CoffeeApp().run()
