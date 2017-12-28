# django-olimpo
## Não esta funcionando nada, não há garantias
Sistema Financeiro simples em django para uso pessoal,

ele roda localmente um servidor python para uso em desenvolvimento.

Para rodalo na inicialização do seu computador use esse tutorial para deploy na sua maquina:
[Deploy + guinicor + postgres + nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)

* não e necessario usar postgress inicialmente, mas e aconselhado

# Para instalar ambinete
clone o repositorio:
```
git clone https://github.com/Perceu/django-olimpo.git
```

entre na pasta: 
```
cd django-olimpo
```

Crie uma virtualenv usando python3
```
python -m venv .olimpo
```

Ative a Virutual Env
```
source .olimpo/bin/activate
```

Instale as dependencias
```
pip install -r requirements.txt
```

# Para instalar sistema
Rode as migrações:
```
python manage.py migrate
```

Rode o comando:
```
python manage.py runserver
```

Para acessar o va no seu navegador e acesse:
```
127.0.0.1:8000/
```



# Para contribuir/fazer pedidos/ajustes/reportar bugs/ 

favor colocar no assunto [django-olimpo]
perceubertoletti@gmail.com


