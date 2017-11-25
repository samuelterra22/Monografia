# Diagramas e Expansões de Casos de Uso


**Módulo Pré-Reunião**

\begin{figure}[ht here top]
\begin{center}
\caption{\label{ap1}DCSU - Pré-Reunião.}
\includegraphics[width=0.85\textwidth]{imagens/ap1.png}
\legend{Fonte: Elaborada pelo autor.}
\end{center}
\end{figure}

**Responsável pela Reunião**

**ID:** CSU 01

**Nome do CSU:** Logar

**Pré-condições:** 

\tab \quad 1. Usuários (servidores) estarem cadastrados

**Fluxo Principal:**

\tab \quad 1. O servidor entra com o seu e-mail 

\tab \quad 2. O servidor entra com sua senha 

\tab \quad 3. O servidor clica em “Logar”

\tab \quad 4. O sistema autentica os dados

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** E-mail e senha não encontrados, o sistema deve limpar os campos e retornar à tela de login
Pós-condições: O sistema exibe a interface doravante, no caso o menu principal/inicial, do sistema

\vspace{1cm}

**ID:** CSU 09

**Nome do CSU:** Criar reunião

**Pré-condições:** 

\tab \quad 1. O Responsável pela Reunião deve estar logado no sistema

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Reunião seleciona a opção Agendar Reunião no submenu de Reunião

\tab \quad 2. O sistema exibe a GUI Agendar Reunião - Básicas

\tab \quad 3. O Responsável pela Reunião entra com a data estipulada para a reunião

\tab \quad 4. O Responsável pela Reunião entra com a sala estipulada para a reunião

\tab \quad 5. O Responsável pela Reunião entra com o horário estipulado para a reunião

\tab \quad 6. O Responsável pela Reunião clica em “Salvar e Continuar”

\tab \quad 7. O sistema exibe a GUI Agendar Reunião – Participantes

\tab \quad 8. O Responsável pela Reunião seleciona as comissões participantes

\tab \quad 9. O Responsável pela Reunião clica em “Buscar Participantes”

\tab \quad 10. O sistema exibe os servidores de acordo com as comissões selecionadas

\tab \quad 11. O Responsável pela Reunião seleciona os servidores que serão convidados à reunião

\tab \quad 12. O Responsável pela Reunião seleciona se deseja (sim/não) definir o Responsável pela Ata

\tab \quad \quad a. Caso selecione “sim” o sistema exibe os servidores convidados e o participante seleciona aquele que será o Responsável pela Ata

\tab \quad 13. O Responsável pela Reunião clica em “Salvar e Continuar”

\tab \quad 14. O sistema exibe a GUI Agendar Reunião – Pauta

\tab \quad 15. O Responsável pela Reunião entra com os itens de pauta

\tab \quad 16. O Responsável pela Reunião entra com o tempo dos itens de pauta

\tab \quad 17. O Responsável pela Reunião define (sim/não) se o item é sigiloso

\tab \quad 18. O Responsável pela Reunião clica em “Inserir Item”

\tab \quad 19. O Responsável pela Reunião clica em “Salvar e Continuar”

\tab \quad 20. O sistema exibe a GUI Agendar Reunião – Convite

\tab \quad 21. O sistema exibe as informações geradas de acordo com os dados inseridos

\tab \quad 22. O Responsável pela Reunião clica em “Confirmar Dados”

\tab \quad 23. O sistema cria a reunião e armazena as informações referentes à mesma

\tab \quad 24. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** Data e horário inexistentes, o sistema deve limpar os campos e retornar à tela Criar Reunião

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião 


\vspace{1cm}


**ID:** CSU 10

**Nome do CSU:** Selecionar comissão

**Pré-condições: **

\tab \quad 1. O Responsável pela Reunião deve ter iniciado uma reunião e estar na opção na aba Participantes

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Reunião seleciona as comissões cadastradas

\tab \quad 2. O sistema exibe os servidores cadastrados de acordo com as comissões selecionadas

\tab \quad 3. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** Se não houver nenhuma comissão cadastrada no sistema, deve ser retornada a mensagem “É preciso haver uma comissão cadastrada para que a reunião seja criada” e então o sistema retorna a tela referente ao menu da reunião

**Pós-condições:** -

\vspace{1cm}
**ID:**: CSU 13

