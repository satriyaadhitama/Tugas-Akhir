from pynput.keyboard import Controller as KeyboardController, KeyCode
from pynput.keyboard import Key

def speech_to_command(key:str, keywords:list, keyboard:object):
    if key in keywords:
        if key == 'right':
            # Press and release the Right arrow key
            keyboard.press(KeyCode.from_vk(0x27))
            keyboard.release(KeyCode.from_vk(0x27))
        elif key == 'left':
            # Press and release the Left arrow key
            keyboard.press(KeyCode.from_vk(0x25))
            keyboard.release(KeyCode.from_vk(0x25))
        elif key == 'up':
            # Press and release the Up arrow key
            keyboard.press(KeyCode.from_vk(0x26))
            keyboard.release(KeyCode.from_vk(0x26))
        elif key == 'down':
            # Press and release the Down arrow key
            keyboard.press(KeyCode.from_vk(0x28))
            keyboard.release(KeyCode.from_vk(0x28))
        elif key == 'go':
            # Simulate pressing the spacebar key
            keyboard.press(Key.f5)
            keyboard.release(Key.f5)
        elif key == 'stop':
            # Simulating Esc key press and release
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)