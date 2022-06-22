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

augmented_matrix_colors = [RED, GREEN, BLUE, TEAL]

def finishScene(self):
    self.play(*[FadeOut(mob) for mob in self.mobjects])

class Start(Scene):
    def construct(self):
        title = Tex(r"Encontre a solução do sistema linear:")
        VGroup(title, equations).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(equations, shift=UP),
        )
        self.wait()

        self.add(equations)
        self.play(title.animate.scale(0.8).to_corner(corner=UP*0.1 + LEFT, buff=0.5))
        self.play(equations.animate.scale(0.8).to_corner(corner=UP + LEFT, buff=0.5))
        self.wait(0.5)

        primeiro_passo = Tex(r"Primeiro montamos a matriz amplidada do sistema:")

        self.play(Write(primeiro_passo), run_time = 5)

        self.wait(2.5)

        self.play(FadeOut(primeiro_passo), run_time=3)
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
        primeira_entrada = SurroundingRectangle(coefficient_matrix.get_entries()[0][0], color=RED)
        self.play(Create(primeira_entrada))
        rref_matrix = Matrix(
            [("1", "-3", "4", "15"), ("3", "1", "-2", "7"), ("2", "-2", "1", "12")])
        rref_matrix_flat = VGroup(*VGroup(*rref_matrix)[0])
        rref_matrix.shift(RIGHT*3)
        bottom_text = Tex(r"Como esse coeficiente é diferente de 1 \\ vamos trocar a primeira linha com a segunda linha.")
        bottom_text.shift(DOWN*1.8)
        self.play(Write(bottom_text), **{"run_time":1})
        self.wait()
        for i in VGroup(*rref_matrix)[1:]:
            self.play(Write(i))
        arrow = Arrow(LEFT*0.9, RIGHT*0.5)
        arrow = Arrow(LEFT*0.9, RIGHT*0.5)
        self.play(Create(arrow), **{"run_time":0.4})
        for i in range(0,12):
            rref_matrix_flat[i].set_color(augmented_matrix_colors[i%4])
            if i < 4:
                rref_matrix_flat[i+4].set_color(augmented_matrix_colors[i%4])
                self.play(Transform(coefficient_matrix_flat[i], rref_matrix_flat[i+4]), **{"run_time": 0.75})
            if i > 3 and i < 8:
                rref_matrix_flat[i-4].set_color(augmented_matrix_colors[i%4])
                self.play(Transform(coefficient_matrix_flat[i], rref_matrix_flat[i-4]), **{"run_time": 0.75})
            if i > 7 and i < 12:
                self.play(Transform(coefficient_matrix_flat[i], rref_matrix_flat[i]), **{"run_time": 0.75})


        self.play(Create(separator2), **{"run_time": 0.25})
        self.wait()
        self.remove(bottom_text)

        bottom_text = Tex(r"Agora vamos zerar os coeficiente na primeira coluna que estão abaixo do 1.")
        bottom_text.shift(DOWN*1.8)
        coluna1 = SurroundingRectangle(rref_matrix.get_columns()[0], color=BLUE)
        self.play(Create(coluna1), **{"run_time":0.4})
        self.play(Write(bottom_text), **{"run_time":1})
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
