# Projeto Site de Orçamento

# Sobre 

Um sistema de Orçamento, onde o cliente fornece informações pessoais e descreve detalhadamente suas preferências por meio de um formulário. 

As informações são então armazenadas em um banco de dados Oracle através de uma procedure (PL/SQL). Além disso, o sistema envia automaticamente um e-mail para meu endereço de e-mail pessoal, contendo todas as informações fornecidas pelo cliente, bem como a descrição do pedido.


## Layout web

![pagina_vazia1](https://github.com/iuriAvil4/Projeto-Site-Orcamento/assets/92445654/e85df7ed-a8b8-42c9-9d1e-8b344554e9af)

![pagina_preenchida1](https://github.com/iuriAvil4/Projeto-Site-Orcamento/assets/92445654/3882e7f1-9971-49ee-8864-c319c4e2ffaf)


## Estrutura do e-mail enviado para o meu e-mail pessoal após a realização do orçamento
![print_email](https://github.com/iuriAvil4/Projeto-Site-Orcamento/assets/92445654/118cedbd-3a23-4136-9370-cdeaf90d6415)

## E assim ficará registrado no Oracle Database
![print_oracledb](https://github.com/iuriAvil4/Projeto-Site-Orcamento/assets/92445654/41169cd7-3672-46a3-8be6-b7df42459788)

## Procedure ADD_CLIENTE no sqldeveloper
```bash
CREATE OR REPLACE PROCEDURE add_cliente    (pnome      IN VARCHAR2,
                                            psobrenome IN VARCHAR2,
                                            pemail     IN VARCHAR2,
                                            ptelefone  IN VARCHAR2,  
                                            pdescricao IN NCLOB) IS
                            
BEGIN
    INSERT INTO app_orcamento_cliente  (nome,
                                        sobrenome,
                                        email,
                                        telefone,  
                                        descricao)
                                        
                             VALUES    (pnome,
                                        psobrenome,
                                        pemail,
                                        ptelefone, 
                                        pdescricao);

EXCEPTION
    WHEN OTHERS THEN
        -- Imprime o erro no console de saída do PL/SQL
        DBMS_OUTPUT.PUT_LINE('Erro ao inserir cliente: ' || SQLERRM);
END add_cliente;


```

# Tecnologias utilizadas
## Back end
- Python
- Django
- Oracle Database
- PL/SQL

## Front end
- HTML / CSS 
- Bootstrap

# Como executar o projeto

## Back end
Pré-requisitos: Python 3.1, Django 5.0

```bash
# Clonar repositório
git clone https://github.com/iuriAvil4/Projeto-Site-Orcamento

# Acessar a pasta projeto_orcamento no terminal integrado
cd projeto_orcamento

# Instalar o Framework Django
pip install django

# Configurar banco de dados
# entre no arquivo setting.py, e altere os campos contidos dentro da constant DATABASES,
# para as informações do seu banco de dados pra realizar a conexão

# Fazer migrações e aplicar no banco de dados
python manage.py makemigrations
python manage.py migrate

# Execute o projeto e clique no endereço fornecido
python manage.py runserver
```


# Autor

Iuri Avila Guerra

https://www.linkedin.com/in/iuriavilaguerra
