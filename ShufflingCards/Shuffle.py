from manim import *
import numpy as np
import random as rd

l = [ 'A' , *[ str(i) for i in range(2,11)] , 'J' , 'Q' , 'K' ]

class Card(VGroup):
    def __init__(
        self,
        value: str = "A",
        height: float = 1.5,
        width: float = 1.5 * 0.65,
        num: int = 1,
        back: bool = 0,
        **kwargs,
    ):
        super().__init__(**kwargs)
        if(back):
            x = RoundedRectangle(height = height,
                                  width = width,
                                  color = BLUE,
                                  fill_opacity = 1.0,
                                  stroke_color = WHITE,
                                  corner_radius = 0.1,
                                  **kwargs)
            ds_m = MathTex(r"\mathbb{M}", fill_color="#343434")
            self.add(x,ds_m)
        else:
            b = RoundedRectangle(height = height,
                                 width = width,
                                 color = WHITE,
                                 fill_opacity = 1.0,
                                 corner_radius = 0.1,
                                 **kwargs)
            co = BLACK
            if (num > 2):
                co = RED
            if (num > 4):
                co = ORANGE
            v = Text(value,
                    font_size = 14,
                    font = "Comic Sans MS",
                    color = co,
                    ).shift(UP*0.53+LEFT*0.33)
            v_ = v.copy().rotate(about_point=ORIGIN,
                            angle=PI)
            sign = "♠"
            if (num == 2):
                sign = "♣"
            elif (num == 3):
                sign = "♥"
            elif (num == 4):
                sign = "♦"
            elif (num == 5):
                sign = "⭐"
            x = Text(sign,
                     font_size = 14,
                     color = co)
            x1 = x.copy().move_to(v.get_center()+DOWN*0.23)
            x2 = x1.copy().rotate(about_point=ORIGIN,
                            angle=PI)
            self.add(b,v,v_,x1,x2)

class Cover(Scene):
    def construct(self):
        self.camera.background_color=GREY_E
        v1 , v2 = VGroup() , VGroup()
        for i in range(100):
            x = 1.5*(i%8)-5
            y = (int(i/8))-5
            xx = x - y
            yy = x + y
            if (y%2==1):
                xx += 0.5
                yy += 0.5
            c = Card(value = l[ i % len(l)],
                     num = (i%4)+1,
                    ).rotate(about_point = ORIGIN,
                             angle = 3*PI/4)
            self.add(c.shift(xx*RIGHT+yy*UP))
            if((int(i/8))&1):
                v1.add(c)
            else:
                v2.add(c)
        Random=Text("Random?",
                      font_size = 200,
                      color = ORANGE,
                      font = "Comic Sans MS")
        self.add(Random)
        self.wait()
        self.play(FadeOut(Random,shift=UP))
        self.play(v1.animate(run_time=3,rate_functions=smooth).shift(UR*15),
                  v2.animate(run_time=3,rate_functions=smooth).shift(DL*15))
        self.wait()
    
def Build(l1,l2):
    return VGroup(*[Card(value = l1[i],
                            num = l2[i])
                    .shift(RIGHT*0.3*i)
                    for i in range(0,len(l1))])

