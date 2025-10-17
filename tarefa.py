class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []
        
    def adicionar_tarefa(self, nome, descricao):
        
        if not nome:
            raise ValueError("O nome da tarefa nao pode ser vazio.")
        
        nova_tarefa = {
            "nome": nome,
            "descricao": descricao,
            "status": "em andamento"
        }
        self.tarefas.append(nova_tarefa)