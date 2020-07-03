from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

#Classe para os Formulários Django

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Nova Tarefa")
    #priodidade = forms.IntegerField(label="Prioridade", min_value=1, max_value=10)


#------------------------------------------#
#iniciando uma Lista vazia (Aqui é o caso sem Sessões, bem simples)
#tasks = [] #Comentado pois vou implementar Sessão de usuário
#------------------------------------------#

#Criando as sessões de usuário (dentro da função Index)

def index(request):
    # Aqui eu verifico se existe alguma "tasks" na sessão deste usuário (usando os cookies dele)
    # Caso não, irei iniciar a "tasks" vazia
    if "tasks" not in request.session:
        request.session["tasks"] = []
    
    #------------------------------------------#
    #Caso antigo sem sessão
    #return render(request, 'task/index.html', {'tasks': tasks})
    #------------------------------------------#

    #Com Sessão
    return render(request, 'task/index.html', {
        "tasks": request.session["tasks"]
    })

def addTask(request):
    #Se o method de envio for POST
    if request.method == "POST":
        #Cria uma variavel e recebe tudo o que o usuário digitou
        form = NewTaskForm(request.POST)
        #Verifica se é valido
        if form.is_valid():
            #Pega os valores e armazena em taks
            task = form.cleaned_data["task"]

            #------------------------------------------#
            #Novamente forma antiga
            #Da um Append na Lista com os valores recebidos
            #task.append(task)
            #------------------------------------------#

            request.session["tasks"] += [task] #Adiciona na lista da sessão
            
            #Retorna através do HTTP para a o html que lista
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            #Não atendeu as "Regras" do servidor quando atualizamos, aqui
            #ele vai retornar o erro e o formulário
            return render(request, "task/addTask.html",{
                "form": form
            })
    # Aqui é o caso da conexão direta, somente cria o form em branco para o usuário
    return render(request, 'task/addTask.html', {
        "form": NewTaskForm()
    })
    