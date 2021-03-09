# WishList using FastAPI
---
<table>
<tr>
<td>
  Using FastAPI to create a wishlist
</td>
</tr>
</table>

## O desafio
  Construir uma API usando Python 🐍

## Requisitos
  [x] Criar uma API para gerir uma WishList (Lista de Desejos)

  [x] O usuário deve poder incluir um produto em sua lista de desejos:

    Título do Produto (obrigatório)
    Descrição (opcional)
    Link de onde encontrar (opcional)
    Foto (opcional)

  [ ] O usuário deve poder informar se já ganhou/comprou um item.

  [ ] Deve existir um endpoint para trazer um item da lista de forma randômica.

  [ ] Ter uma base de dados que armazene as informações

  [ ] Usar o docker-compose para subir um banco de dados junto com a aplicação

  Diferenciais:

    [ ] Suportar múltiplos usuários
    [x] Diferencial: Testes Unitários

## Como desenvolver?

  1. clone o repositório
  2. crie o venv com Python 3.6 ou superior
  3. ative o venv
  4. instale as dependências utilizando `pip install -r dev-requirements.txt`
  5. execute os testes com `python -m pytest`
  6. para executar a API localmente utilize: `uvicorn main:app --reload`
  7. abra o navegador na página indicada: http://127.0.0.1:8000
  8. para acessar a documentação interativa acesse: http://127.0.0.1:8000/docs


  ## Como fazer o Deploy?
  1. crie uma instância no heroku utilizando `heroku create meu_projeto`
  2. envie suas configurações para o heroku com `heroku config:push`
  3. envie o código para o heroku utilizando `git push heroku master --force`

