from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


def image_widget(path):
    return Button(text=path)


class PathInput(GridLayout):
    def __init__(self, **kwargs):
        super(PathInput, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Path:'))
        self.path = TextInput(multiline=False)
        self.add_widget(self.path)


class MainImage(GridLayout):
    def __init__(self):
        super(MainImage, self).__init__()
        self.cols = 1
        self.add_widget(image_widget('Main image'))


class TopSection(GridLayout):
    def __init__(self):
        super(TopSection, self).__init__()
        self.cols = 2
        self.add_widget(PathInput())
        self.add_widget(MainImage())


class Images(GridLayout):
    def __init__(self):
        super(Images, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='All images'))
        self.add_widget(Label(text='Similar images'))
        self.add_widget(ImagesList())
        self.add_widget(ImagesList())


class ImagesList(GridLayout):
    def __init__(self):
        super(ImagesList, self).__init__()
        self.cols = 6
        for i in range(20):
            self.add_widget(image_widget('Image {}'.format(i)))


class AllImagesLayout(GridLayout):
    def __init__(self, **kwargs):
        super(AllImagesLayout, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(TopSection())
        self.add_widget(Images())


class TestApp(App):
    def build(self):
        return AllImagesLayout()


if __name__ == '__main__':
    TestApp().run()
