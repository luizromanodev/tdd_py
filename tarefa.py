class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []
        
    def adicionar_tarefa(self, nome, descricao):
        nova_tarefa = {
            "nome": nome,
            "descricao": descricao,
            "status": "em andamento"
        }
        self.tarefas.append(nova_tarefa)