**Nome do CSU:** Enviar Convite

**Pré-condições:** 

\tab \quad 1. O Responsável pela Reunião deve estar no menu referente a reunião em questão, sendo que as comissões/participantes e sala já devem estar definidos

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Reunião seleciona a opção “Confirmar Dados” na GUI Agendar Reunião - Convite

\tab \quad 2. O sistema envia o convite para todos os participantes inseridos na reunião

\tab \quad 3. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** (a existência de comissões/participantes é imposta como pré-condição)

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião

\vspace{1cm}
**ID:** CSU 14

**Nome do CSU:** Definir Itens de Pauta

**Pré-condições:** 

\tab \quad 1. O Responsável pela Reunião deve estar no menu referente a reunião que está sendo criada

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Reunião seleciona a opção Pauta no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Definir Itens de Pauta

\tab \quad 3. O Responsável pela Reunião entra com o nome dos itens de pauta (obrigatório)

\tab \quad 4. O Responsável pela Reunião entra com o tempo para dos itens de pauta

\tab \quad 5. O Responsável pela Reunião entra com o sigilo dos itens de pauta (obrigatório)

\tab \quad 6. O Responsável pela Reunião clica em “Inserir Item”

\tab \quad 7. O sistema armazena os Itens de Pauta definidos referentes à reunião

\tab \quad 8. O Responsável pela Reunião clica em “Salvar e Continuar”

\tab \quad 9. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** Caso não seja inserido nenhum Item de Pauta, deve ser retornada a mensagem “Ao menos um Item de Pauta deve ser inserido para que a reunião aconteça” e o sistema retorna à tela de inserção de Itens de Pauta

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião

\vspace{1cm}
**ID:** CSU 16

**Nome do CSU:** Definir Responsável pela Ata

**Pré-condições:** 

\tab \quad 1. O Responsável pela Reunião deve estar logado e no menu referente a reunião em questão, sendo que a reunião já deve ter sido criada

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Reunião seleciona a opção “sim” na opção de Selecionar Responsável pela Ata, estando no submenu da reunião

\tab \quad 2. O Responsável pela Reunião seleciona o Responsável pela Ata dentre os participantes da reunião

\tab \quad 3. O sistema armazena o Responsável pela Ata definido para a reunião

\tab \quad 4. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião

\vspace{1cm}
**ID:** CSU 17

**Nome do CSU:** Definir Tipo de Ata

**Pré-condições:** 

\tab \quad 1. O Responsável pela Reunião deve estar no menu referente a reunião em questão, sendo que a reunião já deve ter sido criada

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Reunião seleciona a opção Definir Tipo Ata no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Definir Tipo de Ata

\tab \quad 3. O Responsável pela Reunião entra seleciona o tipo de ata (aberta/fechada) referente à reunião

\tab \quad 4. O Responsável pela Reunião clica em “Definir Tipo de Ata”

\tab \quad 5. O sistema armazena o tipo de ata definido referente à reunião

\tab \quad 6. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** (como o RR pode definir o tipo de ata a qualquer momento antes de a reunião ser iniciada, não há fluxo de exceção)

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião

\vspace{1cm}
**Participante**

**ID:** CSU 18

**Nome do CSU:** Visualizar Convites de Reunião

**Pré-condições:** 

\tab \quad 1. O participante deve estar logado no sistema

**Fluxo Principal:**

\tab \quad 1. O Participante seleciona a opção Visualizar Convites de Reunião no menu

\tab \quad 2. O sistema exibe a GUI Visualizar Convites de Reunião

\tab \quad 3. O Participante então visualiza todos os convites que possui

\tab \quad 4. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** Caso não houver nenhum convite, é retornada a mensagem “Você não possui nenhum convite”

**Pós-condições:** O sistema exibe a interface doravante, no caso o menu principal/inicial, do sistema


\vspace{1cm}
**ID:** CSU 19

**Nome do CSU:** Confirmar Participação

**Pré-condições:** 

\tab \quad 1. O Participante deve estar no menu referente à reunião

**Fluxo Principal:**

\tab \quad 1. O Participante seleciona a opção Confirmar Participação no submenu da Reunião

\tab \quad 2. O sistema exibe a GUI Confirmar Participação

\tab \quad 3. O Participante então seleciona sua opção (sim/não) quanto a sua presença na reunião

