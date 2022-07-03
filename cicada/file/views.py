import fileinput
import hashlib
import os
from flask import request
from werkzeug.utils import secure_filename
from . import upload_bp


current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
UPLOAD_FOLD = parent_dir
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@upload_bp.route('/article', methods=['POST'])
def upload_article_image():
    if request.method == 'POST':
        # 获取通过前端发送的图片   Content-Type: enctype=multipart/form-data
        file = request.files['file']
        # print('--->', file)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # TODO 保存图片数据
            filename_md5 = hashlib.md5(filename.split('.')[0].encode()).hexdigest()
            # print('--->', filename_md5)
            path = '/static/article_image/'
            if not os.path.exists(parent_dir + path):
                os.makedirs(parent_dir + path)
            file_path = parent_dir + path + filename_md5 + '.' + filename.split('.')[-1]
            # print(file_path)
            file.save(os.path.join(parent_dir+path, filename_md5 + '.' + filename.split('.')[-1]))
            info = 'http://127.0.0.1:5000/static/article_image/' + filename_md5 + '.' + filename.split('.')[-1]
            return {"retCode": '200', "retMsg": "上传成功", "info": info}