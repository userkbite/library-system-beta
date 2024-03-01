from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

emprestimos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome_aluno = request.form.get("nome_aluno")
        nome_livro = request.form.get("nome_livro")
        curso_aluno = request.form.get("curso_aluno")
        data_emprestimo = request.form.get("data_emprestimo")
        data_devolucao = request.form.get("data_devolucao")

        data_emprestimo_python = datetime.strptime(data_emprestimo, '%Y-%m-%d')
        data_devolucao_python = datetime.strptime(data_devolucao, '%Y-%m-%d')

        data_emprestimo_br = data_emprestimo_python.strftime('%d/%m/%Y')
        data_devolucao_br = data_devolucao_python.strftime('%d/%m/%Y')

        emprestimo = {
            "nome_aluno": nome_aluno,
            "nome_livro": nome_livro,
            "curso_aluno": curso_aluno,
            "data_emprestimo": data_emprestimo_br,
            "data_devolucao": data_devolucao_br,
        }
        
        emprestimos.append(emprestimo)

        print(emprestimos)

        return redirect(url_for("index"))
    
    return render_template("index.html", emprestimos=emprestimos)

if __name__ == "__main__":
    app.run(debug=True)