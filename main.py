from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.95, 0.95, 0.95, 1)

class PesoIdealApp(App):
    def build(self):
        self.title = "PesoIdeal"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text="CALCULADORA DE PESO IDEAL", color=(0, 0, 0, 1), font_size='18sp', bold=True))

        self.input_altura = TextInput(hint_text="Altura em cm (ex: 175)", input_filter='int', multiline=False)
        layout.add_widget(self.input_altura)

        self.input_massa = TextInput(hint_text="Peso/Massa em kg (ex: 70)", input_filter='int', multiline=False)
        layout.add_widget(self.input_massa)

        btn = Button(text="Calcular IMC", background_color=(0.1, 0.6, 0.4, 1))
        btn.bind(on_press=self.calcular)
        layout.add_widget(btn)

        self.lbl_resultado = Label(text="", color=(0, 0, 0, 1), font_size='14sp', halign='center')
        layout.add_widget(self.lbl_resultado)

        return layout

    def calcular(self, instance):
        try:
            altura = int(self.input_altura.text)
            massa = int(self.input_massa.text)
            imc = massa / ((altura * altura) / 10000)
            alvomin = ((altura * altura) * 18.5) / 10000
            alvomax = ((altura * altura) * 24.99) / 10000

            if imc < 17:
                status = "Você está MUITO ABAIXO do peso ideal."
            elif imc < 18.5:
                status = "Você está ABAIXO do peso ideal."
            elif imc < 25:
                status = "Você está com o peso IDEAL."
            elif imc < 30:
                status = "Você está ACIMA do peso ideal."
            elif imc < 35:
                status = "Você está OBESO, procure um médico."
            elif imc < 40:
                status = "OBESIDADE SEVERA, procure um médico urgente."
            else:
                status = "OBESIDADE MÓRBIDA, risco elevado."

            self.lbl_resultado.text = f"IMC: {round(imc, 2)}\n{status}\nPeso Ideal: {round(alvomin, 2)}kg a {round(alvomax, 2)}kg"
        except ValueError:
            self.lbl_resultado.text = "Por favor, insira valores inteiros válidos!"

if __name__ == "__main__":
    PesoIdealApp().run()