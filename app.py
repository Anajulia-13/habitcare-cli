from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>HabitCare CLI</h1>
    <p>Projeto desenvolvido para o Bootcamp.</p>
    <p>Banco de Dados: Supabase</p>
    <p>CI/CD: GitHub Actions</p>
    <p>Versão: 3.0.0</p>
    <p>Aplicação CLI publicada para fins acadêmicos.</p>
    """

if __name__ == "__main__":
    app.run()