# 📚 Instruções para Deploy no GitHub

## ⚠️ Pré-requisito: Instalar Git

Se você ainda não tem Git instalado, baixe em: https://git-scm.com/download/win

Após instalar, reinicie o PowerShell.

## 🚀 Passos para Deploy

### 1️⃣ Abra PowerShell/Git Bash na pasta do projeto

```powershell
cd C:\Users\joaof\Desktop\NEKOPLAY
```

### 2️⃣ Inicialize o repositório Git

```powershell
git init
```

### 3️⃣ Configure seu Git (primeira vez)

```powershell
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
```

### 4️⃣ Adicione todos os arquivos

```powershell
git add .
```

### 5️⃣ Faça o commit inicial

```powershell
git commit -m "Initial commit: NekoPlay Dashboard"
```

### 6️⃣ Adicione o remote do seu repositório

Se já tem repositório no GitHub:
```powershell
git remote add origin https://github.com/seu-usuario/jfar.git
```

### 7️⃣ Faça o push para main/master

```powershell
git branch -M main
git push -u origin main
```

## ✅ Pronto!

Seu repositório foi atualizado com sucesso em:
`https://github.com/seu-usuario/jfar`

---

### 📝 Atualizações Futuras

Para fazer atualizações:

```powershell
git add .
git commit -m "Descrição da mudança"
git push
```

### 🔑 Autenticação via Token (se needed)

Se pedir autenticação:
1. Gere um token em: https://github.com/settings/tokens
2. Use o token como senha no terminal

---

Qualquer dúvida, consulte a documentação: https://docs.github.com/pt/github
