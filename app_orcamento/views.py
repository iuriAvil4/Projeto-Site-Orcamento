from django.db import connection
from django.shortcuts import render, redirect
from .forms import ClienteForm
from django.contrib import messages
from .email_utils import enviar_email


def home(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.clean_email()
            form.clean_telefone()
            
            adicionar_cliente_procedure(
                form.cleaned_data['nome'],
                form.cleaned_data['sobrenome'],
                form.cleaned_data['email'],
                form.cleaned_data['telefone'],
                form.cleaned_data['descricao']
            )

            enviar_email(
                form.cleaned_data['nome'],
                form.cleaned_data['sobrenome'],
                form.cleaned_data['email'],
                form.cleaned_data['telefone'],
                form.cleaned_data['descricao']
            )
            
            messages.success(request, "Orçamento enviado com sucesso!")
            return redirect('home')  
        else:
            messages.error(request, "Erro ao adicionar o registro. Verifique os campos.")
    else:
        form = ClienteForm()

    return render(request, 'orcamento/home.html', {'form': form})


def adicionar_cliente_procedure(nome, sobrenome, email, telefone, descricao):
    with connection.cursor() as cursor:
        try:
            # Executa a stored procedure
            cursor.callproc('ADD_CLIENTE', [nome, sobrenome, email, telefone, descricao])

            # Faz commit da transação
            connection.commit()

        finally:
            # Fecha o cursor automaticamente devido ao uso do 'with'
            pass