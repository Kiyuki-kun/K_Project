from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
#from gtts import gTTS
from  kivy.uix.textinput import TextInput
import pyttsx3 

class ChooseScr(Screen):
	def __init__(self, name='choose'):
		super().__init__(name=name) # здесь надо передавать имя. Что будет, если не передать?
		self.engine = pyttsx3.init()
		ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
		self.engine.setProperty('voice', ru_voice_id) 
		vl = BoxLayout(orientation='vertical')

		self.txtInput = TextInput(text='Озвучь меня!')
		self.btnVoice = Button(text="Озвучить")
		self.btnVoice.on_press = self.Play
		
		btnCategory = Button(text="Категорий")
		btnCategory.on_press = self.categories
		
		vl.add_widget(self.txtInput)
		vl.add_widget(self.btnVoice)
		vl.add_widget(btnCategory)
		self.add_widget(vl)

	def categories(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'first'

	def Play(self):
		self.engine.say(self.txtInput.text)
		self.engine.runAndWait()

class FirstScr(Screen):
	def __init__(self, name='first'):
		super().__init__(name=name) # здесь надо передавать имя. Что будет, если не передать?
		self.engine = pyttsx3.init()
		ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
		self.engine.setProperty('voice', ru_voice_id) 
		vl = BoxLayout(orientation='vertical')
		
		#Кнопка для категории "Дом"
		self.btnHome = Button(text="Дом")
		self.btnHome.on_press = self.toHome
		self.btnStreet = Button(text="Улица")
		self.btnStreet.on_press = self.next
		self.btnTransport = Button(text="Транспорт")
		self.btnTransport.on_press = self.transport
		self.btnMusic = Button(text="Музыка")
		self.btnMusic.on_press = self.music
		self.btnMain = Button(text="Главное меню")
		self.btnMain.on_press = self.back
		vl.add_widget(self.btnHome)
		vl.add_widget(self.btnStreet)
		vl.add_widget(self.btnTransport)
		vl.add_widget(self.btnMusic)
		vl.add_widget(self.btnMain)
		self.add_widget(vl)

	def back(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'choose'

	def next(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'third'

	def toHome(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'second'

	def transport(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'fourth'

	def music(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'fifth'

class SecondScr(Screen):
	def __init__(self, name='second'):
		super().__init__(name=name)
		self.engine = pyttsx3.init()
		ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
		self.engine.setProperty('voice', ru_voice_id) 
		vl = BoxLayout(orientation='vertical')
		#Создайте кнопки для озвучки
		#Хочу есть
		btnEat = Button(text="Хочу есть")
		vl.add_widget(btnEat)
		btnEat.on_press = lambda : self.Play("Хочу есть")
		#Нужно в туалет
		btnToilet = Button(text="Нужно в туалет")
		vl.add_widget(btnToilet)
		btnToilet.on_press = lambda : self.Play("Нужно в туалет")
		#Пойдем гулять
		btnWalk = Button(text="Пойдем гулять")
		vl.add_widget(btnWalk)
		btnWalk.on_press = lambda : self.Play("Пойдем гулять")
		#Кнопка "Улица"
		#Кнопка "Назад"'''
		btnBack = Button(text="К категориям")
		btnBack.on_press = self.back
		vl.add_widget(btnBack)
		self.add_widget(vl)
		
	def back(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'first'

	def Play(self,txt):
		self.engine.say(txt)
		self.engine.runAndWait()

class ThirdScr(Screen):
	def __init__(self, name='third'):
		super().__init__(name=name)
		self.engine = pyttsx3.init()
		ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
		self.engine.setProperty('voice', ru_voice_id) 
		vl = BoxLayout(orientation='vertical')

		btnLift = Button(text="Вызовите лифт")
		btnLift.on_press = lambda : self.Play("Вызовите лифт")
		vl.add_widget(btnLift)

		btnPark = Button(text="Пойдем в парк")
		btnPark.on_press = lambda : self.Play("Пойдем в парк")
		vl.add_widget(btnPark)

		btnRoad = Button(text="Помогите перейти дорогу")
		btnRoad.on_press = lambda : self.Play("Помогите перейти дорогу")
		vl.add_widget(btnRoad)

		btnMain = Button(text="К категориям")
		btnMain.on_press = self.main
		vl.add_widget(btnMain)
		self.add_widget(vl)	

	def main(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'first'

	def Play(self,txt):
		self.engine.say(txt)
		self.engine.runAndWait()

class FourthScr(Screen):
	def __init__(self, name='fourth'):
		super().__init__(name=name)
		self.engine = pyttsx3.init()
		ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
		self.engine.setProperty('voice', ru_voice_id) 
		vl = BoxLayout(orientation='vertical')

		btnTaxi = Button(text="Вызовите такси")
		btnTaxi.on_press = lambda : self.Play("Вызовите такси")
		vl.add_widget(btnTaxi)

		btnBus = Button(text="Остановите автобус")
		btnBus.on_press = lambda : self.Play("Остановите автобус")
		vl.add_widget(btnBus)

		btnTrain = Button(text="Когда приедет поезд?")
		btnTrain.on_press = lambda : self.Play("Когда приедет поезд?")
		vl.add_widget(btnTrain)

		btnMain = Button(text="К категориям")
		btnMain.on_press = self.main
		vl.add_widget(btnMain)
		self.add_widget(vl)

	def main(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'first'

	def Play(self,txt):
		self.engine.say(txt)
		self.engine.runAndWait()

class FifthScr(Screen):
	def __init__(self, name='fifth'):
		super().__init__(name=name)
		self.engine = pyttsx3.init()
		ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
		self.engine.setProperty('voice', ru_voice_id) 
		vl = BoxLayout(orientation='vertical')

		btnVolumeUp = Button(text="Увеличьте громкость")
		btnVolumeUp.on_press = lambda : self.Play("Увеличьте громкость")

		btnVolumeDown = Button(text="Уменьшите громкость")
		btnVolumeDown.on_press = lambda : self.Play("Уменьшите громкость")

		btnNextSong = Button(text="Переключите песню,пожалуйста")
		btnNextSong.on_press = lambda : self.Play("Переключите песню,пожалуйста")

		btnMain = Button(text="К категориям")
		btnMain.on_press = self.main
		vl.add_widget(btnVolumeUp)
		vl.add_widget(btnVolumeDown)
		vl.add_widget(btnNextSong)
		vl.add_widget(btnMain)
		self.add_widget(vl)

	def main(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'first'

	def Play(self,txt):
		self.engine.say(txt)
		self.engine.runAndWait()

class MyApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(ChooseScr(name='choose'))
		sm.add_widget(FirstScr(name='first'))
		sm.add_widget(SecondScr(name='second'))
		sm.add_widget(ThirdScr(name='third'))
		sm.add_widget(FourthScr(name='fourth'))
		sm.add_widget(FifthScr(name='fifth'))

		return sm

app = MyApp()
app.run()