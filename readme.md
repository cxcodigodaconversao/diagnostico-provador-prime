# 🎯 Diagnóstico Provador Prime

Uma aplicação web interativa para avaliar o nível atual de competências no provador e identificar oportunidades de melhoria através da formação **Provador Prime**.

## ✨ Funcionalidades

- ✅ **Quiz Interativo** - 20 perguntas personalizadas otimizadas
- ✅ **Navegação Fluida** - Uma pergunta por vez com transições suaves
- ✅ **Roda de Resultado** - Gráfico radar mostrando gaps de competência
- ✅ **Análise Detalhada** - Pontuação individual por área
- ✅ **Design Mobile-First** - Otimizado especialmente para mobile
- ✅ **CTA Integrado** - Direcionamento para página de vendas Eduzz

## 🎨 Design

### Paleta de Cores
- **#21082a** - Roxo escuro (principal)
- **#d4af37** - Dourado (destaques)
- **#ffffff** - Branco (contraste)

### Tipografia
- **Sorts Mill Goudy** - Títulos
- **Montserrat Bold** - Textos em destaque
- **Montserrat Regular** - Textos padrão

## 🚀 Como Usar

### Deploy no Netlify (Recomendado)

1. **Faça fork ou clone do repositório:**
   ```bash
   git clone [URL_DO_REPOSITORIO]
   cd provador-prime-diagnostico
   ```

2. **Conecte ao Netlify:**
   - Acesse [netlify.com](https://netlify.com)
   - Clique em "New site from Git"
   - Conecte seu repositório GitHub
   - Configure:
     - **Build command:** `echo 'Build complete'`
     - **Publish directory:** `.`

3. **Deploy automático:**
   - O Netlify fará deploy automaticamente
   - Cada push para main/master atualiza o site

### Deploy Manual no Netlify

1. **Baixe os arquivos do projeto**
2. **Comprima em ZIP:**
   - Selecione todos os arquivos
   - Crie um arquivo ZIP
3. **Upload no Netlify:**
   - Acesse netlify.com
   - Arraste o ZIP para a área de deploy
   - Site estará online em poucos segundos

## 📊 Temas Avaliados

1. **Rotina e Constância no Provador**
2. **Descoberta do Próprio Estilo** 
3. **Conhecimento de Produto**
4. **Roteiro Estratégico**
5. **Provador na Prática**
6. **Criatividade no Dia a Dia**
7. **Estratégias de Vendas**
8. **Curso de Tecidos (Bônus)**
9. **Comunicação Autêntica**
10. **Presença e Desbloqueio**

## 🔧 Estrutura do Projeto

```
/
├── index.html          # Aplicação principal
├── netlify.toml        # Configurações do Netlify
├── README.md           # Documentação
└── assets/             # Recursos (se houver)
```

## 📱 Funcionalidades Técnicas

- **Progressive Web App** ready
- **Chart.js** para gráficos radar
- **LocalStorage** para salvar progresso
- **Animações CSS** suaves
- **Validação** em tempo real
- **SEO otimizado**

## 🎯 Fluxo do Usuário

1. **Início** - Apresentação do diagnóstico
2. **Quiz** - 20 perguntas otimizadas (uma por vez)
3. **Progresso** - Barra de progresso visual
4. **Resultados** - Pontuação e gráfico radar
5. **CTA** - Direcionamento para página de vendas

## 🌟 Personalização

### Alterar Perguntas
Edite o array `topics` no JavaScript dentro do `index.html`:

```javascript
const topics = [
    {
        name: 'tema',
        label: 'Nome do Tema',
        color: '#d4af37', // ou '#21082a'
        questions: [
            {
                text: 'Sua pergunta aqui?',
                labels: ['Resposta mínima', 'Resposta máxima']
            }
        ]
    }
];
```

### Alterar Link CTA
Modifique o href do botão final:
```html
<a href="https://sun.eduzz.com/60EEK1P803" class="btn-cta">Garantir Minha Vaga</a>
```

### Personalizar Cores
Altere as variáveis CSS no `<style>`:
```css
/* Cor principal */
#21082a

/* Cor dourada */
#d4af37

/* Branco */
#ffffff
```

## 📈 Analytics e Tracking

Para adicionar Google Analytics, insira antes do `</head>`:

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

## 🔒 Segurança

- Headers de segurança configurados no `netlify.toml`
- Proteção XSS
- Content Security Policy
- HTTPS automático pelo Netlify

## 📞 Suporte

Para dúvidas ou suporte técnico:
- Abra uma issue no GitHub
- Documentação do Netlify: [docs.netlify.com](https://docs.netlify.com)

## 📄 Licença

Este projeto é propriedade do **Provador Prime** e destinado exclusivamente para uso na formação presencial.

---

**Desenvolvido com ❤️ para transformar lojistas em referências de provador**
