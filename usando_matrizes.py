from manim import *

first_eqn = MathTex("3", "x_{1}", "+", "1", "y_{1}", "-", "2", "z_{1}", "=", "7")
second_eqn = MathTex("1", "x_{1}", "-", "3", "y_{1}", "+", "4", "z_{1}", "=", "15")
third_eqn = MathTex("2", "x_{1}", "-", "2", "y_{1}", "+", "1", "z_{1}", "=", "12")
equations_array = [first_eqn, second_eqn, third_eqn]
equations = MobjectMatrix(
    [[first_eqn], [second_eqn], [third_eqn]],
    left_bracket="\\{",
    right_bracket="\\")
for eqn in equations_array:
    eqn.set_color_by_tex_to_color_map({
        "x": RED,
        "y": GREEN,
        "z": BLUE,
    })

first_eqn1 = MathTex("3", "x_{2}", "+", "1", "y_{2}", "-", "2", "z_{2}", "=", "-3")
second_eqn1 = MathTex("1", "x_{2}", "-", "3", "y_{2}", "+", "4", "z_{2}", "=", "21")
third_eqn1 = MathTex("2", "x_{2}", "-", "2", "y_{2}", "+", "1", "z_{2}", "=", "3")
equations_array1 = [first_eqn1, second_eqn1, third_eqn1]
equations1 = MobjectMatrix(
    [[first_eqn1], [second_eqn1], [third_eqn1]],
    left_bracket="\\{",
    right_bracket="\\")
for eqn in equations_array1:
    eqn.set_color_by_tex_to_color_map({
        "x": RED,
        "y": GREEN,
        "z": BLUE,
    })

equation_matrix_colors = [RED, GREEN, BLUE]
augmented_matrix_colors = [RED, GREEN, BLUE, TEAL]
big_augmented_matrix_colors = [RED, GREEN, BLUE, TEAL, ORANGE]

first_algebra_eqn1 = MathTex("a_{11}", "x_{11}", "+", "a_{12}", "x_{21}", "+", "a_{13}", "x_{31}", "=", "1")
second_algebra_eqn1 = MathTex("a_{21}", "x_{11}", "+", "a_{22}", "x_{21}", "+", "a_{23}", "x_{31}", "=", "0")
third_algebra_eqn1 = MathTex("a_{31}", "x_{11}", "+", "a_{32}", "x_{21}", "+", "a_{33}", "x_{31}", "=", "0")
sub_first_algebra_eqn1 = MathTex("1", "x_{11}", "+", "0", "x_{21}", "+", "0", "x_{31}", "=", "a")
sub_second_algebra_eqn1 = MathTex("0", "x_{11}", "+", "1", "x_{21}", "+", "0", "x_{31}", "=", "d")
sub_third_algebra_eqn1 = MathTex("0", "x_{11}", "+", "0", "x_{21}", "+", "1", "x_{31}", "=", "g")
equations_array1 = [first_algebra_eqn1, second_algebra_eqn1, third_algebra_eqn1, sub_first_algebra_eqn1, sub_second_algebra_eqn1, sub_third_algebra_eqn1]
for item in equations_array1:
    for i in range(1, 8, 3):
        item[i].set_color(equation_matrix_colors[int((i - 1) / 3)])
algebra_equations_1 = MobjectMatrix(
    [[first_algebra_eqn1], [second_algebra_eqn1], [third_algebra_eqn1]],
    left_bracket="\\{",
    right_bracket="\\")
sub_algebra_equations_1 = MobjectMatrix(
    [[sub_first_algebra_eqn1], [sub_second_algebra_eqn1], [sub_third_algebra_eqn1]],
    left_bracket="\\{",
    right_bracket="\\")
algebra_equations_1.shift(DOWN * 1.5).scale(0.8)
sub_algebra_equations_1.shift(DOWN * 2).scale(0.8)

