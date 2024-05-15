# Título: MarsuZap
# Botão de iniciar chat
    # popup
    # Título: Bem-vindo ao MarsuZap
    # Campo de texto: Escreva seu nome
    # Botão: Entrar no chat
        # Sumir com o título
        # fechar o popup
        # carregar o chat
            # as mensagens que já foram enviadas
            # campo: Digite sua mensagem
            # botão enviar

import flet as ft

# criar a principal função do seu app

def main(page):
    # criar todas as funcionalidades

    
    # cria elemento

    titulo = ft.Text("MarsuZap")

    titulo_janela = ft.Text("Bem-vindo ao MarsuZap")
    campo_nome = ft.TextField(label="Escreva seu nome")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        page.update()

    page.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_msg(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome.value
        mensagem = f"{nome_usuario}: {texto_mensagem}"
        page.pubsub.send_all(mensagem)
        campo_mensagem.value = ""
        page.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_msg)
    botao_send = ft.ElevatedButton("Enviar", on_click=enviar_msg)
    linha_msg = ft.Row([campo_mensagem, botao_send])

    def entrar_chat(evento):
        page.remove(titulo)
        page.remove(botao_iniciar)
        janela.open = False

        page.add(chat)
        page.add(linha_msg)
        mensagem = f"{campo_nome.value} entrou no chat!"
        page.pubsub.send_all(mensagem)
        page.update()

    botao = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome, actions=[botao])

    def iniciar_chat(evento):
        page.dialog = janela
        janela.open = True
        page.update()

    botao_iniciar = ft.ElevatedButton("Iniciar", on_click=iniciar_chat)

    # adiciona o elemento na página
    page.add(titulo)
    page.add(botao_iniciar)

# rodar app
ft.app(main, view=ft.WEB_BROWSER)
