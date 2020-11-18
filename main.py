from flask import Flask, request, jsonify
app = Flask(__name__)
import psycopg2


connection = psycopg2.connect(
    database="scrapedigging",
    user="****",
    password="****",
    host="localhost"
)

cursor = connection.cursor()

cursor.execute("create table if not exists users (id serial PRIMARY KEY, username varchar);")
connection.commit()


@app.route("/login", methods=["GET"])
def user_login():
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    users = cursor.fetchall()
    return jsonify(users)

@app.route("/sign-up", methods=["POST"])
def book_create():
    sql = "INSERT INTO users (username) VALUES (%s);"
    cursor.execute(sql, (request.json["username"],))
    connection.commit()

    sql = "SELECT * FROM users ORDER BY ID DESC LIMIT 1"
    cursor.execute(sql)
    user = cursor.fetchone()
    return jsonify(user)

@app.route("/user/<int:id>", methods=["GET"])
def user_profile(id):
    return "working"


@app.route("/user/<int:id>", methods=["PUT", "PATCH"])
def user_update(id):
    sql = "UPDATE users SET title = %s WHERE id = %s;"
    cursor.execute(sql, (request.json["title"], id))
    connection.commit()

    sql = "SELECT * FROM users WHERE id = %s"
    cursor.execute(sql, (id,))
    user = cursor.fetchone()
    return jsonify(user)

@app.route("/user/<int:id>", methods=["DELETE"])
def book_delete(id):
    sql = "SELECT * FROM users WHERE id = %s;"
    cursor.execute(sql, (id,))
    user = cursor.fetchone()

    if user:
        sql = "DELETE FROM users WHERE id = %s;"
        cursor.execute(sql, (id,))
        connection.commit()

    return jsonify(book)