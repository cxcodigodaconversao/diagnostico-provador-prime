#!/usr/bin/env python3
"""
Aplicação Flask para o Diagnóstico Provador Prime
Este arquivo é opcional - o projeto funciona como site estático no Netlify
"""

from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# Carregar o HTML principal
def load_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/')
def index():
    """Página principal do diagnóstico"""
    html_content = load_html()
    return render_template_string(html_content)

@app.route('/diagnostico')
def diagnostico():
    """Rota alternativa para o diagnóstico"""
    return index()

@app.route('/quiz')
def quiz():
    """Rota alternativa para o quiz"""
    return index()

@app.route('/health')
def health_check():
    """Endpoint de health check"""
    return {'status': 'ok', 'app': 'Provador Prime Diagnostico'}, 200

@app.route('/favicon.ico')
def favicon():
    """Favicon placeholder"""
    return '', 204

@app.errorhandler(404)
def not_found(error):
    """Página 404 personalizada"""
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Página não encontrada - Provador Prime</title>
        <style>
            body {
                font-family: 'Montserrat', sans-serif;
                background: linear-gradient(135deg, #21082a 0%, #2a0a35 50%, #1a0620 100%);
                color: #fff;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0;
            }
            .container {
                text-align: center;
                padding: 40px;
            }
            h1 {
                font-size: 3rem;
                color: #d4af37;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 30px;
            }
            .btn {
                background: linear-gradient(45deg, #d4af37, #21082a);
                color: #fff;
                padding: 15px 30px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>404</h1>
            <p>Página não encontrada</p>
            <a href="/" class="btn">Voltar ao Diagnóstico</a>
        </div>
    </body>
    </html>
    """), 404

if __name__ == '__main__':
    # Configurações para desenvolvimento
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
