# Eventex

Sistema de Eventos encomendado pela Morena

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o seu virtualenv
4. Insstale as dependências
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:ruanmoa/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```
## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para instância. 
4. Defina DEBUG=false.
5. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secrec_gen.py`
heroku config:set DEBUG=False
# configure o email
git push heroku master --force 
```
