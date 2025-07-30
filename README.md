# 🌳 Trees Everywhere – Django Technical Challenge

Este projeto é parte de um teste técnico para a empresa **Youshop**, com foco em desenvolvimento backend utilizando **Django**, além de HTML, CSS e JavaScript com boas práticas.

---

## 🧱 Estrutura do Projeto

- **Autenticação**: Login com `LoginView`, botão de logout fixado no topo do dashboard.
- **Dashboard**: Exibe cards com contagem de usuários, contas e árvores, além de gráfico com distribuição de árvores (Chart.js).
- **Gerenciamento**:
  - Contas (`Account`)
  - Usuários (`User` e `Profile`)
  - Tipos de plantas (`Plant`)
  - Árvores plantadas (`PlantedTree`)

---

## ✅ Páginas Criadas

### 🔐 Login (`login.html`)
- Campo de usuário e senha com botão "Esqueceu a senha?"
- Estilo com tema de floresta/verde

### 📊 Dashboard (`dashboard.html`)
- Cards com dados do sistema (usuários, contas, etc)
- Gráfico com Chart.js
- Responsivo e com menu lateral + topbar

### 🧾 Listagem de Contas (`list_accounts.html`)
- Cards com: `name`, `created`, `active`
- Botão de ativar/desativar status via link

### ➕ Cadastro de Conta (`register_account.html`)
- Formulário com campo único `name`

### 👤 Listagem de Usuários (`list_users.html`)
- Cards com: `username`, `email`, `date_joined`, `is_active`
- Botão para cadastrar novo usuário

### ➕ Cadastro de Usuário (`register_user.html`)
- Campos: `first_name`, `last_name`, `email`, `password`
- Checklist de contas disponíveis
- Seleção de tipo de acesso: `Admin` (1) ou `Standard` (2)
- Se `Standard`, checklist se torna obrigatória (JS)

### 🌱 Listagem de Plantas (`list_plants.html`)
- Cards com: `name`, `scientific_name`, `description`
- Botão para cadastrar nova planta
- Botão “Ver Plantas” em cada card

### ➕ Cadastro de Planta (`register_plant.html`)
- Campos: `name` e `scientific_name`

### 🌳 Listagem de Árvores Plantadas (`list_planted_trees.html`)
- Cards com: `plant.name`, `user`, `latitude`, `longitude`, `created_at`
- Botão “Adicionar Planta Plantada”

---

## 🧠 Funcionalidades JavaScript
- Mostrar/ocultar senha no cadastro
- Esconder checklist de contas ao escolher “Admin”
- Validar que conta seja selecionada se o tipo for “Standard”
- Estrutura preparada para filtros, ordenações e melhorias futuras

---

## 📁 Estrutura de Arquivos Estáticos

```
core/static/
├── css/
│   ├── style.css              # Base geral (dashboard)
│   ├── account.css            # Estilo para listagem de contas
│   ├── user.css               # Estilo para listagem de usuários
│   ├── user-register.css      # Estilo para cadastro de usuários
│   ├── plant.css              # Estilo para listagem de plantas
│   ├── plant-register.css     # Estilo para cadastro de plantas
│   ├── planted.css            # Estilo para árvores plantadas
├── js/
│   ├── dashboard.js
│   ├── account-list.js
│   ├── user-list.js
│   ├── user-register.js
│   ├── plant-list.js
│   ├── plant-register.js
│   ├── planted-list.js
└── img/
    └── tree-logo.png          # Logo simples do projeto
```

---

## 📌 Observações Técnicas
- Templates utilizam herança via `base.html`
- Estilo visual consistente (tema verde/natureza)
- Dashboard e páginas são responsivos (flexbox e media queries)
- Uso de `related_name` para evitar conflitos de FK
- Cuidados com `Profile.DoesNotExist` e `ValueError` resolvidos

## 🙌 Autor
Teste técnico realizado por **Raphael Laurintino**