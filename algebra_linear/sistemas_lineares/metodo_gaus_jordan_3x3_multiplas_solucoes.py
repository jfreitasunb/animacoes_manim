from manim import *
import sys
import os
sys.path.append(os.path.abspath("/home/jfreitas/GitHub/animacoes_manim"))
import time
from logo import Logo as l

start = time.time()

#####Define o idioma do vídeo###########################################

texto_br =  True

#####Define as equações do sistema######################################
first_eqn = MathTex("\phantom{0}1", "x_1", "+", "\phantom{0}2", "x_2", "+", "\phantom{0}3", "x_3", "=", "\phantom{0}4")

second_eqn = MathTex("\phantom{0}5", "x_1", "+", "\phantom{0}6", "x_2", "+", "\phantom{0}7", "x_3", "=", "\phantom{0}8")

third_eqn = MathTex("\phantom{0}9", "x_1", "+", "10", "x_2", "+", "11", "x_3", "=", "12")

equations_array = [first_eqn, second_eqn, third_eqn]

equations = MobjectMatrix(
    [[first_eqn], [second_eqn], [third_eqn]],
    left_bracket="\\{",
    right_bracket="\\}")

brackets = equations.get_brackets()

brackets[1].set_color(BLACK)

for eqn in equations_array:
    eqn.set_color_by_tex_to_color_map({
        "x_1": RED,
        "x_2": GREEN,
        "x_3": BLUE,
    })

x1= Tex("$x_1$", color=RED)

x2= Tex("$x_2$", color=GREEN)

x3= Tex("$x_3$", color=BLUE)

augmented_matrix_colors = [RED, GREEN, BLUE, TEAL]

####Textos presentes no vídeo############

if texto_br == True:
    title = Tex(r"Encontre a solução do sistema linear, onde $x_1$, $x_2$ e $x_3 \in \mathbb{R}$:")

    subtitle = Tex(r"Vamos usar o método de eliminação de Gauss-Jordan\\ para encontrar a solução do sistema.")

    primeiro_passo = Tex(r"Primeiro montamos a matriz amplidada do sistema:")

    passo_1 = Tex(r"Como esse coeficiente já é 1, vamos zerar os coeficientes")

    passo_1a = Tex(r"na primeira coluna que estão abaixo do 1.")

    passo_2a = Tex(r"Começamos multiplicando a primeira linha por -5.")

    passo_2b = Tex(r"E somamos com a segunda linha.")

    passo_3a = Tex(r"Agora multiplicamos a primeira linha por -9.")

    passo_3b = Tex(r"E somamos com a terceira linha.")

    passo_4 = Tex(r"Como esse coeficiente é diferente de 1 \\ vamos multiplicar a segunda linha por -1/4.")

    passo_5 = Tex(r"Agora vamos zerar os coeficiente \\ na segunda coluna que estão abaixo e acima do 1.")

    passo_6a = Tex(r"Começamos multiplicando a segunda linha por -2.")

    passo_6b = Tex(r"E somamos com a primeira linha.")

    passo_7a = Tex(r"Agora vamos multiplicar a segunda linha por 8.")

    passo_7b = Tex(r"E somamos com a terceira linha.")

    passo_8a = Tex(r"A matriz resultante desse último passo,")

    passo_8b = Tex(r"está na forma linha reduzida à forma em escada.")

    passo_8c = Tex(r"Observe que a última linha é nula,")

    passo_8d = Tex(r"com isso o sistema admite múltiplas soluções.")

    passo_8e = Tex(r"Vamos encontrar essas soluções.")

    passo_9a = Tex(r"Na matriz abaixo:")

    passo_9b = Tex(r"as três primeiras colunas representam as incógnitas do sistema.")

    passo_9c = Tex(r"Da segunda linha dessa matriz obtemos a equação:")

    passo_9d = Tex(r"que pode ser escrita como: ")

    passo_9e = Tex(r"Da primeira linha dessa matriz obtemos a equação:")

    passo_10a = Tex(r"$x_2 + 2x_3 = 3$")

    passo_10b = Tex(r"$x_2 = 3 - 2x_3$")

    passo_10c = Tex(r"$x_1 - x_3 = -2$")

    passo_10d = Tex(r"$x_1 = -2 + x_3$")

    passo_11a = Tex(r"Assim a solução do sistema")

    passo_11b = Tex(r"é dada pelo conjunto:")

    passo_12 = Tex(r"$S = \{x_1, x_2, x_3 \in \mathbb{R} \mid x_1 = -2 + x_3,\ x_2 = 3 - 2x_3\}$")
