from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
from math import *
import sys

a = 0

def calculaNormalFace(v0, v1, v2):
    x = 0
    y = 1
    z = 2
    U = (v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z])
    V = (v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z])
    N = ((U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return (N[x]/NLength, N[y]/NLength, N[z]/NLength)

def prisma():
    raio = 4
    raio2 = 2
    numeroLados = 6
    altura = 3
    angulo = (2*math.pi)/numeroLados
    pontosBase = []
    pontosBase2 = []
    
    glPushMatrix()
    glTranslatef(0,-2,0)
    glRotatef(a,0.0,1.0,0.0)
    glRotatef(-110,5.0,0.0,0.0)

    # Base 1
    glBegin(GL_POLYGON)
    for i in range(0,numeroLados):
        x = raio * math.cos(i*angulo)
        y = raio * math.sin(i*angulo)
        pontosBase += [ (x,y) ]
        glVertex3f(x,y,0.0)

    u = (pontosBase[0][0], pontosBase[0][1], 0)
    v = (pontosBase[1][0], pontosBase[1][1], 0)
    p = (pontosBase[2][0], pontosBase[2][1], 0)

    glNormal3fv(calculaNormalFace(u,v,p))
    glEnd()

    # Base 2
    glBegin(GL_POLYGON)
    for j in range(0,numeroLados):
        x2 = raio2 * math.cos(j*angulo)
        y2 = raio2 * math.sin(j*angulo)
        pontosBase2 += [(x2,y2)]
        glVertex3f(x2,y2,altura)

    u2 = (pontosBase2[0][0], pontosBase2[0][1], altura)
    v2 = (pontosBase2[1][0], pontosBase2[1][1], altura)
    p2 = (pontosBase2[2][0], pontosBase2[2][1], altura)

    glNormal3fv(calculaNormalFace(u2,v2,p2))
    glEnd()

    # Faces Laterais
    glBegin(GL_QUADS)
    for i in range(0,numeroLados):
        u = (pontosBase[i][0], pontosBase[i][1],0.0)
        v = (pontosBase2[i][0],pontosBase2[i][1],altura)
        p = (pontosBase2[(i+1)%numeroLados][0],pontosBase2[(i+1)%numeroLados][1],altura)
        q = (pontosBase[(i+1)%numeroLados][0],pontosBase[(i+1)%numeroLados][1],0.0)

        glNormal3fv(calculaNormalFace(u,v,q))

        glVertex3fv(u)
        glVertex3fv(v)
        glVertex3fv(p)
        glVertex3fv(q)
    glEnd()

    glPopMatrix()

def display():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    prisma()
    a+=0.5
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(15,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(65,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(10,0,0,0,0,0,0,1,0)

def init():
    mat_ambient = (0.25, 0.148, 0.06475, 1.0)
    mat_diffuse = (0.4, 0.2368, 0.1036, 1.0)
    mat_specular = (0.774597, 0.458561, 0.200621, 1.0)
    mat_shininess = (76.8)
    light_position = (300.0, 300.0, 300.0, 1.0)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_SMOOTH)
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Prisma Iluminado")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45,800.0/600.0,0.1,100.0)
    glTranslatef(0.0,0.0,-10)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()