\tab \quad 4. O Participante clica em “Confirmar presença/ausência”

\tab \quad 5. O sistema armazena a opção selecionada pelo participante

\tab \quad 6. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** (como o Participante pode definir sua presença a qualquer momento antes de a reunião ser iniciada, não há fluxo de exceção)

**Pós-condições:** O sistema exibe a interface doravante, no caso o menu principal/inicial, do sistema


\vspace{1cm}
**ID:** CSU 20

**Nome do CSU:** Enviar justificativa

**Pré-condições:** 

\tab \quad 1. O Participante deve estar no menu referente à reunião e deve ter escolhido a opção “NÃO” quanto à participação na reunião

**Fluxo Principal:**

\tab \quad 1. O Participante seleciona a opção Enviar Justificativa no submenu da Reunião

\tab \quad 2. O sistema exibe a GUI Enviar Justificativa

\tab \quad 3. O Participante entra como justificativa pela qual não comparecerá à reunião

\tab \quad 4. O Participante clica em “Enviar Justificativa”

\tab \quad 5. O sistema armazena a justificativa

\tab \quad 6. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** Caso não seja encontrada uma justificativa, retornar a mensagem “Digite a sua justificativa” e voltar à GUI Enviar Justificativa

**Pós-condições:** O sistema exibe a interface doravante, no caso o menu principal/inicial, do sistema

\newpage

**Módulo Em Reunião**
\begin{figure}[ht here top]
\begin{center}
\caption{\label{ap1}DCSU - Em Reunião.}
\includegraphics[width=0.85\textwidth]{imagens/ap2.png}
\legend{Fonte: Elaborada pelo autor.}
\end{center}
\end{figure}




**Responsável pela Reunião**

**ID:** CSU 23

**Nome do CSU:** Abrir reunião

**Pré-condições:** 

\tab \quad 1. O Responsável pela Reunião deve estar no menu referente a uma reunião para que possa “abrir” a mesma

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Reunião seleciona a opção Abrir Reunião no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Abrir Reunião

\tab \quad 3. O Responsável pela Reunião clica em “Abrir Reunião”

\tab \quad 4. O sistema define o status da reunião como aberta

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião


\vspace{1cm}
**ID:** CSU 24

**Nome do CSU:** Definir Tempo para Item de Pauta

**Pré-condições:** 

\tab \quad 1. A reunião deve estar aberta

\tab \quad 2. O Responsável pela Reunião deve estar no menu referente a reunião

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Reunião seleciona a opção Definir Tempo para Item de Pauta no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Definir Tempo para Item de Pauta

\tab \quad 3. O Responsável pela Reunião define os tempos para os Itens de Pauta existentes na reunião

\tab \quad 4. O sistema armazena o tempo definido para os itens de pauta

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** Caso não sejam encontrados os Tempos para os Itens de Pauta, retornar a mensagem “Informe os Tempos de Itens de Pauta” e voltar à GUI Definir Tempo para Item de Pauta

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião


\vspace{1cm}
**ID:** CSU 25

**Nome do CSU:** Abrir Item de Pauta para Discussão

**Pré-condições:** 

\tab \quad 1. A reunião deve estar aberta

\tab \quad 2. Os tempos de Item de Pauta devem estar definidos

\tab \quad 3. O Responsável pela Reunião deve estar no menu referente a reunião

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Reunião seleciona a opção Abrir Item de Pauta para Discussão no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Abrir Item de Pauta para Discussão

\tab \quad 3. O Responsável pela Reunião seleciona o Item de Pauta que será discutido

\tab \quad 4. O sistema inicia uma contagem de acordo com o tempo pré-estabelecido para o Item de Pauta

\tab \quad 5. O sistema encerra a contagem

\tab \quad 6. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a GUI Abrir Item de Pauta para Discussão

\vspace{1cm}
**Responsável pela Ata**

**ID:** CSU 26

**Nome do CSU:** Validar presenças/ausências

**Pré-condições:** 

\tab \quad 1. A reunião deve estar aberta 

\tab \quad 2. O Responsável pela Ata deve estar no menu referente a reunião

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Ata seleciona a opção Validar Presenças/Ausências no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Validar Presenças/Ausências

\tab \quad 3. O sistema exibe a lista dos convidados à reunião