else:
    title = Tex(r"Find the solution of the linear system, where $x_1$, $x_2$ and $x_3 \in \mathbb{R}$:")

    subtitle = Tex(r"We are going to apply the Gauss-Jordan Algorithm\\ to find the solution of the linear system.")

    primeiro_passo = Tex(r"First we write the augmented matrix of the system:")

    passo_1 = Tex(r"As this coefficient is 1, we are going to cancel the coefficients")

    passo_1a= Tex(r"in the first column that are bellow 1.")

    passo_2a = Tex(r"We start by multiplying the first row by -5.")

    passo_2b = Tex(r"And we add it to the second row.")

    passo_3a = Tex(r"Now we multiply the first row by -9.")

    passo_3b = Tex(r"And we add it to the third row.")

    passo_4 = Tex(r"This coefficient is different from 1,\\ so we are going to multiply the second row by -1/4.")

    passo_5 = Tex(r"Now lets cancel the coefficients\\ in the second row that are above and below 1.")

    passo_6a = Tex(r"We start by multiplying the second row by -2.")

    passo_6b = Tex(r"And we add it to the first row.")

    passo_7a = Tex(r"Now multiply the second row by 8.")

    passo_7b = Tex(r"And add it to the third row.")

    passo_8a = Tex(r"The matrix resulting from this last step:")

    passo_8b = Tex(r"is in the reduced row echolon form.")

    passo_8c = Tex(r"As the last row the linear is null,")

    passo_8d = Tex(r"the systema admits multiples solutions.")

    passo_8e = Tex(r"Let's find these solutions.")

    passo_9a = Tex(r"In the matrix:")

    passo_9b = Tex(r"the first three columns are for the variables of the system.")

    passo_9c = Tex(r"From the second row of this matrix we have the equation:")

    passo_9d = Tex(r"that can be writen as: ")

    passo_9e = Tex(r"From the first row of this matrix we have the equation:")

    passo_11a = Tex(r"So the solution of the system")

    passo_11b = Tex(r"is given by the set:")

def finishScene(self):
    self.play(*[FadeOut(mob) for mob in self.mobjects])

