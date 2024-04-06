import pyfiglet
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, init

# Inicialize o colorama
init(autoreset=True)

# Função para renderizar o texto com pyfiglet e cor vermelha
def render_text(text, color):
    ascii_banner = pyfiglet.Figlet(font='slant')
    banner = ascii_banner.renderText(text)
    colored_banner = getattr(Fore, color) + banner
    return colored_banner

banner = render_text("Light-Ban", "RED")
print(banner)

print(Fore.BLUE + "Oi! Vamos começar a dar um ban nesses caras.")

numero = input("Número alvo: ")
EMAIL = "lightbot72@gmail.com"
PASSWORD = "ikin exme hcsz puxl"
TO_EMAIL = "support@support.whatsapp.com"

def enviar_email(subject, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)

        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = TO_EMAIL
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server.sendmail(EMAIL, TO_EMAIL, msg.as_string())
        server.quit()
        return "E-mail enviado com sucesso!"

    except Exception as e:
        return f"Erro ao enviar o e-mail: {e}"

# Exemplo de utilização
assunto = "Perdido/Roubado: Por favor, desative minha conta"
mensagem = f"""Estou solicitando a desativação temporária de minha conta no WhatsApp,
meu número: {numero}
Perdido/Roubado: Por favor, desative minha conta
"""

resultado = enviar_email(assunto, mensagem)
print(Fore.BLUE + resultado)
