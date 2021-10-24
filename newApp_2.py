from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
#from gtts import gTTS
from  kivy.uix.textinput import TextInput
import pyttsx3 

class EN_RU_Choose(Screen):
	def __init__(self,name='en_ru'):
		super().__init__(name=name)
		vl = BoxLayout(orientation='vertical')
		self.btnRU = Button(text="Русский")
		self.btnRU.on_press = self.Pick_Ru
		vl.add_widget(self.btnRU)
		self.btnEn = Button(text="English")
		self.btnEn.on_press = self.Pick_En
		vl.add_widget(self.btnEn)

		self.add_widget(vl)

	def Pick_Ru(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'choose'

	def Pick_En(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'choose_en'

class ChooseScr(Screen):
	def __init__(self, name='choose'):
		super().__init__(name=name) # здесь надо передавать имя. Что будет, если не передать?
		self.engine = pyttsx3.init()
		ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
		self.engine.setProperty('voice', ru_voice_id) 
		vl = BoxLayout(orientation='vertical')

		self.txtInput = TextInput(text='Озвучь меня!')
		self.btnVoice = Button(text="Озвучить(to voice)")
		self.btnVoice.on_press = self.Play
		
		btnCategory = Button(text="Категорий(Categories)")
		btnCategory.on_press = self.categories

		btnLangs = Button(text="Back to language/Назад к языкам")
		btnLangs.on_press = self.Langs
		
		vl.add_widget(self.txtInput)
		vl.add_widget(self.btnVoice)
		vl.add_widget(btnCategory)
		vl.add_widget(btnLangs)
		self.add_widget(vl)

	def categories(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'first'

	def Play(self):
		self.engine.say(self.txtInput.text)
		self.engine.runAndWait()

	def Langs(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'en_ru'

class FirstScr(Screen):
	def __init__(self, name='first'):
		super().__init__(name=name) # здесь надо передавать имя. Что будет, если не передать?
		self.engine = pyttsx3.init()
		ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
		self.engine.setProperty('voice', ru_voice_id) 
		vl = BoxLayout(orientation='vertical')
		
		#Кнопка для категории "Дом"
		self.btnHome = Button(text="Дом(House)")
		self.btnHome.on_press = self.toHome
		self.btnStreet = Button(text="Улица(Street)")
		self.btnStreet.on_press = self.next
		self.btnTransport = Button(text="Транспорт(Transport)")
		self.btnTransport.on_press = self.transport
		self.btnMusic = Button(text="Музыка(Music)")
		self.btnMusic.on_press = self.music
		self.btnMain = Button(text="Главное меню(Main menu)")
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
		btnEat = Button(text="Хочу есть(I'm hungry)")
		vl.add_widget(btnEat)
		btnEat.on_press = lambda : self.Play("Хочу есть")
		#Нужно в туалет
		btnToilet = Button(text="Нужно в туалет(I need to go to the toilet)")
		vl.add_widget(btnToilet)
		btnToilet.on_press = lambda : self.Play("Нужно в туалет")
		#Пойдем гулять
		btnWalk = Button(text="Пойдем гулять(Let's go for a walk)")
		vl.add_widget(btnWalk)
		btnWalk.on_press = lambda : self.Play("Пойдем гулять")
		#Кнопка "Улица"
		#Кнопка "Назад"'''
		btnBack = Button(text="К категориям(Categories)")
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

		btnLift = Button(text="Вызовите лифт(Call a elevator)")
		btnLift.on_press = lambda : self.Play("Вызовите лифт")
		vl.add_widget(btnLift)

		btnPark = Button(text="Пойдем в парк(Let's go to the park)")
		btnPark.on_press = lambda : self.Play("Пойдем в парк")
		vl.add_widget(btnPark)

		btnRoad = Button(text="Помогите перейти дорогу(Help cross the road)")
		btnRoad.on_press = lambda : self.Play("Помогите перейти дорогу")
		vl.add_widget(btnRoad)

		btnMain = Button(text="К категориям(Categories)")
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

		btnTaxi = Button(text="Вызовите такси(Call taxi)")
		btnTaxi.on_press = lambda : self.Play("Вызовите такси")
		vl.add_widget(btnTaxi)

		btnBus = Button(text="Остановите автобус(Stop the bus)")
		btnBus.on_press = lambda : self.Play("Остановите автобус")
		vl.add_widget(btnBus)

		btnTrain = Button(text="Когда приедет поезд?(When is the train coming?) ")
		btnTrain.on_press = lambda : self.Play("Когда приедет поезд?")
		vl.add_widget(btnTrain)

		btnMain = Button(text="К категориям(Categories)")
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

		btnVolumeUp = Button(text="Увеличьте громкость(Turn up the volume,please)")
		btnVolumeUp.on_press = lambda : self.Play("Увеличьте громкость")

		btnVolumeDown = Button(text="Уменьшите громкость(Decrease volume,please)")
		btnVolumeDown.on_press = lambda : self.Play("Уменьшите громкость")

		btnNextSong = Button(text="Переключите песню,пожалуйста(Change the song ,please)")
		btnNextSong.on_press = lambda : self.Play("Переключите песню,пожалуйста")

		btnMain = Button(text="К категориям(Categories)")
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
#_______________________________________________________________

#_______________________________________________________________


class ChooseScr_en(Screen):
	def __init__(self, name='choose_en'):
		super().__init__(name=name) # здесь надо передавать имя. Что будет, если не передать?
		self.engine = pyttsx3.init()
		en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
		self.engine.setProperty('voice', en_voice_id) 
		vl = BoxLayout(orientation='vertical')

		self.txtInput = TextInput(text='Voice me!')
		self.btnVoice = Button(text="To voice(Озвучь меня)")
		self.btnVoice.on_press = self.Play
		
		btnCategory = Button(text="Categories(Категорий)")
		btnCategory.on_press = self.categories_en
		
		btnLangs = Button(text="Back to language/Назад к языкам")
		btnLangs.on_press = self.Langs

		vl.add_widget(self.txtInput)
		vl.add_widget(self.btnVoice)
		vl.add_widget(btnCategory)
		vl.add_widget(btnLangs)
		self.add_widget(vl)

	def categories_en(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'first_en'

	def Play(self):
		self.engine.say(self.txtInput.text)
		self.engine.runAndWait()

	def Langs(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'en_ru'

class FirstScr_en(Screen):
	def __init__(self, name='first_en'):
		super().__init__(name=name) # здесь надо передавать имя. Что будет, если не передать?
		self.engine = pyttsx3.init()
		en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
		self.engine.setProperty('voice', en_voice_id) 
		vl = BoxLayout(orientation='vertical')
		
		#Кнопка для категории "Дом"
		self.btnHome = Button(text="Home(Дом)")
		self.btnHome.on_press = self.toHome_en
		self.btnStreet = Button(text="Street(Улица)")
		self.btnStreet.on_press = self.next_en
		self.btnTransport = Button(text="Transport(Транспорт)")
		self.btnTransport.on_press = self.transport_en
		self.btnMusic = Button(text="Music(Музыка)")
		self.btnMusic.on_press = self.music_en
		self.btnMain = Button(text="Main menu(Главное меню)")
		self.btnMain.on_press = self.back_en
		vl.add_widget(self.btnHome)
		vl.add_widget(self.btnStreet)
		vl.add_widget(self.btnTransport)
		vl.add_widget(self.btnMusic)
		vl.add_widget(self.btnMain)
		self.add_widget(vl)

	def back_en(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'choose_en'

	def next_en(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'third_en'

	def toHome_en(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'second_en'

	def transport_en(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'fourth_en'

	def music_en(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'fifth_en'

class SecondScr_en(Screen):
	def __init__(self, name='second_en'):
		super().__init__(name=name)
		self.engine = pyttsx3.init()
		en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
		self.engine.setProperty('voice', en_voice_id) 
		vl = BoxLayout(orientation='vertical')
		#Создайте кнопки для озвучки
		#Хочу есть
		btnEat = Button(text="I am hungry(Я хочу есть)")
		vl.add_widget(btnEat)
		btnEat.on_press = lambda : self.Play("I am hungry")
		#Нужно в туалет
		btnToilet = Button(text="I need to go to the toilet(Мне нужно в туалет)")
		vl.add_widget(btnToilet)
		btnToilet.on_press = lambda : self.Play("I need to go to the toilet")
		#Пойдем гулять
		btnWalk = Button(text="Let's go for a walk(Пойдем погуляем) ")
		vl.add_widget(btnWalk)
		btnWalk.on_press = lambda : self.Play("	Let's go for a walk")
		#Кнопка "Улица"
		#Кнопка "Назад"'''
		btnBack = Button(text="Categories(Категорий)")
		btnBack.on_press = self.back_en
		vl.add_widget(btnBack)
		self.add_widget(vl)
		
	def back_en(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'first_en'

	def Play(self,txt):
		self.engine.say(txt)
		self.engine.runAndWait()

class ThirdScr_en(Screen):
	def __init__(self, name='third_en'):
		super().__init__(name=name)
		self.engine = pyttsx3.init()
		en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
		self.engine.setProperty('voice', en_voice_id) 
		vl = BoxLayout(orientation='vertical')

		btnLift = Button(text="Call the elevator(вызовите лифт)")
		btnLift.on_press = lambda : self.Play("Call the elevator")
		vl.add_widget(btnLift)

		btnPark = Button(text="Let's go to the park(Пошли в парк)")
		btnPark.on_press = lambda : self.Play("Let's go to the park")
		vl.add_widget(btnPark)

		btnRoad = Button(text="Help cross the road(Помогите перейти дорогу)")
		btnRoad.on_press = lambda : self.Play("Help cross the road ,please")
		vl.add_widget(btnRoad)

		btnMain = Button(text="Categories(Категорий)")
		btnMain.on_press = self.main_en
		vl.add_widget(btnMain)
		self.add_widget(vl)	

	def main_en(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'first_en'

	def Play(self,txt):
		self.engine.say(txt)
		self.engine.runAndWait()

class FourthScr_en(Screen):
	def __init__(self, name='fourth_en'):
		super().__init__(name=name)
		self.engine = pyttsx3.init()
		en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
		self.engine.setProperty('voice', en_voice_id) 
		vl = BoxLayout(orientation='vertical')

		btnTaxi = Button(text="Call taxi(Вызовите такси)")
		btnTaxi.on_press = lambda : self.Play("Call taxi")
		vl.add_widget(btnTaxi)

		btnBus = Button(text="Stop the bus ,please(Остановите автобус,пожалуйста)")
		btnBus.on_press = lambda : self.Play("Stop the bus ,please")
		vl.add_widget(btnBus)

		btnTrain = Button(text="When is the train coming?(Когда приедет поезд?)")
		btnTrain.on_press = lambda : self.Play("When is the train coming?")
		vl.add_widget(btnTrain)

		btnMain = Button(text="Categories(Категорий)")
		btnMain.on_press = self.main_en
		vl.add_widget(btnMain)
		self.add_widget(vl)

	def main_en(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'first_en'

	def Play(self,txt):
		self.engine.say(txt)
		self.engine.runAndWait()

class FifthScr_en(Screen):
	def __init__(self, name='fifth_en'):
		super().__init__(name=name)
		self.engine = pyttsx3.init()
		en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
		self.engine.setProperty('voice', en_voice_id) 
		vl = BoxLayout(orientation='vertical')

		btnVolumeUp = Button(text="Turn up the volume(Увеличьте громкость)")
		btnVolumeUp.on_press = lambda : self.Play("Turn up the volume ,please")

		btnVolumeDown = Button(text="Decrease the volume(Уменьшите громкость)")
		btnVolumeDown.on_press = lambda : self.Play("Decrease the volume ,please")

		btnNextSong = Button(text="Change the song ,please(Переключите песню,пожалуйста)")
		btnNextSong.on_press = lambda : self.Play("Change the song ,please")

		btnMain = Button(text="Categories(Категорий)")
		btnMain.on_press = self.main_en
		vl.add_widget(btnVolumeUp)
		vl.add_widget(btnVolumeDown)
		vl.add_widget(btnNextSong)
		vl.add_widget(btnMain)
		self.add_widget(vl)

	def main_en(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'first_en'

	def Play(self,txt):
		self.engine.say(txt)
		self.engine.runAndWait()

class MyApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(EN_RU_Choose(name='en_ru'))
		sm.add_widget(ChooseScr(name='choose'))
		sm.add_widget(FirstScr(name='first'))
		sm.add_widget(SecondScr(name='second'))
		sm.add_widget(ThirdScr(name='third'))
		sm.add_widget(FourthScr(name='fourth'))
		sm.add_widget(FifthScr(name='fifth'))
		sm.add_widget(ChooseScr_en(name='choose_en'))
		sm.add_widget(FirstScr_en(name='first_en'))
		sm.add_widget(SecondScr_en(name='second_en'))
		sm.add_widget(ThirdScr_en(name='third_en'))
		sm.add_widget(FourthScr_en(name='fourth_en'))
		sm.add_widget(FifthScr_en(name='fifth_en'))

		return sm

app = MyApp()
app.run()