class Start(Scene):
    def construct(self):
        # l.logo_principal(self, texto_br)

        l.logo_right_corner(self, texto_br)

        VGroup(title, equations).arrange(DOWN)

        self.play(
            Write(title),
            FadeIn(equations, shift=UP),
        )
        self.wait()

        self.add(equations)

        self.play(title.animate.scale(0.8).to_corner(corner=UP*0.1 + LEFT, buff=0.5))

        self.play(equations.animate.scale(0.8).to_corner(corner=UP + LEFT, buff=0.5))

        self.wait(1)

        self.play(Write(subtitle), run_time = 5)

        self.wait(3)

        self.play(FadeOut(subtitle), run_time=1.5)

        self.play(Write(primeiro_passo), run_time = 5)

        self.wait(3)

        self.play(FadeOut(primeiro_passo), run_time=3)

        coefficient_matrix = Matrix(
            [("1", "2", "3", "4"), ("5", "6", "7", "8"), ("9", "10", "11", "12")]
        )

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
            self.remove(fade)

        self.play(ApplyMethod(coefficient_matrix.shift, LEFT*3.5))

        separator1 = Line(LEFT*2.2 + UP*1.1, LEFT*2.2 + DOWN*1.1, color=YELLOW)

        separator2 = Line(RIGHT*4.2 + UP*1.1, RIGHT*4.2 + DOWN*1.1, color=YELLOW)

        self.play(Create(separator1), **{"run_time":0.15})

        for i in range(0,4):
            for j in range(0,3):
                self.play(VGroup(*VGroup(*coefficient_matrix)[0])[i+4*j].animate.set_color(augmented_matrix_colors[i]),**{"run_time": 0.1})

        coefficient_matrix_flat = VGroup(*VGroup(*coefficient_matrix)[0]).copy()

        primeira_entrada = SurroundingRectangle(coefficient_matrix.get_entries()[0], color=RED)

        self.play(Create(primeira_entrada))

        passo_1.shift(DOWN*1.8)

        self.play(Write(passo_1), **{"run_time": 3})

        self.wait(1.5)

        self.play(FadeOut(primeira_entrada))

        passo_1a.shift(DOWN*2.6)

        coluna1 = SurroundingRectangle(coefficient_matrix.get_columns()[0], color=BLUE)

        self.play(Create(coluna1), **{"run_time": 0.4})

        self.play(Write(passo_1a), **{"run_time": 3})

        self.wait(2)

        self.play(FadeOut(passo_1), FadeOut(passo_1a), FadeOut(coluna1), **{"run_time": 0.25})

        passo_2a.shift(DOWN*1.8)

        self.play(Write(passo_2a), **{"run_time": 3})

        linha1p3 = SurroundingRectangle(coefficient_matrix.get_rows()[0], color=BLUE)

        self.play(Create(linha1p3), **{"run_time": 3})

        self.wait(3)

        passo_2b.shift(DOWN*2.5)

        linha2p3 = SurroundingRectangle(coefficient_matrix.get_rows()[1], color=BLUE)

        self.play(ReplacementTransform(linha1p3, linha2p3), Write(passo_2b),**{"run_time":3})

        self.wait(3)

        self.play(FadeOut(passo_2a), FadeOut(passo_2b), FadeOut(linha2p3), **{"run_time": 0.25})

        arrow = Arrow(LEFT*0.9, RIGHT*0.5)

        arrow.next_to(coefficient_matrix, RIGHT)

        self.play(Create(arrow), **{"run_time":0.4})

        self.wait(2)

        rref_matrix_p1 = Matrix(
            [("1", "2", "3", "4"), ("0", "-4", "-8", "-12"), ("9", "10", "11", "12")])

        rref_matrix_p1_flat = VGroup(*VGroup(*rref_matrix_p1)[0])

        rref_matrix_p1.next_to(arrow, RIGHT)

        for i in VGroup(*rref_matrix_p1)[1:]:
            self.play(Write(i))

        text=Text("-5.  +  = ", font_size=36)
        text.shift(DOWN*2.8 + LEFT*3.5)

        for i in range(0,12):
            rref_matrix_p1_flat[i].set_color(augmented_matrix_colors[i%4])
            if i >= 4 and i < 8:

                entrada_11 = coefficient_matrix.get_entries()[i-4].copy()

                entrada_1 = coefficient_matrix.get_entries()[i-4].copy()

                entrada_1.to_corner(DOWN*2.09 + LEFT*6.7)

                entrada_2 = coefficient_matrix.get_entries()[i].copy()

                entrada_22 = coefficient_matrix.get_entries()[i].copy()

                entrada_2.to_corner(DOWN*2.09 + LEFT*8)

                resultado_operacao = rref_matrix_p1_flat[i].copy()

                resultado_operacao.to_corner(DOWN*2.09 + LEFT*9.3)

                self.play(Write(text), **{"run_time": 2})

                self.play(Transform(entrada_11, entrada_1), Transform(entrada_22, entrada_2), **{"run_time": 0.75})

                self.play(Write(resultado_operacao), **{"run_time": 2})

                self.play(Transform(resultado_operacao.copy(), rref_matrix_p1_flat[i]), **{"run_time": 1})

                self.wait(2)

                self.play(FadeOut(text), FadeOut(entrada_11), FadeOut(entrada_22), FadeOut(resultado_operacao),  **{"run_time": 0.2})
            else:
                self.play(Transform(coefficient_matrix_flat[i], rref_matrix_p1_flat[i]), **{"run_time": 0.75})

        separator2 = Line(RIGHT*4 + UP*1.1, RIGHT*4 + DOWN*1.1, color=YELLOW)

        self.play(Create(separator2), **{"run_time": 0.25})

        passo_3a.shift(DOWN*1.8)

        linha1p4 = SurroundingRectangle(rref_matrix_p1.get_rows()[0], color=BLUE)

        self.play(Write(passo_3a), Create(linha1p4), **{"run_time": 3})

        self.wait(3)

        passo_3b.shift(DOWN*2.5)

        linha3p4 = SurroundingRectangle(rref_matrix_p1.get_rows()[2], color=BLUE)

        self.play(ReplacementTransform(linha1p4,linha3p4), Write(passo_3b), **{"run_time": 3})

        self.wait(3)

        self.play(FadeOut(linha3p4), FadeOut(passo_3a), FadeOut(passo_3b), **{"run_time": 0.25})

        self.play(
             *[FadeOut(mob)for mob in self.mobjects]
        )

        l.logo_right_corner(self, texto_br)

        rref_matrix_p1_flat = VGroup(*VGroup(*rref_matrix_p1)[0]).copy()

        rref_matrix_p2 = Matrix(
             [("1", "2", "3", "4"), ("0", "-4", "-8", "-12"), ("0", "8", "-16", "-24")])

        rref_matrix_p1.to_corner(LEFT*0.35 + UP*0.5)

        rref_matrix_p1_flat.to_corner(LEFT + UP)

        rref_matrix_p2_flat = VGroup(*VGroup(*rref_matrix_p2)[0])

        arrow = Arrow(LEFT*0.9, RIGHT*0.5)

        arrow.next_to(rref_matrix_p1, RIGHT)

        self.play(Create(arrow), **{"run_time":0.4})

        rref_matrix_p2.next_to(arrow, RIGHT)

        for i in VGroup(*rref_matrix_p1)[1:]:
            self.play(Write(i))

        for i in range(0,12):
            rref_matrix_p1_flat[i].set_color(augmented_matrix_colors[i%4])
            self.play(Write(rref_matrix_p1_flat[i]), **{"run_time": 0.75})

        separator4 = Line(LEFT*3.5 + UP*1.4, LEFT*3.5 + UP*3.7, color=YELLOW)

        self.play(Create(separator4), **{"run_time": 0.25})

        self.wait(3)

        for i in VGroup(*rref_matrix_p2)[1:]:
            self.play(Write(i))

        text=Text("-9.  +    =  ", font_size=36)
        text.shift(DOWN*2.8 + LEFT*3.5)

        for i in range(0,12):
            rref_matrix_p2_flat[i].set_color(augmented_matrix_colors[i%4])
            if i >= 8 and i < 12:

                entrada_11 = rref_matrix_p1.get_entries()[i-8].copy()

                entrada_1 = rref_matrix_p1.get_entries()[i-8].copy()

                entrada_1.to_corner(DOWN*2.09 + LEFT*6.5)

                entrada_2 = rref_matrix_p1.get_entries()[i].copy()

                entrada_22 = rref_matrix_p1.get_entries()[i].copy()

                entrada_2.to_corner(DOWN*2.09 + LEFT*7.8)

                resultado_operacao = rref_matrix_p2_flat[i].copy()

                resultado_operacao.to_corner(DOWN*2.09 + LEFT*9.6)

                self.play(Write(text), **{"run_time": 2})

                self.play(Transform(entrada_11, entrada_1), Transform(entrada_22, entrada_2), **{"run_time": 0.75})

                self.play(Write(resultado_operacao), **{"run_time": 2})

                self.play(Transform(resultado_operacao.copy(), rref_matrix_p2_flat[i]), **{"run_time": 1})

                self.wait(2)

                self.play(FadeOut(text), FadeOut(entrada_11), FadeOut(entrada_22), FadeOut(resultado_operacao),  **{"run_time": 0.25})
            else:
                self.play(Transform(rref_matrix_p1_flat[i].copy(), rref_matrix_p2_flat[i]), **{"run_time": 0.75})

        separator4 = Line(RIGHT*2.9 + UP*3.6, RIGHT*2.9 + UP*1.4, color=YELLOW)

        self.play(Create(separator4), **{"run_time": 0.25})

        primeira_entrada_segunda_linha = SurroundingRectangle(rref_matrix_p2.get_entries()[5], color=RED)

        self.play(Create(primeira_entrada_segunda_linha))

        passo_4.shift(DOWN*1.4)

        self.play(Write(passo_4), **{"run_time": 3})

        self.wait(2)

        self.play(FadeOut(passo_4), FadeOut(primeira_entrada_segunda_linha), **{"run_time": 0.25})

        self.remove(passo_4, primeira_entrada_segunda_linha)

        rref_matrix_p3 = Matrix(
            [("1", "2", "3", "4"), ("0", "1", "2", "3"), ("0", "-8", "-16", "-24")])

        rref_matrix_p3_flat = VGroup(*VGroup(*rref_matrix_p3)[0])

        arrow = Arrow(LEFT*0.9, RIGHT*0.5)

        arrow.next_to(rref_matrix_p2, RIGHT)

        self.play(Create(arrow), **{"run_time":0.4})

        rref_matrix_p3.next_to(rref_matrix_p1, DOWN)

        for i in VGroup(*rref_matrix_p3)[1:]:
            self.play(Write(i))

        text=Text("(-1/4).       =   ", font_size=36)

        text.shift(DOWN*2.8 + LEFT*3.5)

        for i in range(0,12):
            rref_matrix_p3_flat[i].set_color(augmented_matrix_colors[i%4])
            if i >= 4 and i < 8:

                entrada_11 = rref_matrix_p1.get_entries()[i].copy()

                entrada_1 = rref_matrix_p1.get_entries()[i].copy()

                entrada_1.to_corner(DOWN*2.09 + LEFT*7.6)

                resultado_operacao = rref_matrix_p3_flat[i].copy()

                resultado_operacao.to_corner(DOWN*2.09 + LEFT*10.2)

                self.play(Write(text), **{"run_time": 2})

                self.play(Transform(entrada_11, entrada_1), **{"run_time": 0.75})

                self.play(Write(resultado_operacao), **{"run_time": 2})

                self.play(Transform(resultado_operacao.copy(), rref_matrix_p3_flat[i]), **{"run_time": 1})

                self.wait(2)

                self.play(FadeOut(text), FadeOut(entrada_11), FadeOut(resultado_operacao),  **{"run_time": 0.25})
            else:
                self.play(Transform(rref_matrix_p2_flat[i].copy(), rref_matrix_p3_flat[i]), **{"run_time": 0.75})

        separator5 = Line(LEFT*3.4 + DOWN*1.4, LEFT*3.4 + UP, color=YELLOW)

        self.play(Create(separator5), **{"run_time": 0.25})

        passo_5.shift(DOWN*2.5)

        coluna2 = SurroundingRectangle(rref_matrix_p3.get_columns()[1], color=BLUE)

        self.play(Create(coluna2), Write(passo_5), **{"run_time": 3})

        self.wait(3)

        self.play(FadeOut(passo_5), FadeOut(coluna2), **{"run_time": 0.25})

        passo_6a.shift(DOWN*2.5)

        linha2p7 = SurroundingRectangle(rref_matrix_p3.get_rows()[1], color=BLUE)

        self.play(Write(passo_6a), Create(linha2p7), **{"run_time": 3})

        self.wait(3)

        passo_6b.shift(DOWN*3)

        linha1p7 = SurroundingRectangle(rref_matrix_p3.get_rows()[0], color=BLUE)

        self.play(ReplacementTransform(linha2p7,linha1p7), Write(passo_6b), **{"run_time": 3})

        self.wait(3)

        self.play(FadeOut(linha1p7), FadeOut(passo_6a), FadeOut(passo_6b), **{"run_time": 0.25})

        rref_matrix_p3_flat = VGroup(*VGroup(*rref_matrix_p3)[0]).copy()

        rref_matrix_p4 = Matrix(
            [("1", "0", "-1", "-2"), ("0", "1", "2", "3"), ("0", "-8", "-16", "-24")])

        rref_matrix_p4_flat = VGroup(*VGroup(*rref_matrix_p4)[0])

        arrow = Arrow(LEFT*0.9, RIGHT*0.5)

        arrow.next_to(rref_matrix_p3, RIGHT)

        self.play(Create(arrow), **{"run_time":0.4})

        rref_matrix_p4.next_to(arrow, RIGHT)

        for i in VGroup(*rref_matrix_p4)[1:]:
            self.play(Write(i))

        text=Text("(-2).   +   =   ", font_size=36)

        text.shift(DOWN*2.8 + LEFT*3.5)

        for i in range(0,12):
            rref_matrix_p4_flat[i].set_color(augmented_matrix_colors[i%4])
            if i >= 0 and i < 4:

                entrada_11 = rref_matrix_p3.get_entries()[i+4].copy()

                entrada_1 = rref_matrix_p3.get_entries()[i+4].copy()

                entrada_1.to_corner(DOWN*2.09 + LEFT*6.9)

                entrada_2 = rref_matrix_p3.get_entries()[i].copy()

                entrada_22 = rref_matrix_p3.get_entries()[i].copy()

                entrada_2.to_corner(DOWN*2.09 + LEFT*8.5)

                resultado_operacao = rref_matrix_p4_flat[i].copy()

                resultado_operacao.to_corner(DOWN*2.09 + LEFT*9.7)

                self.play(Write(text), **{"run_time": 2})

                self.play(Transform(entrada_11, entrada_1), Transform(entrada_22, entrada_2), **{"run_time": 0.75})

                self.play(Write(resultado_operacao), **{"run_time": 2})

                self.play(Transform(resultado_operacao.copy(), rref_matrix_p4_flat[i]), **{"run_time": 1})

                self.wait(2)

                self.play(FadeOut(text), FadeOut(entrada_11), FadeOut(entrada_22), FadeOut(resultado_operacao),  **{"run_time": 0.25})
            else:
                self.play(Transform(rref_matrix_p3_flat[i].copy(), rref_matrix_p4_flat[i]), **{"run_time": 0.75})

        separator6 = Line(RIGHT*2.9 + DOWN*1.3, RIGHT*2.9 + UP*1, color=YELLOW)

        self.play(Create(separator6), **{"run_time": 0.25})

        self.wait(3)

        passo_7a.shift(DOWN*2.3)

        linha2p8 = SurroundingRectangle(rref_matrix_p4.get_rows()[1], color=BLUE)

        self.play(Write(passo_7a), Create(linha2p8), **{"run_time": 3})

        self.wait(3)

        passo_7b.shift(DOWN*2.8)

        linha3p8 = SurroundingRectangle(rref_matrix_p4.get_rows()[2], color=BLUE)

        self.play(ReplacementTransform(linha2p8,linha3p8), Write(passo_7b), **{"run_time": 3})

        self.wait(3)

        self.play(FadeOut(linha3p8), FadeOut(passo_7a), FadeOut(passo_7b), **{"run_time": 0.25})

        arrow = Arrow(LEFT*0.9, RIGHT*0.3)

        arrow.next_to(rref_matrix_p4, RIGHT)

        self.play(Create(arrow), **{"run_time":0.4})

        self.wait(3)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        l.logo_right_corner(self, texto_br)

        rref_matrix_p5 = Matrix(
            [("1", "0", "-1", "-2"), ("0", "1", "2", "3"), ("0", "-8", "-16", "-24")])

        rref_matrix_p5_flat = VGroup(*VGroup(*rref_matrix_p5)[0])

        rref_matrix_p5.to_corner(corner=UP + LEFT)

        for i in VGroup(*rref_matrix_p5)[1:]:
            self.play(Write(i))

        for i in range(0,12):
            rref_matrix_p5_flat[i].set_color(augmented_matrix_colors[i%4])
            self.play(Write(rref_matrix_p5_flat[i]), **{"run_time": 0.75})

        separator7 = Line(LEFT*3.15 + UP*3.4, LEFT*3.15 + UP*1.1, color=YELLOW)

        self.play(Create(separator7), **{"run_time": 0.25})

        self.wait(2)

        arrow = Arrow(LEFT*0.9, RIGHT*0.5)

        arrow.next_to(rref_matrix_p5, RIGHT)

        self.play(Create(arrow), **{"run_time":0.4})

        rref_matrix_p6 = Matrix(
            [("1", "0", "-1", "-2"), ("0", "1", "2", "3"), ("0", "0", "0", "0")])

        rref_matrix_p6_flat = VGroup(*VGroup(*rref_matrix_p6)[0])

        rref_matrix_p6.next_to(arrow, RIGHT)

        for i in VGroup(*rref_matrix_p6)[1:]:
            self.play(Write(i))

        text=Text("8.   +       =  ", font_size=36)

        text.shift(DOWN*2.8 + LEFT*3.5)

        for i in range(0,12):
            rref_matrix_p4_flat[i].set_color(augmented_matrix_colors[i%4])
            if i >= 8 and i < 12:

                entrada_11 = rref_matrix_p5.get_entries()[i-4].copy()

                entrada_1 = rref_matrix_p5.get_entries()[i-4].copy()

                entrada_1.to_corner(DOWN*2.09 + LEFT*5.8)

                entrada_2 = rref_matrix_p5.get_entries()[i].copy()

                entrada_22 = rref_matrix_p5.get_entries()[i].copy()

                entrada_2.to_corner(DOWN*2.09 + LEFT*7.5)

                resultado_operacao = rref_matrix_p6_flat[i].copy()

                resultado_operacao.to_corner(DOWN*2.09 + LEFT*9.9)

                self.play(Write(text), **{"run_time": 2})

                self.play(Transform(entrada_11, entrada_1), Transform(entrada_22, entrada_2), **{"run_time": 0.75})

                self.play(Write(resultado_operacao), **{"run_time": 2})

                self.play(Transform(resultado_operacao.copy(), rref_matrix_p6_flat[i]), **{"run_time": 1})

                self.wait(2)

                self.play(FadeOut(text), FadeOut(entrada_11), FadeOut(entrada_22), FadeOut(resultado_operacao),  **{"run_time": 0.25})
            else:
                self.play(Transform(rref_matrix_p5_flat[i].copy(), rref_matrix_p6_flat[i]), **{"run_time": 0.75})

        separator8 = Line(RIGHT*3.5 + UP*3.4, RIGHT*3.5 + UP*1.1, color=YELLOW)

        self.play(Create(separator8), **{"run_time": 0.25})

        self.wait(3)

        self.play(Write(passo_8a), **{"run_time":3})

        passo_8b.shift(DOWN*0.8)

        self.play(Write(passo_8b), **{"run_time":3})

        self.play(FadeOut(passo_8a), FadeOut(passo_8b), **{"run_time": 0.74})

        linha3pf = SurroundingRectangle(rref_matrix_p6.get_rows()[2], color=BLUE)

        self.play(Write(passo_8c), Create(linha3pf), **{"run_time": 3})

        passo_8d.shift(DOWN*0.8)

        self.play(Write(passo_8d), **{"run_time": 3})

        self.play(FadeOut(passo_8c), FadeOut(passo_8d), **{"run_time": 0.74})

        self.play(Write(passo_8e), **{"run_time": 3})

        self.play(
             *[FadeOut(mob)for mob in self.mobjects]
        )

        l.logo_right_corner(self, texto_br)

        rref_matrix_p7 = Matrix(
            [("1", "0", "-1", "-2"), ("0", "1", "2", "3"), ("0", "0", "0", "0")])

        rref_matrix_p7_flat = VGroup(*VGroup(*rref_matrix_p7)[0])

        passo_9a.shift(UP*2.5)

        self.play(Write(passo_9a), **{"run_time": 3})

        for i in VGroup(*rref_matrix_p7)[1:]:
             self.play(Write(i))

        for i in range(0,12):
             rref_matrix_p7_flat[i].set_color(augmented_matrix_colors[i%4])
             self.play(Write(rref_matrix_p7_flat[i]), **{"run_time": 0.75})

        separator11 = Line(RIGHT*1.2 + DOWN, RIGHT*1.2 + UP*1.05, color=YELLOW)

        self.play(Create(separator11), **{"run_time":0.15})

        passo_9b.shift(DOWN*2)

        self.play(Write(passo_9b), **{"run_time": 3})

        x1.shift(UP*1.25 + LEFT*1.9)

        x2.shift(UP*1.25 + LEFT*0.7)

        x3.shift(UP*1.25 + RIGHT*0.55)

        self.play(Write(x1), Write(x2), Write(x3), **{"run_time": 0.25})

        self.wait(5)

        self.play(FadeOut(passo_9b), **{"run_time": 0.5})

        passo_9c.shift(DOWN*2)

        passo_9d.shift(DOWN*3.2+LEFT*2.5)

        passo_10a.shift(DOWN*2.7)

        passo_10b.shift(DOWN*3.2+RIGHT*2.5)

        row2 = SurroundingRectangle(rref_matrix_p7.get_rows()[1])

        self.play(Write(passo_9c), Create(row2), **{"run_time": 1.75})

        self.play(Write(passo_10a), **{"run_time": 1.75})

        self.wait(3)

        self.play(Write(passo_9d), **{"run_time": 1.75})

        self.play(Transform(passo_10a.copy(), passo_10b), replace_mobject_with_target_in_scene = True, **{"run_time": 1.75})

        self.wait(5)

        self.play(FadeOut(row2), FadeOut(passo_9c), FadeOut(passo_9d), FadeOut(passo_10a), FadeOut(passo_10b), **{"run_time": 1.75})

        passo_temp1 = passo_10b.copy()

        passo_temp1.to_edge(UP + LEFT)

        self.play(Write(passo_temp1))

        self.wait(5)

        passo_9e.shift(DOWN*2)

        passo_10c.shift(DOWN*2.7)

        passo_10d.shift(DOWN*3.2+RIGHT*2.5)

        row3 = SurroundingRectangle(rref_matrix_p7.get_rows()[0])

        self.play(Write(passo_9e), Create(row3), **{"run_time": 1.75})

        self.play(Write(passo_10c), **{"run_time": 1.75})

        self.wait(3)

        self.play(Write(passo_9d), **{"run_time": 1.75})

        self.play(Transform(passo_10c.copy(), passo_10d), replace_mobject_with_target_in_scene = True, **{"run_time": 1.75})

        self.wait(5)

        self.play(FadeOut(row3), FadeOut(passo_9a), FadeOut(passo_9e), FadeOut(passo_9d), FadeOut(passo_10c), FadeOut(passo_10d), **{"run_time": 1.75})

        passo_temp2 = passo_10d.copy()

        passo_temp2.to_edge(UP*2 + LEFT)

        self.play(Write(passo_temp2))

        self.wait(5)

        self.play(
             *[FadeOut(mob)for mob in self.mobjects]
        )

        l.logo_right_corner(self, texto_br)

        passo_11a.shift(UP*2)

        self.play(Write(passo_11a), **{"run_time": 2.75})

        self.play(FadeIn(equations, shift=UP))

        self.add(equations)

        passo_11b.shift(DOWN*2)

        self.play(Write(passo_11b), **{"run_time": 2.75})

        passo_12.shift(DOWN*3.7)

        self.play(Write(passo_12), **{"run_time": 4})

        self.wait(10)

        finishScene(self)

        l.logo_right_corner(self, texto_br)

        l.fechamento(self, texto_br)

        print("GPU Render Time: %s seconds" % (str(time.time() - start)))