first_algebra_eqn2 = MathTex("a_{11}", "x_{12}", "+", "a_{12}", "x_{22}", "+", "a_{13}", "x_{32}", "=", "0")
second_algebra_eqn2 = MathTex("a_{21}", "x_{12}", "+", "a_{22}", "x_{22}", "+", "a_{23}", "x_{32}", "=", "1")
third_algebra_eqn2 = MathTex("a_{31}", "x_{12}", "+", "a_{32}", "x_{22}", "+", "a_{33}", "x_{32}", "=", "0")
sub_first_algebra_eqn2 = MathTex("1", "x_{12}", "+", "0", "x_{22}", "+", "0", "x_{32}", "=", "b")
sub_second_algebra_eqn2 = MathTex("0", "x_{12}", "+", "1", "x_{22}", "+", "0", "x_{32}", "=", "e")
sub_third_algebra_eqn2 = MathTex("0", "x_{12}", "+", "0", "x_{22}", "+", "1", "x_{32}", "=", "h")
equations_array2 = [first_algebra_eqn2, second_algebra_eqn2, third_algebra_eqn2, sub_first_algebra_eqn2, sub_second_algebra_eqn2, sub_third_algebra_eqn2]
for item in equations_array2:
    for i in range(1, 8, 3):
        item[i].set_color(equation_matrix_colors[int((i - 1) / 3)])
algebra_equations_2 = MobjectMatrix(
    [[first_algebra_eqn2], [second_algebra_eqn2], [third_algebra_eqn2]],
    left_bracket="\\{",
    right_bracket="\\")
sub_algebra_equations_2 = MobjectMatrix(
    [[sub_first_algebra_eqn2], [sub_second_algebra_eqn2], [sub_third_algebra_eqn2]],
    left_bracket="\\{",
    right_bracket="\\")
algebra_equations_2.shift(DOWN * 1.5).scale(0.8)
sub_algebra_equations_2.shift(DOWN * 2).scale(0.8)

first_algebra_eqn3 = MathTex("a_{11}", "x_{13}", "+", "a_{12}", "x_{23}", "+", "a_{13}", "x_{33}", "=", "0")
second_algebra_eqn3 = MathTex("a_{21}", "x_{13}", "+", "a_{22}", "x_{23}", "+", "a_{23}", "x_{33}", "=", "0")
third_algebra_eqn3 = MathTex("a_{31}", "x_{13}", "+", "a_{32}", "x_{23}", "+", "a_{33}", "x_{33}", "=", "1")
sub_first_algebra_eqn3 = MathTex("1", "x_{13}", "+", "0", "x_{23}", "+", "0", "x_{33}", "=", "c")
sub_second_algebra_eqn3 = MathTex("0", "x_{13}", "+", "1", "x_{23}", "+", "0", "x_{33}", "=", "f")
sub_third_algebra_eqn3 = MathTex("0", "x_{13}", "+", "0", "x_{23}", "+", "1", "x_{33}", "=", "i")
equations_array3 = [first_algebra_eqn3, second_algebra_eqn3, third_algebra_eqn3, sub_first_algebra_eqn3, sub_second_algebra_eqn3, sub_third_algebra_eqn3]
for item in equations_array3:
    for i in range(1, 8, 3):
        item[i].set_color(equation_matrix_colors[int((i - 1) / 3)])
algebra_equations_3 = MobjectMatrix(
    [[first_algebra_eqn3], [second_algebra_eqn3], [third_algebra_eqn3]],
    left_bracket="\\{",
    right_bracket="\\")
sub_algebra_equations_3 = MobjectMatrix(
    [[sub_first_algebra_eqn3], [sub_second_algebra_eqn3], [sub_third_algebra_eqn3]],
    left_bracket="\\{",
    right_bracket="\\")
algebra_equations_3.shift(DOWN * 1.5).scale(0.8)
sub_algebra_equations_3.shift(DOWN * 2).scale(0.8)

all_algebra_equations = [algebra_equations_1, algebra_equations_2, algebra_equations_3]
sub_all_algebra_equations = [sub_first_algebra_eqn1, sub_second_algebra_eqn1, sub_third_algebra_eqn1,
                             sub_first_algebra_eqn2, sub_second_algebra_eqn2, sub_third_algebra_eqn2,
                             sub_first_algebra_eqn3, sub_second_algebra_eqn3, sub_third_algebra_eqn3]
real_all_algebra_equations =  [first_algebra_eqn1, second_algebra_eqn1, third_algebra_eqn1,
                             first_algebra_eqn2, second_algebra_eqn2, third_algebra_eqn2,
                             first_algebra_eqn3, second_algebra_eqn3, third_algebra_eqn3]
