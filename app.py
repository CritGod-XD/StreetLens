from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

DISTRESS = [
    {"label": "Alligator crack", "pct": 62, "color": "#3b82f6", "sub": "Avg width 5mm · high density"},
    {"label": "Longitudinal", "pct": 21, "color": "#f97316", "sub": "Total length 8.5m · stable"},
    {"label": "Transverse", "pct": 11, "color": "#eab308", "sub": "4 cracks · 10m avg spacing"},
    {"label": "Pothole", "pct": 6, "color": "#a855f7", "sub": "1 count · 25mm depth"},
]
PILLS = [
    {"label": "Longitudinal", "score": 78},
    {"label": "Alligator", "score": 81},
    {"label": "Transverse", "score": 84},
    {"label": "Pothole", "score": 91},
]

@app.route('/')
def login():
    return render_template('index.html', screen='login')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html', screen='dashboard', distress=DISTRESS, pills=PILLS)

if __name__ == '__main__':
    app.run(debug=True)