class Landlord(Scene):
    def construct(self):
        self.camera.background_color=GREY_E
        #self.play(Create(NumberPlane()))
        vs   = ['Q','3','3','2','A','A','10','8','7','6','5','4','4','4','4']
        nums = [ 5 , 5 , 5 , 3 , 3 , 2 , 3  , 1 , 2 , 1 , 3 , 1 , 3 , 2 , 4 ]
        P1 = VGroup(*[Card(value = vs[i],
                           num = nums[i]).shift(RIGHT*0.3*i)
                           for i in range(0,len(vs))]).move_to(DOWN*5)
        P2 = VGroup(*[Card(back = 1).shift(UR*0.18*i).rotate(angle=0.08*PI)
                           for i in range(0,18)]).shift(LEFT*12).scale(0.8)
        P3 = VGroup(*[Card(back = 1).shift(UL*0.18*i).rotate(angle=-0.08*PI)
                           for i in range(0,17)]).shift(RIGHT*12).scale(0.8)
        self.add(P1,P2,P3)
        self.play(P1.animate(run_time=2,lag_ratio=0.1).shift(UP*2),
                  P2.animate(run_time=2,rate_functions=smooth).shift(RIGHT*6),
                  P3.animate(run_time=2,rate_functions=smooth).shift(LEFT*6))
        self.wait()
        
        Shannon = ImageMobject("shannon").move_to(LEFT*6+UP*3).scale(0.9)
        Aldous = ImageMobject("aldous").move_to(RIGHT*6+UP*3).scale(0.4)
        self.play(FadeIn(Shannon),FadeIn(Aldous))
        
        c1 = SVGMobject("clock").set_color(color=WHITE).move_to(DOWN).scale(0.2).set_opacity(opacity=0)
        c2 = c1.copy().move_to(LEFT*2+UP)
        c3 = c1.copy().move_to(RIGHT*2+UP)
        self.add(c1,c2,c3)

        vs   = ['Q','3','3','2','A','A','10','8','7','6','5']
        nums = [ 5 , 5 , 5 , 3 , 3 , 2 , 3  , 1 , 2 , 1 , 3 ]
        vt   = ['4','4','4','4']
        numt = [ 1 , 3 , 2 , 4 ]
        c1.set_opacity(opacity=1)
        self.wait()
        VGroup(*[P1[i] for i in range(11,15)]).shift(UP/4)
        self.wait()
        tmp1 = VGroup(*[P1[i] for i in range(11,15)])
        P1.remove(*[x for x in tmp1])
        tmp1.move_to(DOWN).scale(0.8)
        c1.set_opacity(opacity=0)
        self.add(tmp1)
        self.wait()

        c3.set_opacity(opacity=1)
        self.wait(0.2)
        VGroup(*[P1[i] for i in range(6,11)]).shift(UP/4)
        self.wait()
        c3.set_opacity(opacity=0)

        c2.set_opacity(opacity=1)
        self.wait(0.5)
        P1[2].shift(UP/4)
        self.wait()
        c2.set_opacity(opacity=0)

        vs   = ['Q','3','2','A','A']
        nums = [ 5 , 5 , 3 , 3 , 2 ]
        vt   = ['10','9','8','7','6','5']
        numt = [ 3  , 5 , 1 , 2 , 1 , 3 ]
        self.remove(tmp1)
        c1.set_opacity(opacity=1)
        self.wait()
        self.remove(P1)
        P1 = Build(vs,nums).move_to(DOWN*3)
        tmp1 = Build(vt,numt).move_to(DOWN).scale(0.8)
        c1.set_opacity(opacity=0)
        self.add(P1,tmp1)
        self.wait()

        c3.set_opacity(opacity=1)
        self.wait()
        c3.set_opacity(opacity=0)

        c2.set_opacity(opacity=1)
        self.wait()
        c2.set_opacity(opacity=0)

        vs   = ['Q','3','A','A']
        nums = [ 5 , 5 , 3 , 2 ]
        vt   = ['2']
        numt = [ 3 ]
        self.remove(tmp1)
        c1.set_opacity(opacity=1)
        self.wait()
        P1[2].shift(UP/4)
        self.wait()
        self.remove(P1)
        P1 = Build(vs,nums).move_to(DOWN*3)
        tmp1 = Build(vt,numt).move_to(DOWN).scale(0.8)
        self.add(P1,tmp1)
        c1.set_opacity(opacity=0)
        self.wait()

        vp   = ['7','7','7','7']
        nump = [ 5 , 1 , 3 , 4 ]
        c3.set_opacity(opacity=1)
        self.wait()
        for i in range(0,4):
            x = P3[0]
            P3.remove(x)
            self.remove(x)
        tmp3 = Build(vp,nump).shift(UR).scale(0.8)
        c3.set_opacity(opacity=0)
        self.add(tmp3)
        self.wait()

        vp   = ['K','K','K','K','K']
        nump = [ 5 , 5 , 5 , 2 , 4 ]
        c2.set_opacity(opacity=1)
        self.wait()
        for i in range(0,5):
            x = P2[0]
            P2.remove(x)
            self.remove(x)
        tmp2 = Build(vp,nump).move_to(LEFT*2+UP).scale(0.8)
        self.add(tmp2)
        c2.set_opacity(opacity=0)
        self.wait()

        vp   = ['J','J','J','10','10','10','9','9','9','8','8','5']
        nump = [ 1 , 2 , 4 , 5  , 1  , 4  , 1 , 3 , 4 , 2 , 4 , 2 ]
        self.remove(tmp1)
        c1.set_opacity(opacity=1)
        self.wait()
        c1.set_opacity(opacity=0)
        self.remove(tmp3)
        c3.set_opacity(opacity=1)
        self.wait()
        c3.set_opacity(opacity=0)
        self.remove(tmp2)
        c2.set_opacity(opacity=1)
        self.wait()
        c2.set_opacity(opacity=0)
        tmp2 = Build(vp,nump).shift(LEFT*2+UP).scale(0.8)
        self.add(tmp2)
        self.remove(P2)
        self.wait()

