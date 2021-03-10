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

  [x] Deve existir um endpoint para trazer os itens da lista que ainda não foram ganhos / adquiridos.

    [ ] Evoluir o endpoint trazer um item da lista de forma randômica.

  [x] Ter uma base de dados que armazene as informações

  [ ] Usar o docker-compose para subir um banco de dados junto com a aplicação

  Diferenciais:

    [ ] Suportar múltiplos usuários
    [ ] Diferencial: Testes Unitários

## Como desenvolver?

  1. clone o repositório com `git clone https://github.com/mabittar/wishlist.git`
  2. mova o caminho para o diretório do projeto `cd wishlist`
  3. crie o venv com Python 3.6 ou superior `python -m venv .`
  4. ative o venv `.\Scritps\activate`
  5. instale as dependências utilizando `pip install -r dev-requirements.txt`
  6. execute os testes com `python -m pytest`
  7. para executar a API localmente utilize: `uvicorn main:app --reload`
  8. abra o navegador na página indicada: http://127.0.0.1:8000
  9. para acessar a documentação interativa acesse: http://127.0.0.1:8000/docs


  ## Como fazer o Deploy?
  1. crie uma instância no heroku utilizando `heroku create meu_projeto` substitua o meu_projeto pelo seu projeto
  2. envie suas configurações para o heroku com `heroku config:push`
  3. envie o código para o heroku utilizando `git push heroku main --force`
  4. para abrir sua aplicação online utilize `heroku open`
