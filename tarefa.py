class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []
        
    def _validar_indice(self, indice):
        if not (0 <= indice < len(self.tarefas)):
            raise IndexError("Tarefa Inexistente")
        
    def adicionar_tarefa(self, nome, descricao):
        
        if not nome:
            raise ValueError("O nome da tarefa nao pode ser vazio.")
        
        nova_tarefa = {
            "nome": nome,
            "descricao": descricao,
            "status": "em andamento"
        }
        self.tarefas.append(nova_tarefa)
        
    def marcar_como_concluida(self, indice_tarefa):
        self._validar_indice(indice_tarefa)
        if self.tarefas[indice_tarefa]['status'] == "concluída":
            raise ValueError("A tarefa ja esta concluída")
        self.tarefas[indice_tarefa]['status'] = "concluída"
        
    def marcar_como_em_andamento(self, indice_tarefa):
        self._validar_indice(indice_tarefa)
        if self.tarefas[indice_tarefa]['status'] == "em andamento":
            raise ValueError("Não é possivel alterar o status de uma tarefa concluida")
        self.tarefas[indice_tarefa]['status'] = "em andamento"
        
    def editar_tarefa(self, indice_tarefa, novo_nome, nova_descricao):
        self._validar_indice(indice_tarefa)
        self.tarefas[indice_tarefa]['nome'] = novo_nome
        self.tarefas[indice_tarefa]['descricao'] = nova_descricao
        
    def excluir_tarefa(self, indice_tarefa):
        self.tarefas.pop(indice_tarefa)