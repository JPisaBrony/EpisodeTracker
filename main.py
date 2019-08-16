from kivy.app import App
from kivy.app import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')

size = Window.size
SPACE_WIDTH = size[0] / 3
ELEMENT_HEIGHT = size[1] / 5
FONT_SIZE = size[1] / (5 * 4)

class EpisodeRow(BoxLayout):
    SPACE_WIDTH = SPACE_WIDTH
    ELEMENT_HEIGHT = ELEMENT_HEIGHT
    FONT_SIZE = FONT_SIZE

    def minus_ep(self):
        ep_num = int(self.ids.episodenum.text)
        ep_num -= 1
        if ep_num > 0:
            self.ids.episodenum.text = str(ep_num)

    def plus_ep(self):
        ep_num = int(self.ids.episodenum.text)
        ep_num += 1
        self.ids.episodenum.text = str(ep_num)

class EpisodeTrackerScreen(Screen):
    SPACE_WIDTH = SPACE_WIDTH
    ELEMENT_HEIGHT = ELEMENT_HEIGHT
    FONT_SIZE = FONT_SIZE
    
    def add_ep(self):
        show = EpisodeRow()
        text = self.ids.addshow.text
        if text != "":
            print show.ids.show.text
            print text
            show.ids.show.text = text
            self.ids.tvshow.add_widget(show)
            self.ids.addshow.text = ""

class MainScreenManager(ScreenManager):
    pass

root = Builder.load_string('''
MainScreenManager:
    EpisodeTrackerScreen

<EpisodeRow>:
    name: 'episoderow'
    size_hint_y: None
    height: root.ELEMENT_HEIGHT
    Label:
        id: show
        font_size: root.FONT_SIZE
    BoxLayout:
        size_hint_x: None
        width: root.SPACE_WIDTH
        Button:
            text: '-'
            font_size: root.FONT_SIZE
            on_press: root.minus_ep()
        Label:
            id: episodenum
            font_size: root.FONT_SIZE
            text: '1'
        Button:
            text: '+'
            font_size: root.FONT_SIZE
            on_press: root.plus_ep()

<EpisodeTrackerScreen>:
    name: 'episodetracker'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: root.ELEMENT_HEIGHT
            Label:
                text: 'Show Name'
                font_size: root.FONT_SIZE
            Label:
                size_hint_x: None
                width: root.SPACE_WIDTH
                font_size: root.FONT_SIZE
                text: 'Episode'
        ScrollView:
            GridLayout:
                id: tvshow
                orientation: 'vertical'
                cols: 1
        BoxLayout:
            size_hint_y: None
            height: root.ELEMENT_HEIGHT
            TextInput:
                id: addshow
                font_size: root.FONT_SIZE
            Button:
                size_hint_x: None
                width: root.SPACE_WIDTH
                text: 'Add'
                font_size: root.FONT_SIZE
                on_press: root.add_ep()
''')

class EpisodeTracker(App):
    def build(self):
        return root

if __name__ == '__main__':
    EpisodeTracker().run()
