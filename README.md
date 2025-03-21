# Caso de Teste: Registro de Atendimento de Aluno

**Objetivo:** Verificar se o sistema consegue registrar corretamente o atendimento a um aluno.

**Pré-condição:** O assessor já deve ter feito login no sistema.

**Procedimento de Teste:** 
1. Fazer login com a conta de assessor.
2. Navegar até a interface de gerenciamento de alunos.
3. Selecionar o aluno para o qual será registrado o atendimento.
4. Preencher os campos obrigatórios do atendimento.
5. Confirmar o registro do atendimento.

**Resultado Esperado:** O atendimento deve ser registrado corretamente, associado ao aluno.

**Resultado Obtido:** O atendimento foi registrado corretamente e exibido na interface do aluno.

**Pós-condição:** O atendimento é visível na ficha do aluno.

**Código do Teste:** [test_atendimento.py](test_atendimento.py)
