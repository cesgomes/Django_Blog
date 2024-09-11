# Django_Blog

Treinamento em Django, criação de Blog.

## Getting Started
Criar o projeto: 
```python
django-admin startproject <nome_do_projeto>

```
Executar o servidor:

```python
python.exe .\manage.py runserver
```

## Applications and routes
Criar o app:
```python
python.exe .\manage.py startapp <AppName>
```

## Templates
Há algum problema ao carregar o static para o CSS (pode ser para todos os static). Recomenda-se reiniciar o servidor para corrigir

## Admin Page 
### Primeiramente precisa efetuar as migrações

```python
python.exe .\manage.py makemigrations 
python.exe .\manage.py migrate  
python.exe .\manage.py createsuperuser #Cria o admin do app
```

### Criação via  admin page: 
- *active*: Pode efetuar logon no site
- *Staff*: Permite entrar na área administrativa do site
- *Superuser*: Status de Power user do site 

## Database and Migrations
Após a criação do model, necessário makemigrations para preparar a criação da tabela
Para visualizar o comando SQL que será executado, precisa do nome do app e do ID do programa a ser gerado (na pasta migrations):
```python
python.exe .\manage.py sqlmigrate <app> <id> 
``` 
por exemplo:
```python
python.exe .\manage.py sqlmigrate blog 0001
``` 
