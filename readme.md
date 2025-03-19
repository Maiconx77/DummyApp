# DummyApp

DummyApp é um projeto de estudo que implementa o padrão de arquitetura **MVC (Model-View-Controller)** utilizando Python e SQLAlchemy. O objetivo principal deste projeto é explorar e compreender os conceitos fundamentais do padrão MVC, aplicando-os em um ambiente prático e funcional.

## Estrutura do Projeto

O projeto está organizado em três camadas principais:

- **Model (Modelo):** Responsável pela definição e manipulação dos dados. Utiliza o SQLAlchemy para mapear as tabelas do banco de dados e gerenciar as interações com o SQLite.
- **View (Visão):** Será responsável pela interface com o usuário, podendo ser implementada como uma interface gráfica ou uma interface de linha de comando.
- **Controller (Controlador):** Gerencia a lógica de negócios, conectando os modelos e as visões para garantir o fluxo correto de informações.

## Tecnologias Utilizadas

- **Python 3.10+**
- **SQLAlchemy:** Para ORM (Object-Relational Mapping) e manipulação do banco de dados.
- **SQLite:** Banco de dados leve e integrado para armazenamento de dados.

## Estrutura Atual

Atualmente, o projeto conta com as seguintes tabelas no banco de dados:

- **Projects:** Representa os projetos, contendo informações como código, título e descrição.
- **Deliverables:** Representa os entregáveis associados a um projeto, com informações como título, peso e status de conclusão.
- **Progresses:** Representa o progresso de um entregável, incluindo marcos, datas planejadas e realizadas, e valores associados.

## Objetivo do Estudo

Este projeto tem como objetivo:

1. Compreender o padrão MVC e sua aplicação prática.
2. Aprender a utilizar o SQLAlchemy para modelagem e manipulação de dados.
3. Desenvolver habilidades em organização de código e boas práticas de desenvolvimento.

## Como Executar

1. Clone este repositório em sua máquina local.
2. Certifique-se de ter o Python 3.10+ instalado.
3. Instale as dependências necessárias:
   ```bash
   pip install sqlalchemy