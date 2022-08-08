from manim import *

text = VGroup()

text1_br = Text("J", font="Tex Gyre Chorus", slant=ITALIC, font_size = 58)

text2_br = Text("A", font="Tex Gyre Chorus", slant=ITALIC, font_size = 58)

text3_br = Text("F", font="Tex Gyre Chorus", slant=ITALIC, font_size = 58)

text1_en = Tex(r"$\Sigma$", color=RED,font_size=174)

text2_en = Text("Math", font="Tex Gyre Chorus", slant=ITALIC, font_size = 58)

text3_en = Text("Exercicises", font="Tex Gyre Chorus", slant=ITALIC, font_size = 58)

text.add(text2, text3)

text.arrange(DOWN, center = False, aligned_edge = LEFT)

text.next_to(text1, RIGHT)

texto_logo = VGroup()

texto_logo.add(text1, text)

circle_logo = Circle(fill_opacity=5).scale(2.2)

circle_logo.set_fill()

circle_logo.set_color(GREEN)

circle_logo_right_corner = circle_logo.copy().scale(0.1)

texto_logo_right_corner = texto_logo.copy().scale(0.1)

texto_final_1 = Tex(r"Thanks for watching!", color=RED, font_size=100)

texto_final_2 = Tex(r"Don't forget to like,\\ share and subscribe!", color=RED, font_size=100)

class Logo(Scene):
    CONFIG = {
        "camera_config" : {"background_color": BLACK}
    }

    def logo_principal():

        texto_logo.next_to(circle_logo, 0, buff=1).scale(0.9)

        return VGroup(circle_logo, texto_logo)

    def logo_right_corner():
        circle_logo_right_corner.to_corner(DOWN + RIGHT)

        text2 = texto_logo_right_corner.next_to(circle_logo_right_corner, 0 , buff = 1)

        return VGroup(circle_logo_right_corner, text2)

    def fechamento(self):
        self.play(Write(texto_final_1), run_time = 3)

        self.wait(3)

        self.play(FadeOut(texto_final_1), run_time = 0.5)

        self.play(Write(texto_final_2), run_time = 3)

        self.wait(5)
