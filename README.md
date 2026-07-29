# 🐙 GitHub User Activity CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/GitHub%20REST%20API-v3-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub API" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

> Uma interface de linha de comando (CLI) leve, performática e construída exclusivamente com módulos nativos do Python para buscar e exibir o histórico recente de atividades públicas de qualquer usuário do GitHub.

Projeto desenvolvido para resolver o desafio [GitHub User Activity](https://roadmap.sh/projects/github-user-activity) do **roadmap.sh**.

---

## 🎯 Destaques do Projeto

- **Zero Dependências Externas:** Desenvolvido puramente com a biblioteca padrão do Python (`urllib.request`, `json`, `argparse`), garantindo instalação e execução instantâneas.
- **Arquitetura Limpa (Clean Code):** Separação clara de responsabilidades entre a interface de linha de comando (CLI) e a camada de integração com a API.
- **Padrão de Projeto Dispatch Table:** Elimina encadeamentos gigantescos de `if/elif/else`, facilitando a manutenção e adição de novos tipos de eventos.
- **Tratamento Defensivo de Erros:** Manipulação graciosa de falhas de conexão, limites da API, erros HTTP (como `404 Not Found`) e validações de input.

---

## 🚀 Como Executar

### Pré-requisitos

- **Python 3.10+** instalado no seu sistema.

### Passo a Passo

1. **Clone o repositório:**

   ```bash
   git clone [https://github.com/SEU-USUARIO/Atividade_do_usuario_GITHUB.git](https://github.com/SEU-USUARIO/Atividade_do_usuario_GITHUB.git)
   cd Atividade_do_usuario_GITHUB
   ```

2. **Execute a aplicação:**

   ```bash
   python3 main.py "<nome-do-usuario>"
   ```

3. **Exemplo**

   ```bash
   python3 main.py "PedroManoel22"
   ```
