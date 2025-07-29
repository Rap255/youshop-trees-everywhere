import os
import smtplib
import mimetypes
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def form_formatter(POST: dict, *args: str) -> dict:
    exclude = ['csrfmiddlewaretoken']
    exclude.extend(args)
    form = {key:value for key, value in POST.items() if key not in exclude}
    return form


def send_email_code(code:str,destinatario:str, name_destinatario:str):
    
    remetente = ''
    assunto = f'Sales Assist - Olá {name_destinatario} Solictação Resete de Senha 1'
    mensagem = f'Teste de disparo code:{code}'

    senha = ""
    msg = MIMEMultipart('alternative')
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    html = f"""
        <html>
        <head>
            <style>
            .container {{
                padding: 20px;
                background-color: #f9f9f9;
                font-family: Arial, sans-serif;
                color: #333;
                border: 1px solid #ccc;
                border-radius: 8px;
                max-width: 600px;
                margin: auto;
            }}
            .code {{
                font-size: 24px;
                font-weight: bold;
                color: #4CAF50;
            }}
            </style>
        </head>
        <body>
            <div class="container">
            <h2>Seu código de verificação:</h2>
            <p class="code">{code}</p>
            <p>Use este código para continuar com seu processo de verificação.</p>
            </div>
        </body>
        </html>
    """

    parte_html = MIMEText(html, 'html')
    msg.attach(parte_html)

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as email:
        email.login(remetente,senha)
        email.send_message(msg)
        email.quit()

    print('email enviado')
