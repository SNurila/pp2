import pygame
from pynput import keyboard

pygame.mixer.init()

playlist = [
    'song1.mp3',
    'song2.mp3',
    'song3.mp3'
]

current_track = 0

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_music():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def prev_music():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

def on_press(key):
    try:
        if key.char == 'p':
            play_music()
        elif key.char == 's':
            stop_music()
        elif key.char == 'n':
            next_music()
        elif key.char == 'v':
            prev_music()
    except AttributeError:
        pass
    
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()