from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from facerec.face import ver

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images' 
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect('/')
    
    images = request.files.getlist('image')
    image_list = []

    for image in images:
        filename = image.filename
        image.save('./static/images/' + filename)
        image_list.append('./static/images/' + filename)

    result_array = ver(image_list) 
    
    return render_template('index.html', result=list(result_array[0]),result_nv=list(result_array[1]), image_list=image_list)


if __name__ == '__main__':
    app.run(debug=True)

app.config['UPLOAD_FOLDER'] = 'static/images'