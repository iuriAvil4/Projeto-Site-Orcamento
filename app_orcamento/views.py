from django.shortcuts import render, redirect
from .forms import ClienteForm
from django.contrib import messages
from .email_utils import enviar_email


def home(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            enviar_email(cliente)
            messages.success(request, "Orçamento enviado com sucesso!")
            return redirect('home')  
        else:
            messages.error(request, "Erro ao adicionar o registro. Verifique os campos.")
    else:
        form = ClienteForm()

    return render(request, 'orcamento/home.html', {'form': form})