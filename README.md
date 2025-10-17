# Definição de Casos de Teste (Esboço Textual)

## TEST-01: Validação da Criação de Tarefa com Dados Válidos
    - Objetivo: Verificar se, ao prover um nome e uma descrição válidos, uma nova tarefa é instanciada e corretamente adicionada à lista de tarefas do sistema. 
      A asserção deve confirmar que o tamanho da lista aumentou e que os dados da nova tarefa correspondem aos que foram fornecidos.
## TEST-02: Tratamento de Entrada Inválida na Criação de Tarefa
    - Objetivo: Assegurar que o sistema rejeita a criação de uma tarefa quando o campo "nome" é nulo ou vazio. 
      O comportamento esperado é o lançamento de uma exceção para sinalizar a violação da regra de negócio.
## TEST-03: Validação da Transição de Status para "Concluída"
    - Objetivo: Testar se o status de uma tarefa existente é corretamente atualizado para "concluída". 
      A verificação deve ser feita acessando o atributo de status do objeto da tarefa após a execução da função.
## TEST-04: Prevenção de Transição Redundante de Status
    - Objetivo: Validar que uma tarefa já com o status "concluída" não pode ser marcada como concluída novamente. 
      O sistema deve emitir um aviso ou lançar uma exceção para indicar que a operação é inválida.
## TEST-05: Validação da Transição de Status para "Em Andamento"
    - Objetivo: Verificar se o status de uma tarefa pode ser alterado para "em andamento". 
    A asserção deve confirmar que o atributo de status reflete a nova modificação.
## TEST-06: Validação de Regra de Negócio para Status Concluído
    - Objetivo: Garantir que uma tarefa com status "concluída" não pode ter seu estado revertido para "em andamento". 
    O sistema deve impedir essa transição, lançando uma exceção que informe a violação da regra.
## TEST-07: Validação da Atualização de Dados da Tarefa
    - Objetivo: Assegurar que os campos "nome" e "descrição" de uma tarefa existente podem ser editados com sucesso. 
      Os novos dados devem ser persistidos corretamente no objeto da tarefa.
## TEST-08: Tratamento de Referência Inexistente na Edição
    - Objetivo: Testar a robustez do sistema ao tentar editar uma tarefa que não existe na lista. 
      O comportamento esperado é o lançamento de uma exceção de índice (ex: IndexError), prevenindo falhas na aplicação.
## TEST-09: Validação da Remoção de Tarefa
    - Objetivo: Verificar se uma tarefa existente pode ser removida da lista com sucesso. 
      A asserção principal é que o tamanho da lista de tarefas deve ser decrementado em uma unidade.
## TEST-10: Tratamento de Referência Inexistente na Remoção
    - Objetivo: Assegurar que o sistema trata corretamente a tentativa de excluir uma tarefa inexistente. 
      Similar ao TEST-08, o sistema deve lançar uma exceção de índice para indicar o erro sem interromper a execução.
