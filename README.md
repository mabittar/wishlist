# WishList using FastAPI
---

FastAPI framework, high performance, easy to learn, fast to code, ready for production

All documentation is in the "docs" directory and online at https://fastapi.tiangolo.com/. If you're just getting started, here's how we recommend you read the docs:

## WebApp

<table>
<tr>
<td>
  Usingo FastAPI to create a wishlist
</td>
</tr>
</table>


## Como desenvolver?

  1. clone o repositório
  2. crie o venv com Python 3.6 ou superior
  3. ative o venv
  4. instale as dependências utilizando `pip install -r requirements-dev.txt`
  5. execute os testes com `python -m pytest`
  6. para executar a API localmente utilize: `uvicorn main:app --reload`
  7. abra o navegador na página indicada: http://127.0.0.1:8000
  8. para acessar a documentação interativa acesse: http://127.0.0.1:8000/docs


  ## Como fazer o Deploy?
  1. crie uma instância no heroku utilizando `heroku create meu_projeto`
  2. envie suas configurações para o heroku com `heroku config:push`
  3. envie o código para o heroku utilizando `git push heroku master --force`