\tab \quad 4. O Responsável pela Ata seleciona aqueles que faltaram à reunião

\tab \quad 5. O sistema armazena os dados referentes aos presentes/ausentes

\tab \quad 6. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião



\vspace{1cm}
**ID:** CSU 27

**Nome do CSU:** Registrar Votações

**Pré-condições:** 

\tab \quad 1. A reunião deve estar aberta 

\tab \quad 2. O Responsável pela Ata deve estar no menu referente a reunião

\tab \quad 3. O Item de Pauta ter sido iniciado

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Ata seleciona a opção Registrar Votações no submenu o item de pauta

\tab \quad 2. O sistema exibe a GUI Registrar Votações


\tab \quad 3. O Responsável pela Ata entra com os valores de acordo com a votação

\tab \quad 4. O sistema armazena os dados referentes à votação

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião


\vspace{1cm}
**ID:** CSU 28

**Nome do CSU:** Registrar Encaminhamentos

**Pré-condições:** 

\tab \quad 1. A reunião deve estar aberta 

\tab \quad 2. O Responsável pela Ata deve estar no menu referente a reunião

\tab \quad 3. O Item de Pauta ter sido finalizado

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Ata seleciona a opção Registrar Encaminhamentos no submenu o item de pauta

\tab \quad 2. O sistema exibe a GUI Registrar Encaminhamentos

\tab \quad 3. O Responsável pela Ata seleciona os participantes para os quais serão encaminhados as discussões a respeito do Item de Pauta

\tab \quad 4. O sistema armazena os dados referentes aos encaminhamentos e os envia aos participantes selecionados

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** Caso não seja encontrado nenhum participante selecionado, retornar a mensagem “Selecione ao menos um participante para encaminhar os dados”

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião


\vspace{1cm}
**ID:** CSU 30

**Nome do CSU:** Inserir Posicionamento Sobre Item de Pauta

**Pré-condições:** 

\tab \quad 1. A reunião deve estar aberta 

\tab \quad 2. O Responsável pela Ata deve estar no menu referente ao Item de Pauta

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Ata seleciona a opção Inserir Posicionamento no submenu do Item de Pauta

\tab \quad 2. O sistema exibe a GUI Inserir Posicionamento

\tab \quad 3. O Responsável pela Ata entra com o posicionamento do participante referente ao Item de Pauta em questão

\tab \quad 4. O sistema armazena o posicionamento

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** (não há fluxo de exceção, pois o participante pode optar por não se posicionar)

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião


\vspace{1cm}
**Responsável pela Reunião**

**ID:** CSU 31

**Nome do CSU:** Finalizar Reunião

**Pré-condições:** 

\tab \quad 1. O Responsável pela Reunião deve estar no menu referente à reunião para que possa “finalizar” a mesma

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Reunião seleciona a opção Finalizar Reunião no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Finalizar Reunião

\tab \quad 3. O Responsável pela Reunião clica em “Encerrar Reunião”

\tab \quad 4. O sistema define o status da reunião como finalizada

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião

**ID:** CSU 32

**Nome do CSU:** Imprimir Ata

**Pré-condições:** 

\tab \quad 1. O Usuário deve estar no menu referente à reunião para que possa imprimir a ata

**Fluxo Principal:**

\tab \quad 1. O Usuário seleciona a opção Imprimir Ata no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Imprimir Ata

\tab \quad 3. O Usuário clica em “Confirmar impressão”


\tab \quad 4. O sistema envia o documento a ser impresso para a impressora

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião


\vspace{1cm}
**Responsável pela Ata**

**ID:** CSU 33

**Nome do CSU:** Enviar Ata para Participantes

**Pré-condições:** 

\tab \quad 1. O Responsável pela Ata deve estar no menu referente a reunião

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Ata seleciona a opção Enviar Ata para Participantes no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Enviar Ata para Participantes

\tab \quad 3. O sistema exibe a lista dos convidados à reunião

\tab \quad 4. O Responsável pela Ata seleciona aqueles para os quais enviará a ata

\tab \quad 5. O Responsável pela Ata clica em “Enviar”

\tab \quad 6. O sistema envia a ata aos participantes selecionados

\tab \quad 7. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião

\newpage

