from manim import *


class HelloManim(Scene):
    def construct(self):
        title = Text("Hello, Manim")
        formula = MathTex(r"\int_0^1 x^2\,dx = \frac{1}{3}")
        formula.next_to(title, DOWN)
        self.play(Write(title))
        self.play(Write(formula))
        self.wait(1)
