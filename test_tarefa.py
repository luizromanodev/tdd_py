import unittest
from tarefa import GerenciadorDeTarefas

class TestGerenciadorDeTarefas(unittest.TestCase):
    
    def setUp(self):
        self.gerenciador = GerenciadorDeTarefas()
    
    def test_adicionar_tarefa_com_sucesso(self):
        self.gerenciador.adicionar_tarefa("Estudar TDD", "Aprender a usar TDD em projetos Python")
        self.assertEqual(len(self.gerenciador.tarefas), 1)
        self.assertEqual(self.gerenciador.tarefas[0]['nome'], "Estudar TDD")
    
    def test_rejeitar_tarefa_sem_nome(self):
        with self.assertRaises(ValueError):
            self.gerenciador.adicionar_tarefa("", "Descrição sem nome")
            
    def test_marcar_tarefa_como_concluida(self):
        self.gerenciador.adicionar_tarefa("Estudar", "Estudar para a prova")
        self.gerenciador.marcar_como_concluida(0)
        self.assertEqual(self.gerenciador.tarefas[0]['status'], "concluída")
        
    def test_nao_marcar_tarefa_ja_concluida(self):
        self.gerenciador.adicionar_tarefa("Tarefa X", "Descrição")
        self.gerenciador.marcar_como_concluida(0)
        with self.assertRaises(ValueError):
            self.gerenciador.marcar_como_concluida(0)
            
    def test_marcar_tarefa_como_em_andamento(self):
        self.gerenciador.adicionar_tarefa("Tarefa Y", "Descrição")
        self.gerenciador.tarefas[0]['status'] = 'pendente'
        self.gerenciador.marcar_como_em_andamento(0)
        self.assertEqual(self.gerenciador.tarefas[0]['status'], "em andamento")
        
    def test_nao_marcar_em_andamento_tarefa_concluida(self):
        self.gerenciador.adicionar_tarefa("Tarefa Z", "Descrição")
        self.gerenciador.marcar_como_concluida(0)
        with self.assertRaises(ValueError):
            self.gerenciador.marcar_como_em_andamento(0)
            
    def test_editar_tarefa_existente(self):
        self.gerenciador.adicionar_tarefa("Nome Antigo", "Descrição Antiga")
        self.gerenciador.editar_tarefa(0, "Nome Novo", "Descrição Nova")
        self.assertEqual(self.gerenciador.tarefas[0]['nome'], "Nome Novo")
        self.assertEqual(self.gerenciador.tarefas[0]['descricao'], "Descrição Nova")
        
    def test_editar_tarefa_inexistente(self):
        with self.assertRaises(IndexError):
            self.gerenciador.editar_tarefa(99, "Nome", "Desc")
            
    def test_excluir_tarefa_com_sucesso(self):
        self.gerenciador.adicionar_tarefa("Tarefa para excluir", "...")
        self.assertEqual(len(self.gerenciador.tarefas), 1)
        self.gerenciador.excluir_tarefa(0)
        self.assertEqual(len(self.gerenciador.tarefas), 0)
        
    def test_excluir_tarefa_inexistente(self):
        with self.assertRaises(IndexError):
            self.gerenciador.excluir_tarefa(99)
    
if __name__ == '__main__':
    unittest.main()