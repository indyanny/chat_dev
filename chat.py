#INSTALACOES INICIAIS
#pip install flet 

import flet as ft 

#FUNCAO PRINCIPAL
def main(page):
    title = ft.Text("What's Up")
    title_popup = ft.Text("Bem vindo ao Chat")
    username_space = ft.TextField(label="Escreva seu nome no chat")
    
    chat = ft.Column()
    
    def send_tunnel_message(message):
        text_chat = ft.Text(message)
        chat.controls.append(text_chat)
        page.update()
    page.pubsub.subscribe(send_tunnel_message)
    
    def send_message(event):
        text_message = message_space.value
        username = username_space.value
        message = f"{username}: {text_message}"
        page.pubsub.send_all(message)
        message_space.value = ""
        page.update()
                
    message_space = ft.TextField(label="Digite sua mensagem", on_submit=send_message)
    send_message_bottom = ft.ElevatedButton("Enviar", on_click=send_message)
    message_line = ft.Row([message_space, send_message_bottom])
    
    def enter_chat(event):
        page.remove(title)
        page.remove(start_bottom)
        popup.open = False
        page.add(chat)
        page.add(message_line)
        mensagem = f"{username_space.value} entrou no chat"
        page.pubsub.send_all(mensagem)
        page.update()
        
    enter_bottom = ft.ElevatedButton("Entrar no chat", on_click=enter_chat)
    popup = ft.AlertDialog(title=title_popup, content=username_space, actions=[enter_bottom])
    
    def start_chat(event):
        page.dialog = popup
        popup.open = True
        page.update()
    start_bottom = ft.ElevatedButton("Iniciar Chat", on_click=start_chat)
    
    page.add(title)
    page.add(start_bottom)

#RODA O APP    
ft.app(main, view=ft.WEB_BROWSER)