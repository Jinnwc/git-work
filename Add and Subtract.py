import flet as ft

def main(page: ft.Page):
    page.title = "Basic Calculator"
    page.scroll = "auto"

    num1 = ft.TextField(label="Number 1", width=150)
    num2 = ft.TextField(label="Number 2", width=150)
    result = ft.Text(value="", size=16)

    def add_subtract(e):
        try:
            a = float(num1.value)
            b = float(num2.value)

            if e.control.text == "+":
                result.value = f"Result: {a + b}"
            elif e.control.text == "-":
                result.value = f"Result: {a - b}"
        except:
            result.value = "Error: Invalid input"

        page.update()

    page.add(
        ft.Column(
            [
                ft.Row([num1, num2]),
                ft.Row(
                    [
                        ft.ElevatedButton("+", on_click=add_subtract),
                        ft.ElevatedButton("-", on_click=add_subtract),
                    ]
                ),
                result,
            ]
        )
    )

ft.app(target=main)