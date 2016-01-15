from flask import Flask, render_template, redirect
from subprocess import call
app = Flask(__name__)
app.debug = True
state = False

pin = 0
transmitter = 1235262

@app.route("/")
def main():
    return render_template('index.html', on=state)

@app.route("/on")
def on():
    send_signal(True)
    global state
    state = True
    return redirect("/")
    #return render_template('index..html', on=state)

@app.route("/off")
def off():
    send_signal(False)
    global state
    state = False
    return redirect("/")
    #return render_template('index..html', on=state)

def send_signal(state):
    cmd = ""
    if state:
        cmd = "on"
    else:
        cmd = "off"
    call(["piHomeEasy", str(pin), str(transmitter), str(-1), cmd], shell=True)

if __name__ == '__main__':
    app.run()
