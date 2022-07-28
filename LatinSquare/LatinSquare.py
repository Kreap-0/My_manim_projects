from manim import *

class LatinSquare(VGroup):
    def __init__(self,n,*vmobjects,**kwargs):
        super().__init__(*vmobjects,**kwargs)
        self.n=n
        self.txt,self.e=[0],[[0]*(n+1)]*(n+1)
        self.L,self.C=[0],[0]
        x,y=0,0
        if (n%2)==0:
            x,y=-(n/2)+0.5,(n/2)-0.5
        else:
            x,y=-((n-1)/2),((n-1)/2)
        for i in range(n):
            for j in range(n):
                s=Square(side_length=1).move_to([x+j,y-i,0])
                s.set_stroke(color=GREY_E)
                s.set_fill(color=GREY_D,opacity=1)
                self+=s
        for i in range(n):
            ro=[0]
            for j in range(n):
                txt_tmp=Text("")
                ro.append(txt_tmp)
                self+=txt_tmp
            self.txt.append(ro)
    def build(self):
        for i in range(self.n):
            self.L.append(VGroup())
            self.C.append(VGroup())
        for i in range(self.n):
            for j in range(self.n):
                self.L[i+1].add(self.txt[i+1][j+1])
                self.C[j+1].add(self.txt[i+1][j+1])
    def fill(self,x,y,e,txt_color=GREY_B):
        if e==0:
            self.e[x][y]=0
            self.txt[x][y]=Text("")
            return self.txt[x][y]
        else:
            tmp=Text(str(e),color=txt_color).move_to(self[(x-1)*self.n+y-1].get_center())
            self.e[x][y]=e
            self.txt[x][y].become(tmp)
            return self.txt[x][y]

