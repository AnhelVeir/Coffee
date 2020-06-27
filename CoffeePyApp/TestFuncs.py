from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from datetime import datetime
import pandas as pd
import re

Builder.load_string("""
#:import SlideTransition kivy.uix.screenmanager.FadeTransition

<LoginScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'data/fon.png'
    FloatLayout:
        Label:
            id: title_label
            text: "[b][color=#A6622B]Coffee Company[/color][/b]"
            markup: True
            font_size: '24sp'
            size_hint: (.6, .1)
            pos_hint: {'x':.2, 'y':.8}
        
        Label:
            id: info_label
            text: ''
            markup: True
            font_size: '18sp'
            size_hint: (.6, .1)
            pos_hint: {'x':.2, 'y':.15} 
        Button:
            id: main_button
            size_hint: (.2, .08)
            pos_hint: {'x':.3, 'y':.3}
            text: 'Войти'
            on_press: 
                root.btn_press()
            on_release:
                root.btn_release()
            background_color: (.94, .66, .39, 1)
            background_normal: ''
            background_down: ''
            
        Button:
            id: register_button
            size_hint: (.2, .08)
            pos_hint: {'x':.501, 'y':.3}
            text: 'Зарегистироваться'
            on_press: 
                root.register()
            on_release:
                root.btn_release()
            background_color: (.94, .66, .39, 1)
            background_normal: ''
            background_down: ''
            
        Label:
            text:'[color=#231C0B]Login[/color]'
            markup : True
            font_size : '20sp'
            size_hint: (.5, .1)
            halign:'left'
            pos_hint:{'x':.1, 'y':.65}
            
        TextInput:
            id: login_enter
            text: ''
            size_hint:(.4, .05)
            pos_hint:{'x':.3, 'y':.6}
            multiline:False
            
        Label:
            text:'[color=#231C0B]Password[/color]'
            markup : True
            font_size : '20sp'
            size_hint: (.55, .1)
            halign: 'left'
            pos_hint: {'x':.1, 'y':.5}
            
        TextInput:
            id: passw_enter
            text: ''
            size_hint: (.4, .05)
            pos_hint: {'x':.3, 'y':.45}
            multiline: False
            password : True

<MainScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'data/fon2.png'
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
            id: print_report
            text: 'Посмотреть отчёт'
            font_size : '20sp'
            size_hint: (.25, .1)
            pos_hint: {'x':.55, 'y':.6}
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: ''
            on_press:
                root.manager.current = 'report'
        
        Button:
            text: 'Выйти'
            on_press:
                root.manager.current = 'login'
            size_hint: (.1, .05)
            pos_hint: {'x':.85, 'y':.1}
            
            
            
<AddNote>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'data/fon3.png'
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
            size_hint: (.5, .1)
            halign: 'left'
            pos_hint: {'x':.09, 'y':.63}
            
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
            size_hint: (.475, .1)
            halign: 'left'
            pos_hint: {'x':0, 'y':.525}
            
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
            size_hint: (.1, .05)
            pos_hint: {'x':.8, 'y':.1}
            text: 'Назад'
            on_press: 
                root.manager.current = 'main'
        
        Label:
            id: info_label
            text: ''
            markup : True
            font_size : '18sp'
            size_hint: (1, .1)
            pos_hint: {'x':0, 'y':.2}       
        

<ReportScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'data/fon3.png'
    FloatLayout:
        Label:
            text: '[color=#A6622B]Отчёт[/color]'
            markup : True
            font_size : '20sp'
            size_hint: (1, .1)
            pos_hint: {'x':0, 'y':.8}
            
        Label:
            text: "[color=#A6622B]Введите начальную дату[/color]"
            markup : True
            size_hint: (.25, .1)
            pos_hint: {'x':.25, 'y':.72}            
            
        Label:
            text: "[color=#A6622B]Введите конечную дату[/color]"
            markup : True
            size_hint: (.25, .1)
            pos_hint: {'x':.52, 'y':.72}            
            
        DataInput:
            id:start_date
            text: '01/01/20'
            size_hint: (.25, .05)
            pos_hint: {'x':.25, 'y':.7}
            multiline: False
        
        DataInput:
            id:end_date
            text: '01/12/20'
            size_hint: (.25, .05)
            pos_hint: {'x':.52, 'y':.7}  
            multiline: False
            
        Button:
            id: confirm_report
            text: "Подтвердить"
            size_hint: (.25, .05)
            pos_hint: {'x':.25, 'y':.65}   
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
            pos_hint: {'x':.52, 'y':.65}
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
            pos_hint: {'x':0, 'y':.5} 
            color: (.25, .22, .19, 1)
            
        Button:
            text: 'Назад'
            size_hint: (.2, .05)
            pos_hint: {'x':.6, 'y':.1} 
            on_press:
                root.manager.current = 'main'
            
    
    
""")

user = ''

