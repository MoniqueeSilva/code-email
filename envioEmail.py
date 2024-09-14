import smtplib  # Biblioteca para enviar e-mails usando o protocolo SMTP
from email.mime.text import MIMEText  # Classe para criar o corpo do e-mail em texto
import getpass  # Biblioteca para obter a senha do usuário de forma segura

def enviar_email():
    # Configurações do servidor SMTP do Gmail
    smtp_servidor = 'smtp.gmail.com'  # Servidor SMTP do Gmail
    smtp_porta = 587  # Porta para conexão TLS

    # Solicitar informações ao usuário
    usuario = input("Digite o seu endereço de e-mail do Gmail (remetente): ")  # E-mail do remetente
    senha = getpass.getpass("Digite a sua senha de e-mail: ")  # Senha do e-mail (oculta enquanto digita)
    destinatario = input("Digite o endereço de e-mail do destinatário (destinatário): ")  # E-mail do destinatário
    assunto = input("Digite o assunto do e-mail: ")  # Assunto do e-mail
    corpo = input("Digite o corpo do e-mail: ")  # Corpo do e-mail

    # Configurar a mensagem
    mensagem = MIMEText(corpo)  # Cria o corpo do e-mail em formato de texto
    mensagem['From'] = usuario  # Define o remetente do e-mail
    mensagem['To'] = destinatario  # Define o destinatário do e-mail
    mensagem['Subject'] = assunto  # Define o assunto do e-mail

    try:
        # Conectar ao servidor SMTP e enviar o e-mail
        with smtplib.SMTP(smtp_servidor, smtp_porta) as servidor:  # Conecta ao servidor SMTP
            servidor.starttls()  # Inicia a conexão segura usando TLS
            servidor.login(usuario, senha)  # Faz login no servidor SMTP com as credenciais fornecidas
            servidor.sendmail(usuario, destinatario, mensagem.as_string())  # Envia o e-mail
        print("Seu e-mail foi enviado!")  # Mensagem de sucesso
    except Exception as e:  # Captura qualquer exceção que ocorra durante o envio
        print(f"Erro ao enviar e-mail: {e}")  # Exibe a mensagem de erro

# Chamar a função para enviar o e-mail
enviar_email()

