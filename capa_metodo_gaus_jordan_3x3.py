from manim import *
import sys
import os
sys.path.append(os.path.abspath("/home/jfreitas/GitHub_Repos/animacoes_manim"))
from logo import Logo as l

first_eqn = MathTex("3", "x", "+", "1", "y", "-", "2", "z", "=", "7")

second_eqn = MathTex("1", "x", "-", "3", "y", "+", "4", "z", "=", "15")

third_eqn = MathTex("2", "x", "-", "2", "y", "+", "1", "z", "=", "12")

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

####Textos presentes no vídeo############
texto_br = False

if texto_br == True:
    title = Tex(r"Encontre a solução do sistema linear, onde $x$, $y$ e $z \in \mathbb{R}$:")

    subtitle = Tex(r"Vamos usar o Método de eliminação de Gauss-Jordam para encontrar a solução do sistema.")

    primeiro_passo = Tex(r"Primeiro montamos a matriz amplidada do sistema:")

    passo_1 = Tex(r"Como esse coeficiente é diferente de 1 \\ vamos trocar a primeira linha com a segunda linha.")

    passo_2= Tex(r"Agora vamos zerar os coeficiente \\ na primeira coluna que estão abaixo do 1.")

    passo_3a = Tex(r"Começamos multiplicando a primeira linha por -3.")

    passo_3b = Tex(r"E somamos com a segunda linha.")

    passo_4a = Tex(r"Agora multiplicamos a primeira linha por -2.")

    passo_4b = Tex(r"E somamos com a terceira linha.")

    passo_5 = Tex(r"Como esse coeficiente é diferente de 1 \\ vamos multiplicar a segunda linha por 1/10.")

    passo_6= Tex(r"Agora vamos zerar os coeficiente \\ na segunda coluna que estão abaixo e acima do 1.")

    passo_7a = Tex(r"Começamos multiplicando a segunda linha por 3.")

    passo_7b = Tex(r"E somamos com a primeira linha.")

    passo_8a = Tex(r"Agora vamos multiplicar a segunda linha por -4.")

    passo_8b = Tex(r"E somamos com a terceira linha.")

    passo_9 = Tex(r"Como esse coeficiente é diferente de 1 \\ vamos multiplicar a terceira linha por -5/7.")

    passo_10 = Tex(r"Agora vamos zerar os coeficiente \\ na terceira coluna que estão acima do 1.")

    passo_11a = Tex(r"Começamos multiplicando a terceira linha por 7/5.")

    passo_11b = Tex(r"E somamos com a segunda linha.")

    passo_12a = Tex(r"Agora multiplicamos a terceira linha por 1/5.")

    passo_12b = Tex(r"E somamos com a primeira linha.")

    passo_13a = Tex(r"A matriz resultante desse último passo:")

    passo_13b = Tex(r"está na forma linha reduzida à forma em escada. Com isso\\ o sistema admite uma única solução que será:")
else:
    title = Tex(r"Find the solution of the linear system, where $x$, $y$ and $z \in \mathbb{R}$:")

    subtitle = Tex(r"We are going to apply the Gauss-Jordan Algorithm\\ to find the solution of the linear system.")

    primeiro_passo = Tex(r"First we write the augmented matrix of the system:")

    passo_1 = Tex(r"This coefficient is different from 1 \\ so we are going to swap the first and second row.")

    passo_2= Tex(r"Now lets cancel the coefficients\\ in the first column that are bellow 1.")

    passo_3a = Tex(r"We start by multiplying the first row by -3.")

    passo_3b = Tex(r"And we add it to the second row.")

    passo_4a = Tex(r"Now we multiply the first row by -2.")

    passo_4b = Tex(r"And we add it to the third row.")

    passo_5 = Tex(r"This coefficient is different from 1,\\ so we are going to multiply the second row by 1/10.")

    passo_6= Tex(r"Now lets cancel the coefficients\\ in the second row that are above and below 1.")

    passo_7a = Tex(r"We start by multiplying the second row by 3.")

    passo_7b = Tex(r"And we add it to the first row.")

    passo_8a = Tex(r"Now multiply the second row by -4.")

    passo_8b = Tex(r"And add it to the third row.")

    passo_9 = Tex(r"This coefficient is different from 1,\\ so we multiply the third row by -5/7.")

    passo_10 = Tex(r"Lets cancel the coefficients in the third column that are above 1.")

    passo_11a = Tex(r"Multiply the third row by 7/5.")

    passo_11b = Tex(r"And add it to the second row.")

    passo_12a = Tex(r"Then multiply the third row by 1/5.")

    passo_12b = Tex(r"And add it to the first row.")

    passo_13a = Tex(r"The matrix resulting from this last step:")

    passo_13b = Tex(r"is in the reduced row echolon form.\\ Thus, the linear systema admits a unique solution that will be:")


def finishScene(self):
    self.play(*[FadeOut(mob) for mob in self.mobjects])

class Start(Scene):
    def construct(self):

        title.shift(UP*2)
        self.add(title,equations)


