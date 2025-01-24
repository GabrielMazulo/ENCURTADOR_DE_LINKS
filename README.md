# URL Shortener API  
Uma API para encurtar links, com suporte a controle de cliques únicos, expiração de links e redirecionamento.  

🚀 Funcionalidades  

- Criar link curto: Gera um link único com limite de cliques e data de expiração.
- Redirecionamento: Redireciona para o link original ao acessar o link curto.
- Controle de cliques únicos: Limita o número de cliques únicos permitidos por link.
- Atualizar link: Permite modificar os detalhes de um link existente, como o token, o link de redirecionamento, etc.

🛠️ Como Configurar

-  Clone o Repositório
bash
Copiar
Editar
git clone https://github.com/seu-usuario/url-shortener-api.git
cd url-shortener-api
-  Crie um Ambiente Virtual
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate
 - venv\Scripts\activate
-  Instale as Dependências
bash
Copiar
Editar
pip install -r requirements.txt
-  Configure o Banco de Dados
Edite o arquivo settings.py para configurar o banco de dados.
Aplique as migrações:
bash
Copiar
Editar
python manage.py makemigrations
python manage.py migrate
-  Inicie o Servidor
bash
Copiar
Editar
python manage.py runserver
A API estará disponível em http://127.0.0.1:8000/.

🔗 Endpoints da API  

1. Criar um Link Curto
  - URL: /create/
  - Método: POST
  - Corpo da Requisição (JSON):
  - Respostas:
     - 200: Link criado com sucesso.
     - 409: Token já existe.
       
2. Redirecionar para o Link Original
  - URL: /{token}
  - Método: GET
  - Descrição: Redireciona para o link original associado ao token.
  - Respostas:
     - 200: Redireciona para o link original.
     - 404: Link expirado ou não encontrado.
       
3. Atualizar um Link Existente
 - URL: /{link_id}/
- Método: PUT
 - Corpo da Requisição (JSON):
 - Respostas:
    - 200: Link atualizado com sucesso.
    - 409: Token já está em uso.
      
🧪 Testes  
Use ferramentas como Postman ou curl para testar os endpoints.   

📚 Modelos Utilizados  
Links  
Armazena os dados dos links curtos criados.  

- Campos principais:
 - token: Identificador único do link.
 - redirect_link: URL original para onde o link curto redirecionará.
 - expiration_time: Data e hora de expiração.
 - max_uniques_cliques: Limite de cliques únicos.

Clicks  
Registra os cliques realizados em cada link.   
- Campos principais:
  - link: Referência ao link curto associado.
  - ip: Endereço IP de quem clicou.

🛡️ Regras de Validação  
1. Token único: Tokens duplicados não são permitidos.  
2. Expiração: Links expirados não redirecionam.  
3. Cliques únicos: O limite de cliques únicos é respeitado.

🖋️ Contribuição  
Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar esta API.  