def finishScene(self):
    self.play(*[FadeOut(mob) for mob in self.mobjects])

class Start(Scene):
    def construct(self):
        title = Tex(r"Linear Equations")
        VGroup(title, equations).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(equations, shift=UP),
        )
        self.wait()
        finishScene(self)

class Second(Scene):
    def construct(self):
        self.add(equations)
        self.play(equations.animate.scale(0.8).to_corner(corner=UP + LEFT, buff=0.5))
        self.wait(0.5)

        coefficient_matrix = Matrix(
            [("3", "1", "-2", "7"), ("1", "-3", "4", "15"), ("2", "-2", "1", "12")])
        coefficient_matrix_flat = VGroup(*VGroup(*coefficient_matrix)[0]).copy()
        for i in VGroup(*coefficient_matrix)[1:]:
            self.play(Write(i))
        self.wait()
        toFade = []
        for (variable) in range(0,4):
            for (eqnz) in range(0,3):
                resultant = variable + 4 * eqnz
                which_eqn = third_eqn
                if eqnz == 0:
                    which_eqn = first_eqn
                elif eqnz == 1:
                    which_eqn = second_eqn
                toFade.append(which_eqn[variable*3].copy())
                self.play(Transform(toFade[-1], coefficient_matrix_flat[resultant]), **{"run_time":0.75})
        for fade in toFade:
            self.play(FadeOut(fade), **{"run_time":0.01})
        self.play(ApplyMethod(coefficient_matrix.shift, LEFT*3.5))
        separator1 = Line(LEFT*2.2 + UP*1.1, LEFT*2.2 + DOWN*1.1, color=YELLOW)
        separator2 = Line(RIGHT*4.2 + UP*1.1, RIGHT*4.2 + DOWN*1.1, color=YELLOW)
        self.play(Create(separator1), **{"run_time":0.15})
        for i in range(0,4):
            for j in range(0,3):
                self.play(VGroup(*VGroup(*coefficient_matrix)[0])[i+4*j].animate.set_color(augmented_matrix_colors[i]),**{"run_time": 0.1})
        coefficient_matrix_flat = VGroup(*VGroup(*coefficient_matrix)[0]).copy()

        rref_matrix = Matrix(
            [("1", "0", "0", "4"), ("0", "1", "0", "-1"), ("0", "0", "1", "2")])
        rref_matrix_flat = VGroup(*VGroup(*rref_matrix)[0])
        rref_matrix.shift(RIGHT*3)
        for i in VGroup(*rref_matrix)[1:]:
            self.play(Write(i))
        bottom_text = Tex("Apply the Gauss-Jordan Algorithm")
        bottom_text.shift(DOWN*1.8)
        arrow = Arrow(LEFT*0.9, RIGHT*0.5)
        self.play(Create(arrow), **{"run_time":0.4})
        self.play(Write(bottom_text), **{"run_time":1})
        self.wait()

        for i in range(0,12):
            rref_matrix_flat[i].set_color(augmented_matrix_colors[i%4])
            self.play(Transform(coefficient_matrix_flat[i], rref_matrix_flat[i]), **{"run_time": 0.75})

        self.play(Create(separator2), **{"run_time": 0.25})
        self.wait()
        self.remove(bottom_text)
        for i in range(0,3):
            row = SurroundingRectangle(rref_matrix.get_rows()[i])
            if i == 0:
                bottom_text = Tex("x", " = 4")
                bottom_text.set_color_by_tex('x', RED)
            elif i == 1:
                bottom_text = Tex("y", " = -1")
                bottom_text.set_color_by_tex('y', GREEN)
            else:
                bottom_text = Tex("z", " = 2")
                bottom_text.set_color_by_tex('z', BLUE)
            self.play(Create(row), **{"run_time": 1.75})
            bottom_text.shift(DOWN*1.8)
            self.play(Write(bottom_text), **{"run_time": 1.2})
            self.wait()
            self.remove(bottom_text)
            self.remove(row)
        finishScene(self)

