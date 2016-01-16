from flask import Flask, render_template, redirect
from subprocess import call
app = Flask(__name__)
app.debug = True

pin = 0
transmitter = 1235262

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/on/<int:id>")
def on(id=0):
    send_signal(True, id-1)
    return redirect("/")
    #return render_template('index..html', on=state)

@app.route("/off/<int:id>")
def off(id=0):
    send_signal(False, id-1)
    return redirect("/")
    #return render_template('index..html', on=state)

def send_signal(state, id):
    on_off = ""
    if state:
        on_off = "on"
    else:
        on_off = "off"
    cmd = "piHomeEasy {} {} {} {}".format(pin, transmitter, id, on_off)
    print cmd
    call(cmd, shell=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
