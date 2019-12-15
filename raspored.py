from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    f=open("RAFraspored.csv",encoding="utf-8")
    redovi = f.readlines()
    sviProfesori = [red.split(',')[2] for red in redovi]
    jedinstveniProfesori = []
    for profesor in sviProfesori:
        if profesor not in jedinstveniProfesori:
            jedinstveniProfesori.append(profesor)
    jedinstveniProfesori.sort()

    sveUcionice = [red.split(',')[6].strip() for red in redovi]
    jedinstveneUcionice = []
    for ucionica in sveUcionice:
        if ucionica not in jedinstveneUcionice:
            jedinstveneUcionice.append(ucionica)
    jedinstveneUcionice.sort()
    
    return render_template('index.html', redovi = redovi, jedinstveniProfesori = jedinstveniProfesori, jedinstveneUcionice = jedinstveneUcionice)

if __name__ == "__main__":
    app.run(debug=True)