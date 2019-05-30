# 作者：wjq   
# 创建时间: 2019/5/15  
# 文件: web.py   
# 软件名称: PyCharm
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')





if __name__ == "__main__":
    app.run()