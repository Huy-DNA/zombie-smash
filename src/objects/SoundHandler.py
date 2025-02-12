import pygame
import os


def play_background_music(file_path):
    """
    Stops the current background music (if any), loads a new music file from 'file_path',
    and plays it on loop.
    """
    # Ensure that the mixer is initialized
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    # Stop any currently playing music
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Music file not found: {file_path}")
        return

    try:
        # Load the new music file
        pygame.mixer.music.load(file_path)
        # Play the music indefinitely (-1 means loop forever)
        pygame.mixer.music.play(-1)
        print(f"Playing background music: {file_path}")
    except Exception as e:
        print(f"Error playing background music: {e}")


def play_sound_with_lowered_bg(sound_path, bg_volume=0.2):
    """
    Play a sound effect while lowering the background music volume,
    then restore the background music volume when the effect finishes.

    :param sound: The pygame.mixer.Sound object to play.
    :param bg_volume: The volume level to set for the background music during the effect.
    """
    # Load the sound effect.
    sound = pygame.mixer.Sound(sound_path)

    # Save the current volume so we can restore it later.
    current_volume = pygame.mixer.music.get_volume()

    # Lower the background music volume.
    pygame.mixer.music.set_volume(bg_volume)

    # Play the sound effect.
    channel = sound.play()

    # Restore the original background music volume.
    pygame.mixer.music.set_volume(current_volume)

