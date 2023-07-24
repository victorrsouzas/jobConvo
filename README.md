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
   python manage.py migrate
   ```
5. Inicie o servidor de desenvolvimento do Django:
   ```
   python manage.py runserver
   ```
6. Acesse o sistema no navegador: http://127.0.0.1:8000/

## Contribuição

Se você quiser contribuir com o projeto, sinta-se à vontade para abrir uma "issue" ou enviar um "pull request" com suas melhorias.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
