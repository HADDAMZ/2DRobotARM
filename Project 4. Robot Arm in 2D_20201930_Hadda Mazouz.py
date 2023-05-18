import pygame
import numpy as np

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (192, 192, 192)

def Rmat(degree):
    radian = np.deg2rad(degree)
    cos = np.cos(radian)
    sin = np.sin(radian)
    R = np.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
    return R

def Tmat(tx, ty):
    T = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
    return T

pygame.init()

pygame.display.set_caption("Robot Arm")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

done = False

def drawRectangle(rect, M, screen, color):
    points = [np.dot(M, [x, y, 1])[:2] for x, y in rect]
    pygame.draw.polygon(screen, color, points, 0)
    pygame.draw.polygon(screen, BLACK, points, 2)

rectangle1 = np.array([[0, 0], [200, 0], [200, 40], [0, 40]])
rectangle2 = np.array([[0, 0], [200, 0], [200, 40], [0, 40]])

I = np.array([[1, 0, 0, ], [0, 1, 0], [0, 0, 1]])

theta2 = 0  # degrees
theta2_vel = .1  # 1 degree / FPS

# Load background image
background_image = pygame.image.load('ROBOT.PNG')
background_image = pygame.transform.scale(background_image, (700, 700))

# Load background sound
pygame.mixer.music.load('robot.wav')
pygame.mixer.music.play(-1)  # Play the sound on loop

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    # Draw background image
    screen.blit(background_image, (250, 100))

    theta2 += theta2_vel

    M1 = I @ Tmat(710, 300)
    drawRectangle(rectangle1, M1, screen, GREY)

    M2 = M1 @ Tmat(200, 0) @ Rmat(theta2)
    drawRectangle(rectangle2, M2, screen, GREY)

    pygame.display.flip()

    clock.tick(60)

pygame.mixer.music.stop()  # Stop the background sound
pygame.quit()



