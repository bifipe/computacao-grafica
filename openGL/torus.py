from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = ( (1,1,0),(0.5,0.5,0) )

r = 1
R = 2
n = 50
halfpi = math.pi/2

def f(u, v):
    theta = (u*2*math.pi/(n-1))-halfpi
    phi = (v*2*math.pi)/(n-1)
    x = (R + r*math.cos(theta))*math.cos(phi)
    y = r*math.sin(theta)
    z = (R + r*math.cos(theta))*math.sin(phi)
    return x, y, z

def desenhaEsfera():
    glBegin(GL_QUAD_STRIP)
    glColor3fv(cores[0])
    for i in range(n):
        for j in range(n):
            glColor3fv(cores[(i+1)%len(cores)])
            glVertex3fv(f(i,j))
            glVertex3fv(f(i+1,j))
    glEnd()

a = 0

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a,1,1,0)
    desenhaEsfera()    
    glPopMatrix()
    glutSwapBuffers()
    a += 2
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("TORUS")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()