class Third(Scene):
    def construct(self):
        opening_text1 = Tex("Two linear equations with")
        opening_text2 = Tex("the same set of coefficients")
        opening_text = VGroup(opening_text1, opening_text2).arrange(DOWN, buff=0.2)
        self.play(Write(opening_text), **{"run_time":2.25})
        self.wait()
        self.play(FadeOut(opening_text))

        and_text = Tex("and")
        matrix_eqns_group = VGroup(equations, and_text , equations1).arrange(RIGHT, buff=1)
        self.play(FadeIn(matrix_eqns_group), **{"run_time":1.5})
        self.wait()
        self.play(FadeOut(and_text), **{"run_time":0.5})
        self.play(*[equations.animate.scale(0.6).to_corner(corner=UP + LEFT, buff=0.5), equations1.animate.scale(0.6).to_corner(corner=UP + RIGHT, buff=0.5)])

        coefficient_matrix1 = Matrix(
            [("3", "1", "-2", "7"), ("1", "-3", "4", "15"), ("2", "-2", "1", "12")])
        coefficient_matrix1.shift(LEFT*3.5)
        coefficient_matrix1_flat = VGroup(*VGroup(*coefficient_matrix1)[0])
        coefficient_matrix2 = Matrix(
            [("3", "1", "-2", "-3"), ("1", "-3", "4", "21"), ("2", "-2", "1", "3")])
        coefficient_matrix2.shift(RIGHT * 3)
        coefficient_matrix2_flat = VGroup(*VGroup(*coefficient_matrix2)[0])
        rref_matrix1 = Matrix(
            [("1", "0", "0", "4"), ("0", "1", "0", "-1"), ("0", "0", "1", "2")])
        rref_matrix_flat1 = VGroup(*VGroup(*rref_matrix1)[0])
        rref_matrix1.shift(LEFT * 3.5)
        rref_matrix2 = Matrix(
            [("1", "0", "0", "3"), ("0", "1", "0", "6"), ("0", "0", "1", "9")])
        rref_matrix_flat2 = VGroup(*VGroup(*rref_matrix2)[0])
        rref_matrix2.shift(RIGHT * 3)

        separator1 = Line(LEFT * 2.2 + UP * 1.1, LEFT * 2.2 + DOWN * 1.1, color=YELLOW)
        separator2 = Line(RIGHT * 4.2 + UP * 1.1, RIGHT * 4.2 + DOWN * 1.1, color=YELLOW)

        for (i,j) in zip(VGroup(*coefficient_matrix1)[1:], VGroup(*coefficient_matrix2)[1:]):
            self.play(*[Write(i), Write(j)])

        toFade = []
        for (variable) in range(0, 4):
            for (eqnz) in range(0, 3):
                resultant = variable + 4 * eqnz
                which_eqn1 = third_eqn
                which_eqn2 = third_eqn1
                if eqnz == 0:
                    which_eqn1 = first_eqn
                    which_eqn2 = first_eqn1
                elif eqnz == 1:
                    which_eqn1 = second_eqn
                    which_eqn2 = second_eqn1
                toFade.append(which_eqn1[variable * 3].copy())
                toFade.append(which_eqn2[variable * 3].copy())
                coefficient_matrix1_flat[resultant].set_color(augmented_matrix_colors[resultant % 4])
                coefficient_matrix2_flat[resultant].set_color(augmented_matrix_colors[resultant % 4])
                rref_matrix_flat1[resultant].set_color(augmented_matrix_colors[resultant % 4])
                rref_matrix_flat2[resultant].set_color(augmented_matrix_colors[resultant % 4])
                self.play(*[Transform(toFade[-1], coefficient_matrix2_flat[resultant]), Transform(toFade[-2], coefficient_matrix1_flat[resultant])], **{"run_time": 0.75})

        self.play(*[Create(separator1), Create(separator2)], **{"run_time": 0.4})
        self.wait()
        bottom_text = Tex("Apply Gauss-Jordan Algorithm")
        bottom_text.shift(DOWN * 1.8)
        self.play(FadeIn(bottom_text))
        self.wait()
        self.play(FadeOut(bottom_text))


        for i in range(0, 12):
            self.remove(toFade[i*2])
            self.remove(toFade[i*2+1])
        self.play(*[FadeIn(rref_matrix1), FadeIn(rref_matrix2)])
        self.wait()

        for i in range(0,3):
            row1 = SurroundingRectangle(rref_matrix1.get_rows()[i])
            row2 = SurroundingRectangle(rref_matrix2.get_rows()[i])
            bottom_text1 = MathTex()
            bottom_text2 = MathTex()
            if i == 0:
                bottom_text1 = MathTex("x_{1}", " = 4")
                bottom_text1.shift(LEFT * 3.5 + DOWN * 1.8)
                bottom_text1.set_color_by_tex('x', RED)

                bottom_text2 = MathTex("x_{2}", " = 3")
                bottom_text2.shift(RIGHT * 3 + DOWN * 1.8)
                bottom_text2.set_color_by_tex('x', RED)
            elif i == 1:
                bottom_text1 = MathTex("y_{1}", " = -1")
                bottom_text1.shift(LEFT * 3.5 + DOWN * 1.8)
                bottom_text1.set_color_by_tex('y', GREEN)

                bottom_text2 = MathTex("y_{2}", " = 6")
                bottom_text2.shift(RIGHT * 3 + DOWN * 1.8)
                bottom_text2.set_color_by_tex('y', GREEN)
            else:
                bottom_text1 = MathTex("z_{1}", " = 2")
                bottom_text1.shift(LEFT * 3.5 + DOWN * 1.8)
                bottom_text1.set_color_by_tex('z', BLUE)

                bottom_text2 = MathTex("z_{2}", " = 9")
                bottom_text2.shift(RIGHT * 3 + DOWN * 1.8)
                bottom_text2.set_color_by_tex('z', BLUE)
            self.play(*[Create(row1), Create(row2)], **{"run_time": 1.75})
            self.play(*[Write(bottom_text1), Write(bottom_text2)], **{"run_time": 1.5})
            self.wait()
            self.play(*[FadeOut(row1), FadeOut(row2), FadeOut(bottom_text1), FadeOut(bottom_text2)], **{"run_time": 2})

        self.play(*[FadeOut(rref_matrix1), FadeOut(rref_matrix2), FadeOut(separator1), FadeOut(separator2)])
        center_text1 = Tex("Instead of viewing them as distinct matrices,")
        center_text2 = Tex("we can combine them as one augmented matrix")
        center_text = VGroup(center_text1, center_text2).arrange(DOWN*1.2).shift(DOWN*2.2)
        self.play(FadeIn(center_text), **{"run_time": 1.5})
        self.wait(1.5)
        self.play(FadeOut(center_text))
        self.play(*[ApplyMethod(VGroup(*coefficient_matrix1)[1].shift, RIGHT * 3.1 + LEFT * 0.22), #left bracket
                    ApplyMethod(VGroup(*coefficient_matrix2)[1].shift, LEFT * 3.4 + LEFT * 0.22),   #right bracket
                    ApplyMethod(VGroup(*coefficient_matrix1)[2].shift, RIGHT * 3.9 + RIGHT * 0.22), #left b
                    ApplyMethod(VGroup(*coefficient_matrix2)[2].shift, LEFT * 2.6 + RIGHT * 0.22)]    #right b
                )

        augmented_matrix = Matrix(
            [("1", "0", "0", "4", "3"), ("0", "1", "0", "-1", "6"), ("0", "0", "1", "2", "9")])
        augmented_matrix_flat = VGroup(*VGroup(*augmented_matrix)[0])
        for i in range(0, 15):
            augmented_matrix_flat[i].set_color(big_augmented_matrix_colors[i % 5])
        self.play(FadeIn(augmented_matrix), **{"run_time": 1.2})

        separator1 = Line(RIGHT * 0.6 + UP * 1.1, RIGHT * 0.6 + DOWN * 1.1, color=YELLOW)
        self.play(Create(separator1))
        for j in range(0,2):
            if j == 0:
                for k in range(1,4):
                    self.play(FadeOut(augmented_matrix_flat[k * 5 - j - 1]), **{"run_time":0.4})
            if j == 1:
                for k in range(1,4):
                    self.play(*[FadeIn(augmented_matrix_flat[k * 5 - 1]), FadeOut(augmented_matrix_flat[k * 5 - j - 1])], **{"run_time":0.4})
            for i in range(0, 3):
                row1 = SurroundingRectangle(augmented_matrix.get_rows()[i])
                bottom_text1 = MathTex()
                if i == 0:
                    if j == 0:
                        bottom_text1 = MathTex("x_{1}", " = 4")
                    else:
                        bottom_text1 = MathTex("x_{2}", " = 3")
                    bottom_text1.shift(DOWN * 1.8)
                    bottom_text1.set_color_by_tex('x', RED)
                elif i == 1:
                    if j == 0:
                        bottom_text1 = MathTex("y_{1}", " = -1")
                    else:
                        bottom_text1 = MathTex("y_{2}", " = 6")
                    bottom_text1.shift(DOWN * 1.8)
                    bottom_text1.set_color_by_tex('y', GREEN)
                else:
                    if j == 0:
                        bottom_text1 = MathTex("z_{1}", " = 2")
                    else:
                        bottom_text1 = MathTex("z_{2}", " = 9")
                    bottom_text1.shift(DOWN * 1.8)
                    bottom_text1.set_color_by_tex('z', BLUE)
                self.play(*[Create(row1), Write(bottom_text1)], **{"run_time":1.5})
                self.wait(0.5)
                self.play(*[FadeOut(row1), FadeOut(bottom_text1)])
        finishScene(self)

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
            [(MathTex("x_{11}"), MathTex("x_{12}"), MathTex("x_{13}")),
             (MathTex("x_{21}"), MathTex("x_{22}"), MathTex("x_{23}")),
             (MathTex("x_{31}"), MathTex("x_{32}"), MathTex("x_{33}"))])
        algebra_matrix.next_to(matrix_A, RIGHT)
        equal_sign = MathTex("=", color=BLUE, font_size=72)
        equal_sign.next_to(algebra_matrix, RIGHT)
        identity_matrix = MobjectMatrix(
            [(MathTex("1"), MathTex("0"), MathTex("0")),
             (MathTex("0"), MathTex("1"), MathTex("0")),
             (MathTex("0"), MathTex("0"), MathTex("1"))])
        identity_matrix.next_to(equal_sign, RIGHT)
        identity_matrix_flat = VGroup(*VGroup(*identity_matrix)[0])
        matrix_equation = VGroup(matrix_A, algebra_matrix, equal_sign, identity_matrix)
        matrix_equation.shift(UP * 1.5)
        self.play(*[FadeIn(matrix_A), FadeIn(algebra_matrix), FadeIn(equal_sign), FadeIn(identity_matrix)])

        # row = SurroundingRectangle(rref_matrix.get_rows()[i])
        for i in range(0,3):
            second_column = SurroundingRectangle(algebra_matrix.get_columns()[i])
            self.play(*[Create(second_column), FadeIn(all_algebra_equations[i])])
            for j in range(0,3):
                first_row = SurroundingRectangle(matrix_A.get_rows()[j])
                self.play(Create(first_row), **{"run_time":0.8})
                identity_matrix_rect = SurroundingRectangle(identity_matrix_flat[i*3+j])
                self.play(Create(identity_matrix_rect), **{"run_time":0.8})
                algebra_equation_rect = SurroundingRectangle(all_algebra_equations[i].get_rows()[j], color=ORANGE)
                self.play(Create(algebra_equation_rect), **{"run_time":1.2})
                self.wait(1.25)
                self.play(*[FadeOut(first_row), FadeOut(identity_matrix_rect), FadeOut(algebra_equation_rect)], **{"run_time":0.5})
            all_algebra_equations[i].save_state()
            if i == 0:
                self.play(all_algebra_equations[i].animate.scale(0.6).to_corner(corner=DOWN + LEFT, buff=0.2))
            elif i == 2:
                self.play(all_algebra_equations[i].animate.scale(0.6).to_corner(corner=DOWN + RIGHT, buff=0.2))
            else:
                self.play(all_algebra_equations[i].animate.scale(0.6).to_edge(edge=DOWN, buff=0.2))
            self.play(*[FadeOut(second_column)], **{"run_time": 0.5})

        finishScene(self)

