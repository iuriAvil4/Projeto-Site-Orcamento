import smtplib
import email.message

def enviar_email(nome, sobrenome, Email, telefone, descricao):
    corpo_email = f"""
    <p><strong>Novo Orçamento Recebido</strong></p>
    <p><strong>Nome:</strong> {nome}</p>
    <p><strong>Sobrenome:</strong> {sobrenome}</p>
    <p><strong>Email:</strong> {Email}</p>
    <p><strong>Telefone:</strong> {telefone}</p>
    <p><strong>Descrição:</strong> {descricao}</p>
    """
    msg = email.message.Message()
    msg['Subject'] = "Novo Orçamento Recebido"
    msg['From'] = 'minhacontaauxiliar1@gmail.com'  # Substitua pelo seu endereço de e-mail
    msg['To'] = 'iuriguerra03@gmail.com'  # Substitua pelo destinatário desejado
    password = 'kgazacfhvhkyhrnt'  # Substitua pela senha do seu e-mail
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')