class Main1(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        self.camera.frame.scale(0.8)
        
        self.wait()
        LS1=LatinSquare(4)
        tmp=[[1,2,3,4],[2,1,4,3],[4,3,1,2],[3,4,2,1]]
        for i in range(4):
            for j in range(4):
                LS1.fill(i+1,j+1,tmp[i][j])
        self.play(Create(LS1),run_time=3)
        self.wait()
        
        A1=Arrow(start=np.array([-1.7,2.5,0]),end=np.array([1.7,2.5,0]),color=BLUE)
        self.play(GrowArrow(A1))
        A2=Arrow(start=np.array([-2.5,1.7,0]),end=np.array([-2.5,-1.7,0]),color=BLUE)
        self.play(GrowArrow(A2))

        self.wait()
        self.play(Uncreate(LS1),Uncreate(A1),Uncreate(A2))
        self.wait()

        LS2=LatinSquare(4)
        tmp=[[0,0,1,3],[3,0,0,0],[4,0,0,2],[3,0,4,0]]
        for i in range(4):
            for j in range(4):
                LS2.fill(i+1,j+1,tmp[i][j])
        LS2.shift(LEFT*6)

        LS3=LatinSquare(5)
        tmp=[[1,4,2,5,3],[4,2,5,3,1],[2,5,3,1,4],[5,3,1,4,2]]
        for i in range(4):
            for j in range(5):
                LS3.fill(i+1,j+1,tmp[i][j])

        LS4=LatinSquare(5)
        tmp=[[1,2,3,4,0],[0,0,0,0,5]]
        for i in range(2):
            for j in range(5):
                LS4.fill(i+1,j+1,tmp[i][j])
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
            self.play(Write(LS3.fill(5,i+1,tmp[i])),run_time=0.5)
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
        s=Text("Sufficient!").move_to(cd.copy().shift(DOWN*2))
        self.play(FadeIn(s),shift=DOWN)
        self.wait()
        self.play(FadeOut(VGroup(LS4_,cd,s)))
        self.wait()

class Process(Scene):
    def construct(self):
        self.camera.background_color=GREY_E
        n1=Text("P.Hall",font_size=32).move_to(LEFT*5)
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
                LS1.fill(i+1,j+1,tmp[i][j])
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

        LS1_=LatinSquare(3)
        tmp=[[1,2,3],[2,3,1],[3,1,2]]
        for i in range(3):
            for j in range(3):
                LS1_.fill(i+1,j+1,tmp[i][j])
        LS1_.move_to(LEFT*3)
        self.play(Transform(LS1,LS1_))
        self.wait()
        self.play(Uncreate(LS1),FadeOut(VGroup(RG,CG,EG)))
        self.wait()

class Hall_intro(Scene):
    def construct(self):
        self.camera.background_color=GREY_E
        X=MathTex(r"X").move_to(UP*2)
        A=X.copy()
        self.wait()
        self.play(Write(X))
        self.wait()
        self.play(Transform(A,MathTex(r"A_1",r'\ ',r"A_2",r'\ ',r"A_3",r'\ ',r"\dots",r'\ ',r"A_n")))
        self.wait()
        x=MathTex(r"x_1",r'\ ',r"x_2",r'\ ',r"x_3",r'\ ',r"\dots",r'\ ',r"x_n").move_to(DOWN*2)
        self.play(FadeIn(x,shift=DOWN))
        self.wait()
        x_=MathTex(r"{{x_1}}\neq {{x_2}}\neq {{x_3}}\neq {{\dots}} \neq {{x_n}}").move_to(DOWN*2)
        self.play(TransformMatchingTex(x,x_))
        self.wait()
        self.play(FadeOut(x_),FadeOut(X))

        girl,boy,mline=VGroup(),VGroup(),VGroup()
        for i in range(4):
            tmp=Circle(radius=0.3,color=PINK).move_to(LEFT*3+(1.5-i)*UP*1.2).set_fill(PINK,1)
            girl.add(tmp)
        for i in range(4):
            tmp=Circle(radius=0.3,color=BLUE).move_to(RIGHT*3+(1.5-i)*UP*1.2).set_fill(BLUE,1)
            boy.add(tmp)
        B=A.copy()
        self.remove(A)
        tmp=[0,2,4,8]
        self.play(FadeIn(girl),
                  AnimationGroup(*[B[tmp[i]].animate.move_to(girl[i].get_center()+LEFT) for i in range(4)]))
        for i in tmp:
            girl+=B[i]
        self.wait()
        tmp=[[0,2],[0,1],[3],[0,3]]
        for i in range(4):
            for j in tmp[i]:
                l=Line(start=girl[i].get_center(),end=boy[j].get_center())
                mline.add(l)
        self.play(FadeIn(boy),Create(mline))
        self.wait()
        for i in [1,3,4,5]:
            self.wait(0.5)
            mline[i].become(mline[i].copy().set_color(color=BLUE))
        self.wait()
        self.play(FadeOut(VGroup(mline,boy,girl)))
        self.wait()

        H=MathTex(r"\forall m\in[1,n],|A_{i_1} \cup A_{i_2} \cup \dots \cup A_{i_m}| \geq m")
        self.play(Write(H))
        self.wait()
        self.play(Unwrite(H),run_time=1)
        self.wait()

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
                self.play(Write(j),run_time=0.2)

        tmp=[H[2],H[6],V2[0],V2[2]]
        self.play(*[Transform(i,i.copy().set_color(color=BLUE)) for i in tmp])
        self.wait()
        self.play(Circumscribe(H[2]),Circumscribe(H[6]))
        self.wait()
        self.play(Circumscribe(V2[2]))
        self.wait()

        tmp=[1,2,3,4]
        for i in range(4):
            x=Text(str(tmp[i]),font_size=32).move_to(H[2*i].get_center()+DOWN)
            V1+=x
            self.play(FadeIn(x,shift=DOWN),run_time=0.5)
        self.wait()
        self.play(FadeOut(VGroup(H,V1,V2,V3,V4)))
        self.wait()
    
class Hall_prove(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        A=MathTex(r"\{1,2\}\quad \{1\}").move_to(UP)
        self.play(Write(A))
        X=A.copy()
        self.play(Transform(X,MathTex(r"\{1\}").move_to(DOWN)))
        self.play(Wiggle(X))
        self.play(Unwrite(VGroup(A,X)))
        self.wait()

        Case1=Text("Case 1").move_to(5*LEFT+3*UP)
        Case2=Text("Case 2").move_to(5*LEFT+3*UP)
        self.play(Write(Case1))
        self.wait()

        A=MathTex(r"\{",r"1",r",3\},\{",r"1",r",2\},\{2,3,4\},\{",r"1",r",4\}").move_to(UP*1.5)
        self.play(Write(A))
        self.wait()
        self.play(Transform(A[5],A[5].copy().set_color(color=BLUE)))
        self.play(Transform(A[1],A[1].copy().set_color(color=BLUE)),
                  Transform(A[3],A[3].copy().set_color(color=BLUE)))
        self.wait()
        A_=MathTex(r"\{3\},\{2\},\{2,3,4\}")
        self.play(FadeIn(A_,shift=DOWN))
        self.wait()
        x=A_.copy()
        self.play(Transform(x,MathTex(r"{{3,2,4}}").move_to(DOWN*1.5)))
        self.wait()
        x_=MathTex(r"{{3,2,4}},1").move_to(DOWN*1.5)
        self.play(TransformMatchingTex(x,x_))
        self.wait()
        self.play(Unwrite(VGroup(A,A_,x_)))
        
        self.play(Transform(Case1,Case2))
        B=MathTex(r"\{1,3\}",",",r"\{1,2\}",",",r"\{3,4\}",",",r"\{1,4\}",",",r"\{2,5\}").move_to(UP*1.5)
        self.play(Write(B))
        self.wait()
        self.play(*[B[i].animate.set_color(color=BLUE) for i in [0,4,6]])
        self.wait()
        self.play(B[2].animate.move_to(B[6]),
                  B[6].animate.move_to(B[2]))
        self.wait()
        S=MathTex("S").next_to(B[0],LEFT)
        S_sz=MathTex("|S|=l(=3)",font_size=28).move_to(S.copy().shift(DOWN*0.7))
        self.play(Write(S))
        self.wait()
        self.play(Write(S_sz))
        self.wait()
        x_1=VGroup(*[B[i].copy() for i in [0,4,6]])
        self.play(Transform(x_1,MathTex(r"1,4,3").move_to(DOWN*1.5)))
        self.wait()
        self.play(B[2].animate.set_color(color=YELLOW))
        U=MathTex(r"U").next_to(B[8],RIGHT)
        U_sz=MathTex("|U|=m(=1)",font_size=28).move_to(U.copy().shift(DOWN*0.7))
        self.play(Write(U))
        self.wait()
        self.play(Write(U_sz))
        self.wait()
        self.play(Circumscribe(B))
        self.wait()
        self.play(Wiggle(U))
        U_S=MathTex(r"A_{l+1}/S,\dots,A_{n}/S").move_to(LEFT*4+DOWN*1)
        tmp,tmp2=B[2].copy(),B[8].copy()
        self.play(Transform(tmp,MathTex(r"\{2\}").move_to(B[2].get_center()+DOWN*1.5)),
                  Transform(tmp2,MathTex(r"\{5\}").move_to(B[8].get_center()+DOWN*1.5)),
                  Write(U_S))
        self.wait()
        x_2,x_5=tmp.copy(),tmp2.copy()
        self.play(Transform(x_2,MathTex(r"2").move_to(tmp.get_center()+DOWN*1.5)),
                  Transform(x_5,MathTex(r"5").move_to(tmp2.get_center()+DOWN*1.5)))
        self.wait()
        X=VGroup(x_1,x_2,x_5)
        self.play(TransformMatchingShapes(X,MathTex(r"1,4,3,2,5").move_to(DOWN*1.5)))
        self.wait()
        self.play(self.camera.frame.animate.shift(DOWN*10))

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

        LS=LatinSquare(5)
        tmp=[[1,4,2,5,3],[4,2,5,3,1],[2,5,3,1,4]] #[5,3,1,4,2]
        for i in range(3):
            for j in range(5):
                LS.fill(i+1,j+1,tmp[i][j])
        self.play(Create(LS))
        self.wait()
        self.play(Circumscribe(VGroup(*[LS[i] for i in range(15)])))
        self.wait(0.5)
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
        B=MathTex("B").move_to(A.get_center()+RIGHT*2)
        self.play(Write(m),
                  Transform(A.copy(),B,replace_mobject_with_target_in_scene=1))
        self.wait()
        self.play(FadeIn(M,shift=LEFT))
        self.wait()
        self.play(Wiggle(H))
        self.wait()
        self.play(Transform(M,MathTex(r"\frac{2m}{2}\geq m").move_to(M.get_center())))
        self.wait()
        self.play(FadeOut(VGroup(LS,H,A,m,M,B)))
        self.wait()

class Lemma2_1(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        T1=Tex(r"一个至多已经填好 $n-1$ 个格子，且至多包含 $\frac{n}{2}$ 种不同元素的 $n$ 阶部分拉丁方一定能被填完整",
               tex_template=TexTemplateLibrary.ctex,font_size=28)
        self.play(Write(T1))
        self.wait()
        self.play(FadeOut(T1,shift=UP))
        Ls1=LatinSquare(4)
        Ls1.fill(1,1,2)
        Ls1.fill(2,4,3)
        Ls1.fill(3,2,3)
        self.play(Create(Ls1))
        self.wait()
        self.play(FadeOut(VGroup(Ls1.txt[1][1],Ls1.txt[2][4])),
                  FadeIn(VGroup(Ls1.fill(2,1,1),Ls1.fill(3,4,2))))
        self.wait()
        self.play(Ls1.txt[3][2].animate.shift(UP*2),
                  Ls1.txt[3][4].animate.shift(UP*2))
        self.wait()
        Ls=LatinSquare(4)
        Ls.fill(1,2,3)
        Ls.fill(1,4,2)
        Ls.fill(2,1,1)
        Ls1.become(Ls)
        self.wait()
        tmp=VGroup(
            MathTex(r"r\leq \frac{n}{2}"),
            MathTex(r"f_1+f_2+\dots+f_r<n"),
            MathTex(r"f_1\geq f_2\geq \dots \geq f_r")
        ).arrange(direction=DOWN).shift(RIGHT*3)
        self.play(Ls1.animate.shift(LEFT*3))
        self.wait()
        self.play(Write(tmp[0]),
                  Circumscribe(VGroup(*[Ls1[i] for i in range(8)])))
        self.wait()
        self.play(Write(tmp[1]))
        self.wait()
        self.play(Write(tmp[2]))
        self.wait()
        self.play(Unwrite(tmp,run_time=0.8))
        self.play(Ls1.animate.shift(RIGHT*3))
        Ls2=LatinSquare(n=4)
        Ls2.fill(1,2,3)
        Ls2.fill(1,4,2)
        Ls2.fill(2,1,1)
        self.add(Ls2)
        self.remove(Ls1)
        self.wait()
        tmp=[[4,3,1,2],[1,2,3,4],[2,1,4,3],[3,4,2,1]]
        self.play(Write(VGroup(Ls2.fill(1,1,4),Ls2.fill(1,3,1))))
        self.play(Write(VGroup(*[Ls2.fill(2,i+1,tmp[1][i]) for i in range(1,4)])))
        self.wait()
        self.play(Write(VGroup(*[Ls2.fill(3,i+1,tmp[2][i]) for i in range(4)])))
        self.play(Write(VGroup(*[Ls2.fill(4,i+1,tmp[3][i]) for i in range(4)])))
        self.wait()
        self.play(Uncreate(Ls2))
        self.wait()

class Lemma2_2(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        Ls=LatinSquare(8).shift(DOWN)
        tmp=[[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,1],[0,0,0,0,0,0,1,2],[0,5,0,0,0,0,0,0]]
        for i in range(4):
            for j in range(8):
                Ls.fill(i+1,j+1,tmp[i][j])
        tmp=[2,6,11,13,22,23,25]
        for i in tmp:
            Ls[i].set_fill(color=GREY_C)
        self.play(FadeIn(Ls,shift=UP))
        f,num=VGroup(),[2,2,2,1]
        for i in range(4):
            tmp=MathTex(r"f_"+str(i+1)+r"="+str(num[i])).next_to(Ls[8*i+7],RIGHT)
            f+=tmp
        self.play(Write(f))
        self.wait()
        X=MathTex("X").next_to(Ls[8*2],LEFT)
        Em=VGroup(*[Ls[i] for i in range(16,22)])
        self.play(Write(X))
        self.wait()
        A=VGroup()
        for i in range(6):
            tmp=MathTex(r"A_"+str(i+1)).next_to(Ls[i],UP)
            A+=tmp
        self.play(Write(A))
        self.wait()
        self.play(Circumscribe(Em))
        self.wait()
        R1=SurroundingRectangle(VGroup(*[Ls[8*i+1] for i in range(8)]))
        R2=SurroundingRectangle(VGroup(*[Ls[8*i+3] for i in range(8)])+
                                VGroup(*[Ls[8*i+4] for i in range(8)]))
        self.play(Create(VGroup(R1,R2)))
        self.wait()
        self.play(self.camera.frame.animate.shift(UP*2.5))
        self.wait()
        F1=MathTex(r"m(n-f_l-|B|)",r"\leq",r"c",r"\leq (l-1)\times m",r"+f_{l+1}+\dots+f_{r}").move_to(UP*5)
        self.play(Write(F1[2]))
        self.wait()
        R3=SurroundingRectangle(VGroup(*[Ls[i] for i in range(16)]),color=BLUE)
        R4=SurroundingRectangle(VGroup(*[Ls[i] for i in range(24,32)]),color=BLUE)
        self.play(Create(R3),Write(F1[3]))
        self.wait(0.6)
        self.play(Create(R4),Indicate(f[3]),Write(F1[4]))
        self.wait()
        self.play(Write(VGroup(F1[1],F1[0])),FadeOut(VGroup(R3,R4)))
        self.wait()
        F2=MathTex(r"|B|\geq n-f_l-(l-1)-\frac{1}{m}(f_{l+1}+\dots+f_r)",r">m-1").next_to(F1,DOWN)
        self.play(FadeIn(F2[0],shift=DOWN),VGroup(Ls,A,X,f,R1,R2).animate.shift(DOWN))
        self.wait(0.5)
        self.play(Write(F2[1]))
        self.wait()
        F3=MathTex(r"m({{n-f_l-}}{{l}}+2-m){{>f_{l+1}+\dots+f_r}}",
                   substrings_to_isolate="m").next_to(F2,DOWN)
        self.play(self.camera.frame.animate.shift(DOWN),
                  VGroup(Ls,A,X,R1,R2,f,F1).animate.shift(DOWN*10),
                  Write(F3))
        self.wait()
        ax=Axes(
            x_range=[0,10,10],
            y_range=[0,25,25],
            axis_config={"include_tip": False}
        )
        ax_labels=ax.get_axis_labels(x_label="m",y_label="f(m)")
        g=ax.plot(lambda x:x*(10-x),color=BLUE,x_range=[0,10])
        G=VGroup(ax,ax_labels,g).scale(0.6)
        self.play(Transform(F3,F3.copy().set_color_by_tex("m",ORANGE)),
                  Create(G),
                  run_time=2)
        self.wait()
        D1=Dot(ax.i2gp(1,g))
        D2=Dot(ax.i2gp(9,g))
        d_labels=VGroup(
            MathTex(r"m=1",font_size=28).next_to(D1,DR*0.5),
            MathTex(r"m=n-f_l-l+1",font_size=28).next_to(D2,DR*0.5)
        )
        self.play(Create(VGroup(D1,D2)))
        self.play(FadeIn(d_labels,shift=UP))
        F5=MathTex(r"{{n-f_l-}}{{l}}{{+1}}{{>f_{l+1}+\dots+f_r}}").move_to(F3)
        self.play(TransformMatchingTex(F3,F5))
        self.wait()
        D3=D1.copy()
        self.play(MoveAlongPath(D3,
                                ax.plot(lambda x:x*(10-x),color=BLUE,x_range=[1,9])))
        self.wait()
        F5_=MathTex(r"{{n-f_l-}}{{l}}{{+1}}{{>f_{l+1}+\dots+f_r}}+l-1").move_to(F3)
        self.play(TransformMatchingTex(F5,F5_))
        self.wait()
        self.play(FadeOut(VGroup(G,D1,D2,D3,d_labels),shift=DOWN),
                  FadeOut(F2,shift=UP))
        self.wait()
        F6=MathTex(r"{{n}}-{{f_l}}{{-1+1}}{{>}}{{f_{l+1}+\dots+f_r}}+1-1").next_to(F3,DOWN)
        F7=MathTex(r"{{n}}{{>}}{{f_l}}+{{f_{l+1}+\dots+f_r}}").move_to(F6)
        self.play(FadeIn(F6,shift=DOWN))
        self.wait()
        self.play(TransformMatchingTex(F6,F7))
        self.wait()
        F8=MathTex(r"{{n}}{{>}}f_1{{+}}f_2{{+}}f_3{{+\dots}}+{{f_l}}{{+\dots+f_r}}").next_to(F6,DOWN)
        self.play(FadeIn(F8,shift=DOWN*2))
        self.wait()
        F9=MathTex(r"{{n}}{{>}}f_{l-1}{{+}}f_{l-1}{{+}}f_{l-1}{{+\dots}}+{{f_l}}{{+\dots+f_r}}").move_to(F8)
        self.play(TransformMatchingTex(F8,F9))
        self.wait()
        F10=MathTex(r"{{n}}{{>}}(l-1)f_{l-1}+{{f_l}}{{+\dots+f_r}}").move_to(F8)
        self.play(TransformMatchingTex(F9,F10))
        self.wait()
        F11=MathTex(r"{{n}}-{{f_l}}-l+1{{>}}l-1+f_{l+1}{{+\dots+f_r}}").move_to(F8)
        self.play(TransformMatchingTex(F10,F11))
        self.wait()
        F12=MathTex(r"{{n}}{{>}}2(l-1)+",r"1+\dots+1").move_to(F8)
        self.play(TransformMatchingTex(F11,F12))
        self.wait()
        br=Brace(F12[1]).shift(RIGHT*3.5)
        br_txt=br.get_tex(r"r-l+1")
        self.play(Create(br),Write(br_txt))
        self.wait()
        F13=MathTex(r"{{n}}{{>}}r+l-1").move_to(F8)
        self.play(TransformMatchingTex(F12,F13),
                  FadeOut(VGroup(br,br_txt)))
        self.wait()
        self.play(FadeOut(VGroup(F13,F7),shift=UP),
                  VGroup(Ls,A,X,R1,R2,f).animate.shift(UP*10),
                  F5_.animate.shift(UP))
        self.wait()
        F5=MathTex(r"{{n-f_l-}}{{l}}{{+1}}>",r"{{f_{l+1}+\dots+f_r}}+l-1").move_to(F5_)
        self.play(TransformMatchingTex(F5_,F5))
        R3=SurroundingRectangle(VGroup(F5[4],F5[5]))
        self.play(Circumscribe(VGroup(*[Ls[i] for i in range(16)]),color=BLUE),
                  Create(R3))
        self.wait()
        self.play(Circumscribe(VGroup(*[Ls[i] for i in range(24,32)]),color=BLUE))
        self.play(FadeOut(R3))
        self.wait()
        Line_=VGroup()
        st,ed,co=[4,0,3,8,1,24],[4+8*7,7,3+8*7,15,1+7*8,31],[ORANGE,ORANGE,GREEN,GREEN,PINK,PINK]
        for i in range(6):
            Line_.add(Line(start=Ls[st[i]].get_center(),end=Ls[ed[i]].get_center(),color=co[i]))
        self.play(Create(Line_))
        self.wait()
        F14=MathTex(r"m>{{n-f_l-}}{{l}}{{+1}}>{{f_{l+1}+\dots+f_r}}+l-1").move_to(F5)
        self.play(TransformMatchingTex(F5,F14))
        self.wait()
        F15=MathTex(r"|B|=|X|=n-f_l\geq m").move_to(F14)
        self.play(Transform(F14,F15))
        self.wait()
        self.play(FadeOut(VGroup(Ls,A,X,R1,R2,f,Line_),shift=DOWN),
                  FadeOut(VGroup(F14),shift=UP))
        self.wait()

class Lemma3_1(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        Ls=LatinSquare(7)
        Ls.fill(2,2,2)
        Ls.fill(2,5,7)
        Ls.fill(3,3,5)
        Ls.fill(3,5,4)
        Ls.fill(5,4,5)
        Ls.fill(7,2,4)
        tmp,num=[1,2,4,6],[2,2,1,1]
        s_label=VGroup(*[MathTex(r"s_"+str(i+1)).next_to(Ls[tmp[i]*7],LEFT) for i in range(4)])
        f_label=VGroup(*[MathTex(r"f_"+str(i+1)+r"="+str(num[i])).next_to(Ls[tmp[i]*7+6],RIGHT) for i in range(4)])
        self.play(FadeIn(Ls),Write(s_label),Write(f_label))
        self.wait()
        basket=VGroup(
            Line(start=[-1,np.sqrt(3)/3,0],end=LEFT*0.5),
            Line(start=LEFT*0.5,end=RIGHT*0.5),
            Line(start=RIGHT*0.5,end=[1,np.sqrt(3)/3,0]),
            Dot().shift(UP*0.23+LEFT*0.24).scale(3),
            Dot().shift(UP*0.23+RIGHT*0.24).scale(3)
        )
        b=VGroup(*[basket.copy() for _ in range(4)]).arrange_submobjects().shift(UP*4.5)
        tmp=b[0][4].copy()
        b[0]-=b[0][4]
        self.play(*[Create(b[i]) for i in range(4)],
                  self.camera.frame.animate.shift(UP*2.5))
        self.wait()
        tmp_=b[1][4].copy()
        self.play(Transform(b[1][4],tmp,path_arc=PI))
        self.play(Transform(b[3][4],tmp_,path_arc=PI))
        self.wait()
        self.play(FadeOut(b,shift=UP),
                  self.camera.frame.animate.shift(DOWN*2.5))
        self.wait()
        self.play(Indicate(Ls.txt[2][5]))
        self.play(Indicate(s_label[0]))
        self.wait()
        self.play(Indicate(s_label[0]))
        self.play(Indicate(f_label[0]))
        self.wait()
        Ls.build()
        self.play(Ls.C[2].animate.shift(LEFT))
        self.play(Ls.C[5].animate.shift(LEFT*3))
        self.wait()
        self.play(VGroup(Ls.L[3],s_label[1],f_label[1]).animate.shift(DOWN*2),
                  VGroup(Ls.L[5],s_label[2],f_label[2]).animate.shift(UP*2))
        self.wait()
        self.play(VGroup(Ls.L[5],s_label[2],f_label[2]).animate.shift(DOWN*3))
        self.wait()
        self.play(FadeOut(VGroup(s_label,f_label)),
                  *[Uncreate(Ls[i]) for i in range(7)],
                  *[Uncreate(Ls[7*i+6]) for i in range(1,7)],
                  FadeOut(Ls.txt[2][5]))
        Ls1=LatinSquare(6).shift(DL*0.5)
        Ls1.fill(1,1,2)
        Ls1.fill(4,2,4)
        Ls1.fill(4,3,5)
        Ls1.fill(5,4,5)
        Ls1.fill(6,1,4)
        self.add(Ls1)
        self.play(FadeOut(Ls,run_time=0))
        self.play(Ls1.animate.shift(UR*0.5))
        self.wait()
        tmp=[[2,3,4,1,6,5],[5,6,1,4,2,3],[1,2,3,6,5,4],[6,4,5,2,3,1],[3,1,6,5,4,2],[4,5,2,3,1,6]]
        self.play(*[Write(Ls1.fill(1,i+1,tmp[0][i])) for i in range(1,6)],
                  *[Write(Ls1.fill(2,i+1,tmp[1][i])) for i in range(6)],
                  *[Write(Ls1.fill(3,i+1,tmp[2][i])) for i in range(6)],
                  *[Write(Ls1.fill(4,i+1,tmp[3][i])) for i in [0]+list(range(3,6))],
                  *[Write(Ls1.fill(5,i+1,tmp[4][i])) for i in [0,1,2,4,5]],
                  *[Write(Ls1.fill(6,i+1,tmp[5][i])) for i in range(1,6)])
        self.wait()
        mv=[RIGHT]*6+[DOWN]*6
        sq=VGroup(Ls1[0].copy().shift(UP))
        for i in range(12):
            sq.add(sq[i].copy().shift(mv[i]))
        self.play(Create(sq))
        Ls1.add(sq)
        self.play(Ls1.animate.shift(DL*0.5))
        self.wait()

# manim -pqh LatinSquare.py Lemma3_2
# manim -ps LatinSquare.py Lemma3_2
class Lemma3_2(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        tmp=[[2,3,4,1,6,5],[5,6,1,4,2,3],[1,2,3,6,5,4],[6,4,5,2,3,1],[3,1,6,5,4,2],[4,5,2,3,1,6]]
        Ls=LatinSquare(7)
        for i in range(1,7):
            for j in range(6):
                Ls.fill(i+1,j+1,tmp[i-1][j])
        self.add(Ls)
        self.wait()
        self.play(*[Ls.txt[i][i].animate.shift((7-i)*RIGHT) for i in range(2,7)])
        tmp=VGroup(*[Text("7",color=GREY_B).move_to(Ls[i*7+i-8]) for i in range(2,8)])
        self.play(*[Write(tmp[i]) for i in range(6)])
        self.wait()
        self.play(Circumscribe(Ls.txt[2][2]),Circumscribe(Ls.txt[5][5]))
        self.wait()
        self.play(*[Unwrite(tmp[i]) for i in range(6)])
        self.play(*[Ls.txt[i][i].animate.shift((7-i)*LEFT) for i in range(2,7)])
        self.wait()
        self.play(Write(Ls.fill(2,7,7)))
        self.play(Ls.txt[2][7].animate.shift(LEFT*5),
                  Ls.txt[2][2].animate.shift(RIGHT*5))
        self.wait()
        self.play(Write(Ls.fill(3,7,7)))
        self.play(Ls.txt[3][7].animate.shift(LEFT*4),
                  Ls.txt[3][3].animate.shift(RIGHT*4))
        self.wait()
        self.play(Write(Ls.fill(4,7,7),run_time=0.4))
        self.play(Ls.txt[4][7].animate(run_time=0.4).shift(LEFT*3),
                  Ls.txt[4][4].animate(run_time=0.4).shift(RIGHT*3))
        self.play(Write(Ls.fill(5,7,7),run_time=0.4))
        self.play(Ls.txt[5][7].animate(run_time=0.4).shift(LEFT*2),
                  Ls.txt[5][5].animate(run_time=0.4).shift(RIGHT*2))
        self.wait()
        self.play(Indicate(Ls.txt[2][2]),Indicate(Ls.txt[5][5]))
        Ls.build()
        Ls.save_state()
        self.play(Ls.txt[2][5].animate.shift(RIGHT*2),
                  Ls.txt[2][2].animate.shift(LEFT*2))
        self.wait()
        self.play(Ls.txt[4][5].animate.shift(RIGHT*2),
                  Ls.txt[4][4].animate.shift(LEFT*2))
        self.wait()
        L=VGroup(*[Dot(color=GRAY_B).move_to(Ls[i*7+13].get_center()+RIGHT*2) for i in range(4)])
        R=L.copy().shift(RIGHT*1.5)
        mline=VGroup(*[DashedLine(start=L[i],end=R[i]) for i in range(4)],
                     Line(start=L[0],end=R[2]),
                     Line(start=L[3],end=R[0]))
        self.play(self.camera.frame.animate.shift(RIGHT*2),
                  FadeIn(VGroup(L,R),shift=LEFT),
                  Restore(Ls))
        self.wait()
        self.play(*[Create(mline[i]) for i in range(4)])
        self.wait()
        self.play(*[Create(mline[i]) for i in range(4,6)])
        self.wait()
        c=Circle(radius=0.2).move_to(R[3])
        self.play(GrowFromCenter(c))
        self.wait()
        c_=c.copy()
        for target in [L[3],R[0],L[0],R[2],L[2]]:
            self.play(c_.animate.move_to(target))
        self.wait()
        g1=VGroup(c,c_,L,R,mline)
        g2=VGroup(Dot(color=GRAY_B).scale(3),
                 Text("...").shift(1.5*UP),
                 Text("...").shift(1.6*RIGHT),
                 Text("...").shift(1.5*DOWN),
                 Arrow(ORIGIN,UP*1.5,buff=0.2,color=BLUE),
                 Arrow(RIGHT*1.5,ORIGIN,buff=0.2,color=BLUE),
                 Arrow(DOWN*1.5,ORIGIN,buff=0.2,color=BLUE)).move_to(g1.get_center()+DOWN*3).scale(0.6)
        self.play(FadeIn(g2,shift=UP),
                  g1.animate.shift(UP))
        self.wait()
        self.play(FadeOut(VGroup(g1,g2),shift=RIGHT),
                  self.camera.frame.animate.shift(LEFT*2),
                  Ls.txt[2][5].animate.shift(RIGHT*2),
                  Ls.txt[2][2].animate.shift(LEFT*2),
                  Ls.txt[4][5].animate.shift(RIGHT*2),
                  Ls.txt[4][4].animate.shift(LEFT*2)
                )
        self.play(Write(Ls.fill(6,7,7),run_time=0.4))
        self.play(Ls.txt[6][7].animate(run_time=0.4).shift(LEFT),
                  Ls.txt[6][6].animate(run_time=0.4).shift(RIGHT))
        self.play(Write(Ls.fill(7,7,7),run_time=0.4))
        self.wait()
        tmp=[0,7,3,1,6,5,2,4]
        self.play(*[Write(Ls.fill(1,i,tmp[i])) for i in range(1,8)])
        self.wait()

class Lemma3_3(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        Ls=LatinSquare(7)
        tmp=[[7,3,1,6,5,2,4],
             [2,7,4,1,3,5,6],
             [5,6,7,4,2,3,1],
             [1,2,3,7,6,4,5],
             [6,4,5,2,7,1,3],
             [3,1,6,5,4,7,2],
             [4,5,2,3,1,6,7]]
        for i in range(7):
            for j in range(7):
                Ls.fill(i+1,j+1,tmp[i][j])
        self.add(Ls)
        Ls.build()
        self.play(Ls.C[1].animate.shift(RIGHT),
                  Ls.C[2].animate.shift(RIGHT*3),
                  Ls.C[5].animate.shift(LEFT*4))
        self.play(Ls.L[3].animate.shift(DOWN*3),
                  Ls.L[5].animate.shift(UP*2),
                  Ls.L[6].animate.shift(UP))
        self.wait()
        x,y=[2,2,5,5,6,7],[1,2,2,3,4,1]
        self.play(*[Transform(Ls.txt[x[i]][y[i]],
                              Ls.txt[x[i]][y[i]].copy().set_color(BLUE)) for i in range(6)])
        self.wait()
        self.play(self.camera.frame.animate.shift(UP*10))               

# manim -ps LatinSquare.py Test
class Test(Scene):
    def construct(self):
        g=VGroup(Dot(color=GRAY_B).scale(3),
                 Text("...").shift(1.5*UP),
                 Text("...").shift(1.6*RIGHT),
                 Text("...").shift(1.5*DOWN),
                 Arrow(ORIGIN,UP*1.5,buff=0.2,color=BLUE),
                 Arrow(RIGHT*1.5,ORIGIN,buff=0.2,color=BLUE),
                 Arrow(DOWN*1.5,ORIGIN,buff=0.2,color=BLUE)).move_to(RIGHT*4+DOWN*2).scale(0.8)
        self.add(g)

class Cover(Scene):
    def construct(self):
        self.camera.background_color=GREY_E
        Ls=LatinSquare(8)
        tmp=[[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,1],[0,0,0,0,0,0,1,2],[0,5,0,0,0,0,0,0]]
        for i in range(4):
            for j in range(8):
                Ls.fill(i+1,j+1,tmp[i][j])
        tmp=[2,6,11,13,22,23,25]
        for i in tmp:
            Ls[i].set_fill(color=GREY_C)
        R1=SurroundingRectangle(VGroup(*[Ls[8*i+1] for i in range(8)]))
        R2=SurroundingRectangle(VGroup(*[Ls[8*i+3] for i in range(8)])+
                                VGroup(*[Ls[8*i+4] for i in range(8)]))
        A=VGroup(Ls,R1,R2)
        A.scale(0.8).shift(LEFT*3+DOWN)
        self.add(A)

class Simulate1(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        Ls=LatinSquare(4)
        Ls.fill(1,1,2)
        Ls.fill(2,4,3)
        Ls.fill(3,2,3)
        self.play(Create(Ls),run_time=2)
        self.wait(2)
        S=VGroup(MathTex("s_1").next_to(Ls[0],LEFT),
                 MathTex("s_2").next_to(Ls[4],LEFT),
                 MathTex("s_3").next_to(Ls[8],LEFT))
        F=VGroup(MathTex("f_1=1").next_to(Ls[3],RIGHT),
                 MathTex("f_2=1").next_to(Ls[7],RIGHT),
                 MathTex("f_3=1").next_to(Ls[11],RIGHT))
        self.play(FadeIn(S))
        self.wait()
        self.play(FadeIn(F))
        self.wait()
        self.play(FadeOut(VGroup(S,F)))
        self.play(Transform(Ls.txt[1][1],Text("4",color=GREY_B).move_to(Ls[0])))
        self.wait(5)
        self.play(Ls.txt[2][4].animate.shift(DOWN),
                  Ls.txt[3][2].animate.shift(DOWN))
        self.wait()
        self.play(*[Circumscribe(VGroup(*[Ls[j] for j in range(i*5,(i+1)*4)])) for i in range(4)])
        self.wait()
        self.play(Circumscribe(Ls[0]))
        self.wait()
        r1=SurroundingRectangle(VGroup(*[Ls[i*4] for i in range(4)]))
        r2=SurroundingRectangle(VGroup(*[Ls[i] for i in range(4)]))
        self.play(Create(r1),Create(r2))
        self.wait(2)
        self.play(r1.animate.shift(RIGHT*3),
                  r2.animate.shift(DOWN*2))
        self.wait()
        self.play(VGroup(Ls.txt[2][4],r1).animate.shift(LEFT*2),
                  Ls.txt[3][2].animate.shift(RIGHT*2))
        self.wait()
        self.play(r1.animate.shift(RIGHT*2),
                  r2.animate.shift(DOWN))
        self.wait()
        self.play(VGroup(r1,Ls.txt[3][2]).animate.shift(LEFT))
        self.wait()
        self.play(Uncreate(VGroup(r1,r2)))
        Ls2=LatinSquare(3)
        Ls2.fill(2,2,3)
        Ls2.fill(3,3,3)
        self.play(*[Uncreate(Ls[i]) for i in [0,1,2,3,7,11,15]],
                  Unwrite(Ls.txt[1][1]))
        self.play(Ls.animate.shift(UR*0.5))
        self.add(Ls2)
        self.remove(Ls)
        self.wait()
        self.play(Ls2.animate.shift(LEFT*3))
        tmp=[[0,0,0],[0,3,0],[0,0,3]]
        R_txt,C_txt,E_txt=Text("R").move_to(UR),Text("C").move_to(RIGHT),Text("E").move_to(DR)
        self.play(Write(R_txt),Write(C_txt),Write(E_txt))
        RG,CG,EG=VGroup(R_txt),VGroup(C_txt),VGroup(E_txt)
        for i in range(3):
            for j in range(3):
                tmpR=Text(str(i)).move_to(Ls2[i*3+j])
                tmpC=Text(str(j)).move_to(Ls2[i*3+j])
                tmpE=Text(str(tmp[i][j])).move_to(Ls2[i*3+j])
                self.add(tmpR,tmpC,tmpE)
                self.play(tmpR.animate.move_to([1+(i*3+j+1)/2,1,0]),
                          tmpC.animate.move_to([1+(i*3+j+1)/2,0,0]),
                          tmpE.animate.move_to([1+(i*3+j+1)/2,-1,0]),run_time=0.3)
                RG+=tmpR
                CG+=tmpC
                EG+=tmpE
        self.wait()
        self.play((RG-RG[0]).animate.shift(DOWN*2),
                  (EG-EG[0]).animate.shift(UP*2))
        self.wait()
        self.play(FadeOut(Ls2.txt[2][2]),
                  Write(Ls2.fill(3,2,2)))
        Ls3=LatinSquare(3).move_to(Ls2)
        Ls3.fill(3,2,2)
        Ls3.fill(3,3,3)
        Ls2.become(Ls3)
        self.play(Unwrite(VGroup(RG,CG,EG)),run_time=1)
        self.play(Ls2.animate.shift(RIGHT*3))
        self.wait()
        self.play(VGroup(Ls2.txt[3][2],Ls2.txt[3][3]).animate.shift(UP*2))
        self.wait()
        self.play(self.camera.frame.animate.shift(RIGHT*10))
        self.wait()

class Simulate2(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        self.camera.frame.shift(RIGHT*10)
        Ls2=LatinSquare(3)
        Ls2.fill(1,2,2)
        Ls2.fill(1,3,3)
        self.add(Ls2)
        self.play(self.camera.frame.animate.shift(LEFT*10))
        self.wait()
        Ls1=LatinSquare(3)
        Ls1.fill(1,2,2)
        Ls1.fill(1,3,3)
        Ls2.become(Ls1)
        self.play(Write(Ls2.fill(1,1,1)))
        self.wait()
        tmp=[2,3,1]
        self.play(Write(VGroup(*[Ls2.fill(2,i+1,tmp[i]) for i in range(3)])))
        self.wait(0.5)
        tmp=[3,1,2]
        self.play(Write(VGroup(*[Ls2.fill(3,i+1,tmp[i]) for i in range(3)])))
        self.wait()
        self.play(VGroup(*[Ls2.txt[1][i+1] for i in range(3)]).animate.shift(DOWN*2),
                  VGroup(*[Ls2.txt[2][i+1] for i in range(3)]).animate.shift(UP),
                  VGroup(*[Ls2.txt[3][i+1] for i in range(3)]).animate.shift(UP))
        Ls1=LatinSquare(3)
        tmp=[[2,3,1],[3,1,2],[1,2,3]]
        for i in range(3):
            for j in range(3):
                Ls1.fill(i+1,j+1,tmp[i][j])
        Ls2.become(Ls1)
        self.wait()
        x,y,tmp=[1,1,2,2,3,3],[1,2,1,2,1,2],[3,2,1,3,2,1]
        self.play(AnimationGroup(*[
                    Transform(Ls2.txt[x[i]][y[i]],
                              Text(str(tmp[i]),color=GREY_B).move_to(Ls2.txt[x[i]][y[i]]))
                    for i in range(6)
                  ]))
        self.wait()
        
        self.play(Ls2.animate.shift(DL*0.5))
        mv=[RIGHT]*3+[DOWN]*3
        sq=VGroup(Ls2[0].copy().shift(UP))
        for i in range(6):
            sq.add(sq[i].copy().shift(mv[i]))
        self.play(Create(sq))
        Ls2.add(sq)

        Ls=LatinSquare(4)
        tmp=[[0,0,0,0],[3,2,1,0],[1,3,2,0],[2,1,3,0]]
        for i in range(4):
            for j in range(4):
                Ls.fill(i+1,j+1,tmp[i][j])
        self.add(Ls)
        self.remove(Ls2)
        self.wait()
        self.play(Write(Ls.fill(2,4,4)))
        self.play(Ls.txt[2][2].animate.move_to(Ls.txt[2][4]),
                  Ls.txt[2][4].animate.move_to(Ls.txt[2][2]))
        self.wait()
        self.play(Write(Ls.fill(3,4,4)))
        self.play(Ls.txt[3][3].animate.move_to(Ls.txt[3][4]),
                  Ls.txt[3][4].animate.move_to(Ls.txt[3][3]))
        self.wait()
        self.play(Circumscribe(VGroup(Ls[7],Ls[11])))
        self.wait()
        self.play(Ls.txt[2][3].animate.move_to(Ls.txt[2][2]),
                  Ls.txt[2][2].animate.move_to(Ls.txt[2][3]))
        self.wait()
        self.play(Write(Ls.fill(4,4,4)))
        self.wait()
        tmp=[4,2,1,3]
        for i in range(4):
            self.play(Write(Ls.fill(1,i+1,tmp[i]),run_time=0.5))
        self.wait()
        Ls1=LatinSquare(4)
        tmp=[[4,2,1,3],[3,4,2,1],[1,3,4,2],[2,1,3,4]]
        for i in range(4):
            for j in range(4):
                Ls1.fill(i+1,j+1,tmp[i][j])
        self.add(Ls1)
        self.remove(Ls)
        self.wait()
        C2=VGroup(*[Ls1.txt[i][2] for i in range(1,5)])
        C3=VGroup(*[Ls1.txt[i][3] for i in range(1,5)])
        C4=VGroup(*[Ls1.txt[i][4] for i in range(1,5)])
        self.play(C3.animate.move_to(C4),
                  C4.animate.move_to(C3))
        self.play(C3.animate.move_to(C2),
                  C2.animate.move_to(C3))
        self.play(VGroup(*[Ls1.txt[2][i] for i in range(1,5)]).animate.shift(DOWN*2),
                  VGroup(*[Ls1.txt[3][i] for i in range(1,5)]).animate.shift(UP),
                  VGroup(*[Ls1.txt[4][i] for i in range(1,5)]).animate.shift(UP))
        self.wait()
        Ls=LatinSquare(4)
        tmp=[[4,1,3,2],[1,4,2,3],[2,3,4,1],[3,2,1,4]]
        for i in range(4):
            for j in range(4):
                Ls.fill(i+1,j+1,tmp[i][j])
        self.add(Ls)
        self.remove(Ls1)
        self.wait()
        y=[0,4,3,1,2]
        self.play(*[Transform(Ls.txt[i][i],
                              Text("2",color=GREY_B).move_to(Ls.txt[i][i])) for i in range(1,5)],
                  *[Transform(Ls.txt[i][y[i]],
                              Text("4",color=GREY_B).move_to(Ls.txt[i][y[i]])) for i in range(1,5)])
        self.wait()
        self.play(Transform(Ls.txt[1][1],Ls.txt[1][1].copy().set_color(color=BLUE)),
                  Transform(Ls.txt[2][4],Ls.txt[2][4].copy().set_color(color=BLUE)),
                  Transform(Ls.txt[3][2],Ls.txt[3][2].copy().set_color(color=BLUE)))
        self.wait()

class Hungary(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        girl,boy,mline,G,B=VGroup(),VGroup(),VGroup(),VGroup(),VGroup()
        for i in range(4):
            tmp=Circle(radius=0.3,color=PINK).move_to(LEFT*3+(1.5-i)*UP*1.2).set_fill(PINK,1)
            girl.add(tmp)
            tmp_t=MathTex(r"C_"+str(i+1),font_size=28).move_to(tmp)
            G.add(tmp_t)
        for i in range(4):
            tmp=Circle(radius=0.3,color=BLUE).move_to(RIGHT*3+(1.5-i)*UP*1.2).set_fill(BLUE,1)
            boy.add(tmp)
            tmp_t=MathTex(str(i+1),font_size=28).move_to(tmp)
            B.add(tmp_t)
        e=[[0,2],[0,1],[3],[0,3]]
        for i in range(4):
            for j in e[i]:
                l=Line(start=girl[i].get_center(),end=boy[j].get_center())
                mline.add(l)
        self.add(VGroup(girl,boy))
        T=MathTex(r"timer=1").shift(LEFT*5)
        t=VGroup(*[MathTex(r"t_"+str(i+1)+r"=0").next_to(B[i],RIGHT*1.5) for i in range(4)])
        self.wait()
        self.play(Write(G))
        self.play(Write(B))
        self.wait()
        self.play(Create(mline))
        self.wait()
        self.play(Write(VGroup(T,t)))
        self.wait()
        self.play(Flash(mline[0]))
        self.play(Transform(mline[0],mline[0].copy().set_color(color=BLUE)))
        self.wait()
        self.play(Transform(t[0],MathTex(r"t_1=1").move_to(t[0])))   
        self.wait()
        self.play(Transform(T,MathTex(r"timer=2").move_to(T)))
        self.play(Flash(mline[2]))
        self.wait()
        self.play(Transform(t[0],MathTex(r"t_1=2").move_to(t[0])))
        self.play(Transform(mline[0],mline[0].copy().set_color(color=WHITE)),
                  Transform(mline[2],mline[2].copy().set_color(color=BLUE)))
        self.wait()
        self.play(Transform(mline[1],mline[1].copy().set_color(color=BLUE)),
                  Transform(t[2],MathTex(r"t_3=2").move_to(t[2])))
        self.wait()
        self.play(Transform(T,MathTex(r"timer=3").move_to(T)))
        self.wait()
        self.play(Flash(mline[4]))
        self.play(Transform(mline[4],mline[4].copy().set_color(color=BLUE)),
                  Transform(t[3],MathTex(r"t_4=3").move_to(t[3])))
        self.wait()
        self.play(Transform(T,MathTex(r"timer=4").move_to(T)))
        self.wait()
        self.play(Flash(mline[5]))
        self.play(Transform(mline[2],mline[2].copy().set_color(color=WHITE)),
                  Transform(mline[5],mline[5].copy().set_color(color=BLUE)),
                  Transform(t[0],MathTex(r"t_1=4").move_to(t[0])))
        self.wait()
        self.play(Flash(mline[3]))
        self.play(Transform(mline[3],mline[3].copy().set_color(color=BLUE)),
                  Transform(t[1],MathTex(r"t_2=4").move_to(t[1])))
        self.wait()
        self.play(self.camera.frame.animate.shift(LEFT*15))

class Network_flow(Scene):
    def construct(self):
        self.camera.background_color=GREY_E
        L,R,mline=VGroup(),VGroup(),VGroup()
        for i in range(4):
            tmp=Circle(radius=0.3,color=GRAY_B).move_to(LEFT*3+(1.5-i)*UP*1.2).set_fill(GRAY_B,1)
            L.add(tmp)
        for i in range(4):
            tmp=Circle(radius=0.3,color=GRAY_B).move_to(RIGHT*3+(1.5-i)*UP*1.2).set_fill(GRAY_B,1)
            R.add(tmp)
        tmp=[[0,2],[0,1],[3],[0,3]]
        for i in range(4):
            for j in tmp[i]:
                l=Arrow(start=L[i].get_center(),
                        end=R[j].get_center(),
                        buff=0.3,
                        max_tip_length_to_length_ratio=0.05,
                        stroke_width=2)
                mline.add(l)
        S,T=Dot([-6,0,0]),Dot([6,0,0])
        for i in range(4):
            l1=Arrow(start=S.get_center(),
                    end=L[i].get_center(),
                    buff=0.3,
                    max_tip_length_to_length_ratio=0.05,
                    stroke_width=2)
            l2=Arrow(start=R[i].get_center(),
                    end=T.get_center(),
                    buff=0.3,
                    max_tip_length_to_length_ratio=0.05,
                    stroke_width=2)
            mline.add(l1,l2)
        self.add(L,R,mline,S,T)

# manim -ps LatinSquare.py
# manim -pql LatinSquare.py
# manim -pqh LatinSquare.py
# manim -pqp LatinSquare.py