class Last(Scene):
    def construct(self):
        opening_text = Tex("Now let's put all 3 systems of linear equations together!")
        self.play(Write(opening_text), **{"run_time": 1.5})
        self.play(FadeOut(opening_text))

        augmented_matrix = MobjectMatrix(
            [(MathTex("a_{11}"), MathTex("a_{12}"), MathTex("a_{13}"), MathTex("1"), MathTex("0"), MathTex("0")),
             (MathTex("a_{21}"), MathTex("a_{22}"), MathTex("a_{23}"), MathTex("0"), MathTex("1"), MathTex("0")),
             (MathTex("a_{31}"), MathTex("a_{32}"), MathTex("a_{33}"), MathTex("0"), MathTex("0"), MathTex("1"))])

        separator1 = Line(UP * 1.1 + RIGHT * 0.2, DOWN * 1.1 + RIGHT * 0.2, color=YELLOW)
        separator2 = Line(UP * 1.1 + LEFT * 0, DOWN * 1.1 + LEFT * 0, color=YELLOW)
        final_matrix = VGroup(augmented_matrix, separator1)
        final_matrix.shift(UP * 0.5)
        self.play(FadeIn(augmented_matrix), **{"run_time":1.5})
        self.play(Create(separator1), **{"run_time":0.5})

        bottom_text = Tex("Apply the Gauss-Jordan Algorithm")
        bottom_text.shift(DOWN * 1.5)
        self.play(FadeIn(bottom_text))
        self.wait(1)
        self.play(FadeOut(bottom_text))

        answer_matrix = MobjectMatrix(
            [(MathTex("1"), MathTex("0"), MathTex("0"), MathTex("a"), MathTex("b"), MathTex("c")),
             (MathTex("0"), MathTex("1"), MathTex("0"), MathTex("d"), MathTex("e"), MathTex("f")),
             (MathTex("0"), MathTex("0"), MathTex("1"), MathTex("g"), MathTex("h"), MathTex("i"))])
        answer_matrix_flat = VGroup(*VGroup(*augmented_matrix)[0])
        final_matrix2 = VGroup(answer_matrix, separator2)
        final_matrix2.shift(UP * 0.5)
        self.play(Transform(final_matrix, final_matrix2), **{"run_time":1.5})

        true_answer_matrix = MobjectMatrix(
            [(MathTex("1"), MathTex("0"), MathTex("0"), MathTex("x_{11}"), MathTex("x_{12}"), MathTex("x_{13}")),
             (MathTex("0"), MathTex("1"), MathTex("0"), MathTex("x_{21}"), MathTex("x_{22}"), MathTex("x_{23}")),
             (MathTex("0"), MathTex("0"), MathTex("1"), MathTex("x_{31}"), MathTex("x_{32}"), MathTex("x_{33}"))])

        true_answer_matrix.shift(UP * 0.5)
        true_answer_matrix_flat = VGroup(*VGroup(*true_answer_matrix)[0])
        bottom_text = Tex("Let's find out what the values on the right matrix mean")
        bottom_text.shift(DOWN * 1.5)
        self.play(FadeIn(bottom_text), **{"run_time": 0.5})
        ans_rectangle = SurroundingRectangle(answer_matrix.get_columns()[3:6], color=TEAL)
        self.play(Create(ans_rectangle), **{"run_time":1.5})
        self.wait(0.5)
        self.play(*[FadeOut(bottom_text), FadeOut(ans_rectangle)], **{"run_time": 0.75})
        for i in range(0,3):
            self.play(FadeIn(all_algebra_equations[i]))
            for j in range(0,3):
                first_rectangle = SurroundingRectangle(true_answer_matrix.get_rows()[j][0:3], color=ORANGE)
                ans_rectangle = SurroundingRectangle(true_answer_matrix.get_columns()[i+3], color=ORANGE)
                eqn_rectangle = SurroundingRectangle(all_algebra_equations[i].get_rows()[j], color=BLUE)
                self.play(*[Create(first_rectangle), Create(ans_rectangle)])
                self.play(Create(eqn_rectangle))
                self.play(Transform(all_algebra_equations[i].get_rows()[j], sub_all_algebra_equations[i*3+j]))
                resultant = (j * 2 + 1) * 3 + i
                self.play(Transform(answer_matrix_flat[resultant], true_answer_matrix_flat[resultant]))
                self.wait()
                self.play(*[FadeOut(first_rectangle), FadeOut(ans_rectangle), FadeOut(eqn_rectangle)], **{"run_time":1.5 })
            self.wait(0.5)
            self.play(FadeOut(all_algebra_equations[i]))
            toFade = []
            for j in range(1, 32):
                toFade.append(self.mobjects[-j])
            self.play(*[FadeOut(mob) for mob in toFade])
        finishScene(self)

class Full(Scene):
    def construct(self):
        Third.construct()
        Fourth.construct()
        Last.construct()




















