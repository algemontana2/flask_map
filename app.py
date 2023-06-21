from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import main  # import your mapping code

# Create 'uploads' directory if it doesn't exist
if not os.path.exists('uploads'):
    os.makedirs('uploads')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # create a folder named 'uploads' in your project directory

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'gedcom_file' not in request.files:
        return 'No file part'
    file = request.files['gedcom_file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # call your main function here with the path to the saved file
        main.main(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded and processed successfully'
        
if __name__ == '__main__':
    app.run(debug=True)