class Intro(MovingCameraScene):
    def construct(self):
        #self.play(Create(NumberPlane()))
        self.camera.background_color=GREY_E
        t1 = Text('一副牌要洗多少次才能足够随机？',
                  t2c={'随机':ORANGE})
        self.play(Write(t1))
        self.wait()
        x = VGroup(*[Card(value = l[i],num = j+1)
                     for i in range(0,len(l))
                     for j in range(0,4)]).move_to(LEFT*4+DOWN*7)
        self.play(self.camera.frame.animate(rate_functions=smooth).move_to(LEFT*4.5+DOWN*3.5).scale(0.65))
        self.add(x)
        self.play(x.animate(rate_functions=smooth).shift(UP*2))
        self.play(AnimationGroup(*[
            Rotate(mobject=x[i],
                   angle=-2*i*PI/52,
                   about_point=LEFT*4.5+DOWN*3.6)
            for i in range(0,len(l)*4)]),
        )
        self.wait()
        self.play(self.camera.frame.animate(rate_functions=smooth).shift(RIGHT*9))
        self.wait()
        self.play(self.camera.frame.animate(rate_functions=smooth).move_to(RIGHT*3.75))
        w = VGroup(t1[12].copy(),t1[13].copy())
        self.add(w)
        self.wait(0.5)
        self.play(FadeOut(t1))
        self.play(w.animate().scale(2))
        self.wait()
        self.play(Unwrite(w))
        self.wait()

