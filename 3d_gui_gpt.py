import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

rotation_speed = 1  # Adjust the rotation speed as needed

def draw_quadrants():
    # Draw first quadrant
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glEnd()

    # Draw second quadrant
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glEnd()

    # Draw third quadrant
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()

    # Draw fourth quadrant
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(0.0, -1.0, 0.0)
    glEnd()

def draw_line_to_point(x, y):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(x, y, 0.0)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(-rotation_speed, 0, 1, 0)
                elif event.key == pygame.K_RIGHT:
                    glRotatef(rotation_speed, 0, 1, 0)
                elif event.key == pygame.K_UP:
                    glRotatef(-rotation_speed, 1, 0, 0)
                elif event.key == pygame.K_DOWN:
                    glRotatef(rotation_speed, 1, 0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_quadrants()
        target = [1.5, -.5]
        draw_line_to_point(target[0], target[1])
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()