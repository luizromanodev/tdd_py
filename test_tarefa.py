import unittest

from tarefa import GerenciadorDeTarefas

class TestGerenciadorDeTarefas(unittest.TestCase):
    
    def test_adicionar_tarefa_com_sucesso(self):
        gerenciador = GerenciadorDeTarefas()
        gerenciador.adicionar_tarefa("Estudar TDD", "Aprender a usar TDD em projetos Python")
        
        self.assertEqual(len(gerenciador.tarefas), 1)
        
        self.assertEqual(gerenciador.tarefas[0]['nome'], "Estudar TDD")
    
    def test_rejeitar_tarefa_sem_nome(self):
        gerenciador = GerenciadorDeTarefas()
        
        with self.assertRaises(ValueError):
            gerenciador.adicionar_tarefa("", "Descrição sem nome")
    
if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)