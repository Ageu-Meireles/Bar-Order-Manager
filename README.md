# Bar Order Manager 

## Descrição
<p align="justify">Sistema de gerenciamento de pedidos para bares e/ou restaurantes.</p>

## Links úteis  :sos:
- [Documentação Django](https://docs.djangoproject.com/)
- [Documentação HTML5](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
- [Documentação CSS3](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
- Instalação do python3:
    - [Linux](https://python.org.br/instalacao-linux)
    - [Windows](https://python.org.br/instalacao-windows)
    - [Mac](https://python.org.br/instalacao-mac)


## Requisitos de sistema
- python 3.8.10+ (consulte [links úteis](https://github.com/Ageu-Meireles/Bar-Order-Manager#links-%C3%BAteis--sos))
- pip 20.0.2+
- python3-virtualenv 20.14.x+
```
$> pip3 install virtualenv     # Podem ser necessários privilégios de superusuário
```

## Dependências
Consulte [requirements](./requirements.txt)

## Instruções de construção

### Configuração

1. Primeiro clone o repositório localmente e depois acesse seu diretório
```
$> git clone https://github.com/Ageu-Meireles/Bar-Order-Manager.git

$> cd Bar-Order-Manager
```

2. Crie o ambiente virtual:
```
$> python3 -m venv .env
```

3. Ative o ambiente virtual:
```
$> source .env/bin/activate
```

4. Instale as dependências:
```
$> pip3 install -r requirements.txt
```

### Banco de dados

- Crie e aplique as migrations
```
$> python3 manage.py makemigrations

$> python3 manage.py migrate
```

## Utilização

Acesse o diretório raiz da aplicação e execute o comando:
```
$> python3 manage.py runserver
```
Em seu navegador acesse o servidor local através da url `http://127.0.0.1:8000/` ou `http://localhost:8000/`
