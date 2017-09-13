import MiOpeneGL
# o


class Window(MiOpeneGL.Window):
    def __inti__(self,*args,**kwargs):
        super(Window,self).__init__(*args,**kwargs)
    def draw(self):
        self.drawRect(10,10,100,100,color=[0,.8,1])
        self.drawLine([0,0],[200,200],color=[0,0.5,1])
        self.drawPoint(220,80,size=5,color=[1,0,0])
        self.drawDick()

Window().createWindow(800,600,'Title')
