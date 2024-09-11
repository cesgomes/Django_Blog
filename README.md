# Django_Blog

Treinamento em Django, criação de Blog.

### Getting Started
Criar o projeto: 
```python
django-admin startproject <nome_do_projeto>

```
Executar o servidor:

```python
python.exe .\manage.py runserver
```

### Applications and routes
Criar o app:
```python
python.exe .\manage.py startapp <AppName>
```

### Templates
Há algum problema ao carregar o static para o CSS (pode ser para todos os static). Recomenda-se reiniciar o servidor para corrigir

### Admin Page 
## Primeiramente precisa efetuar as migrações

```python
python.exe .\manage.py makemigrations 
python.exe .\manage.py migrate  
python.exe .\manage.py createsuperuser #Cria o admin do app
```
