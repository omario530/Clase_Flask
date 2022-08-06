from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/acerca")
def acerca():
    return render_template('acerca_de.html')

@app.route("/num_pag")
def selecc():  # https://codepen.io/matuzo/pen/KOdpmq
    return """
<body>
    <div class="container">
        <h1 class="text-center">Count Pages inside PDF Document</h1>
    <div class="form-group container">
        <input type="file" accept=".pdf" required id="files" class="form-control">
    </div>
    <br><br>
    <h1 class="text-primary container" id="result"></h1>
    </div>
</body>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.12.313/pdf.min.js"></script>
        <script>
        
        let inputElement = document.getElementById('files')
        
           inputElement.onchange = function(event) {
        
            var file = event.target.files[0];
        
            //Step 2: Read the file using file reader
            var fileReader = new FileReader();  
        
            fileReader.onload = function() {
        
                //Step 4:turn array buffer into typed array
                var typedarray = new Uint8Array(this.result);
        
                //Step 5:pdfjs should be able to read this
                const loadingTask = pdfjsLib.getDocument(typedarray);
                loadingTask.promise.then(pdf => {
        
                    document.getElementById('result').innerHTML = "The number of Pages inside " + file.name + " is " + pdf.numPages
                    // The document is loaded here...
                });
                            
        
            };
            //Step 3:Read the file as ArrayBuffer
            fileReader.readAsArrayBuffer(file);
         
         }
        </script>
        <ul id="result"></ul>
"""


@app.route("/seleccion_1")
def selecc_1():  #https://developer.mozilla.org/es/docs/Web/API/File/webkitRelativePath
    return render_template('seleccion_1.html')
    return r

if __name__ == '__main__':
    app.run(debug=True)


