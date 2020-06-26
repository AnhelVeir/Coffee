from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.textinput import TextInput



class BoxApp(App):
    
    def build (self):
        self.title = 'Coffee Company'
        self.icon = 'myicon.png'
        Window.clearcolor = (1, 1, 1, 1)
        FL = FloatLayout()
        title_label = Label(text='[color=#A6622B]Coffee Company[/color]', markup = True,
                  font_size = '20sp',
                  size_hint=(.6, .1), 
                  pos_hint={'x':.2, 'y':.8})
        FL.add_widget(title_label)

        # Нужно придумать куда это все сохранять
        self.login = ''
        self.passw = ''


        login_label = Label(text='[color=#231C0B]Login[/color]', markup = True,
                  font_size = '20sp',
                  size_hint=(.5, .1),
                  halign='left',
                  pos_hint={'x':0, 'y':.65})
        FL.add_widget(login_label)
        self.input_login = TextInput(text='',
                              size_hint=(.6, .05),
                              pos_hint={'x':.2, 'y':.6},
                              multiline=False)
        FL.add_widget(self.input_login)

        passw_label = Label(text='[color=#231C0B]Password[/color]', markup = True,
                  font_size = '20sp',
                  size_hint=(.55, .1),
                  halign='left',
                  pos_hint={'x':0, 'y':.5})
        FL.add_widget(passw_label)
        self.input_passw = TextInput(text='',
                              size_hint=(.6, .05),
                              pos_hint={'x':.2, 'y':.45},
                              multiline=False,
                              password = True)
        FL.add_widget(self.input_passw)



        button = Button(text='Press me',
                        size_hint=(.6, .1),
                        pos_hint={'x':.2, 'y':.3},
                        background_color = (1, .73, .52, 1),
                        background_normal='',
                        background_down='',
                        on_press = self.btn_press,
                        on_release = self.btn_release)
        FL.add_widget(button)

        return FL
    
    #def on_enter(instance, value):
     #   print('User pressed enter in', instance)
     #   print(value.text)
     #   instance.login_label.text = '[color=#231C0B]'+value.text+'[/color]'
        


    def btn_press(self, instance):
        instance.text = ('I was pressed')
        background_normal=''
        instance.background_color = (.6, .24, .2, 1.0)
        self.login = self.input_login.text
        self.passw = self.input_passw.text
        print(f'Login = {self.login}\nPassword = {self.passw}')



    def btn_release(self, instance):
        instance.text = ('Press me')
        background_normal=''
        instance.background_color = (1, .73, .52, 1)
   

if __name__ == "__main__":
    BoxApp().run()