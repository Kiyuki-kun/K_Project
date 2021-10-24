from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from gtts import gTTS
from  kivy.uix.textinput import TextInput
from kivy.core.audio import SoundLoader


class FirstScr(Screen):
	def __init__(self, name):
		super().__init__() # здесь надо передавать имя. Что будет, если не передать?
		vl = BoxLayout(orientation='vertical')
		self.txtInput = TextInput(text='Озвучь меня!')
		vl.add_widget(self.txtInput)
		btnVoice = Button(text='Озвучить')
		btnVoice.on_press = self.Play
		vl.add_widget(btnVoice)
		self.add_widget(vl)

	def Play(self):
		tts = gTTS(text=self.txtInput.text, lang='ru')
		tts.save("current.mp3")
		playsound.playsound('current.mp3')



class MyApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(FirstScr(name='first'))

		return sm

app = MyApp()
app.run()