**Módulo Pós-Reunião**
\begin{figure}[ht here top]
\begin{center}
\caption{\label{ap1}DCSU - Pós-Reunião.}
\includegraphics[width=0.70\textwidth]{imagens/ap3.png}
\legend{Fonte: Elaborada pelo autor.}
\end{center}
\end{figure}

**Participante**

**ID:** CSU 34

**Nome do CSU:** Revisar Ata

**Pré-condições:** 

\tab \quad 1. A reunião deve ter sido finalizada 

\tab \quad 2. O Participante deve estar no menu referente à reunião

**Fluxo Principal:**

\tab \quad 1. O Participante seleciona a opção Revisar Ata no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Revisar Ata

\tab \quad 3. O Participante entra com as sugestões e posicionamentos quanto a ata

\tab \quad 4. O sistema envia tais sugestões e posicionamentos para o Responsável pela Ata

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** (não há fluxo de exceção, pois o participante pode optar por não se posicionar)

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião


\vspace{1cm}
**Responsável pela Ata**

**ID:** CSU 35

**Nome do CSU:** Efetivar Mudanças na Ata

**Pré-condições:** 

\tab \quad 1. A reunião deve ter sido finalizada 

\tab \quad 2. O Responsável pela Ata deve estar no menu referente à reunião

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Ata seleciona a opção Efetivar Mudanças na Ata no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Efetivar Mudanças na Ata

\tab \quad 3. O Responsável pela Ata efetiva as sugestões enviadas pelos participantes

\tab \quad 4. O sistema armazena tais sugestões

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao menu da reunião


\vspace{1cm}
**Participante**

**ID:** CSU 36

**Nome do CSU:** Visualizar Atas a Revisar

**Pré-condições:** 

\tab \quad 1. O Participante deve estar logado no sistema

**Fluxo Principal:**

\tab \quad 1. O Participante seleciona a opção Visualizar Atas a Revisar no menu

\tab \quad 2. O sistema exibe a GUI Atas a Revisar

\tab \quad 3. O Participante então visualiza todas as atas que necessitam de revisão

\tab \quad 4. O caso de uso é encerrado

**Fluxos Alternativos:** Caso não haja nenhuma ata, retornar a mensagem “Você não possui atas a revisar”

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao menu principal do sistema


\vspace{1cm}
**ID:** CSU 37


**Nome do CSU:** Visualizar Avisos para Assinatura

**Pré-condições:** 

\tab \quad 1. O Participante deve estar logado no sistema

**Fluxo Principal:**

\tab \quad 1. O Participante seleciona a opção Visualizar Avisos para Assinatura no menu

\tab \quad 2. O sistema exibe a GUI Avisos para Assinatura

\tab \quad 3. O Participante então visualiza todos os avisos para assinatura pendentes

\tab \quad 4. O caso de uso é encerrado

**Fluxos Alternativos:** Caso não haja nenhuma ata, retornar a mensagem “Você não possui assinaturas pendentes”

**Fluxos Exceção:** -


**Pós-condições:** O sistema exibe a interface referente ao menu principal do sistema

\vspace{1cm}
**Responsável pela Ata**

**ID:** CSU 38

**Nome do CSU:** Visualizar Atas Concluídas

**Pré-condições:** 

\tab \quad 1. O Responsável pela Ata deve estar logado no sistema

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Ata seleciona a opção Visualizar Atas Concluídas no menu

\tab \quad 2. O sistema exibe a GUI Atas Concluídas 

\tab \quad 3. O Responsável pela Ata então visualiza todas as atas já concluídas

\tab \quad 4. O caso de uso é encerrado


**Fluxos Alternativos:** Caso não haja nenhuma ata concluída, retornar a mensagem “Não há nenhuma ata concluída”

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao menu principal do sistema


\vspace{1cm}
**ID:** CSU 39

**Nome do CSU:** Enviar Avisos para Assinatura

**Pré-condições:** 

\tab \quad 1. O Responsável pela Ata deve estar logado no sistema

\tab \quad 2. O Responsável pela Ata deve estar no menu da reunião

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Ata seleciona a opção Enviar Avisos para Assinatura no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Enviar Avisos para Assinatura

\tab \quad 3. O Responsável pela Ata clica em “Enviar Avisos”

\tab \quad 4. O sistema envia avisos de assinatura para todos os participantes da reunião

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao menu principal do sistema