class P2(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        self.wait()
        man = SVGMobject("man").shift(LEFT*8)
        self.add(man)
        self.play(man.animate(rate_functions=smooth).shift(RIGHT*4))
        self.wait()

        vs   = [['4','4','4','4'],
                ['10','9','8','7','6','5'],
                ['2'],
                ['7','7','7','7'],
                ['K','K','K','K','K'],
                ['J','J','J','10','10','10','9','9','9','8','8','5']]
        nums = [[ 1 , 3 , 2 , 4 ],
                [ 3  , 5 , 1 , 2 , 1 , 3 ],
                [ 3 ],
                [ 5 , 1 , 3 , 4 ],
                [ 5 , 5 , 5 , 2 , 4 ],
                [ 1 , 2 , 4 , 5  , 1  , 4  , 1 , 3 , 4 , 2 , 4 , 2 ]]
        cards = [Build(vs[i],nums[i]).shift(UP*10).rotate(about_point=ORIGIN,angle=-PI/6*i)
                 for i in range(0,len(vs))]
        self.play(LaggedStart(*[
            x.animate().move_to(ORIGIN) for x in cards
        ],run_time=3,lag_ratio=0.2))
        self.wait()
        v   = ['A','2','3','4','5']
        num = [ 1 , 1 , 1 , 1 , 1 ]
        c1 = Build(v,num).arrange().shift(DOWN*8)
        c2 = VGroup(*[Card(back=1) for i in range(0,5)]).arrange().shift(DOWN*8)
        self.add(c1,c2)
        self.play(*[x.animate(rate_functions=smooth).shift(UP*6)
                    for x in cards],
                    c1.animate().shift(UP*8))
        self.wait()
        self.play(VGroup(c1,c2).animate().shift(UP*8))
        c2.save_state()
        self.wait()
        def swap(mob,tar):
            return MoveAlongPath(mobject=mob,
                                 path=ArcBetweenPoints(start=mob.get_center(),end=tar,angle=PI),
                                 run_time=0.5)
        mob = [[1,2,3,4,5],[3,5,1,4,2],[4,3,5,1,2],[5,2,1,3,4]]
        tar = [[3,5,1,4,2],[2,3,4,1,5],[5,4,1,3,2],[3,1,5,2,4],[2,3,5,4,1]]
        pos = [c2[i].get_center() for i in range(0,5)]
        for i in range(0,len(mob)):
            self.play(*[swap(c2[mob[i][j]-1],pos[tar[i][j]-1]) for j in range(0,len(mob[i]))])
        self.wait()
        a = Arrow().rotate(angle=-PI/2).move_to(DOWN*2)
        self.play(GrowArrow(a))
        c3 = Build(['2','3','5','4','A'],[1,1,1,1,1]).arrange().move_to(DOWN*2)
        self.play(VGroup(c2,a).animate().shift(UP*2),
                  FadeIn(c3,shift=UP*2))
        IsTrue = Text("你对了吗？",color=GREEN).move_to(DOWN*2+RIGHT*5).scale(0.8)
        self.play(Write(IsTrue))
        self.wait()

class P2_sup(MovingCameraScene):
    def construct(self):
        bg = ImageMobject("tmp").scale(0.75)
        self.add(bg)
        self.wait()
        x = Dot([2.3,1.5,0])
        c2 = VGroup(*[Card(back=1) for i in range(0,5)]).arrange()
        self.play(AnimationGroup(*[
            Create(CurvedArrow(x.get_center(),
                               c2[i].get_center()))
            for i in range(3)
        ]))
        self.wait()

class P2_2(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E
        self.wait()
        t1 = Text("同一事件\n对于知情者而言就是「确定事件」，\n对于不知情者而言就是「随机事件」。",
                  t2c={"确定事件":BLUE,"随机事件":BLUE}).scale(0.8).move_to(LEFT*5+UP,LEFT)
        self.play(Write(t1),run_time=3)
        self.wait()
        t2 = Text("随机性并不源于事件本身是否发生，\n而只是描述观察者对该事件的知识状态。",
                  t2c={"随机性":ORANGE,"观察者":RED,"知识状态":BLUE,}).scale(0.8).move_to(LEFT*5+DOWN,LEFT)
        self.play(Write(t2),run_time=3)
        self.wait()
        Bayes_i = ImageMobject("Bayes").shift(RIGHT*5).scale(2)
        Bayes_n = Text("Bayes",font_size=28).shift(DOWN*2+RIGHT*5)
        self.play(VGroup(t1,t2).animate().shift(LEFT),
                  FadeIn(Bayes_i,shift=LEFT))
        self.play(Write(Bayes_n))
        self.wait()

class P3(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GREY_E

        bar_style = dict(
            fill_color=BLUE,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=0.1,
        )

        def get_axes(x_max = 120, y_max = 1.0,
                     width = 12, height = 100):
            axes = Axes(
                x_range = (0,x_max),
                y_range = (0,y_max,y_max/40),
                x_length = width,
                y_length = height,
                x_axis_config={"tick_size": 0},
                y_axis_config={"include_numbers": True},
                tips = False
            )
            return axes
        
        axes = get_axes().move_to(DOWN*3,DOWN)

        def get_bars(values):
            x_unit = axes.x_axis.unit_size
            y_unit = axes.y_axis.unit_size
            bars = VGroup()
            for x,value in enumerate(values):
                bar = Rectangle(width = x_unit,
                                height = value * y_unit,
                                **bar_style).move_to(axes.c2p(x, 0),DL)
                bars.add(bar)
            bars.set_color_by_gradient(BLUE,GREEN_A)
            return bars
        
        bars = get_bars([0 for i in range(0,120)])

        def update_bars(values):
            bars_ = get_bars(values)
            for i,bar in enumerate(bars_):
                bars[i].target = bar
            return AnimationGroup(*[
                MoveToTarget(bar,rate_functions=smooth)
                for bar in bars
            ])

        self.play(Create(axes))
        self.wait()

        for i in range(4):
            x = [rd.randint(1,1000) for _ in range(120)]
            s = 0
            for i in x:
                s += i
            for i in range(120):
                x[i]/=s
            self.play(update_bars(x))
            self.wait()
        self.play(update_bars([1/120 for _ in range(120)]))
        self.wait()
        t1 = Text("均匀概率分布",font_size=72).set_color_by_gradient(BLUE,GREEN_A).set_stroke(WHITE).shift(UP)
        t2 = Text("Uniform Distribution",font="Comic Sans MS").next_to(t1,DOWN).set_color_by_gradient(BLUE,GREEN_A).set_stroke(WHITE)
        self.play(Write(t1),Write(t2))
        self.wait()

class Test(Scene):
    def construct(self):
        x = Card()
        self.add(x)

# manim -ps Shuffle.py
# manim -pql Shuffle.py
# manim -pqp Shuffle.py