class LoginScreen(Screen):

    def btn_press(self):
        self.users = pd.read_csv('data/users.csv', sep=';', index_col=[0])
        self.login = ''
        self.passw = ''

        self.ids.main_button.text = 'Проверка'
        self.ids.main_button.background_normal = ''
        self.ids.main_button.background_color = (.82, .6, .38, 1.0)
        self.login = self.ids.login_enter.text
        self.passw = self.ids.passw_enter.text
        print(f'Login = {self.ids.login_enter.text}\nPassword = {self.ids.passw_enter.text}')

        try:
            temp_passw = self.users[self.users.user == self.login]['pass'].tolist()[0]
            print(temp_passw)
            print(self.passw)
            if temp_passw == self.passw:
                self.ids.main_button.text = 'Войти'
                self.ids.main_button.background_normal = ''
                self.ids.main_button.background_color = (.94, .66, .39, 1)
                global user
                user = self.login
                self.manager.current = 'main'
                print('Вход')
            else:
                self.ids.info_label.text = '[color=#DD1B07]Неверный пароль[/color]'
                print('Неверный пароль')
        except KeyError:
            self.ids.info_label.text = '[color=#DD1B07]Неверный пароль[/color]'
            print('Неверный пароль')
        except IndexError:
            self.ids.info_label.text = '[color=#DD1B07]Пользователь не найден[/color]'
            print("Пользователь не существует")

    def btn_release(self):
        self.ids.main_button.text = 'Войти'
        self.ids.register_button.text = 'Зарегистироваться'
        self.ids.main_button.background_normal = ''
        self.ids.main_button.background_color = (.94, .66, .39, 1)
        self.ids.register_button.background_normal = ''
        self.ids.register_button.background_color = (.94, .66, .39, 1)

    def register(self):
        self.ids.register_button.text = 'Проверка'
        self.ids.register_button.background_normal = ''
        self.ids.register_button.background_color = (.82, .6, .38, 1.0)

        self.users = pd.read_csv('data/users.csv', sep=';', index_col=[0])
        self.login = self.ids.login_enter.text
        self.passw = self.ids.passw_enter.text
        try:
            self.users[self.users.user == self.login]['pass'].tolist()[0]
        except IndexError:
            if len(self.login) <4 or len(self.passw) < 4:
                self.ids.info_label.text = '[color=#DD1B07]Имя пользователя и пароль должны быть не меньше 4 символов[/color]'
            else:
                self.last_index = self.users.count()[0]
                self.users.loc[self.last_index] = {'user': self.login, 'pass': self.passw}
                self.ids.info_label.text = '[color=#DD1B07]Вы зарегистрированы. Нажмите "Войти"[/color]'
                self.users.to_csv('users.csv', sep=';')
        else:
            self.ids.info_label.text = '[color=#DD1B07]Пользователь с таким именем уже зарегистрирован[/color]'


class MainScreen(Screen):

    def on_enter(self):
        self.ids.addnote_button.background_color = (.69, .49, .33, 1)
        self.ids.addnote_button.background_normal = ''

    def goto_addnote(self):
        self.ids.addnote_button.background_normal = ''
        self.ids.addnote_button.background_color = (.82, .6, .38, 1.0)
        self.manager.current = 'add'


class AddNote(Screen):
    def confirm(self):
        global user
        print(user)
        try:
            datetime.strptime(self.ids.date.text, "%d/%m/%y")
        except:
            self.ids.info_label.text = '[color=#DD1B07]Некорректно введена дата[/color]'
        else:
            if self.ids.liters.text == "":
                self.ids.info_label.text = '[color=#DD1B07]Введите объем[/color]'
            else:
                self.info = pd.read_csv('data/info.csv', sep=';', index_col=[0])
                self.last_index = self.info.count()[0]
                self.info.loc[self.last_index] = {'user': user, 'date': self.ids.date.text, 'liters': self.ids.liters.text}
                self.manager.current = 'main'
                self.info.to_csv('info.csv', sep=';')
        finally:
            self.ids.date.text = '01/01/20'
            self.ids.liters.text = '0.0'

class ReportScreen(Screen):
    def give_report(self):
        global user
        self.info = pd.read_csv('data/info.csv', sep=';', index_col=[0])
        self.info.date = pd.to_datetime(self.info.date)
        try:
            self.dt_s = datetime.strptime(self.ids.start_date.text, "%d/%m/%y")
            self.dt_e = datetime.strptime(self.ids.end_date.text, "%d/%m/%y")
        except ValueError:
            self.ids.report_text.text = "Некорректно введена дата"
            self.ids.report_text.color = (.87, .08, 0, 1)
        else:
            self.summ = self.info[(self.info.date >= self.dt_s) & (self.info.date <= self.dt_e)]['liters'].sum()
            self.ids.report_text.text = f"С {self.ids.start_date.text} по {self.ids.end_date.text} было продано {round(self.summ, 4)} литров кофе"
            self.ids.confirm_report.background_color= (.59, .39, .23, 1)

    def clean(self):
        self.ids.start_date.text = '01/01/20'
        self.ids.end_date.text = '01/12/20'
        self.ids.report_text.text = "..."
        self.ids.clean_button.background_color= (.59, .39, .23, 1)
        self.ids.report_text.color = (.25, .22, .19, 1)

    def restore_buttons(self):
        self.ids.confirm_report.background_color= (.69, .49, .33, 1)
        self.ids.clean_button.background_color= (.69, .49, .33, 1)


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


# Create the screen manager
sm = ScreenManager(transition=FadeTransition(duration=.5))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(AddNote(name='add'))
sm.add_widget(ReportScreen(name='report'))


class TestApp(App):

    def build(self):
        self.title = 'Coffee Company'
        self.icon = 'myicon.png'
        Window.clearcolor = (.94, .82, .75, 1)

        return sm


if __name__ == '__main__':
    TestApp().run()
