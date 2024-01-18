import smtplib
import email.message

def enviar_email(cliente):
    corpo_email = f"""
    <p><strong>Novo Orçamento Recebido</strong></p>
    <p><strong>Nome:</strong> {cliente.nome}</p>
    <p><strong>Sobrenome:</strong> {cliente.sobrenome}</p>
    <p><strong>Email:</strong> {cliente.email}</p>
    <p><strong>Telefone:</strong> {cliente.telefone}</p>
    <p><strong>Descrição:</strong> {cliente.descricao}</p>
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
