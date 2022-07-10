from asyncore import write
from re import M
from turtle import left
from venv import create
from manim import *
from scipy.fftpack import shift

class LatinSquare(VGroup):
    def __init__(self,n=1,*vmobjects,**kwargs):

        super().__init__(*vmobjects,**kwargs)

        self.n=n
        self.txt,self.e=[0],[0]

        x,y=0,0
        if (n%2)==0:
            x,y=-(n/2)+0.5,(n/2)-0.5
        else:
            x,y=-((n-1)/2),((n-1)/2)

        for i in range(n):
            ro=[0]
            for j in range(n):
                s=Square(side_length=1).move_to([x+j,y-i,0])
                s.set_stroke(color=GREY_E)
                s.set_fill(color=GREY_D,opacity=1)
                self+=s
                ro.append(0)
            self.e.append(ro)
        
        for i in range(n):
            ro=[0]
            for j in range(n):
                txt_tmp=Text("")
                ro.append(txt_tmp)
                self+=txt_tmp
            self.txt.append(ro)

    def fill(self,x,y,element,txt_color=GREY_B):
        if element==0 :
            self.txt[x][y]=Text("")
            return self.txt[x][y]
        tmp=Text(str(element),color=txt_color)
        tmp.move_to(self[(x-1)*self.n+y-1].get_center())
        self.e[x][y]=element
        self.txt[x][y].become(tmp)
        return self.txt[x][y]

class Main1(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        self.camera.frame.scale(0.8)
        
        self.wait()
        LS1=LatinSquare(n=4)
        tmp=[[1,2,3,4],[2,1,4,3],[4,3,1,2],[3,4,2,1]]
        for i in range(4):
            for j in range(4):
                LS1.fill(x=i+1,y=j+1,element=tmp[i][j])
        self.play(Create(LS1),run_time=3)
        self.wait()
        
        A1=Arrow(start=np.array([-1.7,2.5,0]),end=np.array([1.7,2.5,0]),color=BLUE)
        self.play(GrowArrow(A1))
        A2=Arrow(start=np.array([-2.5,1.7,0]),end=np.array([-2.5,-1.7,0]),color=BLUE)
        self.play(GrowArrow(A2))

        self.wait()
        self.play(Uncreate(LS1),Uncreate(A1),Uncreate(A2))
        self.wait()

        LS2=LatinSquare(n=4)
        tmp=[[0,0,1,3],[3,0,0,0],[4,0,0,2],[3,0,4,0]]
        for i in range(4):
            for j in range(4):
                LS2.fill(x=i+1,y=j+1,element=tmp[i][j])
        LS2.shift(LEFT*6)

        LS3=LatinSquare(n=5)
        tmp=[[1,4,2,5,3],[4,2,5,3,1],[2,5,3,1,4],[5,3,1,4,2]]
        for i in range(4):
            for j in range(5):
                LS3.fill(x=i+1,y=j+1,element=tmp[i][j])

        LS4=LatinSquare(n=5)
        tmp=[[1,2,3,4,0],[0,0,0,0,5]]
        for i in range(2):
            for j in range(5):
                LS4.fill(x=i+1,y=j+1,element=tmp[i][j])
        LS4.shift(RIGHT*6)
        LS4_=LS4.copy().scale(1.5).move_to(ORIGIN)

        self.camera.frame.scale(2)
        self.play(Create(LS2),Create(LS3),Create(LS4))
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.7))
        self.wait()

        self.play(Circumscribe(VGroup(*[LS3[i] for i in range(20)])))
        self.wait()
        tmp=[3,1,4,2,5]
        for i in range(5):
            self.play(Write(LS3.fill(x=5,y=i+1,element=tmp[i])),run_time=0.5)
        self.wait()
        self.play(self.camera.frame.animate.shift(LEFT*6))
        
        self.play(Circumscribe(LS2[4],time_width=1,run_time=2),
                  Circumscribe(LS2[12],time_width=1,run_time=2))
        self.wait()
        self.play(self.camera.frame.animate.shift(RIGHT*12))

        box1=SurroundingRectangle(LS4[4])
        self.play(Create(box1))
        self.wait()
        self.play(Uncreate(box1))

        self.play(Restore(self.camera.frame))
        self.wait()
        self.play(Uncreate(LS2),Uncreate(LS3),Uncreate(LS4))
        self.wait()

        Q1=Text("在什么样的情况下，一个部分拉丁方一定可以被填充完整呢？")
        Q2=Text("一个部分拉丁方能被填完整的一个充分条件是什么？")
        self.play(Write(Q1))
        self.wait()
        self.play(FadeOut(Q1,shift=UP),FadeIn(Q2,shift=UP))
        self.wait()
        self.play(FadeOut(Q2))
        self.wait()

        self.play(Create(LS4_))
        self.wait()
        self.play(Circumscribe(LS4_[4]))
        self.wait()
        cd=MathTex(r"c<n").scale(1.5).move_to(RIGHT*5)
        self.play(LS4_.animate.shift(LEFT*4),Write(cd))
        self.wait()
        self.play(FadeIn(Text("Sufficient!").move_to(cd.copy().shift(DOWN*2)),shift=DOWN))
        self.wait()

