from manim import *

equation_matrix_colors = [RED, GREEN, BLUE]
augmented_matrix_colors = [RED, GREEN, BLUE, TEAL]
big_augmented_matrix_colors = [RED, GREEN, BLUE, TEAL, ORANGE]
fonte_size=24

def finishScene(self):
    self.play(*[FadeOut(mob) for mob in self.mobjects])

class Fourth(Scene):
    def construct(self):
        opening_text = Tex("Let's apply this to find inverse of a matrix")
        self.play(Write(opening_text), **{"run_time":1.5})
        self.wait()
        self.play(FadeOut(opening_text))

        matrix_A = MobjectMatrix(
            [(MathTex("a_{11}"), MathTex("a_{12}"), MathTex("a_{13}")),
             (MathTex("a_{21}"), MathTex("a_{22}"), MathTex("a_{23}")),
             (MathTex("a_{31}"), MathTex("a_{32}"), MathTex("a_{33}"))])
        matrix_A.shift(LEFT * 4.5)
        algebra_matrix = MobjectMatrix(
            [(MathTex("b_{11}"), MathTex("b_{12}"), MathTex("b_{13}")),
             (MathTex("b_{21}"), MathTex("b_{22}"), MathTex("b_{23}")),
             (MathTex("b_{31}"), MathTex("b_{32}"), MathTex("b_{33}"))])
        algebra_matrix.next_to(matrix_A, RIGHT)
        equal_sign = MathTex("=", color=BLUE, font_size=72)
        equal_sign.next_to(algebra_matrix, RIGHT)

        identity_matrix = MobjectMatrix(
            [(MathTex(r"a_{11}b_{11} + a_{12}b_{21} + a_{13}b_{31}", font_size=fonte_size), MathTex("a_{11}b_{11} + a_{12}b_{22} + a_{13}b_{32}", font_size=fonte_size), MathTex("a_{11}b_{13} + a_{12}b_{23} + a_{13}b_{33}\\\\", font_size=fonte_size)),
             (MathTex("a_{21}b_{11} + a_{22}b_{21} + a_{23}b_{31}"), MathTex("a_{21}b_{12} + a_{22}b_{22} + a_{23}b_{32}"), MathTex("a_{21}b_{13} + a_{22}b_{23} + a_{23}b_{33}", font_size=fonte_size)),
             (MathTex("a_{31}b_{11} + a_{32}b_{21} + a_{33}b_{31}", font_size=fonte_size), MathTex("a_{31}b_{12} + a_{32}b_{22} + a_{33}b_{32}", font_size=fonte_size), MathTex("a_{31}b_{13} + a_{32}b_{23} + a_{33}b_{33}", font_size=fonte_size))])
        temp = MathTex(r"a_{11}b_{11} + a_{12}b_{21} + a_{13}b_{31}\qquad", r"a_{11}b_{11} + a_{12}b_{22} + a_{13}b_{32}\qquad", r"a_{11}b_{13} + a_{12}b_{23} + a_{13}b_{33}\\\\", r"a_{21}b_{11} + a_{22}b_{21} + a_{23}b_{31}\qquad", r"a_{21}b_{12} + a_{22}b_{22} + a_{23}b_{32}\qquad", r"a_{21}b_{13} + a_{22}b_{23} + a_{23}b_{33}\\\\", r"a_{31}b_{11} + a_{32}b_{21} + a_{33}b_{31}\qquad", r"a_{31}b_{12} + a_{32}b_{22} + a_{33}b_{32}\qquad", r"a_{31}b_{13} + a_{32}b_{23} + a_{33}b_{33}\\", font_size=fonte_size)
        identity_matrix_flat = VGroup(*VGroup(*identity_matrix)[0])
        matrix_equation = VGroup(matrix_A, algebra_matrix, equal_sign)
        matrix_equation.shift(UP * 1.5)

        self.play(*[FadeIn(matrix_A), FadeIn(algebra_matrix), FadeIn(equal_sign)])

        texto1 = MathTex("[", font_size=172)
        texto1.next_to(temp, LEFT)
        texto1.shift(DOWN*1.5)
        self.play(Write(texto1))
        temp.shift(DOWN*1.5)
        texto2 = MathTex("]", font_size=48).scale(4)
        texto2.next_to(temp, RIGHT)
        self.play(Write(texto2))

        for i in range(0,3):
            second_column = SurroundingRectangle(matrix_A.get_rows()[i])
            self.play(*[Create(second_column)])
            for j in range(0,3):
                first_row = SurroundingRectangle(algebra_matrix.get_columns()[j])
                self.play(Create(first_row), **{"run_time":0.8})
                identity_matrix_rect = SurroundingRectangle(temp[i*3+j])
                self.play(Create(identity_matrix_rect),FadeIn(temp[i*3+j]), **{"run_time":0.8})
                self.wait(1.25)
                self.play(*[FadeOut(first_row), FadeOut(identity_matrix_rect)], **{"run_time":0.5})
            self.play(*[FadeOut(second_column)], **{"run_time": 0.5})

        finishScene(self)
