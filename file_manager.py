base_dir='./files/'

def readfile(filename):
    try:
        with open(base_dir+filename,'r',encoding='utf8') as file:
            content=file.read()
            return content
    except FileNotFoundError:
        print('文件未找到。')

def write_json(filename,data):
    with open(base_dir+filename,'w',encoding='utf8') as file:
        import json
        json.dump(data,file)

def read_json(filename,default_data):
    try:
        with open(base_dir + filename, 'r', encoding='utf8') as file:
           import json
           return json.load(file)
    except FileNotFoundError:
        print('文件未找到。')
        return default_data