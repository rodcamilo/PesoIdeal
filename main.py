from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class CalcIMC(App):
    def build(self):
        # Variáveis de estado para controlar a sequência de entrada
        self.altura = None
        self.massa = None

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Divisória ajustada para 45 caracteres para caber em telas mobile sem vazar
        self.sep = "============================================="

        self.output = Label(
            text=f"\n[color=#FFFFFF]{self.sep}[/color]\n"
            "[color=#FFFFFF]CALCULADORA DE PESO IDEAL (IMC)[/color]\n"
            f"[color=#FFFFFF]{self.sep}[/color]\n"
            "[color=#FFFFFF]Informe sua altura (apenas 3 números, ex: 175):[/color]",
            size_hint_y=None, 
            markup=True,
            halign='center'
        )
        
        # Mantém a altura dinâmica conforme o texto cresce
        self.output.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        
        scroll = ScrollView(size_hint=(1, 0.7))
        scroll.add_widget(self.output)
        layout.add_widget(scroll)

        # Entrada de texto
        self.input_dado = TextInput(
            hint_text="Digite a altura", 
            multiline=False, 
            input_filter='int', 
            size_hint_y=None, 
            height=100
        )
        self.input_dado.bind(on_text_validate=self.processar_calculo)
        layout.add_widget(self.input_dado)

        btn = Button(text="ENVIAR", size_hint_y=None, height=100)
        btn.bind(on_press=self.processar_calculo)
        layout.add_widget(btn)

        return layout

    def processar_calculo(self, instance):
        valor_str = self.input_dado.text.strip()
        self.input_dado.text = ""
        self.input_dado.focus = True

        if not valor_str.isdigit():
            return

        valor = int(valor_str)

        # Passo 1: Receber Altura
        if self.altura is None:
            self.altura = valor
            self.input_dado.hint_text = "Digite o peso/massa"
            log = (
                f"[color=#FFFFFF]Altura informada: {self.altura} cm[/color]\n"
                "[color=#FFFFFF]Informe seu peso/massa (arredondado, sem decimais):[/color]"
            )
            self.output.text += f"\n{log}"
            return

        # Passo 2: Receber Peso e Processar o Cálculo
        self.massa = valor
        
        altura = self.altura
        massa = self.massa
        
        imc = massa / ((altura * altura) / 10000)
        alvomin = ((altura * altura) * 18.5) / 10000
        alvomax = ((altura * altura) * 24.99) / 10000

        log_resultado = f"[color=#FFFFFF]{self.sep}[/color]\n"
        log_resultado += f"[color=#FFFFFF]Seu IMC é {round(imc, 2)}.[/color]\n"

        if imc < 17:
            log_resultado += f"[color=#FF0000]MAGREZA SEVERA/DESNUTRIÇÃO![/color]\n"
        elif imc < 18.5:
            log_resultado += f"[color=#FFFF00]ABAIXO do peso/massa ideal.[/color]\n"
        elif imc < 25:
            log_resultado += f"[color=#00FF00]Peso/massa IDEAL.[/color]\n"
        elif imc < 30:
            log_resultado += f"[color=#FFFF00]ACIMA do peso/massa ideal.[/color]\n"
        elif imc < 35:
            log_resultado += f"[color=#FF0000]OBESIDADE![/color]\n"
        elif imc < 40:
            log_resultado += f"[color=#FF0000]OBESIDADE SEVERA![/color]\n"
        else:
            log_resultado += f"[color=#FF0000]OBESIDADE MÓRBIDA![/color]\n"

        log_resultado += f"[color=#FFFFFF]Seu peso/massa ideal é entre {round(alvomin, 2)} e {round(alvomax, 2)}.[/color]\n"
        log_resultado += f"[color=#FFFFFF]{self.sep}[/color]\n"
        log_resultado += "[color=#FFFFFF]Para novo cálculo, informe a altura (ex: 175):[/color]"

        self.output.text += f"\n{log_resultado}"

        # Reseta as variáveis para permitir novo cálculo imediato
        self.altura = None
        self.massa = None
        self.input_dado.hint_text = "Digite a altura"

if __name__ == "__main__":
    CalcIMC().run()