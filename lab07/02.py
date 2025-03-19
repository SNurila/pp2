import pygame
from pynput import keyboard

pygame.mixer.init()

playlist = [
    "song1.mp3",
    "song2.mp3",
    "song3.mp3"
]

current_track = 0  

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    print(f"Playing: {playlist[current_track]}")

def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped")

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def prev_track():
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
            next_track()
        elif key.char == 'b':
            prev_track()
    except AttributeError:
        pass

print("Press 'p' to play, 's' to stop, 'n' for next, 'b' for previous")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