# manim -qh LatinSquare.py
class Process(Scene):
    def construct(self):
        self.camera.background_color=GREY_E
        n1=Text("Hall",font_size=32).move_to(LEFT*5)
        n2=Text("Herbert J.Ryser",font_size=32).move_to(UP*0.8)
        n3=Text("Charles C.Lindner",font_size=32).move_to(DOWN*0.8)
        n4=Text("Smetaniuk",font_size=32).move_to(RIGHT*5)
        a1=Arrow(start=LEFT,end=RIGHT).move_to(LEFT*3)
        a2=a1.copy().move_to(RIGHT*3)

        self.play(Write(n1))
        self.wait()
        self.play(GrowArrow(a1))
        self.play(Write(n2),Write(n3))
        self.wait()
        self.play(GrowArrow(a2))
        self.play(Write(n4))
        self.wait()

class Main2(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        LS1=LatinSquare(3)
        tmp=[[1,3,2],[2,1,3],[3,2,1]]
        for i in range(3):
            for j in range(3):
                LS1.fill(x=i+1,y=j+1,element=tmp[i][j])
        self.play(FadeIn(LS1))
        self.wait()

        LS1.save_state()
        self.play(*([LS1.txt[i+1][1].animate.move_to(LS1.txt[i+1][2]) for i in range(3)]+
                    [LS1.txt[i+1][2].animate.move_to(LS1.txt[i+1][1]) for i in range(3)]))
        self.wait()
        self.play(Restore(LS1))
        self.wait()

        LS1.save_state()
        self.play(*([LS1.txt[1][i+1].animate.move_to(LS1.txt[2][i+1]) for i in range(3)]+
                    [LS1.txt[2][i+1].animate.move_to(LS1.txt[1][i+1]) for i in range(3)]))
        self.wait()
        self.play(Restore(LS1))
        self.wait()

        LS1.save_state()
        self.play(Transform(LS1.txt[1][2],Text("2").move_to(LS1.txt[1][2])),
                  Transform(LS1.txt[1][3],Text("3").move_to(LS1.txt[1][3])),
                  Transform(LS1.txt[2][1],Text("3").move_to(LS1.txt[2][1])),
                  Transform(LS1.txt[2][3],Text("2").move_to(LS1.txt[2][3])),
                  Transform(LS1.txt[3][1],Text("2").move_to(LS1.txt[3][1])),
                  Transform(LS1.txt[3][2],Text("3").move_to(LS1.txt[3][2])))
        self.wait()
        self.play(Restore(LS1))
        self.wait()

        self.play(LS1.animate.shift(LEFT*3))
        R_txt,C_txt,E_txt=Text("R").move_to(UR),Text("C").move_to(RIGHT),Text("E").move_to(DR)
        self.play(Write(R_txt),Write(C_txt),Write(E_txt))
        RG,CG,EG=VGroup(R_txt),VGroup(C_txt),VGroup(E_txt)
        for i in range(1,4):
            for j in range(1,4):
                tmpR=Text(str(i)).move_to(LS1[(i-1)*3+j-1])
                tmpC=Text(str(j)).move_to(LS1[(i-1)*3+j-1])
                tmpE=Text(str(tmp[i-1][j-1])).move_to(LS1[(i-1)*3+j-1])
                self.add(tmpR,tmpC,tmpE)
                self.play(tmpR.animate.move_to([1+((i-1)*3+j)/2,1,0]),
                          tmpC.animate.move_to([1+((i-1)*3+j)/2,0,0]),
                          tmpE.animate.move_to([1+((i-1)*3+j)/2,-1,0]),run_time=0.3)
                RG+=tmpR
                CG+=tmpC
                EG+=tmpE
        
        self.wait()
        self.play(Circumscribe(RG,run_time=2),
                  Circumscribe(CG,run_time=2))
        self.wait()
        self.play(Circumscribe(VGroup(RG[1],RG[2]),run_time=1),
                  Circumscribe(VGroup(EG[1],EG[2]),run_time=1))
        self.wait()
        self.play(Circumscribe(VGroup(RG[3],RG[4]),run_time=1),
                  Circumscribe(VGroup(EG[3],EG[4]),run_time=1))
        self.wait()

        box1=SurroundingRectangle(RG)
        box2=SurroundingRectangle(CG)
        box3=SurroundingRectangle(EG)
        self.play(FadeIn(box1),FadeIn(box2))
        self.wait()
        self.play(FadeIn(box3),FadeOut(box2))
        self.wait()
        self.play(FadeIn(box2),FadeOut(box1))
        self.wait()
        self.play(FadeOut(box3),FadeOut(box2))
        self.wait()

        self.play((RG-RG[0]).animate.shift(DOWN*2),
                  (EG-EG[0]).animate.shift(UP*2))
        self.wait()

        LS1_=LatinSquare(n=3)
        tmp=[[1,2,3],[2,3,1],[3,1,2]]
        for i in range(3):
            for j in range(3):
                LS1_.fill(x=i+1,y=j+1,element=tmp[i][j])
        LS1_.move_to(LEFT*3)
        self.play(Transform(LS1,LS1_))
        self.wait()

class Explain_H(Scene):
    def construct(self):
        self.camera.background_color=GREY_E
        H=MathTex(r"\{1,3\}",',',r"\{1,2\}",',',r"\{2,3,4\}",',',r"\{4\}").move_to(UP*3)

        V1=VGroup()
        V1.add(MathTex(r"m=1"),MathTex(r"\{1,3\}"),MathTex(r"\{1,2\}"),MathTex(r"\{2,3,4\}"),MathTex(r"\{4\}")).scale(0.8)
        V1.arrange().shift(UP)
        V1[0].shift(LEFT*3)
        V2=VGroup()
        V2.add(MathTex(r"m=2"),MathTex(r"\{1,2,3\}"),MathTex(r"\{1,2,4\}"),MathTex(r"\{1,3,4\}"),MathTex(r"\{1,2,3,4\}")).scale(0.8)
        V2.arrange()
        V2[0].move_to(V1[0].get_center()+DOWN)
        V3=VGroup()
        V3.add(MathTex(r"m=3"),MathTex(r"\{1,2,3,4\}")).scale(0.8)
        V3.arrange().shift(DOWN)
        V3[0].move_to(V2[0].get_center()+DOWN)
        V4=VGroup()
        V4.add(MathTex(r"m=4"),MathTex(r"\{1,2,3,4\}")).scale(0.8)
        V4.arrange().shift(DOWN*2)
        V4[0].move_to(V3[0].get_center()+DOWN)

        self.play(FadeIn(H))
        self.wait()
        tmp=[V1,V2,V3,V4]
        for i in tmp:
            for j in i:
                self.play(FadeIn(j),run_time=0.3)

        tmp=[H[2],H[6],V2[0],V2[2]]
        self.play(*[i.animate.set_color(color=BLUE) for i in tmp])
        self.wait()
        self.play(Circumscribe(H[2]),Circumscribe(H[6]))
        self.play(Circumscribe(V2[2]))
        self.wait()

        tmp=[1,2,3,4]
        for i in range(4):
            self.play(FadeIn(Text(str(tmp[i]),font_size=32).move_to(H[2*i].get_center()+DOWN),shift=DOWN),run_time=0.5)
        self.wait()

class Hall(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        X=MathTex(r"X").move_to(UP*2)
        A=X.copy()
        self.wait()
        self.play(Write(X))
        self.wait()
        self.play(Transform(A,MathTex(r"A_1,A_2,A_3,\dots,A_n")))
        x=A.copy()
        self.wait()
        self.play(Transform(x,MathTex(r"x_1,x_2,x_3,\dots,x_n").move_to(DOWN*2)))
        self.wait()
        self.play(Transform(x,MathTex(r"x_1\neq x_2\neq x_3\neq \dots \neq x_n").move_to(DOWN*2)))
        self.wait()
        self.play(FadeOut(x),FadeOut(X))
        self.play(A.animate.shift(UP))
        H=MathTex(r"\forall m\in[1,n],|A_{i_1} \cup A_{i_2} \cup \dots \cup A_{i_m}| \geq m").move_to(DOWN)
        self.play(Write(H))
        self.wait()
        self.play(Unwrite(A),Unwrite(H),run_time=1)
        self.wait()

        girl,boy,mline=VGroup(),VGroup(),VGroup()
        for i in range(4):
            tmp=Circle(radius=0.3,color=PINK).move_to(LEFT*3+(1.5-i)*UP*1.2).set_fill(PINK,1)
            girl.add(tmp)
        for i in range(4):
            tmp=Circle(radius=0.3,color=BLUE).move_to(RIGHT*3+(1.5-i)*UP*1.2).set_fill(BLUE,1)
            boy.add(tmp)
        self.play(FadeIn(girl))
        self.wait()
        tmp=[[0,2],[0,1],[3],[0,3]]
        for i in range(4):
            for j in tmp[i]:
                l=Line(start=girl[i].get_center(),end=boy[j].get_center())
                mline.add(l)
        self.play(FadeIn(boy),FadeIn(mline))
        self.wait()
        for i in [1,3,4,5]:
            self.wait(0.5)
            mline[i].set_color(color=YELLOW)
        self.wait()
        self.play(FadeOut(mline),FadeOut(boy),FadeOut(girl))
        self.wait()

        A=MathTex(r"\{1,2\}\quad \{1\}").move_to(UP)
        self.play(Write(A))
        X=A.copy()
        self.play(Transform(X,MathTex(r"\{1\}").move_to(DOWN)))
        self.play(Wiggle(X))
        self.play(Unwrite(A),Unwrite(X))
        self.wait()

        Case1=Text("Case 1").move_to(5*LEFT+3*UP)
        Case2=Text("Case 2").move_to(2*RIGHT+3*UP)
        self.play(Write(Case1),Write(Case2))
        self.wait()

        A=MathTex(r"\{1,3\},\{1,2\},\{2,3,4\},\{",r"1",r",4\}").move_to(LEFT*3.5+UP*1.5)
        self.play(Write(A))
        self.wait()
        self.play(A[1].animate.set_color(color=BLUE))
        self.wait()
        A_=A[0].copy()
        self.play(Transform(A_,MathTex(r"\{3\},\{2\},\{2,3,4\}").move_to(LEFT*3.5)))
        self.wait()
        x=A_.copy()
        self.play(Transform(x,MathTex(r"3,2,4").move_to(LEFT*3.5+DOWN*1.5)))
        self.wait()
        self.play(Transform(x,MathTex(r"3,2,4,1").move_to(LEFT*3.5+DOWN*1.5)))
        self.wait()

        B=MathTex(r"\{1,3\}",",",r"\{1,2\}",",",r"\{3,4\}",",",r"\{1,4\}").move_to(RIGHT*3.5+UP*1.5)
        self.play(Write(B))
        self.wait()
        self.play(*[B[i].animate.set_color(color=BLUE) for i in [0,4,6]])
        self.wait()
        self.play(B[2].animate.move_to(B[6]),
                  B[6].animate.move_to(B[2]))
        self.wait()
        S=MathTex("S").move_to(UP*1.5+RIGHT*0.2)
        S_sz=MathTex("|S|=l",font_size=28).move_to(S.copy().shift(DOWN*0.6))
        self.play(Write(S))
        self.wait()
        self.play(Write(S_sz))
        self.wait()
        x_1=VGroup(*[B[i].copy() for i in [0,4,6]])
        self.play(Transform(x_1,MathTex(r"1,4,3").move_to(RIGHT*2+DOWN*1.5)))
        self.wait()
        self.play(B[2].animate.set_color(color=YELLOW))
        U=MathTex(r"U").move_to(RIGHT*6.7+UP*1.5)
        U_sz=MathTex("|U|=m",font_size=28).move_to(U.copy().shift(DOWN*0.6+LEFT*0.5))
        self.play(Write(U))
        self.wait()
        self.play(Write(U_sz))
        self.wait()
        self.play(Circumscribe(B))
        self.wait()
        self.play(Wiggle(U))
        U_S=MathTex(r"A_{l+1}/S,\dots,A_{n}/S").move_to(RIGHT*3.5+DOWN*3)
        tmp=B[2].copy()
        self.play(Transform(tmp,MathTex(r"\{2\}").move_to(B[2].get_center()+DOWN*1.5)),
                  Write(U_S))
        self.wait()
        x_2=tmp.copy()
        self.play(Transform(x_2,MathTex(r"2").move_to(tmp.get_center()+DOWN*1.5)))
        self.wait()
        X=VGroup(x_1,x_2)
        self.play(Transform(X,MathTex(r"1,4,3,2").move_to(RIGHT*3.5+DOWN*1.5)))
        self.wait()

class Lemma1(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E

        """
        Lemma1_title=Tex(r"$\mathbf{Lemma\ 1.}$")
        Lemma1=Tex(r"任何一个$\mathit{(r\times n)-}$拉丁方都能\\被填充为一个$\mathit{((r+1)\times n)-}$拉丁方",
                       tex_template=TexTemplateLibrary.ctex,font_size=38)
        Lemma1_title.move_to(LEFT*3+UP*1.5)
        self.play(Write(Lemma1),Write(Lemma1_title))
        """

        LS=LatinSquare(n=5)
        tmp=[[1,4,2,5,3],[4,2,5,3,1],[2,5,3,1,4]] #[5,3,1,4,2]
        for i in range(3):
            for j in range(5):
                LS.fill(x=i+1,y=j+1,element=tmp[i][j])
        self.play(Create(LS))
        self.wait()
        self.play(Circumscribe(VGroup(*[LS[i] for i in range(15)])))
        self.play(Circumscribe(VGroup(*[LS[i] for i in range(15,20)])))
        self.wait()
        tmp=Text("")
        self.play(Transform(tmp,Text("3").move_to(DOWN*3),run_time=1))
        self.play(Transform(tmp,Text("2").move_to(DOWN*3),run_time=1))
        self.play(Transform(tmp,Text("1").move_to(DOWN*3),run_time=1))
        self.play(FadeOut(tmp))
        self.wait()

        self.play(LS.animate.shift(LEFT*3))
        A_1=MathTex("A_1=\{3,5\}")
        A_2=MathTex("A_2=\{1,3\}")
        A_3=MathTex("A_3=\{1,4\}")
        A_4=MathTex("A_4=\{2,4\}")
        A_5=MathTex("A_5=\{2,5\}")
        A=VGroup(A_1,A_2,A_3,A_4,A_5).arrange(direction=DOWN).scale(0.8).shift(RIGHT*2)
        self.play(Write(A))
        self.wait()

        H=MathTex(r"\forall m\in[1,n],|A_{i_1} \cup \dots \cup A_{i_m}| \geq m \quad \quad(H)").scale(0.7).shift(RIGHT*3.5+UP*2)
        self.play(Write(H))
        self.wait()

        self.play(Circumscribe(A))
        self.wait()
        m=MathTex("m").move_to(A_5.get_center()+DOWN*1.5)
        M=MathTex("2*m").move_to(m.get_center()+RIGHT*3)
        self.play(Write(m),
                  Transform(A.copy(),MathTex("B").move_to(A.get_center()+RIGHT*2)))
        self.wait()
        self.play(FadeIn(M,shift=LEFT))
        self.wait()
        self.play(Wiggle(H))
        self.wait()
        self.play(Transform(M,MathTex(r"\frac{2m}{2}\geq m").move_to(M.get_center())))
        self.wait()
        self.play(FadeOut(VGroup(LS,H,A,m,M)))
        self.wait()

class Lemma2(Scene):
    def construct(self):
        self.camera.background_color=GREY_E
        T1=Tex(r"一个至多已经填好 $n-1$ 个格子，且至多包含 $\frac{n}{2}$ 种不同元素的 $n$ 阶部分拉丁方一定能被填完整",
               tex_template=TexTemplateLibrary.ctex,font_size=28)
        self.play(Write(T1))
        self.wait()
        self.play(FadeOut(T1,shift=UP))
        Ls1=LatinSquare(n=4)
        Ls1.fill(x=1,y=1,element=2)
        Ls1.fill(x=2,y=4,element=3)
        Ls1.fill(x=3,y=2,element=3)
        self.play(Create(Ls1))
        self.wait()
        Ls2=LatinSquare(n=4)
        Ls2.fill(x=2,y=1,element=1)
        Ls2.fill(x=3,y=2,element=3)
        Ls2.fill(x=3,y=4,element=2)
        self.play(Transform(Ls1,Ls2))
        self.wait()
        self.play(Circumscribe(VGroup(*[Ls1[i] for i in range(4,12)])))
        self.wait()
        self.play(Ls1.txt[3][2].animate.shift(UP*2),
                  Ls1.txt[3][4].animate.shift(UP*2))
        self.wait()
        tmp=VGroup(
            MathTex(r"r\leq \frac{n}{2}"),
            MathTex(r"f_1+f_2+\dots+f_r<n"),
            MathTex(r"f_1\geq f_2\geq \dots \geq f_r")
        ).arrange(direction=DOWN).shift(RIGHT*3)
        self.play(Ls1.animate.shift(LEFT*3))
        self.wait()
        for i in tmp:
            self.play(Write(i))
            self.wait()
        self.play(Unwrite(tmp))
        Ls2=LatinSquare(n=4)
        tmp=[[4,3,1,2],[1,2,3,4],[2,1,4,3],[3,4,2,1]]
        for i in range(2):
            for j in range(4):
                Ls2.fill(x=i+1,y=j+1,element=tmp[i][j])
        self.play(Transform(Ls1,Ls2))
        self.wait()
        txt=VGroup()
        for j in range(4):
            txt+=Ls1.fill(x=3,y=j+1,element=tmp[1][j])
        self.play(FadeIn(txt))
        txt=VGroup()
        for j in range(4):
            txt+=Ls1.fill(x=4,y=j+1,element=tmp[2][j])
        self.play(FadeIn(txt))
        self.wait()
        self.play(Uncreate(Ls1))
        self.wait()
        


# manim -ps LatinSquare.py
# manim -pql LatinSquare.py
# manim -qh LatinSquare.py