import os
import time
from flask import Flask, render_template, send_from_directory, request

import entity

app = Flask(__name__)

UPLOAD_FOLDER = 'pdf'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = {'pdf'}

UPLOAD_HTML = 'upload.html'
OUTPUT_PATH = 'output'
output_dir = os.path.join(basedir, OUTPUT_PATH)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if not os.path.exists('tmp'):
    os.makedirs('tmp')

file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
if not os.path.exists(file_dir):
    os.makedirs(file_dir)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def upload_test():
    message = ''
    return render_template(UPLOAD_HTML, message=message)


@app.route('/api/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    f = request.files['myfile']
    if f:
        old_name = f.filename
        ext = old_name.rsplit('.', 1)[1]
        unix_time = int(time.time())
        new_filename = old_name + str(unix_time) + '.' + ext
        print(new_filename)
        path = os.path.join(file_dir, new_filename)
        f.save(path)
    else:
        message = '你没上传文件哦'
        return render_template(UPLOAD_HTML, message=message)
    if f and allowed_file(f.filename):
        pdf = entity.Pdf(file_dir, new_filename, OUTPUT_PATH)
        return downloader(pdf.get_output_filename())
    else:
        message = '文件类型不支持哦 重新上传试试呢'
        return render_template(UPLOAD_HTML, message=message)


@app.route("/download/<path:filename>")
def downloader(filename):
    dir_path = os.path.join(app.root_path, 'output')
    return send_from_directory(dir_path, filename, as_attachment=True)


if __name__ == '__main__':
    print('启动目录：' + basedir)
    app.run(host='0.0.0.0', port=10088)
