import MiOpenGL



class Window(MiOpenGL.Window):
    def __inti__(self,*args,**kwargs):
        super(Window,self).__init__(*args,**kwargs)
    def DDA(self,P,Q):
        dx=abs(Q[0]-P[0])
        dy=abs(Q[1]-P[1])
        if(dx>= dy):
            step=dx
        else:
            step=dy

        xin=dx/step
        yin=dy/step
        x=P[0]+0.5
        y=P[1]+0.5

        POINTS=[]
        for i in range(step):
            POINTS.append([x,y])
            x=x+xin
            y=y+yin

        return POINTS

    def draw(self):
        self.drawArrayPoints(self.DDA([100,100],[150,150]),color=[0,1,0])
        # self.drawTriangle()
w=Window()
# w.DDA([100,100],[150,150])
w.createWindow(800,600,'Title')
