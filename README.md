# HabitCare CLI

Aplicação em linha de comando desenvolvida em Python para auxiliar usuários no gerenciamento de hábitos diários, promovendo organização, disciplina e acompanhamento de metas pessoais.

---

## Integrantes

- Ana Júlia Cardoso dos Santos
- Maria Morena da Silva Couto
- Victor Otaviano Alves Brito
- Jean de Almeida Brito
- Geovana Cristina Ferreira Moraes

---

## Objetivo

O HabitCare CLI permite que os usuários registrem e acompanhem hábitos diários de forma simples através do terminal.

---

## Funcionalidades

- Adicionar hábitos
- Listar hábitos
- Concluir hábitos
- Exibir frases motivacionais através da API ZenQuotes
- Persistência de dados utilizando Supabase

---

## Público-Alvo

- Estudantes
- Idosos
- Pessoas com rotina intensa
- Usuários que desejam criar hábitos saudáveis

---

## Tecnologias Utilizadas

- Python
- Pytest
- Ruff
- GitHub Actions
- Requests
- Supabase
- PostgreSQL

---

## Banco de Dados

O projeto utiliza o Supabase como solução de banco de dados em nuvem para armazenamento dos hábitos cadastrados pelos usuários.

---

## Configuração do Ambiente

Crie um arquivo `.env` na raiz do projeto contendo:

```env
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_do_supabase
```

> O arquivo `.env` não deve ser enviado ao GitHub.

---

## Instalação

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

---

## Execução

Execute a aplicação:

```bash
python src/main.py
```

---

## Testes

Executar os testes automatizados:

```bash
pytest
```

---

## Análise Estática de Código

Executar verificação com Ruff:

```bash
ruff check .
```

---

## Integração Contínua

O projeto utiliza GitHub Actions para execução automática dos testes e verificações de qualidade a cada Pull Request realizado.

---

## Versionamento

Versão atual:

```text
3.0.0
```

---

## Evolução do Projeto

O HabitCare CLI evoluiu de uma aplicação simples em linha de comando para um projeto que utiliza práticas reais de Engenharia de Software, incluindo:

- Controle de versão com Git e GitHub
- Trabalho colaborativo com Branches e Pull Requests
- Integração Contínua (CI)
- Consumo de APIs REST
- Testes Automatizados
- Banco de Dados em Nuvem (Supabase)
- Versionamento Semântico
- Revisão de Código (Code Review)

---

## Repositório

https://github.com/Anajulia-13/habitcare-cli
