from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
            <link rel="stylesheet" href="styles.css">
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: #f4f4f4;
                }

                .container {
                    max-width: 800px;
                    margin: auto;
                    background-color: white;
                    padding: 20px;
                    border-radius: 5px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }

                h1, h2 {
                    color: #333;
                }

                h1 {
                    border-bottom: 2px solid #4c58af;
                    padding-bottom: 10px;
                }

                h2 {
                    margin-top: 20px;
                }

                p {
                    margin: 5px 0;
                }

                ul {
                    list-style-type: none;
                    padding: 0;
                }

                ul li {
                    margin-bottom: 5px;
                }

                .contact-info {
                    margin-bottom: 20px;
                }
            </style>
        </head>
        <body>

        <div class="container">
            <h1>Matsu Shimote</h1>
            <div class="contact-info">
                <p>Email: seuemail@exemplo.com</p>
                <p>Telefone: (99) 99999-9999</p>
                <p>Endereço: Rua Exemplo, 123 - Cidade, Estado</p>
            </div>

            <h2>Resumo Profissional</h2>
            <p>Graduado em relações internacionais, fluente em inglês, espanhol e francês. Possuo 5 anos de experiência, amplo conhecimento em vendas e negociações internacionais. Agora, desejo reforçar o departamento de relações internacionais da empresa X e alcançar novas conquistas. </p>
            <h2>Experiência Profissional</h2>
            <ul>
                <li><strong>Cargo - Empresa</strong> (MM/AAAA - Presente)
                    <p>Responsável por [responsabilidades e conquistas].</p>
                </li>
                <li><strong>Cargo - Empresa</strong> (MM/AAAA - MM/AAAA)
                    <p>Responsável por [responsabilidades e conquistas].</p>
                </li>
            </ul>

            <h2>Educação</h2>
            <ul>
                <li><strong>Ciencia da Computação - FIB</strong> (MM/AAAA - MM/AAAA)
                    <p>Descrição ou conquistas relevantes.</p>
                </li>
                <li><strong>Curso - Instituição</strong> (MM/AAAA - MM/AAAA)
                    <p>Descrição ou conquistas relevantes.</p>
                </li>
            </ul>

            <h2>Habilidades</h2>
            <ul>
                <li>Habilidade 1</li>
                <li>Habilidade 2</li>
                <li>Habilidade 3</li>
                <li>Habilidade 4</li>
            </ul>

            <h2>Idiomas</h2>
            <ul>
                <li>Inglês - Intermediário</li>
                <li>Idioma 2 - Nível</li>
            </ul>
        </div>

        </body>
        </html>


    """

if __name__ == '__main__':
    app.run(debug=True)
