from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from datetime import datetime
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns


Builder.load_string("""
#:import SlideTransition kivy.uix.screenmanager.FadeTransition
#:import Factory kivy.factory.Factory

<LoginScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//coffee_wall.jpg'
    FloatLayout:
        Label:
            id: title_label
            #text: "[b][color=#A6622B]Coffee Company[/color][/b]"
            text: "[b]Coffee Company[/b]"
            markup: True
            font_size: '28sp'
            size_hint: (.6, .1)
            pos_hint: {'x':.2, 'y':.85}
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
            size_hint: (.21, .06)
            pos_hint: {'x':.2, 'y':.4}
            text: 'Войти'
            background_color: (.94, .66, .39, 1)
            background_normal: ''
            background_down: ''
            canvas.before:
                Color:
                    rgba: .9, .8, .7, 1
                Line:
                    width: 1.5
                    rectangle: self.x, self.y, self.width, self.height
            on_press: 
                app.user=root.log_in(app.users, app.user)
            on_release:
                root.release()  
        Button:
            id: register_button
            size_hint: (.26, .06)
            pos_hint: {'x':.42, 'y':.4}
            text: 'Зарегистироваться'
            background_color: (.94, .66, .39, 1)
            background_normal: ''
            background_down: ''
            canvas.before:
                Color:
                    rgba: .9, .8, .7, 1
                Line:
                    width: 1.5
                    rectangle: self.x, self.y, self.width, self.height
            on_press: 
                root.register(app.users, app.user)
            on_release:
                root.release()
        Label:
            text:'[color=#231C0B]Имя пользователя[/color]'
            markup : True
            font_size : '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint:{'x':.2, 'y':.67} 
        TextInput:
            id: login_enter
            text: ''
            size_hint:(.48, .05)
            pos_hint:{'x':.2, 'y':.6}
            multiline:False  
        Label:
            text:'[color=#231C0B]Пароль[/color]'
            markup : True
            font_size : '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.2, 'y':.56}
        TextInput:
            id: passw_enter
            text: ''
            size_hint: (.48, .05)
            pos_hint: {'x':.2, 'y':.5}
            multiline: False
            password : True

<MainScreen>:
    on_enter:
        root.enter_screen(app.user)
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//coffee.jpg'
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
            pos_hint: {'x':.55, 'y':.6}
            text: 'Посмотреть отчёт'
            font_size : '20sp'
            size_hint: (.25, .1)
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: ''
            on_press:
                root.goto_report()
        Button:
            id: delete_button
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
        Label:
            id: username_label
            text: "[b]Пользователь: [/b]"
            markup: True
            font_size: '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.7, 'y':.9}
            color: (.25, .22, .19, 1)

<CustomDropdown@DropDown>:
    id: dropdown
    on_select:
        app.root.current_screen.ids.date.text = '{}'.format(args[1])
        self.dismiss()
    Button:
        id: btn1
        text: '01/01/20'
        size_hint_y: None
        height: '40dp'
        background_color: (.59, .59, .59, 1)
        background_normal: ''
        background_down: ''
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                width: 2
                rectangle: self.x, self.y, self.width, self.height
        on_release:
            dropdown.select(btn1.text)
    Button:
        id: btn2
        text: '01/02/20'
        size_hint_y: None
        height: '40dp'
        background_color: (.59, .59, .59, 1)
        background_normal: ''
        background_down: ''
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                width: 1.5
                rectangle: self.x, self.y, self.width, self.height
        on_release:
            dropdown.select(btn2.text)            
    Button:
        id: btn3
        text: '01/03/20'
        size_hint_y: None
        height: '40dp'
        background_color: (.59, .59, .59, 1)
        background_normal: ''
        background_down: ''
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                width: 1.5
                rectangle: self.x, self.y, self.width, self.height
        on_release:
            dropdown.select(btn3.text)
    Button:
        id: btn4
        text: '01/04/20'
        size_hint_y: None
        height: '40dp'
        background_color: (.59, .59, .59, 1)
        background_normal: ''
        background_down: ''
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                width: 1.5
                rectangle: self.x, self.y, self.width, self.height
        on_release:
            dropdown.select(btn4.text) 
    Button:
        id: btn5
        text: '01/05/20'
        size_hint_y: None
        height: '40dp'
        background_color: (.59, .59, .59, 1)
        background_normal: ''
        background_down: ''
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                width: 1.5
                rectangle: self.x, self.y, self.width, self.height
        on_release:
            dropdown.select(btn5.text) 
    Button:
        id: btn6
        text: '01/06/20'
        size_hint_y: None
        height: '40dp'
        background_color: (.59, .59, .59, 1)
        background_normal: ''
        background_down: ''
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                width: 1.5
                rectangle: self.x, self.y, self.width, self.height
        on_release:
            dropdown.select(btn6.text) 

<AddnoteScreen>:
    id: addnotescreen
    on_enter:
        root.enter_screen(app.user)
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//paper.jpg'
    FloatLayout:
        Label:
            id: title
            text: '[color=#A6622B]Для добавления записи необходимо ввести дату и объем проданного кофе[/color]'
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
            pos_hint: {'x':.3, 'y':.65}
        DataInput:
            id: date
            text: '01/01/20'
            size_hint:(.4, .05)
            pos_hint:{'x':.3, 'y':.6}
            multiline:False
        Button:
            id: btn
            text: 'V'
            size_hint:(.1, .06)
            pos_hint:{'x':.71, 'y':.595}
            background_color: (.69, .69, .69, 1)
            background_normal: ''
            background_down: ''
            on_press:
                root.dropdown_press()
            on_release:
                Factory.CustomDropdown().open(self)
                root.dropdown_release()

        Label:
            text: '[color=#A6622B]Объем:[/color]'
            markup : True
            font_size : '18sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.3, 'y':.55}  
        FloatInput:
            id: liters
            text: '0.0'
            size_hint:(.4, .05)
            pos_hint:{'x':.3, 'y':.5}
            multiline:False  
        Button:
            id: confirm_button
            size_hint: (.4, .1)
            pos_hint: {'x':.3, 'y':.3}
            text: 'Подтвердить'
            on_press: 
                root.confirm(app.user, app.info)
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: '' 
        Button:
            text: 'Назад'
            size_hint: (.1, .05)
            pos_hint: {'x':.8, 'y':.1} 
            on_press:
                app.info = root.exit(app.user, app.info)
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
            pos_hint: {'x':.7, 'y':.9}
            color: (.25, .22, .19, 1)
<ReportScreen>:
    on_enter:
        root.enter_screen(app.user)
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//paper.jpg'
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
                root.give_report(app.user, app.info)  
            on_release:
                root.release() 
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
                root.release()
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
            source: ''
            size_hint: (1, .48)
            pos_hint: {'x':0, 'y':.15} 
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
            pos_hint: {'x':.7, 'y':.9}
            color: (.25, .22, .19, 1)

<EditScreen>:
    on_enter:
        root.enter_screen(app.user, app.info)
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//paper.jpg'
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
            pos_hint: {'x':.7, 'y':.9}
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
                root.view(app.user, app.info)
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
                root.confirm_edit(app.user, app.info)
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
                root.delete(app.user, app.info)
            on_release:
                root.release()
        Image:
            id: plot
            source: ''
            size_hint: (1, .5)
            pos_hint: {'x':0, 'y':.12} 
            opacity: 0
        Label:
            id: info_label
            text: ''
            markup: True
            font_size: '16sp'
            size_hint: (.6, .1)
            pos_hint: {'x':.2, 'y':.01} 
        Button:
            text: 'Назад'
            size_hint: (.1, .05)
            pos_hint: {'x':.8, 'y':.05} 
            on_press:
                root.manager.current = 'main'

<DeleteScreen>:
    on_enter:
        root.enter_screen(app.user)
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//paper.jpg'
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
            size_hint: (.18, .05)
            pos_hint: {'x':.27, 'y':.5}  
            on_press:
                root.delete_info(app.user, app.users, app.info, acc=True)
            on_release:
                root.release()
        Button:
            id: delete_info
            text: 'Удалить всю информацию'
            background_color: (.69, .49, .33, 1)
            background_normal: ''
            background_down: '' 
            size_hint: (.27, .05)
            pos_hint: {'x':.48, 'y':.5}  
            on_press:
                root.delete_info(app.user, app.users, app.info)
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

def press_color(button):
    button.background_normal = ''
    button.background_color = (.69, .49, .33, 1)


def restore_color(button):
    button.background_normal = ''
    button.background_color = (.82, .6, .38, 1.0)


def plot(df, img, title=False):
    """
    Принимает df, обьект Image для размещения графика, title (bool)
    Строит график по столбцам date (x), liters (y)
    title - наличие названия графика.
    :return: None
    """
    plt.figure(figsize=(10, 5), tight_layout=True)
    ax = plt.subplot(111)
    sns.set(style="darkgrid")
    plt.plot(df['date'].values,
             df['liters'].values)
    x_ticks = df['date'].values
    x_labels = list(df['date'].values)
    if title:
        ax.set_title('Статистика за всё время')
    plt.xticks(x_ticks, rotation='90', labels=x_labels)
    plt.savefig('.data\\partplot.png', optimize=True, quality=100)
    img.reload()
    img.source = ".data\\partplot.png"
    img.opacity = 1


def sort_df(df):
    """
    Принимает df, сортирует по столбцу 'date'
    :return: df
    """
    df['date'] = df['date'].apply(lambda x: datetime.strptime(x, "%d/%m/%y"))
    df = df.sort_values(by=['date'])
    df['date'] = df['date'].apply(lambda x: x.strftime("%d/%m/%y"))
    df = df.reset_index()
    del df['index']
    df.index.name = 'index'
    df.to_csv('.data\\info.csv', sep=';')
    return df

class LoginScreen(Screen):

    def on_enter(self):
        """
        Очищение полей ввода.
        :return: None
        """
        self.ids.login_enter.text = ''
        self.ids.passw_enter.text = ''
        self.ids.info_label.text = ''

    def log_in(self, users, user):
        """
        Проверка логина и пароля на соответствии инф-и в бд.
        Возвращает имя пользователя
        :return: str
        """
        self.ids.enter_button.text = 'Проверка'
        restore_color(self.ids.enter_button)
        try:
            temp_passw = users[users.user == self.ids.login_enter.text]['pass'].tolist()[0]
            if temp_passw == self.ids.passw_enter.text:
                self.ids.enter_button.text = 'Войти'
                self.ids.enter_button.background_normal = ''
                self.ids.enter_button.background_color = (.94, .66, .39, 1)
                user = self.ids.login_enter.text
                self.manager.current = 'main'
                return user
            else:
                self.ids.info_label.text = '[color=#DD1B07]Неверный пароль[/color]'
        except KeyError:
            self.ids.info_label.text = '[color=#DD1B07]Неверный пароль[/color]'
        except IndexError:
            self.ids.info_label.text = '[color=#DD1B07]Пользователь не найден[/color]'

    def register(self, users, user):
        """
        Добавление пользователя в бд users.
        :return: None
        """
        self.ids.register_button.text = 'Проверка'
        restore_color(self.ids.register_button)
        try:
            users[users.user == self.ids.login_enter.text]['pass'].tolist()[0]
        except IndexError:

            if len(self.ids.login_enter.text) < 4 or len(self.ids.passw_enter.text) < 4:
                self.ids.info_label.text = '[color=#DD1B07]Имя пользователя и пароль должны состоять из 4 и более ' \
                                           'символов[/color] '
            else:
                self.last_index = users.count()[0]
                users.loc[self.last_index] = {'user': self.ids.login_enter.text, 'pass': self.ids.passw_enter.text}
                self.ids.info_label.text = '[color=#DD1B07]Вы зарегистрированы. Нажмите "Войти"[/color]'
                users.to_csv('.data\\users.csv', sep=';')
        else:
            self.ids.info_label.text = '[color=#DD1B07]Пользователь с таким именем уже зарегистрирован[/color]'

    def release(self):
        """
        Измененение цвета кнопок на стандартный
        :return: None
        """
        self.ids.enter_button.text = 'Войти'
        self.ids.enter_button.background_normal = ''
        self.ids.enter_button.background_color = (.94, .66, .39, 1)
        self.ids.register_button.text = 'Зарегистироваться'
        self.ids.register_button.background_normal = ''
        self.ids.register_button.background_color = (.94, .66, .39, 1)


class MainScreen(Screen):

    def enter_screen(self, user):
        """
        Добавление логина в верхний label.
        Изменение цвета кнопок на стандартный.
        :return: None
        """
        press_color(self.ids.addnote_button)
        press_color(self.ids.report_button)
        press_color(self.ids.editnote_button)
        press_color(self.ids.delete_button)
        self.ids.username_label.text = f"[b]Пользователь: {user}[/b]"

    def goto_addnote(self):
        restore_color(button=self.ids.addnote_button)
        self.manager.current = 'add'

    def goto_report(self):
        restore_color(button=self.ids.report_button)
        self.manager.current = 'report'

    def goto_edit(self):
        restore_color(button=self.ids.editnote_button)
        self.manager.current = 'edit'

    def goto_del(self):
        restore_color(button=self.ids.delete_button)
        self.manager.current = 'del'


class AddnoteScreen(Screen):

    def enter_screen(self, user):
        """
        Добавление логина в верхний label.
        :return: None
        """
        self.ids.username_label.text = f"[b]Пользователь: {user}[/b]"
        self.ids.info_label.text = ""
        self.ids.title.text = '[color=#A6622B]Для добавления записи необходимо ввести:\nдату и объем проданного кофе[/color]'

    def dropdown_press(self):
        self.ids.btn.background_color = (.49, .49, .49, 1)
        self.ids.btn.background_down =  ''
    def dropdown_release(self):
        self.ids.btn.background_color = (.69, .69, .69, 1)
        self.ids.btn.background_down = ''

    def confirm(self, user, info):
        """
        Добавление записи в бд.
        Если с такой датой запись существует - новое кол-во проданного кофе прибавляется к старому.
        :return: None
        """
        try:
            self.date = datetime.strptime(self.ids.date.text, "%d/%m/%y")
        except ValueError:
            self.ids.info_label.text = '[color=#DD1B07]Некорректно введена дата[/color]'
        else:
            self.ids.info_label.text = ''
            self.date = self.date.strftime("%d/%m/%y")
            if self.ids.liters.text == '' or self.ids.liters.text == '.':
                self.ids.info_label.text = '[color=#DD1B07]Введите объем[/color]'
            else:
                try:
                    self.index = info[(info['user'] == user) & (info['date'] == self.date)].index[0]
                except IndexError:
                    self.last_index = info.count()[0]
                    info.loc[self.last_index] = {'user': user, 'date': self.date, 'liters': float(self.ids.liters.text)}
                    info.to_csv('.data\\info.csv', sep=';')
                    self.ids.info_label.text = "[color=#3E3A37]Добавлена запись:  дата - {},  объем - {}[/color]".format(self.date, self.ids.liters.text)

                else:
                    self.liters = float(info.loc[self.index, 'liters'])
                    self.liters += float(self.ids.liters.text)
                    self.ids.info_label.text = '[color=#DD1B07]Запись с данной датой уже существует.\nНовый объем ' \
                                               'будет прибавлен к записанному ранее[/color][color=#3E3A37]' \
                                               '\nДата - {},  объем - {}[/color]'.format(self.date, self.liters)
                    info.loc[self.index, 'liters'] = self.liters
                    info.to_csv('.data\\info.csv', sep=';')

        finally:
            self.ids.date.text = '01/01/20'
            self.ids.liters.text = '0.0'

    def exit(self, user, info):
        self.manager.current = 'main'
        return sort_df(df=info)


class ReportScreen(Screen):

    def enter_screen(self, user):
        """
        Добавление логина в верхний label.
        Удаление графика
        :return: None
        """
        self.ids.username_label.text = f"[b]Пользователь: {user}[/b]"
        self.ids.report_text.text = "..."
        self.ids.plot.source = ""
        self.ids.plot.opacity = 0

    def give_report(self, user, info):
        """
        Вывод кол-ва проданного кофе за данный промежуток времени.
        Построение графика.
        :return: None
        """
        try:
            self.dt_s = datetime.strptime(self.ids.start_date.text, "%d/%m/%y")
            self.dt_e = datetime.strptime(self.ids.end_date.text, "%d/%m/%y")
        except ValueError:
            self.ids.report_text.text = "Некорректно введена дата"
            self.ids.report_text.color = (.87, .08, 0, 1)
        else:
            self.info_part = info.copy()
            self.info_part.date = self.info_part.date.apply(lambda x: datetime.strptime(x, "%d/%m/%y"))
            self.info_part = self.info_part[
                (self.info_part.user == user) & (self.info_part.date >= self.dt_s) & (self.info_part.date <= self.dt_e)]
            self.summ = self.info_part['liters'].sum()
            self.info_part.date = self.info_part.date.apply(lambda x: x.strftime("%d/%m/%y"))
            self.ids.report_text.text = f"С {self.ids.start_date.text} по {self.ids.end_date.text} было продано {round(self.summ, 4)} л кофе"
            self.ids.confirm_report.background_color = (.59, .39, .23, 1)
            plot(df=self.info_part, img=self.ids.plot)

    def clean(self):
        """
        Вставка шаблонов в поля ввода.
        :return: None
        """
        self.ids.start_date.text = '01/01/20'
        self.ids.end_date.text = '01/12/20'
        self.ids.report_text.text = "..."
        self.ids.clean_button.background_color = (.59, .39, .23, 1)
        self.ids.report_text.color = (.25, .22, .19, 1)
        self.ids.plot.source = ""
        self.ids.plot.opacity = 0

    def release(self):
        """
        Изменение цвета кнопок на стандартный.
        :return: None
        """
        press_color(self.ids.confirm_report)
        press_color(self.ids.clean_button)


class EditScreen(Screen):

    def enter_screen(self, user, info):
        """
        Добавление логина в верхний label.
        Изменение цвета кнопок на стандартный.
        Построение графика за все время.
        :return: None
        """
        self.ids.liters_info.text = '0.0'
        self.ids.date.text = '01/01/20'
        self.ids.liters.text = '0.0'
        self.ids.username_label.text = f"[b]Пользователь: {user}[/b]"
        self.ids.info_label.text = ""
        plot(df=info[info['user'] == user], img=self.ids.plot, title = True)

    def confirm_edit(self, user, info):
        """
        Изменение кол-ва проданного кофе в данный день.
        Обновление графика.
        :return: None
        """
        restore_color(self.ids.confirm_edit)
        if self.check_date(user, info):
            if self.ids.liters.text == '' or self.ids.liters.text == '.':
                self.ids.info_label.text = '[color=#DD1B07]Введите объем[/color]'
            else:
                info.loc[self.index, 'liters'] = float(self.ids.liters.text)
                self.ids.liters_info.text = self.ids.liters.text
                info.to_csv('.data\\info.csv', sep=';')
                self.ids.info_label.text = ''
                plot(df=info[info['user'] == user], img=self.ids.plot, title=True)

    def view(self, user, info):
        """
        Вывод информации о проданном кофе в данный день.
        :return: None
        """
        restore_color(self.ids.view)
        if self.check_date(user, info):
            self.ids.liters_info.text = str(info.loc[self.index, 'liters'])

    def delete(self, user, info):
        """
        Удаление записи из бд. Обновление графика.
        :return: None
        """
        restore_color(self.ids.delete)
        if self.check_date(user, info):
            self.ids.info_label.text = ''
            info.drop(self.index, inplace=True)
            info.index = range(0, info.count()[0])
            info.index.name = 'index'
            self.ids.liters_info.text = '0.0'
            info.to_csv('.data\\info.csv', sep=';')
            plot(df=info[info['user'] == user], img=self.ids.plot, title=False)

    def check_date(self, user, info):
        """
        Проверка введенной даты
        :return: bool
        """
        try:
            datetime.strptime(self.ids.date.text, "%d/%m/%y")
        except ValueError:
            self.ids.info_label.text = '[color=#DD1B07]Некорректно введена дата[/color]'
            return False
        else:
            self.ids.info_label.text = ''
            try:
                self.index = info[(info['user'] == user) & (info['date'] == self.ids.date.text)].index[0]
            except IndexError:
                self.ids.info_label.text = '[color=#DD1B07]Записи с такой датой нет[/color]'
                return False
            else:
                return True

    def release(self):
        """
        Изменение цвета кнопок на стандартный.
        :return: None
        """
        press_color(self.ids.confirm_edit)
        press_color(self.ids.view)
        press_color(self.ids.delete)


class DeleteScreen(Screen):
    def enter_screen(self, user):
        """
        Добавление логина в верхний label.
        Изменение цвета кнопок на стандартный.
        :return: None
        """
        self.ids.username_label.text = f"[b]Пользователь: {user}[/b]"
        press_color(self.ids.delete_info)
        press_color(self.ids.delete_acc)
        self.ids.info_label.text = ''
        self.ids.passw_enter.text = ''

    def delete_info(self,user, users, info, acc=False):
        """
        Введенный пароль сверяется с парлем в бд.
        Если совпадают - стирается вся информация об этом пользователе из info.
        :return: None
        """
        restore_color(self.ids.delete_info)
        temp_passw = users[users.user == user]['pass'].tolist()[0]
        self.index = users[users.user == user].index[0]
        if temp_passw == self.ids.passw_enter.text:
            for i in info[info['user'] == user].index:
                info.drop(i, inplace=True)
            info.index = range(0, info.count()[0])
            info.index.name = 'index'
            info.to_csv('.data\\info.csv', sep=';')
            if acc:
                users.drop(self.index, inplace=True)
                users.to_csv('.data\\users.csv', sep=';')
                self.manager.current = 'login'
            self.ids.info_label.text = '[color=#DD1B07]Информация удалена[/color]'
        else:
            self.ids.info_label.text = '[color=#DD1B07]Неверный пароль[/color]'

    def release(self):
        """
        Изменяет внешний вид кнопок
        :return: None
        """
        press_color(self.ids.delete_info)
        press_color(self.ids.delete_acc)


class FloatInput(TextInput):
    """
    Поле ввода с ограничением на ввод символов - только цифры и точка.
    Для дальнейшего преобразования в float.
    """
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)


class DataInput(TextInput):
    """
    Поле ввода с ограничением на ввод символов - только цифры и слеш.
    Для дальнейшего преобразования в datetime.
    """
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
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
        self.title = 'Coffee Company'
        self.icon = '.data\\myicon.png'
        Window.clearcolor = (.94, .82, .75, 1)
        Window.size = (1024, 576)
        self.user = ''
        self.users = pd.read_csv('.data\\users.csv', sep=';', index_col=[0])
        self.info = pd.read_csv('.data\\info.csv', sep=';', index_col=[0])
        return sm


if __name__ == "__main__":
    CoffeeApp().run()

