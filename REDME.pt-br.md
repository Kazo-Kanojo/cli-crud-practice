# 🚀 Gerenciador de Fila FIFO (CRUD em Python)

*leia em outros idiomas: [English](README.md), [Português](README.pt-br.md).*

Este projeto é um sistema de gerenciamento em terminal desenvolvido em Python. Ele demonstra a implementação prática de um **CRUD completo (Create, Read, Update, Delete)** aplicado a uma estrutura de dados baseada no conceito **FIFO (First-In, First-Out)**.



## 💡 Sobre o Projeto

O objetivo deste projeto é simular uma fila de atendimento onde o primeiro cliente a entrar é, obrigatoriamente, o primeiro a ser servido. A aplicação roda em loop no terminal, oferecendo um menu interativo e tratando exceções para garantir que o programa não quebre com entradas inválidas do usuário.

## 🛠️ Funcionalidades (O CRUD)

O sistema mapeia perfeitamente as operações CRUD para a gestão da fila:

* **Create (Criar):** Adiciona um ou múltiplos clientes ao final da fila simultaneamente.
* **Read (Ler):** Exibe todos os clientes atualmente na fila, mostrando suas respectivas posições.
* **Update (Atualizar):** Permite buscar um cliente pelo nome e alterar seu registro na fila sem perder a posição original.
* **Delete (Deletar):** * *Por atendimento (FIFO):* Atende todos os clientes na ordem correta, removendo-os da fila.
    * *Por desistência:* Remove um cliente específico da fila buscando pelo nome.

## 🧠 Destaques Técnicos

* **Structural Pattern Matching (`match/case`):** Utilização do recurso moderno do Python 3.10+ para um fluxo de controle mais limpo e declarativo no menu principal, substituindo longas cadeias de `if/elif`.
* **Tratamento de Exceções (`try/except`):** Validação de inputs garantindo que o usuário digite números quando solicitado, evitando o erro `ValueError`.
* **Modularização:** Código estruturado em funções com responsabilidades únicas (Single Responsibility Principle), facilitando a manutenção e leitura.

## 🚀 Como Executar na sua Máquina

1. Certifique-se de ter o **Python 3.10 ou superior** instalado (necessário para o `match/case`).
2. Clone este repositório:
   ```bash
   git clone https://github.com/Kazo-Kanojo/cli-crud-practice
   python main.py
