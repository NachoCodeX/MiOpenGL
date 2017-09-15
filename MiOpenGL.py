import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


W,H = 800,600


class Window(object):
    def __init__(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    #Crea la ventana Se le pasa el Ancho , Alto y Titulo
    def createWindow(self,W,H,TITLE,**kwargs):
        #Si no pasamos por parametro color, por defecto pondremos el negro
        self.color= kwargs['color'] if 'color' in kwargs.keys() else [0,0,0,0]

        glutInitWindowSize(W,H)
        glutCreateWindow(TITLE)
        glutDisplayFunc(self._draw)
        glutIdleFunc(self._draw)
        glutMainLoop()

    #Metodo que se sobreescribira para que dibujar
    def draw(self):
        pass

    #Metodo privado que llama a nuestro metodo draw que sobre escribimos

    def _draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(*self.color)
        glLoadIdentity()
        self.refresh2d()
        self.draw()
        glutSwapBuffers()

    #Prepara la ventana para dar una proyecion en 2D
    def refresh2d(self):
        glViewport(0,0,W,H)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0,W,0.0,H,0.0,1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    #Dibuja un rectangulo
    def drawRect(self,x,y,w,h,**kwargs):
        glColor3f(*kwargs['color'] if 'color' in kwargs.keys() else [1,0,0])
        glBegin(GL_QUADS)
        glVertex2f(x,y)
        glVertex2f(x+w,y)
        glVertex2f(x+w,y+h)
        glVertex2f(x,y+h)
        glEnd()

    #Dibuja una line se le pasa en forma de vector las cordenadas. [0,0],[10,10]
    def drawLine(self,P,Q,**kwargs):
        glColor3f(*kwargs['color'] if 'color' in kwargs.keys() else [1,0,0])
        glBegin(GL_LINES);
        glVertex2i(P[0], P[1]);
        glVertex2i(Q[0], Q[1]);
        glEnd()
    #Dibuja un punto
    def drawPoint(self,x,y,**kwargs):
        glPointSize(kwargs['size'])
        glColor3f(*kwargs['color'] if 'color' in kwargs.keys() else [1,0,0])
        glBegin(GL_POINTS);
        glVertex3f(1.0,1.0,1.0);
        glVertex2f(x,y);
        glEnd()

    def drawTriangle(self):
        glDisable(GL_CULL_FACE)
        glTranslatef(-1.5,0,-6)
        glBegin(GL_TRIANGLES)
        glColor3f(1,0,0)
        glVertex3f(0,1,0)
        glVertex3f(-1,-1,0)
        glVertex3f(1,-1,0)
        glEnd()
        glTranslatef(3,0,0)


    # Dibuja un array de puntos
    def drawArrayPoints(self,POINTS, **kwargs):
        for i in range(len(POINTS)):
            self.drawPoint(POINTS[i][0],POINTS[i][1],size=1,color=kwargs['color'])
