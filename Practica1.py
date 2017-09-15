import MiOpenGL


class Window(MiOpenGL.Window):
    def __inti__(self,*args,**kwargs):
        super(Window,self).__init__(*args,**kwargs)
    def draw(self):
        self.drawPoint(50,50,size=2,color=[1,0,0])
        self.drawPoint(50*2,50*2,size=2,color=[1,1,0])
        self.drawPoint(50*3,50*3,size=2,color=[0,0,1])
        self.drawPoint(50*4,50*4,size=2,color=[1,1,1])


w=Window()
# Cambiamos el color de fondo a verder
w.createWindow(800,600,'Title',color=[0.1,0.7,.3,0])
