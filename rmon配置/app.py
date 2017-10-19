import os
from flask import Flask
import json
def create_app():
    app = Flask('rmon')
    file = os.environ.get('RMON_CONFIG')
    string = ""
    try:
        f1 = open(file,'r')
    except FileNotFoundError:
        print('FileNotFoundError')
        exit()
    for line in f1.readlines():
        if '#' not in line:
            string += line
    f1.close()
    config = json.loads(string)

    for k in config:
        app.config[k.upper()] = config[k]

    # dic_key = []
    # for key in config_file.keys():
    # 	if key.isupper() == 0:
    # 		dic_key.append(key)
    # 	else:
    # 		print(config_file[key])
    # for i in range(len(dic_key)):
    # 	config_file.pop(dic_key[i])
    # app.config.from_object(config_file)

    return app



if __name__ == '__main__':
     create_app()
