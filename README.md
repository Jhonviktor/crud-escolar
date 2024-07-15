<h1>Crud escolar</h1>

> Status: Developing

### Bem-vindos ao meu desafio, Sistema CRUD Escolar, onde aqui pude elaborar um banco de dados utilizando o banco SQLite3, nativo do Python, usando o mesmo como linguagem e utilizando o FastAPI para criar interações com o banco e subir uma interface Web.

### Pré-requisitos
+ Utilizei o FastAPI, onde possui um servidor web próprio, cópie o código abaixo para poder instalar a biblioteca, iremos usa-lo para subir o servidor: 

+ `pip install uvicorn`
+ `pip install sqlite3` - apenas para caso não possuir o banco instalado.

+ Não será necessário instalar outra biblioteca, a maioria é nativa do próprio Python, mas caso precise, tente instalar por favor.

## Inicialização rápida

### Observação
+ Por favor executar tudo via terminal e seguir passo a passo para evitar erros.

### 1. Clone repositório e vá ao diretorio raíz:
+ 1 - `git clone https://github.com/Jhonviktor/crud-escolar.git`
+ 2 - `cd app`

### 2. Inicie o servidor web do FastAPI:
+ 1 - `uvicorn app.main:app --reload`
+ 2 - Assim que realizar o comando para subir o Web Server, cole isso no navegador, então isso você irá acessar a interface da API:
+ `http://127.0.0.1:8000/docs/`

### 3. Explicação do que foi feito até agora:
+ Consegui realizar a criação do banco de forma local, usando o SQLite3, um banco simples e fácil de utilizar para aplicações "pequenas", onde não há necessidade de um servidor para o banco.
+ Então eu montei uma API, com o FastAPI, onde consigo inserir, consultar, altera e apagar algum elemento de uma tabela. Realizei testes e tive vários problemas na hora de realizar consulta e deletar, mas consegui consertar esses erros.
+ Não consegui criar um front, tive vários outros rascunhos, mas estava com problema de não salvar as informações no BD, então para o momento optei apenas para deixar a API.

## Considerações Finais
Acredito que tive muitos problemas em ligar a API com o banco, visto que manipular o SQLite é bem simples. E ao tentar criar um front, acabei encontrando vários desafios que seriam de:
+ Não consegui criar uma interface para editar, consultar e apagar, apenas para inserir.
+ Quando criei a interface web para inserir os elementos do banco, as informações não ficavam salvas no banco e isso me custou 2 dias então optei apenas por apresentar a API.
+ Espero que tenham gostado e conseguido realizar o acesso, não consegui cirar um servidor Docker, mas com certeza irei fazer isso daqui para frente.
+ Espero que se tiverem algum problema eu poder realizar a ajuda necessária.
