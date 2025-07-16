from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Input, TextArea, Label

class Agenda(App):

    lista = [
        "Lucas - lucas.a1@email.com",
        "Pedro - Pedro@emnail.com",
        "Leo - leo@email.com",
        "Jessica@email.com"
    ]

    def compose(self) -> ComposeResult:
        with HorizontalGroup():
            yield Label("Email:")
            yield Input(id="campo")
        yield TextArea(disabled=True, id="resultado")

    def on_input_changed(self, event: Input.Changed) -> None:
        texto_input = event.value.capitalize()
        resultado_da_filtragem = self.filtrar(texto_input)
        self.query_one("#resultado", TextArea).text = resultado_da_filtragem

    def filtrar(self, texto_input):
        contatos = ""
        for contato in self.lista:
            if contato.startswith(texto_input):
                contatos += contato + "\n" 
        return contatos
    
    def on_mount(self):
        self.query_one("#resultado", TextArea).text = "\n".join(contato for contato in self.lista)


if __name__ == "__main__":
    Agenda().run()