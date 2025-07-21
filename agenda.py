from textual.app import App
from textual.widgets import Input, TextArea, Label
from textual.events import Click
from textual.containers import HorizontalGroup, VerticalGroup


class Agenda(App):

    CSS = '''
        #container {
            height: 14;
            width: 50%;
            padding: 1;
            color: white;
            background: black;
            margin-bottom: 3;
        }
        #conteudo {
            height: 14;
            width: 100%;
            padding: 1;
            color: black;
            background: white;
            margin-bottom: 3;
        }
        .contatos {
            margin-bottom: 1;
        }
        #lbl_nome {
            margin-top: 1;
        }
    '''

    lista_nomes = { # Chaves horriveis, tem que serem únicas, melhor usar o email.
                   # Botar emojis manualmente também está errado
        "lucas": ["📧 lucas@email.com", "📞 51000000000", "🏢 Avenida Bento Gonçalves 203"],
        "leonardo": ["📧 leonardo@email.com", "📞 51111111111", "🏢 Lopo Gonçalves 23"],
        "william": ["📧 william@email.com", "📞 51333333333", "🏢 João Portinha 193"],
        "gabriele": ["📧 gabriele@email.com","📞 51444444444", "🏢 Travessa Ferreira de Abreu 94"],
        "yuri": ["📧 yuri@email.com","📞 51555555555", "🏢 Felipe de Oliveira 97"],
        "arthur": ["📧 arthur@email.com","📞 51666666666", "🏢 Zélia Maria Abichequer 400"]
    }

    contatos = ""

    async def on_input_changed(self, event: Input.Changed):
        vertical = self.query_one("#container", VerticalGroup)
        await vertical.remove_children() 
        texto_input = event.value.lower()
        self.contatos = self.filtrar(texto_input)
        for contato in self.contatos:
            vertical.mount(Label(f"👤 {contato.capitalize()}", id=f"{contato}", classes="contatos")) # To removendo os Labels e criando novos iguais toda vez que filtro, horrivel para otimização
                         
    def filtrar(self, texto_input):
        lista_contatos = []
        for contato in self.lista_nomes.keys():
            if contato.startswith(texto_input):
                lista_contatos.append(contato)
        return lista_contatos

    def compose(self):
        with HorizontalGroup():
            with VerticalGroup(id="container"):
                for contato in self.lista_nomes.keys():
                    yield Label(f"👤 {contato.capitalize()}", id=contato, classes="contatos")
            with HorizontalGroup(id="resultado"):
                pass
        with HorizontalGroup():
            yield Label("Digite o nome:", id="lbl_nome")
            yield Input(placeholder="Digite aqui")


    def on_click(self, evento: Click):
        if isinstance(evento.widget, Label):
            try:
                self.query_one("#conteudo", TextArea).remove() # Horrivel pra otimização, tem que arrumar, cai muitas vezes no except
            except:
                horizontal = self.query_one("#resultado", HorizontalGroup)
                horizontal.mount(TextArea(id="conteudo"))
                self.query_one("#conteudo", TextArea).text = "\n\n".join(
                        str(informacoes) for informacoes in self.lista_nomes[evento.widget.id])


Agenda().run()
