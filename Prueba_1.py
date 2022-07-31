from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """<H1>
    página de inicio
    </H1>"""

@app.route("/acerca")
def acerca():
    return """<H2>
    acerca de 
    </H2>"""

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
    return """
    <h1><code>&lt;input webkitdirectory&gt;</code> demo</h1>

    <p>The <code>webkitdirectory</code> attribute allows the user to pick a directory via a file input. All files (including nested files) inside that directory are added to the input’s <code>files</code> list. This attribute is supported in Chrome, Edge, and Firefox.</p>
    
    <p>Pick a directory, and all files in that directory will be listed below, represented by their relative path.</p>
    
    <input type="file" id="picker" name="fileList" webkitdirectory multiple>
    
    <ul id="listing"></ul>
"""

if __name__ == '__main__':
    app.run(debug=True)


