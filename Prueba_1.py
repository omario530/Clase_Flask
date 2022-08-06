from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/acerca")
def acerca():
    return render_template('acerca_de.html')

@app.route("/seleccion")
def selecc():  # https://codepen.io/matuzo/pen/KOdpmq
    return """<h1>Folder upload</h1>

    <label for="folder">Select folder</label>
    <input type="file" id="folder" webkitdirectory multiple/>

    <h2>Selected Files</h2>
    <td>
    <ul id="listing"></ul>
    </td>"""


@app.route("/seleccion_1")
def selecc_1():  #https://developer.mozilla.org/es/docs/Web/API/File/webkitRelativePath
    return render_template('seleccion_1.html')
    return r

if __name__ == '__main__':
    app.run(debug=True)


