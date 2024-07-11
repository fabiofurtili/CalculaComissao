#########################################################
## Desenvolvido por Fábio Furtili para empresa Safeeds ##
#########################################################

import flet as ft
import pandas as pd

def main(page: ft.Page):
    page.title = "App CalculaCom"
    page.window_width = 350
    page.window_height = 600
    page.window_always_on_top = True
    page.window_resizable = False

    preco_geral = ft.TextField(label="Preço Geral", width=300)
    preco_unitario = ft.TextField(label="Preço Unitário", width=300)
    icms = ft.TextField(label="ICMS (se houver)", width=300)
    encargos = ft.TextField(label="Encargos (se houver)", width=300)

    def on_enter(e, next_control):
        next_control.focus()
        page.update()

    preco_geral.on_submit = lambda e: on_enter(e, preco_unitario)
    preco_unitario.on_submit = lambda e: on_enter(e, icms)
    icms.on_submit = lambda e: on_enter(e, encargos)
    encargos.on_submit = lambda e: calcular_click(None)

    def buscar_referencia(fator):
        try:
            df = pd.read_excel('dados.xlsx', sheet_name='dados')
            
            menor_fator = df[df['Fator'] <= fator].sort_values(by='Fator', ascending=False)
            
            if menor_fator.empty:
                return "Fator muito baixo, lista não encontrada."
            
            ultimo_fator = df['Fator'].min()
            if menor_fator.iloc[0]['Fator'] < ultimo_fator:
                return "Fator muito baixo, lista não encontrada."
            
            return menor_fator.iloc[0]['Lista']
        except Exception as e:
            print(f"Erro ao carregar a planilha: {e}")
            return "Erro ao carregar a planilha"

    def calcular_click(e):
        try:
            pg = float(preco_geral.value.replace(',', '.')) if preco_geral.value else 0
            pu = float(preco_unitario.value.replace(',', '.')) if preco_unitario.value else 0
            icms_valor = float(icms.value.replace(',', '.')) if icms.value else 0
            encargos_valor = float(encargos.value.replace(',', '.')) if encargos.value else 0
            
            #Logica de calculo de comissão
            encargo_dividido = encargos_valor / 100
            valor_ajustado_encargo = pu - (pu * encargo_dividido)
            icms_dividido = icms_valor / 100
            valor_ajustado_icms = valor_ajustado_encargo - (valor_ajustado_encargo * icms_dividido)
            comissao = valor_ajustado_icms / pg

            referencia = buscar_referencia(comissao)

            resultado.value = f"Fator (3 casas): {comissao:.3f}\nFator (8 casas): {comissao:.8f}\nLista: {referencia}"
            page.update()
        except ValueError as ve:
            resultado.value = "Por favor, insira valores numéricos válidos."
            page.update()
        except Exception as ex:
            resultado.value = "Ocorreu um erro."
            page.update()

    botao_calcular = ft.CupertinoFilledButton(text="Calcular", on_click=calcular_click)

    resultado = ft.TextField(label="Resultado", multiline=True, width=300, height=200, read_only=True)

    page.controls.append(
        ft.Column(
            [
                preco_geral,
                preco_unitario,
                icms,
                encargos,
                ft.Row([botao_calcular], alignment=ft.MainAxisAlignment.CENTER),
                resultado,
                ft.Text("Desenvolvido por Fábio Furtili", size=10, italic=True, color=ft.colors.GREY)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    page.update()

ft.app(target=main)
