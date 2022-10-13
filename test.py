from kivy.tests.common import GraphicUnitTest
from kivy.app import runTouchApp
from kivy.uix.button import Button
from kivy.base import EventLoop
import unittest


# Define test class
class TestCase(GraphicUnitTest):

    def test(self):
        # test on graphical in Kivy
        button = Button()
        runTouchApp(button)

        EventLoop.ensure_window()
        window = EventLoop.window

        # Asserts
        self.assertEqual(window.children[0], button)
        self.assertEqual(window.children[0].height, window.height)


if __name__ == '__main__':
    unittest.main()
