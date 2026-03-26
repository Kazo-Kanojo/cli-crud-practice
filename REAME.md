# 🚀 FIFO Queue Manager (Python CRUD)

*Read this in other languages: [English](README.md), [Português](README.pt-br.md).*

This project is a terminal-based management system developed in Python. It demonstrates the practical implementation of a **complete CRUD (Create, Read, Update, Delete)** applied to a data structure based on the **FIFO (First-In, First-Out)** concept.

## 💡 About the Project

The goal of this project is to simulate a customer service queue where the first customer to enter is, necessarily, the first to be served. The application runs in a loop in the terminal, offering an interactive menu and handling exceptions to ensure the program doesn't crash from invalid user inputs.

## 🛠️ Features (The CRUD)

The system perfectly maps CRUD operations to the queue management:

* **Create:** Adds one or multiple customers to the end of the queue simultaneously.
* **Read:** Displays all customers currently in the queue, showing their respective positions.
* **Update:** Allows searching for a customer by name and modifying their record in the queue without losing their original position.
* **Delete:** * *By service (FIFO):* Serves all customers in the correct order, removing them from the queue.
    * *By cancellation:* Removes a specific customer from the queue by searching for their name.

## 🧠 Technical Highlights

* **Structural Pattern Matching (`match/case`):** Utilization of this modern Python 3.10+ feature for a cleaner and more declarative control flow in the main menu, replacing long `if/elif` chains.
* **Exception Handling (`try/except`):** Input validation ensuring the user types numbers when requested, preventing `ValueError` crashes.
* **Modularization:** Code structured into functions with single responsibilities (Single Responsibility Principle), making maintenance and readability easier.

## 🚀 How to Run

1. Ensure you have **Python 3.10 or higher** installed (required for the `match/case` feature).
2. Clone this repository:
   ```bash
   git clone [https://github.com/Kazo-Kanojo/cli-crud-practice](https://github.com/Kazo-Kanojo/cli-crud-practice)
   python main.py 