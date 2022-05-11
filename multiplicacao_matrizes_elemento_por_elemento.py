from manim.scene.scene import Scene
from manim.mobject.matrix import Matrix
from manim import *

class manim_mobject_matrix_001a(Scene):
    def construct(self):
        sans = 'monospace'
        play_kw = {"run_time": 0.5}

        lines = VGroup(

            Tex("Kernel Matrix", color=BLUE, ),
            Matrix([("0", "-1", "0"),
                    ("-1", "5", "-1"),
                    ("0", "-1", "0")]),

            Matrix([("1", "2", "-1"),
                    ("-3", "1  ", "1"),
                    ("3", "2", "0")]),

            Tex(".", color=BLUE),
            Tex("=", color=BLUE),
            Tex("+", color=BLUE),
            Tex("(", color=BLUE),
            Tex(")", color=BLUE),
            Tex("8", color=BLUE),

            Matrix([("-1", "5", "-1"),
                    ("-9", "21", "-4"),
                    ("1", "-5", "1")]),

            Tex("241", color=BLUE)

        )


        op = VGroup(
            Tex("1"),
            Tex("5"),
            Tex("-1"),
            Tex("-9"),
            Tex("21"),
            Tex("-4"),
            Tex("1"),
            Tex("-5"),
            Tex("1")
        )

        t1_1 = lines[0]
        kernel_matrix = lines[1]
        image_matrix = lines[2]
        multi = lines[3]
        equal = lines[4]
        m_mul = lines[5]
        b_open = lines[6]
        b_close = lines[7]
        plus = lines[8]
        mm = lines[9]
        sum_oppp = lines[-1]
        t1_1.shift(UL * 3)

        kernel_matrix.shift(UP)
        self.play(Write(kernel_matrix))
        self.play(ApplyMethod(kernel_matrix.shift, LEFT*5))
        multi.next_to(kernel_matrix)
        image_matrix.next_to(multi)
        equal.next_to(image_matrix)
        self.play(Write(multi))
        self.play(Write(image_matrix))
        self.play(Write(equal))
        mm.next_to(equal)


        final_mat = VGroup(*mm)
        final_mat1 = VGroup(*final_mat[0])

        for i in final_mat[1:]:
            self.play(Write(i))

        kk = VGroup(*kernel_matrix)
        k1 = VGroup(*kk[0])
        ii = VGroup(*image_matrix)
        i1 = VGroup(*ii[0])

        runtime = 0.1
        flag = True

        for i, j, final_mm, o1 in zip(k1.copy(), i1.copy(), final_mat1.copy(), op):
            i2 = i.copy()
            j2 = j.copy()
            f2 = final_mm.copy()
            m_mul1 = m_mul.copy()
            b_o1 = b_open.copy()
            b_c1 = b_close.copy()
            eq1 = equal.copy()

            b_o1.shift(DOWN*2)
            b_o1.shift(LEFT * 3)
            i2.set_color(RED)
            self.play(Write(b_o1), **play_kw)
            self.play(ApplyMethod(i2.next_to, b_o1), **play_kw)

            m_mul1.next_to(i2)
            self.play(Write(m_mul1), **play_kw)
            j2.set_color(RED)
            self.play(ApplyMethod(j2.next_to, m_mul1), **play_kw)
            b_c1.next_to(j2)
            self.play(Write(b_c1), **play_kw)
            eq1.next_to(b_c1)
            self.play(Write(eq1), **play_kw)
            o1.next_to(eq1)
            self.play(Write(o1),**play_kw)

            self.play(FadeOut(b_o1), FadeOut(i2), FadeOut(m_mul1), FadeOut(j2),
                      FadeOut(b_c1), FadeOut(eq1), Transform(o1, f2))

        self.wait(2)
        self.clear()
        self.wait(2)