\vspace{1cm}
**Responsável pela Reunião**

**ID:** CSU 40

**Nome do CSU:** Arquivar Ata Assinada

**Pré-condições:** 

\tab \quad 1. O Responsável pela Reunião deve estar logado no sistema

\tab \quad 2. O Responsável pela Reunião deve estar no submenu da reunião

\tab \quad 3. A ata da reunião deve ter sido assinada por todos os participantes

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Reunião seleciona a opção Arquivar Ata Assinada no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Arquivar Ata Assinada 

\tab \quad 3. O Responsável pela Reunião visualiza a ata e clica em “Arquivar Ata”

\tab \quad 4. O sistema armazena a ata

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** Caso a ata não esteja assinada, retornar a mensagem “A ata não foi assinada por todos os participantes”, e retornar ao submenu da reunião

**Pós-condições:** O sistema exibe a interface referente ao submenu da reunião


\vspace{1cm}
**ID:** CSU 41

**Nome do CSU:** Restringir Acesso à Ata

**Pré-condições:** 

\tab \quad 1. A ata da reunião deve ter sido assinada por todos os participantes e deve estar arquivada

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Reunião seleciona a opção Restringir Acesso à Ata no submenu da ata

\tab \quad 2. O sistema exibe a GUI Arquivar Restringir Acesso à Ata 

\tab \quad 3. O sistema exibe as comissões/participantes da reunião

\tab \quad 4. O Responsável pela Reunião seleciona aqueles que possuirão acesso à ata ou a marca como pública

\tab \quad 5. O sistema armazena os dados referentes à privacidade da ata

\tab \quad 6. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao submenu da reunião


\vspace{1cm}
**ID:** CSU 42

**Nome do CSU:** Finalizar Ata

**Pré-condições:** 

\tab \quad 1. O status da ata deve ter sido declarado como “Assinada”

**Fluxo Principal:**

\tab \quad 1. O Responsável pela Reunião seleciona a opção Fechar Ata no submenu da ata

\tab \quad 2. O sistema exibe a GUI Fechar Ata

\tab \quad 3. O Responsável pela Reunião clica em “Finalizar”

\tab \quad 4. O sistema armazena a ata e impede alterações

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao submenu da reunião



\newpage

**Módulo Usuário**

\begin{figure}[ht here top]
\begin{center}
\caption{\label{ap1}DCSU - Usuário Externo.}
\includegraphics[width=0.85\textwidth]{imagens/ap4.png}
\legend{Fonte: Elaborada pelo autor.}
\end{center}
\end{figure}


**Usuário Externo**

**ID:** CSU 43

**Nome do CSU:** Consultar Ata

**Pré-condições:** 

\tab \quad 1. O Usuário deve possuir acesso à ata

**Fluxo Principal:**

\tab \quad 1. O Usuário do Sistema seleciona a opção Consultar Ata no submenu da reunião

\tab \quad 2. O sistema exibe a GUI Consultar Ata 

\tab \quad 3. O Usuário do Sistema então pode realizar a consulta via

\tab \quad \quad a. Palavra-chave/assunto
\tab \quad \quad b. Participante
\tab \quad \quad c. Data
\tab \quad \quad d. Unidade

\tab \quad 4. O sistema retorna as atas de acordo com a entrada do usuário

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** Caso a ata não exista nenhuma ata a qual pode ser acessada pelo usuário, retornar a mensagem “Você não possui acesso a nenhuma ata”

**Pós-condições:** O sistema exibe a interface referente ao submenu da reunião

\vspace{1cm}
**ID:** CSU 44

**Nome do CSU:** Salvar Ata em PDF

**Pré-condições:** 

\tab \quad 1. O Usuário deve possuir acesso à ata

**Fluxo Principal:**

\tab \quad 1. O Usuário do Sistema seleciona a opção Salvar Ata em PDF no submenu da ata

\tab \quad 2. O sistema exibe a GUI Salvar Ata em PDF 

\tab \quad 3. O Usuário do Sistema clica em “Salvar”

\tab \quad 4. O sistema salva a ata em PDF e a disponibiliza para download

\tab \quad 5. O caso de uso é encerrado

**Fluxos Alternativos:** -

**Fluxos Exceção:** -

**Pós-condições:** O sistema exibe a interface referente ao submenu da reunião


