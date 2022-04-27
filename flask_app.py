from flask import Flask, render_template

app=Flask(__name__, static_url_path='/static')
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)