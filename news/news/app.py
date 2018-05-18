from flask import Flask, render_template
import os,os.path
import json
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

path_root = '/home/shiyanlou/files'
file_name = os.listdir(path_root)
file_world_name = file_name.pop()
file_shiyanlou_name = file_name.pop()

# config is a dict, so you can use 'update' method
app.config.update(dict(
    path = path_root,
    file_shiyanlou_path = os.path.join(path_root,file_shiyanlou_name),
    file_world_path = os.path.join(path_root,file_world_name)
))

@app.route('/')
def index():
    """ route method parameters only can pass through from rout
    """
    with open(app.config['file_world_path'], 'r') as file_world_path:
        world_content = file_world_path.read()
    file_world = json.loads(world_content)
    with open(app.config['file_shiyanlou_path'], 'r') as file_shiyanlou_path:
        shiyanlou_content = file_shiyanlou_path.read()
    file_shiyanlou = json.loads(shiyanlou_content) 
    return render_template('index.html',title_world=file_world["title"],title_shiyanlou=file_shiyanlou["title"])


@app.route('/files/<filename>')
def file(filename):
    # like this
    file_name_path = os.path.join(app.config['path'],filename) + '.json'
    if os.path.exists(file_name_path):
        with open(file_name_path,'r') as file_name_path:
            file_content_json = file_name_path.read()
        file_name_content = json.loads(file_content_json)
        return render_template('file.html',file_name_content=file_name_content)
    else:
        return render_template('404.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

 

if __name__ == '__main__':
    app.run()
