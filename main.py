import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Peso Ideal"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    txt_altura = ft.TextField(label="Altura em cm (ex: 175)", keyboard_type=ft.KeyboardType.NUMBER)
    txt_massa = ft.TextField(label="Peso/Massa em kg (ex: 70)", keyboard_type=ft.KeyboardType.NUMBER)
    lbl_resultado = ft.Text(size=16, weight=ft.FontWeight.BOLD)

    def calcular(e):
        try:
            altura = int(txt_altura.value)
            massa = int(txt_massa.value)
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

            lbl_resultado.value = f"IMC: {round(imc, 2)}\n{status}\nPeso Ideal: {round(alvomin, 2)}kg a {round(alvomax, 2)}kg"
        except (ValueError, TypeError):
            lbl_resultado.value = "Por favor, insira valores inteiros válidos!"
        page.update()

    btn_calcular = ft.ElevatedButton("Calcular IMC", on_click=calcular)
    page.add(txt_altura, txt_massa, btn_calcular, lbl_resultado)

if __name__ == "__main__":
    ft.app(target=main)