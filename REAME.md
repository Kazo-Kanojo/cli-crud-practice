🚀 Gerenciador de Fila FIFO em Python
Este é um sistema de CRUD (Create, Read, Update, Delete) simples, desenvolvido em Python, para demonstrar o conceito de estrutura de dados FIFO (First-In, First-Out). O projeto simula uma fila de atendimento onde o primeiro cliente a chegar é, obrigatoriamente, o primeiro a ser servido.

📋 Funcionalidades
O sistema oferece um menu interativo com as seguintes opções:

Adicionar Clientes: Permite inserir um ou mais nomes na fila simultaneamente.

Remover Cliente Específico: Busca e remove um cliente da fila pelo nome (útil para desistências).

Atender Clientes (FIFO): Processa toda a fila, removendo os elementos na ordem de chegada.

Visualizar Fila: Exibe todos os clientes atuais e sua posição numérica na espera.

🧠 Conceitos Aplicados
Neste projeto, apliquei conceitos fundamentais de programação e engenharia de software:

Estruturas de Dados: Uso de listas para simular o comportamento de uma fila.

Modularização: O código é dividido em funções com responsabilidades únicas (SRP - Single Responsibility Principle).

Tratamento de Exceções: Uso de blocos try-except para garantir que entradas inválidas do usuário não interrompam a execução do programa.

Lógica de Controle: Implementação de loops while e condicionais if/else para gestão do fluxo de estado.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x
