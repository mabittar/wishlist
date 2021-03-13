# WishList using FastAPI and SQLAlchemy

---


## O desafio

  Construir uma API usando Python 🐍

## Requisitos

  [x] Criar uma API para gerir uma WishList (Lista de Desejos)

  [x] O usuário deve poder incluir um produto em sua lista de desejos:

    Título do Produto (obrigatório)
    Descrição (opcional)
    Link de onde encontrar (opcional)
    Foto (opcional)

  [x] O usuário deve poder informar se já ganhou/comprou um item.

  [x] Deve existir um endpoint para trazer os itens da lista que ainda não foram ganhos / adquiridos.

    [ ] Evoluir o endpoint trazer um item da lista de forma randômica.

  [x] Ter uma base de dados que armazene as informações

  [x] Usar o docker-compose para subir um banco de dados junto com a aplicação

  Diferenciais:

    [ ] Suportar múltiplos usuários
    [x] Testes Unitários

## Como desenvolver?

  1. clone o repositório com `git clone https://github.com/mabittar/wishlist.git`
  2. mova o caminho para o diretório do projeto `cd wishlist`
  3. crie o venv com Python 3.6 ou superior `python -m venv .`
  4. ative o venv `.\Scripts\activate`
  5. instale as dependências utilizando `pip install -r dev-requirements.txt`
  6. execute os testes com `pytest test/`

  7. para executar a API localmente utilize: `uvicorn main:app --reload`
  8. abra o navegador na página indicada: http://127.0.0.1:8000
  9. para acessar a documentação interativa acesse: http://127.0.0.1:8000/docs

Todos os endpoints estão documentados via [SwaggerUI](https://swagger.io/tools/swagger-ui/), que pode ser acessado no endereço indicado no item 9.

  ## Como fazer o Deploy? 
  [minha app no Heroku](https://wishlist-mmb.herokuapp.com/docs)

  0. observe os procedimentos de instalação do Heroku CLI em https://devcenter.heroku.com/articles/heroku-cli
  1. crie uma instância no heroku utilizando `heroku create meu_projeto` substitua meu_projeto pelo nome do seu projeto
  2. envie o código para o heroku utilizando `git push heroku main --force`
  3. para abrir sua aplicação online utilize `heroku open`

Processo de deploy e build são feitos automaticamente na branch main.

  ## Docker

  0. instale o docker conforme orientações em `https://docs.docker.com/compose/install/`
  1. para criar a imagem execute execute o comando no terminal `docker-compose up -d`
  2. verifique se a imagem foi construída com `docker images`
  3. verifique o compartilhamento de rede com `docker ps`
  4. abra o navegador em `http://localhost:8000/docs`
