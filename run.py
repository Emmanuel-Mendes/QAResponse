"""
Ponto de entrada principal para a execução do servidor Flask.
"""

from app.app import create_app

# Instancia a aplicação usando a factory definida no seu app.py
app = create_app()

if __name__ == "__main__":
    ip = "0.0.0.0"
    app.run(host=ip, port=5000, debug=True)
