# Automated Emails

O programa está escrito em Python. O aplicativo lerá os nomes e endereços de e-mail e interesses do arquivo people.xlsx e enviará um e-mail a cada usuário todas as manhãs ou em outras horas do dia. O e-mail conterá as notícias sobre os interesses do usuário para aquele dia.

## Instalar dependências

```bash
pipenv install pytest-cov --dev
```

## Instalar os scripts configurados do pre-commit

```bash
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Rodar o Bandit

```bash
pipenv run python -m bandit .
```

## Rodar o Safety

```bash
pipenv run python -m safety check
```
