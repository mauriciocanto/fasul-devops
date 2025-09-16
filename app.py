from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    conn = psycopg2.connect(
        dbname="meubanco",
        user="postgres",
        password="123456",
        host="db"  # Nome do serviço no docker-compose
    )
    return "Conectado ao PostgreSQL com Docker Compose!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
