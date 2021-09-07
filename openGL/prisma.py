from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = ( (1,1,0),(0.5,0.5,0) )
numeroLados = 10
pontos = []
top = (0,5,0)
raio = 3

def desenhaBase():
    glBegin(GL_POLYGON)
    glColor3fv(cores[0])
    glVertex2f(0,0)   
    for i in range(0,numeroLados+1):
        a = (i/numeroLados) * 2 * math.pi
        x = raio * math.cos(a)
        z = raio * math.sin(a)
        pontos.append((x,0,z))
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(x,0,z)
    glEnd()

def desenhaLados():
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(cores[0])
    glVertex3f(*top)    
    for i in range(0,numeroLados):
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(*pontos[i])
        glVertex3f(*pontos[i+1])
    glEnd()

a = 0

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()   
    glRotatef(a,1,1,0) # vai rotacionar a graus ao redor de x e y
    desenhaBase()
    desenhaLados()   
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
glutCreateWindow("PRISMA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-20) # empurra para dentro da tela
glutTimerFunc(50,timer,1)
glutMainLoop()