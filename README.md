# PsyControl 🧠

Sistema web para gerenciamento psicológico — pacientes e sessões.

## 🛠️ Tecnologias
- Python + Flask
- SQLAlchemy + SQLite
- Bootstrap 5
- Pytest + pytest-cov
- Docker / Docker Compose

---

## 📦 Instalação local

```bash
# 1. Clone o projeto
git clone https://github.com/seu-usuario/psycontrol.git
cd psycontrol

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Instale as dependências
pip install -r requirements.txt
```

---

## ▶️ Rodando o projeto

```bash
python run.py
# Acesse: http://localhost:5000
```

---

## 🐳 Rodando com Docker

```bash
docker-compose up --build
# Acesse: http://localhost:5000
```

---

## 🧪 Executando os testes

```bash
pytest tests/ -v
```

---

## 📊 Gerando relatório de cobertura

```bash
pytest --cov=app tests/ --cov-report=term-missing
# Para HTML:
pytest --cov=app tests/ --cov-report=html
# Abra: htmlcov/index.html
```

---

## 📁 Estrutura do Projeto

```
psycontrol/
├── app/
│   ├── models/
│   │   ├── user.py        # Tabela users
│   │   ├── patient.py     # Tabela patients
│   │   └── session.py     # Tabela sessions
│   ├── routes/
│   │   ├── auth.py        # Login / Cadastro
│   │   ├── dashboard.py   # Dashboard
│   │   ├── patients.py    # CRUD Pacientes
│   │   └── sessions.py    # CRUD Sessões
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── patient_service.py
│   │   └── session_service.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   ├── dashboard/
│   │   ├── patients/
│   │   └── sessions/
│   └── static/css/style.css
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_patients.py
│   └── test_sessions.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── setup.cfg
├── run.py
└── README.md
```

---

## 💾 Exemplos de commits Git

```bash
git init
git add .
git commit -m "feat: estrutura inicial do projeto PsyControl"

git add app/models/
git commit -m "feat: models User, Patient e Session com SQLAlchemy"

git add app/services/
git commit -m "feat: services de autenticação, pacientes e sessões"

git add app/routes/
git commit -m "feat: rotas de auth, dashboard, pacientes e sessões"

git add app/templates/
git commit -m "feat: templates HTML com Bootstrap 5"

git add tests/
git commit -m "test: testes unitários com pytest para auth, pacientes e sessões"

git add Dockerfile docker-compose.yml
git commit -m "chore: adiciona Dockerfile e docker-compose"
```
