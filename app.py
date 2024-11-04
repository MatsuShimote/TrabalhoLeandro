from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Flask App</title>
        </head>
        <body>
            <h1>Welcome to My Flask App!</h1>
            <p>This is a simple web application created using Flask.</p>
            <p>Explore the features of Flask and build your own web apps!</p>
            <ul>
                <li>Easy to learn and use</li>
                <li>Lightweight and flexible</li>
                <li>Perfect for small to medium-sized projects</li>
            </ul>
            <footer>
                <p>Developed by Matsu</p>
            </footer>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
