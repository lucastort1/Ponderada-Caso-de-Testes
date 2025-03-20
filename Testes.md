# Caso de Teste: Registro de Atendimento de Aluno

**Objetivo**: Verificar se o sistema consegue registrar corretamente o atendimento a um aluno.

**Pré-condição:** O assessor já deve ter feito login no sistema.
O aluno a ser atendido já deve estar cadastrado no sistema.
Procedimento de Teste:

1- Fazer login com a conta de assessor.
2- Navegar até a interface de gerenciamento de alunos.
3- Selecionar o aluno para o qual será registrado o atendimento.
4- Preencher os campos obrigatórios do atendimento, como data, descrição e profissional vinculado.
5- Confirmar o registro do atendimento.

**Resultado Esperado:** O atendimento deve ser registrado corretamente, associado ao aluno e à ficha do profissional.
A interface deve apresentar uma mensagem de sucesso indicando que o atendimento foi registrado.

**Resultado Obtido:** O atendimento foi registrado corretamente, com todos os dados inseridos exibidos na ficha do aluno.
A interface apresentou uma mensagem de sucesso como esperado.

**Pós-condição:** O atendimento deve aparecer na lista de atendimentos do aluno, com os dados corretos.
O sistema deve refletir a atualização nas estatísticas da unidade.