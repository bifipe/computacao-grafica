from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

cores = ( (1,1,0),(0.5,0.5,0) )

x0 = -1
xn = 1

y0 = -1
yn = 1

n = 50
dx = (xn - x0)/n
dy = (yn - y0)/n

def f(x,y):
    # Paraboloide Circular
    return x**2-y**2

def f2(x,y):
    # Paraboloide Circular
    return x**2+y**2

def desenhaSuperficie():
    y = y0
    for i in range(n):
        x = x0     
        glBegin(GL_TRIANGLE_STRIP)
        glColor3fv(cores[0])
        for j in range(n): 
            glColor3fv(cores[(i+1)%len(cores)])
            glVertex3f(x, y, f(x, y))
            glVertex3f(x, y + dy, f(x, y + dy))           
            x += dx   
        glEnd()      
        y += dy

def desenhaSuperficie2():
    y = y0
    for i in range(n):
        x = x0       
        glBegin(GL_TRIANGLE_STRIP)
        glColor3fv(cores[0])
        for j in range(n):  
            glColor3fv(cores[(i+1)%len(cores)])
            glVertex3f(x, y, f2(x, y))
            glVertex3f(x, y + dy, f2(x, y + dy))        
            x += dx       
        glEnd()       
        y += dy

a = 0

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslate(-2, 0, 0)
    glRotatef(a,1,0,0) # vai rotacionar a graus ao redor de x e y
    desenhaSuperficie()   
    glPopMatrix()
    glPushMatrix()   
    glTranslate(2, 0, 0)
    glRotatef(a,1,0,0)
    desenhaSuperficie2()  
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
glutCreateWindow("SUPERFICIE")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10) # empurra para dentro da tela
glutTimerFunc(50,timer,1)
glutMainLoop()