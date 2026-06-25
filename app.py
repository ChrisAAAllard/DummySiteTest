"""
Intentionally vulnerable Python for testing CodeQL code scanning.
DO NOT use any of this in real code.
"""
import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def get_user():
    # CWE-89: SQL injection via string concatenation
    user_id = request.args.get("id")
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cur.execute(query)
    return str(cur.fetchall())


@app.route("/ping")
def ping():
    # CWE-78: OS command injection via untrusted input
    host = request.args.get("host")
    return os.popen("ping -c 1 " + host).read()


@app.route("/read")
def read_file():
    # CWE-22: path traversal
    name = request.args.get("name")
    with open("/var/data/" + name) as f:
        return f.read()


if __name__ == "__main__":
    app.run()
