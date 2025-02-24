import pygame
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning, message=".*AVX2.*")

pygame.init()
pygame.mixer.init()

def dot():
    sound = pygame.mixer.Sound("dot.wav")
    sound.play()
    pygame.time.wait(500)  

def dash():
    sound = pygame.mixer.Sound("dash.wav")
    sound.play()
    pygame.time.wait(1000)


