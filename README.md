# # JobConvo - Sistema de Vagas e Candidatos

JobConvo é um sistema web desenvolvido com Django que permite que empresas criem vagas de emprego e os candidatos se candidatem a essas vagas. O sistema também fornece recursos para que as empresas possam visualizar os candidatos que se candidataram a cada vaga e editar ou excluir as vagas criadas.

## Funcionalidades Principais

- Cadastro de usuários com email e senha.
- Empresas podem criar vagas com informações como nome, faixa salarial e requisitos.
- Candidatos podem se candidatar a vagas informando pretensão salarial, experiência e escolaridade.
- Visualização dos candidatos que se candidataram a cada vaga, com detalhes de seus dados.
- Cálculo de pontuação dos candidatos com base na faixa salarial e escolaridade desejada pela empresa.
- Relatório com gráficos usando a biblioteca Charts.js, mostrando quantidade de vagas criadas e candidatos recebidos por mês.

## Pré-requisitos
- Python 3.4 ou superior
- Django 2.2 ou superior
- Bibliotecas listadas no arquivo requirements.txt

## Como Rodar o Projeto

1. Clone o repositório para sua máquina local.
2. Crie um ambiente virtual e ative-o:
   ```
   python -m venv venv
   source venv/bin/activate   # No Windows: venv\Scripts\activate
   ```
3. Instale as dependências do projeto:
   ```
   pip install -r requirements.txt
   ```
4. Crie as tabelas do banco de dados:
   ```
   python manage.py makemigrations jobs
   python manage.py migrate
   ```
4. Para acessar o painel administrativo do Django, é necessário criar um superusuário:
   ```
   python manage.py createsuperuser
   ```
5. Rode os testes:
   ```
   python manage.py test
   ```
6. Inicie o servidor de desenvolvimento do Django:
   ```
   python manage.py runserver
   ```
7. Acesse o sistema no navegador: http://127.0.0.1:8000/

## Fluxo das Rotas
Rota Principal:
- /admin/: Acesso ao painel administrativo do Django
- /accounts/: URLs de autenticação do Django
- /: Lista de vagas de emprego (JobListView)
- /jobs/<int:pk>/: Detalhes de uma vaga específica (JobDetailView)
- /jobs/<int:pk>/apply/: Candidatura a uma vaga específica (job_apply)
- /jobs/<int:pk>/edit/: Edição de uma vaga específica (job_edit)
- /jobs/<int:pk>/delete/: Exclusão de uma vaga específica (job_delete)
- /accounts/login/: Página de login do usuário (job_login)
- /vagas-por-mes/: Gráfico com a quantidade de vagas criadas por mês (VagasPorMesView)
- /candidatos-por-mes/: Gráfico com a quantidade de candidatos recebidos por mês (CandidatosPorMesView)

## Contribuição

Se você quiser contribuir com o projeto, sinta-se à vontade para abrir uma "issue" ou enviar um "pull request" com suas melhorias.
