from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))

back_button = Button(
    text="Back",
    background_normal="back_icon.png",  # ✅ Add a custom back arrow image
    size_hint=(0.2, 1)
)

layout.add_widget(back_button)
