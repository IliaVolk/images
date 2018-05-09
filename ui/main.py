from ui.report_generator import generate_report

from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.filebrowser import FileBrowser
from kivy.uix.popup import Popup
from fs import open_fs
import fs
from fs.walk import Walker
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
import os.path
from kivy.core.window import Window
import json
'''
images = ['/home/ilya/PycharmProjects/images/static/lena_square.jpg',
          '/home/ilya/PycharmProjects/images/static/head.png',
          '/home/ilya/PycharmProjects/images/static/lena_translate10_2.jpg',
          '/home/ilya/PycharmProjects/images/static/lena_harshness.jpg',
          '/home/ilya/PycharmProjects/images/static/lena_rotate180.jpg',
          '/home/ilya/PycharmProjects/images/static/index.html', '/home/ilya/PycharmProjects/images/static/text2.jpg',
          '/home/ilya/PycharmProjects/images/static/text1.jpg',
          '/home/ilya/PycharmProjects/images/static/lena_rotate90.jpg',
          '/home/ilya/PycharmProjects/images/static/baboon.png', '/home/ilya/PycharmProjects/images/static/cor.jpg',
          '/home/ilya/PycharmProjects/images/static/lena_rotate2.jpg',
          '/home/ilya/PycharmProjects/images/static/result.js',
          '/home/ilya/PycharmProjects/images/static/baboon_rotate180.jpg',
          '/home/ilya/PycharmProjects/images/static/lena.jpg', '/home/ilya/PycharmProjects/images/static/lena_blur.jpg',
          '/home/ilya/PycharmProjects/images/static/lena_rotate10.jpg',
          '/home/ilya/PycharmProjects/images/static/baboon.jpg',
          '/home/ilya/PycharmProjects/images/static/baboon_harshness.jpg',
          '/home/ilya/PycharmProjects/images/static/index.js',
          '/home/ilya/PycharmProjects/images/static/lena_rotate10_noblack.jpg',
          '/home/ilya/PycharmProjects/images/static/lena_scale.jpg',
          '/home/ilya/PycharmProjects/images/static/baboon_scale.jpg',
          '/home/ilya/PycharmProjects/images/static/lena_small_transition.jpg',
          '/home/ilya/PycharmProjects/images/static/lena_translate10.jpg',
          '/home/ilya/PycharmProjects/images/static/baboon_square.jpg',
          '/home/ilya/PycharmProjects/images/static/lena_move90.jpg']'''
REPORT_FILENAME = 'reports.json'


def file_chosen(selected, filters, popup, cb):
    result = []
    State.imported_path.text = selected
    if os.path.isdir(selected):
        for file in Walker(filter=filters).files(open_fs(selected)):
            if 'sign' not in file:
                result.append(selected + file)
        print('file chosen', result)
        cb(result, selected)
    else:
        cb(selected, selected)
    popup.dismiss()


def choose_file(filters, cb, dirselect=True):
    browser = FileBrowser(
        select_string='Select',
        filters=filters,
        path='/home/illia/images',
        dirselect=dirselect)
    browser.bind(
        on_success=lambda instance: file_chosen(
            instance.selection[0],
            filters,
            popup,
            cb,
        ),
        on_canceled=lambda _: popup.dismiss(),
    )
    popup = Popup(
        title='Choose directory',
        content=browser
    )
    popup.open()


def save_json_file(files, dirpath):
    report = generate_report(files, False)
    with open(os.path.join(dirpath, REPORT_FILENAME), 'w') as f:
        json.dump(report, f)
    return report


class State:
    pass

def set_main_image(image):
    if isinstance(image['diffs'], list):
        State.main_image.set_image(image)
        State.similar_images.set_images(image['diffs'])


class ImageButtonWithLabel(BoxLayout):
    def __init__(self, source):
        super(ImageButtonWithLabel, self).__init__(
            size_hint=(None, None),
            orientation='vertical',
        )
        self.height = 200
        self.width = 200

        def pressed(button):
            set_main_image(source)

        image = ImageButton(pressed, source=source['image'])

        self.add_widget(image)
        self.add_widget(Button(text=source['text'], size_hint_y=0.01, background_color=(0, 0, 0, 1)))


class ImageButton(ButtonBehavior, Image):
    def __init__(self, pressed=None, **kw):
        super(ImageButton, self).__init__(**kw)
        self.pressed = pressed

    def on_press(self):
        if self.pressed is not None:
            self.pressed(self)


class PathInput(BoxLayout):
    def __init__(self):
        super(PathInput, self).__init__()
        self.size_hint_y = None
        height = 40
        self.size = (self.width, height)
        self.add_widget(Label(text='Path:', size_hint=(.2, None), size=(self.width, height)))
        self.add_widget(State.imported_path)
        self.button = Button(text='Import',
                             size_hint=(.3, None),
                             size=(self.width, height))
        def on_save(file, dirpath):
            filename = file
            with open(filename) as f:
                report = json.load(f)
            State.all_images.set_images(report)
            
        self.button.bind(on_press=lambda _: choose_file(
            ['*.json'],
            on_save,  # State.all_images.set_images(result),
        ))
        self.add_widget(self.button)


class MainImage(BoxLayout):
    def __init__(self):
        super(MainImage, self).__init__()
        self.orientation = 'vertical'
        self.image_button = ImageButton()
        self.add_widget(self.image_button)
        self.button = Button(text='', size_hint_y=0.01, background_color=(0, 0, 0, 1))
        self.add_widget(self.button)
    def set_image(self, image):
        self.button.text = image['text']
        self.image_button.source = image['image']


class ImagesColumn(BoxLayout):
    def init(self, text):
        self.add_widget(Label(text=text, size=(self.width, 30), size_hint=(None, None)))
        scroll_view = ScrollView()
        scroll_view.add_widget(self.images_list)
        self.add_widget(scroll_view)

    def __init__(self):
        super(ImagesColumn, self).__init__()
        self.orientation = 'vertical'
        self.images_list = ImagesList(size_hint_y=None)
        self.images_list.bind(minimum_height=self.images_list.setter('height'))

    def set_images(self, images):
        self.images_list.set_images(images)
        if len(images):
            set_main_image(images[0])


class AllImagesColumn(ImagesColumn):
    def __init__(self):
        super(AllImagesColumn, self).__init__()
        generate_report_button = Button(text='Generate report', size_hint_y=None, height=40)
        def load(files, dirpath):
            report = save_json_file(files, dirpath)
            State.all_images.set_images(report)
        def on_press(_):
            choose_file(['*.jpg', '*.png'], load)
        generate_report_button.bind(
            on_press=on_press
        )
        self.add_widget(generate_report_button)
        self.add_widget(PathInput())
        self.init('All images')



class SimilarImagesColumn(ImagesColumn):
    def __init__(self):
        super(SimilarImagesColumn, self).__init__()
        self.add_widget(State.main_image)
        self.init('Similar images')


class ImagesList(StackLayout):
    def __init__(self, **kw):
        super(ImagesList, self).__init__(**kw)
        self.spacing = 10

    def set_images(self, images):
        self.clear_widgets()
        for image in images:
            self.add_widget(ImageButtonWithLabel(source=image))


class Root(BoxLayout):
    def __init__(self):
        super(Root, self).__init__()
        self.add_widget(State.all_images)
        self.add_widget(State.similar_images)


State.imported_path = Label(size_hint=(.5, None))
State.imported_path.height = 40
State.main_image = MainImage()
State.all_images = AllImagesColumn()
State.similar_images = SimilarImagesColumn()


class TestApp(App):
    def build(self):
        return Root()


if __name__ == '__main__':
    TestApp().run()
