# 🚀 Guia Rápido de Deploy

## 📋 Checklist Pré-Deploy

- [ ] Todos os arquivos estão no repositório
- [ ] Link do CTA está correto: `https://sun.eduzz.com/60EEK1P803`
- [ ] Cores estão corretas: `#21082a`, `#d4af37`, `#ffffff`
- [ ] 33 perguntas estão configuradas
- [ ] Responsividade testada

## 🌐 Deploy no Netlify (RECOMENDADO)

### Método 1: GitHub + Netlify (Automático)

1. **Subir para GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Primeira versão do Diagnóstico Provador Prime"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/provador-prime-diagnostico.git
   git push -u origin main
   ```

2. **Conectar no Netlify:**
   - Acesse [netlify.com](https://netlify.com)
   - Login com GitHub
   - "New site from Git" → GitHub
   - Selecione o repositório
   - Deploy settings:
     - **Branch:** `main`
     - **Build command:** `echo 'Build complete'`
     - **Publish directory:** `.`
   - Deploy!

3. **Configurar domínio personalizado (opcional):**
   - Site settings → Domain management
   - Add custom domain

### Método 2: Drag & Drop (Manual)

1. **Preparar arquivos:**
   - Baixe todos os arquivos
   - Comprima em ZIP (exceto .git, README.md)

2. **Upload no Netlify:**
   - Acesse [netlify.com](https://netlify.com)
   - Arraste o ZIP para a área de deploy
   - Aguarde processamento
   - Site estará online!

## ⚡ Deploy no Vercel (Alternativa)

```bash
# Instalar Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

## 🐍 Deploy no Heroku (com Flask)

1. **Preparar Heroku:**
   ```bash
   heroku create provador-prime-diagnostico
   ```

2. **Deploy:**
   ```bash
   git push heroku main
   ```

3. **Configurar:**
   ```bash
   heroku config:set FLASK_ENV=production
   ```

## 🔧 URLs de Teste

Após deploy, teste estas URLs:

- `/` - Página principal
- `/diagnostico` - Redirect para principal
- `/quiz` - Redirect para principal
- `/health` - Health check (apenas Flask)

## 📊 Analytics (Opcional)

Para adicionar Google Analytics, edite `index.html` e adicione antes de `</head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 🚨 Troubleshooting

### Problema: Site não carrega
- ✅ Verificar se `index.html` está na raiz
- ✅ Conferir `netlify.toml` configurações

### Problema: Gráfico não aparece
- ✅ Verificar se Chart.js está carregando
- ✅ Testar em navegador diferente

### Problema: Link CTA não funciona
- ✅ Conferir URL: `https://sun.eduzz.com/60EEK1P803`
- ✅ Testar link diretamente

## 📱 Teste Mobile

Teste estes pontos no mobile:
- [ ] Botões de 0-10 são tocáveis
- [ ] Navegação funciona
- [ ] Gráfico é visível
- [ ] CTA final funciona

## ✅ Pós-Deploy

1. **Teste completo:**
   - Responda todo o quiz
   - Verifique roda de resultado
   - Clique no CTA final

2. **Compartilhe:**
   - Pegue URL final do Netlify
   - Teste em dispositivos diferentes
   - Compartilhe com equipe

3. **Monitore:**
   - Netlify Analytics (gratuito)
   - Google Analytics (se configurado)

---

**🎉 Parabéns! Seu Diagnóstico Provador Prime está online!**
