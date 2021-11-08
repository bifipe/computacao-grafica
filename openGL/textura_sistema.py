from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png
import math

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\033'

# Number of the glut window.
window = 0

# Rotations. 
xrotSol = yrotSol = zrotSol = xrotLua = yrotLua = xrotTerra = yrotTerra = 0.0

# Parâmetros para esfera
r = 1
n = 50
halfpi = math.pi/2

# texture = []

def LoadTextures():
    global texture
    texture = [ glGenTextures(1), glGenTextures(1), glGenTextures(1) ]

    ################################################################################
    # Sol
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='sol.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    # Lua
    glBindTexture(GL_TEXTURE_2D, texture[1])
    reader = png.Reader(filename='lua.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    # Terra
    glBindTexture(GL_TEXTURE_2D, texture[2])
    reader = png.Reader(filename='terra.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def sol(u, v):
    theta = (u*math.pi/(n-1))-halfpi
    phi = (v*2*math.pi)/(n-1)
    x = r*math.cos(theta)*math.cos(phi)
    y = r*math.sin(theta)
    z = r*math.cos(theta)*math.sin(phi)
    return x, y, z

def lua(u, v):
    theta = (u*math.pi/(n-1))-halfpi
    phi = (v*2*math.pi)/(n-1)
    x = (r/8)*math.cos(theta)*math.cos(phi)
    y = (r/8)*math.sin(theta)
    z = (r/8)*math.cos(theta)*math.sin(phi)
    return x, y, z

def terra(u, v):
    theta = (u*math.pi/(n-1))-halfpi
    phi = (v*2*math.pi)/(n-1)
    x = (r/4)*math.cos(theta)*math.cos(phi)
    y = (r/4)*math.sin(theta)
    z = (r/4)*math.cos(theta)*math.sin(phi)
    return x, y, z

def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1
    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrotSol, yrotSol, zrotSol, xrotLua, yrotLua, xrotTerra, yrotTerra, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   
    glClearColor(0.0,0.0,0.0,1.0)

    # Sol
    glTranslatef(0.0,0.0,-10.0)
    glRotatef(xrotSol,1.0,0.0,0.0)          
    glRotatef(yrotSol,0.0,1.0,0.0)           
    glRotatef(zrotSol,0.0,0.0,1.0) 
    
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUAD_STRIP)              
        
    for i in range(n):
        for j in range(n):
            glTexCoord2f(i/n,j/n); glVertex3fv(sol(i,j))
            glTexCoord2f((i+1)/n,(j)/n); glVertex3fv(sol(i+1,j))
    glEnd()
    
    # Terra
    glTranslatef(0.0,0.0,3.0)
    glRotatef(xrotSol,0.0,1.0,0.0)          
    glRotatef(yrotSol,0.0,1.0,0.0)           
    
    glBindTexture(GL_TEXTURE_2D, texture[2])
    glBegin(GL_QUAD_STRIP)              
        
    for i in range(n):
        for j in range(n):
            glTexCoord2f(i/n,j/n); glVertex3fv(terra(i,j))
            glTexCoord2f((i+1)/n,(j)/n); glVertex3fv(terra(i+1,j))
    glEnd()

    # Lua
    glTranslatef(0.0,0.0,1.0)  
    glRotatef(xrotLua,0.0,1.0,0.0)            
    glRotatef(yrotLua,0.0,1.0,0.0)

    glBindTexture(GL_TEXTURE_2D, texture[1])
    glBegin(GL_QUAD_STRIP)              
        
    for i in range(n):
        for j in range(n):
            glTexCoord2f(i/n,j/n); glVertex3fv(lua(i,j))
            glTexCoord2f((i+1)/n,(j)/n); glVertex3fv(lua(i+1,j))
    glEnd()
    
    xrotSol = xrotSol + 0.1                # X rotation
    yrotSol = yrotSol + 0.1                 # Y rotation
    #zrotSol = zrotSol + 0.01                 # Z rotation

    xrotTerra = xrotTerra + 0.1                # X rotation
    yrotTerra = yrotTerra + 0.1                 # Y rotation

    xrotLua = xrotLua + 0.1                # X rotation
    yrotLua = yrotLua + 0.1                 # Y rotation

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)    
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Sistema Solar")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    InitGL(640, 480)
    glutMainLoop()


main()
