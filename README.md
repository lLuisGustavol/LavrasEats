# LavrasEats — Descubra os Melhores Restaurantes de Lavras com IA! 🤖❤️

Uma plataforma inteligente para avaliar e descobrir restaurantes em Lavras.  
Os usuários escrevem avaliações com texto livre, e a **IA do Google Gemini** analisa o sentimento e atribui uma nota de 0 a 10.  
Além disso, o usuário pode escrever um **prompt** pedindo sugestões, e a IA recomenda os restaurantes mais compatíveis com o pedido.

---

## 💡 Sobre o Projeto

LavrasEats é uma plataforma web onde qualquer pessoa pode deixar uma avaliação textual sobre um restaurante de Lavras.  
Diferente dos sistemas tradicionais, aqui usamos **Inteligência Artificial** para interpretar o sentimento do texto, gerar uma nota e ainda fornecer **sugestões personalizadas** a partir de prompts.

Exemplo:
> "Quero tomar um açaí hoje que seja bem recheado"
  
A IA buscará nas avaliações existentes restaurantes de açaí bem avaliados e indicará os que mais se encaixam no pedido.

---

## 🎯 Objetivos

- Criar uma forma inovadora de avaliar restaurantes com base em sentimentos e experiências reais.  
- Utilizar IA para:
  - Classificar textos como positivos, neutros ou negativos.
  - Atribuir uma nota estimada (0 a 10) com base nos elogios e críticas.  
  - Responder prompts de recomendação de forma inteligente.
- Exibir os restaurantes mais bem avaliados da cidade.
- Permitir buscas avançadas por categoria, preço e qualidade da experiência.

---

## 🧠 Como Funciona

1. **Avaliação:**  
   O usuário escreve uma avaliação livre sobre o restaurante.  
   O texto é enviado ao backend, que chama o modelo **Gemini AI** para:
   - Interpretar o sentimento (positivo, neutro, negativo)
   - Atribuir uma nota (0 a 10)
   - Gerar um breve parágrafo explicativo justificando a nota  

2. **Sugestões via Prompt:**  
   O usuário escreve algo como:  
   `"Quero comer uma pizza com bastante queijo hoje, de um lugar que não demore mais do que 1h para entregar."`  
   A IA filtra e ranqueia os restaurantes avaliados que melhor atendem ao pedido.

---

## 🧪 Critérios de Avaliação da IA

- **Tom geral** do texto  
- **Elogios ou críticas** específicas (atendimento, preço, ambiente, sabor)  
- **Detalhamento**: textos mais ricos tendem a gerar notas mais confiáveis  
- **Uso de adjetivos**: "excelente", "horrível", "ok", etc. influenciam a nota  
- **Contradições internas**: "a comida é boa, mas o atendimento é ruim" → nota intermediária  

⚠️ As análises são automáticas e podem não ser perfeitas — o objetivo é capturar o sentimento geral.

---

## 💡 Recomendações Inteligentes

Além das avaliações de restaurantes, o LavrasEats agora oferece **sugestões personalizadas** com base no que o usuário deseja comer.  
O usuário pode escrever um prompt descrevendo suas preferências, e a IA interpreta o texto para recomendar restaurantes que melhor atendem ao pedido.

**Exemplo de prompt:**

> "Quero comer um hambúrguer artesanal que seja rápido e tenha boas avaliações de sabor."

O sistema analisa:  
- 📝 As avaliações existentes dos restaurantes  
- 🍔 O tipo de comida desejada  
- ⏱️ Critérios como rapidez no atendimento, qualidade, preço e experiência geral  

E retorna uma lista de restaurantes **ordenada pelo melhor encaixe com o prompt**.

---

## 🚀 Funcionalidades

- 📝 **Cadastro de restaurantes** e envio de avaliações textuais  
- 🤖 **Análise automática de sentimento e nota** com IA Gemini  
- 🔎 **Busca por categoria e ranking** (melhores/piores)  
- 💬 **Sistema de prompts** para sugestões personalizadas  
- ⭐ **Cálculo de média de notas** por restaurante  
- 📊 **Ranking geral** dos restaurantes mais bem avaliados  
- ☁️ **API RESTful** para integração com frontend  
- 🔐 **Confirmação de cadastro por email** via SMTP Gmail  

---

## ⚙️ Tecnologias Utilizadas

**Backend**
- Python + Django — Framework principal
- Django REST Framework — Criação de APIs RESTful
- PostgreSQL — Banco de dados relacional
- djangorestframework-simplejwt — Autenticação JWT
- Gemini API — Análise de sentimento e prompts de recomendação
- SMTP Gmail — Envio de emails para confirmação

**Frontend**
- React + Vite — Interface web
- TailwindCSS — Estilização moderna e responsiva

**Infraestrutura**
- Docker & Docker Compose — Containerização do backend, banco e frontend
- pgAdmin4 — Gerenciamento do banco
- Postman — Testes de API

---

## 📖 Guia de Instalação

### 1️⃣ Criar os arquivos `.env`

No diretório `backend`, crie um `.env` com:

```env
GEMINI_API_KEY=sua-chave-gemini-aqui

SECRET_KEY="django-insecure-sua-chave"
DEBUG=True

EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=sua-senha-de-app

DB_NAME=lavraseats
DB_USER=postgres
DB_PASSWORD=sua-senha-do-banco
DB_HOST=db
DB_PORT=5432
```

No diretório `frontend`, crie um `.env` com:

```env
VITE_API_URL=http://localhost:8000/api
VITE_NODE_ENV=development
```

---

### 2️⃣ Subir os containers com Docker Compose

Na raiz do projeto:

```bash
docker-compose up --build
```

Isso irá iniciar:
- Backend Django
- Banco de dados PostgreSQL
- Frontend React

---

### 3️⃣ Aplicar as migrations manualmente

```bash
docker exec -it lavraseats_backend python manage.py migrate
```

---

### 4️⃣ Criar Superusuário do Django

```bash
docker exec -it lavraseats_backend python manage.py createsuperuser
```

---

### 5️⃣ Acessar a aplicação
 
- Frontend: [http://localhost:3000](http://localhost:3000)

Para parar os containers:

```bash
docker-compose down
```

---

## 👥 Integrantes do Projeto

- 🎓 **Leonardo Gonçalves Flora**
- 🎓 **Luis Gustavo Morais** 

---

## 🧠 Inspiração

Comer bem é uma experiência única — mas nem sempre as estrelas do Google contam a história completa.  
O **LavrasEats** quer mudar isso, valorizando o que os clientes realmente sentem e recomendando lugares de forma personalizada.
