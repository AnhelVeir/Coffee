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
            size_hint: (.2, .08)
            pos_hint: {'x':.3, 'y':.3}
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
            size_hint: (.2, .08)
            pos_hint: {'x':.501, 'y':.3}
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
            pos_hint:{'x':.3, 'y':.65}
            
        TextInput:
            id: login_enter
            text: ''
            size_hint:(.4, .05)
            pos_hint:{'x':.3, 'y':.6}
            multiline:False
            
        Label:
            text:'[color=#231C0B]Пароль[/color]'
            markup : True
            font_size : '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.3, 'y':.5}
            
        TextInput:
            id: passw_enter
            text: ''
            size_hint: (.4, .05)
            pos_hint: {'x':.3, 'y':.45}
            multiline: False
            password : True
""")

user = ''

class LoginScreen(Screen):

    def btn_press(self):
        self.users = pd.read_csv('data/users.csv', sep=';', index_col=[0])

        self.ids.enter_button.text = 'Проверка'
        self.ids.enter_button.background_normal = ''
        self.ids.enter_button.background_color = (.82, .6, .38, 1.0)

        print(f'Login = {self.ids.login_enter.text}\nPassword = {self.ids.passw_enter.text}')

        try:
            temp_passw = self.users[self.users.user == self.ids.login_enter.text]['pass'].tolist()[0]
            print(temp_passw)
            print(self.ids.passw_enter.text)
            
            if temp_passw == self.ids.passw_enter.text:
                self.ids.enter_button.text = 'Войти'
                self.ids.enter_button.background_normal = ''
                self.ids.enter_button.background_color = (.94, .66, .39, 1)
                global user
                user = self.ids.login_enter.text
                #! Прописать переход к след. экрану
                #self.manager.current = 'next_screen'
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
        self.ids.enter_button.text = 'Войти'
        self.ids.enter_button.background_normal = ''
        self.ids.enter_button.background_color = (.94, .66, .39, 1)

        self.ids.register_button.text = 'Зарегистироваться'
        self.ids.register_button.background_normal = ''
        self.ids.register_button.background_color = (.94, .66, .39, 1)

    def register(self):
        self.ids.register_button.text = 'Проверка'
        self.ids.register_button.background_normal = ''
        self.ids.register_button.background_color = (.82, .6, .38, 1.0)

        self.users = pd.read_csv('data/users.csv', sep=';', index_col=[0])

        try:
            self.users[self.users.user == self.ids.login_enter.text]['pass'].tolist()[0]

        except IndexError:

            if len(self.ids.login_enter.text) <4 or len(self.ids.passw_enter.text) < 4:
                self.ids.info_label.text = '[color=#DD1B07]Имя пользователя и пароль должны быть не меньше 4 символов[/color]'

            else:
                self.last_index = self.users.count()[0]
                self.users.loc[self.last_index] = {'user': self.ids.login_enter.text, 'pass': self.ids.passw_enter.text}
                self.ids.info_label.text = '[color=#DD1B07]Вы зарегистрированы. Нажмите "Войти"[/color]'
                self.users.to_csv('data/users.csv', sep=';')
        else:

            self.ids.info_label.text = '[color=#DD1B07]Пользователь с таким именем уже зарегистрирован[/color]'


sm = ScreenManager(transition=FadeTransition(duration=.5))
sm.add_widget(LoginScreen(name='login'))

class CoffeeApp(App):

    def build(self):
        self.title = 'Coffee Company'
        self.icon = 'data\myicon.png'
        Window.clearcolor = (.94, .82, .75, 1)

        return sm

        
if __name__ == "__main__":
    CoffeeApp().run()
