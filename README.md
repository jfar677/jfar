# NekoPlay - Dashboard de Animes

Dashboard web completo para gerenciar sua lista de animes com recursos de adição, edição, exclusão e filtros avançados.

## 🎯 Funcionalidades

✅ **Filtros Rápidos**: 3 botões fixos (Assistido, Assistindo, Planejando) com contadores  
✅ **Filtro Detalhado**: Tela separada com busca avançada por nome, tipo, status e data  
✅ **Adicionar Anime**: Formulário completo com tipo, status e notas  
✅ **Editar/Deletar**: Gerenciamento completo dos animes  
✅ **Design Moderno**: Interface web responsiva e intuitiva  
✅ **Dados Persistentes**: Armazenamento em JSON  

## 🛠️ Tecnologias

- **Backend**: Python 3.13 + Flask 2.3.2
- **Frontend**: HTML5 + CSS3 (Responsive Design)
- **Banco de Dados**: JSON

## 📋 Requisitos

- Python 3.7 ou superior
- Flask 2.3.2
- Werkzeug 2.3.6

## ⚙️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/jfar.git
cd jfar
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

1. Execute a aplicação:
```bash
python pagina_principa.py
```

2. Abra o navegador e acesse:
```
http://localhost:5000
```

3. Comece a gerenciar seus animes!

## 📁 Estrutura do Projeto

```
jfar/
├── pagina_principa.py          # App Flask (backend)
├── requirements.txt             # Dependências
├── .gitignore                   # Arquivos ignorados
├── README.md                    # Este arquivo
│
├── templates/                   # Arquivos HTML
│   ├── dashboard.html           # Página principal
│   ├── adicionar.html           # Formulário de adição/edição
│   └── filtro_detalhado.html    # Página de filtros avançados
│
└── static/                      # Arquivos estáticos
    └── style.css                # Estilos CSS
```

## 🎨 Interface

### Dashboard Principal
- Visualização em cards dos animes
- Barra fixa com filtros de status (Assistido, Assistindo, Planejando)
- Contador dinâmico de animes por status
- Botões para adicionar e acessar filtro detalhado

### Tela de Adição/Edição
- Campos: Nome*, Tipo*, Status*, Notas
- Validação de campos obrigatórios
- Data de adição/edição automática

### Filtro Detalhado
- Busca por nome do anime
- Filtro por tipo
- Filtro por status
- Filtro por data (AAAA-MM-DD)
- Resultados em tempo real

## 💾 Dados

Os animes são armazenados em `animes.json` com estrutura:

```json
[
  {
    "id": "1",
    "nome": "Naruto",
    "tipo": "Shonen",
    "status": "Assistido",
    "notas": "Excelente anime",
    "data": "2026-05-26 16:11"
  }
]
```

## 🐛 Troubleshooting

**Flask não encontrado:**
```bash
pip install Flask==2.3.2 Werkzeug==2.3.6
```

**Porta 5000 em uso:**
Edite `pagina_principa.py`:
```python
app.run(debug=True, port=5001)  # Use outra porta
```

## 📝 Licença

MIT License - Veja LICENSE para detalhes

---

**Desenvolvido com ❤️ para gerenciar animes**
