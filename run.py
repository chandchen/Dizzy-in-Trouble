import sys
import pygame

from settings import Settings


def run_game():
    pygame.init()
    DTsettings = Settings()
    screen = pygame.display.set_mode(
        (DTsettings.screen_width, DTsettings.screen_height))
    pygame.display.set_caption('Dizzy in Trouble')
    background = pygame.image.load('images/background.jpg')
    background = pygame.transform.scale(background, (1000, 555))

    font = pygame.font.SysFont("arial", 16)
    text = font.render('Cliked Me please!!!', True, (34, 252, 43))
    mouse_x, mouse_y = 0, 0

    music_file = "musics/adenium.mp3"
    freq = 44100
    bitsize = -16
    channels = 2
    buffer = 2048
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.set_volume(0.8)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background, (0, 0))
        screen.fill((mouse_x, mouse_y, 0))
        screen.blit(text, (40, 100))
        pygame.display.flip()

        try:
            play_music(music_file)
        except KeyboardInterrupt:
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.stop()
            raise SystemExit


def play_music(music_file):
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pygame.error:
        print("File {} not found! {}".format(music_file, pygame.get_error()))
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30)


run_game()
