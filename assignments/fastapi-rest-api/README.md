# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para cadastrar e gerenciar livros usando FastAPI. Ao concluir, você terá praticado rotas HTTP, validação de dados com modelos Pydantic e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Implementar listagem e cadastro de livros

#### Descrição
Complete os endpoints iniciais para listar os livros cadastrados e adicionar um novo livro. Use o código inicial e mantenha os dados em memória enquanto a aplicação estiver em execução.

Para preparar o ambiente, instale FastAPI e Uvicorn e inicie a aplicação:

```bash
python -m pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

Abra `http://127.0.0.1:8000/docs` para interagir com a documentação automática da API.

#### Requisitos
O programa concluído deve:

- Definir um modelo `BookCreate` com título e autor e um modelo `Book` que também tenha um identificador inteiro.
- Implementar `GET /books` para retornar todos os livros, inicialmente como uma lista vazia.
- Implementar `POST /books` para cadastrar um livro, gerar seu identificador no servidor e responder com o livro criado e status `201`.
- Permitir testar os dois endpoints pela página `/docs`.

### 🛠️ Consultar e atualizar um livro

#### Descrição
Adicione operações para consultar um livro pelo identificador e substituir seus dados. A API deve informar claramente quando o identificador solicitado não existir.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` e retornar o livro correspondente.
- Implementar `PUT /books/{book_id}` para atualizar o título e o autor do livro existente.
- Responder com status `404` usando `HTTPException` quando não houver livro com o identificador informado.
- Verificar os resultados e o caso de identificador inexistente em `/docs`.

### 🛠️ Remover livros e conferir os códigos de resposta

#### Descrição
Finalize a API implementando a remoção de livros e revise o comportamento dos endpoints. Os dados podem permanecer em memória; não é necessário criar banco de dados.

#### Requisitos
O programa concluído deve:

- Implementar `DELETE /books/{book_id}` para remover um livro existente e responder com status `204`.
- Responder com status `404` se o livro a remover não existir.
- Confirmar que um livro removido não aparece mais em `GET /books` e que sua consulta individual retorna `404`.
- Usar os métodos HTTP e os códigos de resposta definidos para cada operação da API.
