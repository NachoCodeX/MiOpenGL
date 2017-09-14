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
    def createWindow(self,W,H,TITLE):
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
        # print(*kwargs['color'])
        glColor3f(*kwargs['color'])
        glBegin(GL_QUADS)
        glVertex2f(x,y)
        glVertex2f(x+w,y)
        glVertex2f(x+w,y+h)
        glVertex2f(x,y+h)
        glEnd()

    #Dibuja una line se le pasa en forma de vector las cordenadas. [0,0],[10,10]
    def drawLine(self,P,Q,**kwargs):
        glColor3f(*kwargs['color'])
        glBegin(GL_LINES);
        glVertex2i(P[0], P[1]);
        glVertex2i(Q[0], Q[1]);
        glEnd()
    #Dibuja un punto
    def drawPoint(self,x,y,**kwargs):
        glPointSize(kwargs['size'])
        glColor3f(*kwargs['color'])
        glBegin(GL_POINTS);
        glVertex3f(1.0,1.0,1.0);
        glVertex2f(x,y);
        glEnd();
    #Este me falto alv
    def drawTriangle(slef):
        glBegin(GL_TRIANGLES)
        glVertex3f()

    def drawArrayPoints(self,POINTS):
        for i in range(len(POINTS)):
            self.drawPoint(POINTS[i][0],POINTS[i][1],size=2,color=[1,0,0])
        # glColor3ub(255,255,255)
        # glEnableClientState(GL_VERTEX_ARRAY)
        # glEnableClientState(GL_COLOR_ARRAY)
        # glVertexPointer(2,GL_FLOAT,sys.getsizeof(POINTS),POINTS[0][1])
        # glPointSize(3.0)
        # glDrawArrays(GL_POINTS,0,len(POINTS))
        # glDisableClientState(GL_VERTEX_ARRAY)
        # glDisableClientState(GL_COLOR_ARRAY)
        # glFlush()

    #Dibuja una verga cabezon de color rosa
    def drawDick(self):
        self.drawRect(20*10,20,100,100,color=[1,0,1])
        self.drawRect(20*25,20,100,100,color=[1,0,1])
        self.drawRect(20*17,20,100,500,color=[1,0,1])
        self.drawRect(20*19,520,10,100,color=[1,1,1])
        self.drawRect(20*19,500,10,50,color=[0,0,0])
        self.drawRect(20*17,450,100,10,color=[0,0,0])

# def main():
#     w=Window(800,600,'Pene de negro')
    # glutInit(sys.argv)
    # glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    # window=Window()
    # glutInitWindowSize(W,H)
    # # glutInitWindowPosition(0,0)
    # w= glutCreateWindow('My first window')
    # glutDisplayFunc(window.draw)
    # glutIdleFunc(window.draw)
    # glutMainLoop()

#
# if __name__ == '__main__':
#     main()
