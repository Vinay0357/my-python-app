from flask import Flask, render_template
import os

app  = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

# print("Hello I'm before my_func")
# def my_func():
#   print("My Fun starts here")
#   a = 10
#   b = 20
#   c = a + b
#   print(f"The adding of {a} and {b} is: {c}")
#   print("My Fun ends here")
# print("Hello I'm after my_func")
