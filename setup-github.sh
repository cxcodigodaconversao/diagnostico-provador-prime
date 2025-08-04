#!/bin/bash

# Script para configurar repositório GitHub
# Execute: bash setup-github.sh

echo "🚀 Configurando Repositório GitHub para Provador Prime Diagnóstico"
echo "=============================================================="

# Verificar se git está instalado
if ! command -v git &> /dev/null; then
    echo "❌ Git não está instalado. Instale primeiro: https://git-scm.com/"
    exit 1
fi

# Inicializar repositório
echo "📁 Inicializando repositório..."
git init

# Configurar gitignore se não existir
if [ ! -f .gitignore ]; then
    echo "📝 Criando .gitignore..."
    cat > .gitignore << EOL
__pycache__/
*.pyc
.env
.DS_Store
.vscode/
.idea/
node_modules/
.netlify/
EOL
fi

# Adicionar todos os arquivos
echo "📦 Adicionando arquivos..."
git add .

# Commit inicial
echo "💾 Fazendo commit inicial..."
git commit -m "🎯 Diagnóstico Provador Prime - Versão inicial

✨ Funcionalidades:
- Quiz interativo com 33 perguntas
- Roda de resultado com gráfico radar
- Design responsivo (mobile-first)
- CTA integrado para inscrição
- 3 cores: #21082a, #d4af37, #ffffff
- Tipografia: Sorts Mill Goudy + Montserrat

🚀 Deploy:
- Pronto para Netlify
- Configuração automática
- Headers de segurança
- Redirects configurados"

# Configurar branch principal
git branch -M main

# Instruções para conectar ao GitHub
echo ""
echo "✅ Repositório local configurado!"
echo ""
echo "🔗 Próximos passos:"
echo "1. Crie um repositório no GitHub: https://github.com/new"
echo "2. Nome sugerido: provador-prime-diagnostico"
echo "3. Execute os comandos:"
echo ""
echo "   git remote add origin https://github.com/SEU_USUARIO/provador-prime-diagnostico.git"
echo "   git push -u origin main"
echo ""
echo "4. Conecte ao Netlify: https://netlify.com"
echo "   - New site from Git"
echo "   - Selecione seu repositório"
echo "   - Deploy automático!"
echo ""
echo "📱 Teste o link após deploy:"
echo "   https://seu-site.netlify.app"
echo ""
echo "🎯 CTA configurado para:"
echo "   https://sun.eduzz.com/60EEK1P803"
echo ""
echo "=============================================================="
echo "🚀 Pronto para o GitHub + Netlify!"
