# API Blog post

Sample solution for the [[Blogging Platform API](https://roadmap.sh/projects/blogging-platform-api)] challenge from [[roadmap.sh](https://roadmap.sh/)]

API desenvolvida em Django para gerenciar criacao e atualizacao de posts

## Índice
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Usar](#como-usar)


## Pré-requisitos

- Python  = "^3.12"
- Poetry

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/Edcarloszaya/ApiBlog.git
    ```

2. Entre na pasta do projeto:

    ```bash
    cd ApiBlog
    ```

3. Instale as dependências com Poetry :
    
    se nao tiver o poetry instale
     ```bash
    pip install poetry
    ```
    Instale as depencias
    ```bash
    poetry install
    ```

4. Ative o ambiente virtual gerenciado pelo Poetry:

    ```bash
    poetry shell
    ```

## Configuração


1. Rode as migrações do banco de dados:

    ```bash
    poetry python manage.py migrate
    ```

## Como Usar

1. Para rodar o servidor local, use:

    ```bash
    poetry python manage.py runserver
    ```
2.   Acesse a api no navegador :

    http://127.0.0.1:8000/posts/

    vai ser renderizado uma interface intuitiva pra fazer o crud na api

    exemplo  pra cria o post : 

    {
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"]
    }

## Como Testa use Postman ou Insomnia:
1. Criar  post:
    POST  http://127.0.0.1:8000/posts/

    json body:

    {
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"]
    }

2. Update post:
    PUT /posts/1

    json body:

    {
    "title": "My update First Blog Post",
    "content": "This is the content of my first blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"]
    }

3. Delete post:
    DELETE /posts/1

4 Lista um post:
    GET /posts/1

5. Lista todos os posts:
    GET /posts

6. Filtra post por term:
    GET /posts?term=term

    GET /posts?term=tech

    return:
    {
    "title": "My update First Blog Post",
    "content": "This is the content of my first blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"]
    }

2. Atualiza um unico campo no post:
    PATH /posts/1

    json body:

    {
    "tags": ["Python", "Django"]
    }

    