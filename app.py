from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # 获取表单数据
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    like_ai = request.form.get('like_ai')
    suggest = request.form.get('suggest', '')
    
    # 保存到data.json
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        data = []
    
    data.append({
        'name': name,
        'age': age,
        'gender': gender,
        'like_ai': like_ai,
        'suggest': suggest
    })
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 跳回首页并带上成功标记
    return redirect(url_for('index') + '?success=1')

@app.route('/data')
def data():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        data = []
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)