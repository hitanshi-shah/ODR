from flask import Flask, render_template
import yaml

app = Flask(__name__)

@app.route('/')
def index():
    with open('vars.yml', 'r') as f:
        data = yaml.safe_load(f)
        hosts = data['hosts']
    return render_template('report.html.j2', hosts=hosts)

if __name__ == '__main__':
    app.run(debug=True)
