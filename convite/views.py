from django.shortcuts import render, redirect
from .models import ConfirmacaoPresenca
from django.shortcuts import get_object_or_404


def tela_principal(request):
    return render(request, 'convite/tela_principal.html')

def confirmar_presenca(request):
    return render(request, 'convite/confirmar.html')

def login_admin(request):
    return render(request, 'convite/login_admin.html')

def painel_admin(request):
    return render(request, 'convite/painel_admin.html')



def confirmar_presenca(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        tipo = request.POST.get("tipo")
        if nome and tipo:
            ConfirmacaoPresenca.objects.create(nome=nome, tipo=tipo)
            return render(request, "convite/confirmado.html", {"nome": nome})
    return render(request, "convite/confirmar.html")


# Código de acesso fixo
CODIGO_ACESSO = "noiva123"

def login_admin(request):
    if request.method == "POST":
        codigo = request.POST.get("codigo")
        if codigo == CODIGO_ACESSO:
            request.session["painel_autorizado"] = True
            return redirect("painel_admin")
        else:
            return render(request, "convite/login_admin.html", {"erro": True})
    return render(request, "convite/login_admin.html")

def painel_admin(request):
    if not request.session.get("painel_autorizado"):
        return redirect("login_admin")

    confirmacoes = ConfirmacaoPresenca.objects.all()
    total_presenciais = confirmacoes.filter(tipo="presencial").count()
    total_online = confirmacoes.filter(tipo="online").count()

    sucesso = request.session.pop('sucesso_exclusao', False)

    return render(request, "convite/painel_admin.html", {
        "confirmacoes": confirmacoes,
        "total_presenciais": total_presenciais,
        "total_online": total_online,
        "sucesso_exclusao": sucesso
    })

def logout_admin(request):
    request.session.flush()
    return redirect("tela_principal")


def excluir_confirmacao(request, id):
    if request.method == "POST" and request.session.get("painel_autorizado"):
        confirmacao = get_object_or_404(ConfirmacaoPresenca, id=id)
        confirmacao.delete()
        request.session['sucesso_exclusao'] = True
    return redirect("painel_admin")

