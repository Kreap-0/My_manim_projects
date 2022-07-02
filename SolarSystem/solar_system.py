from manim import *

class test(Scene):
    def construct(self):

        self.camera.background_image="C:\\Users\\12967\\Desktop\\Manim\\starry_sky2.jpg"
        self.camera.init_background()
        timer=ValueTracker(0)
        Sun=Dot(radius=0.32,color=RED)

        Mercury=Dot(color=GREY_A,radius=0.01)
        Mercury.move_to(np.array([0.4,0.6,0]))
        Mercury.add_updater(lambda a,dt: a.rotate(dt*0.3,about_point=ORIGIN))

        Venus=Dot(color=GOLD_D,radius=0.03)
        Venus.move_to(np.array([0.6,-0.8,0]))
        Venus.add_updater(lambda a,dt: a.rotate(dt*0.15,about_point=ORIGIN))

        Earth=Dot(color=BLUE,radius=0.03)
        Earth.move_to(np.array([-1.5,-1.2,0]))
        Earth.add_updater(lambda a,dt: a.rotate(dt*0.1,about_point=ORIGIN))

        Moon=Dot(color=WHITE,radius=0.01)
        Moon.move_to(np.array([-2,-1,0]))
        Moon.add_updater(lambda a,dt: a.move_to(Earth.get_center()+
                                                np.array([0.1*np.cos(timer.get_value()*10),0.1*np.sin(timer.get_value()*10),0])))

        Mars=Dot(color=RED_D,radius=0.02)
        Mars.move_to(np.array([2,-2,0]))
        Mars.add_updater(lambda a,dt: a.rotate(dt*0.05,about_point=ORIGIN))

        Jupiter=Dot(color=GREY_D,radius=0.15)
        Jupiter.move_to(np.array([-3,2,0]))
        Jupiter.add_updater(lambda a,dt: a.rotate(dt*0.001,about_point=ORIGIN))

        Saturn=Dot(color=YELLOW_D,radius=0.17)
        Saturn.move_to(np.array([4,-2.5,0]))
        Rings_of_Saturn=Annulus(color=YELLOW_E,inner_radius=0.25,outer_radius=0.30)
        Rings_of_Saturn.set_opacity(0.5)
        Rings_of_Saturn.move_to(np.array([4,-2.5,0]))

        self.add(Earth,Moon,Sun,Mercury,Mars,Venus,Jupiter,Saturn,Rings_of_Saturn)
        self.play(timer.animate.set_value(600),run_time=600,rate_func=linear)

# manim -pqh solor_system.py test