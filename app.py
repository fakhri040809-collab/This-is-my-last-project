from flask import Flask, render_template, request, flash, jsonify, redirect, url_for
import json
from pathlib import Path

app = Flask(
    __name__,
    template_folder='Templates',
    static_folder='Static'
)

# =====================================
# STUDENT TRACKER DATA
# =====================================

DATA_FILE = Path(__file__).with_name('data_siswa.json')
def load_data():
    try:
        with DATA_FILE.open('r', encoding='utf-8') as file:
            data = json.load(data)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
            return [
            {"nama": "Devon", "nilai": 90},
            {"nama": "Farrel", "nilai": 84},
        ]

# =====================================
# SAVE DATA
# =====================================

def save_data(data):
    with DATA_FILE.open('w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

# =====================================
# PROJECT LIST
# =====================================

project_list = [
    {
        "title": "Academic Student Tracker",
        "description": "Aplikasi pencatat nilai siswa, kelulusan, dan rata-rata nilai.",
        "url": "/student-tracker",
    },
    {
        "title": "Finance Tracker",
        "description": "Aplikasi pencatat saldo, pendapatan, dan pengeluaran.",
        "url": "/finance",
    },
    {
        "title": "To do App",
        "description": "Aplikasi untuk mencatat dan mengelola aktivitas sehari-hari.",
        "url": "/todo",
    },
]

# =====================================
# HOME
# =====================================

@app.route('/')
def index():
    return render_template('index.html')

# =====================================
# ABOUT
# =====================================

@app.route('/about')
def about():
    return render_template('about.html')


# =====================================
# PROJECT
# =====================================

@app.route('/project')
def project():
    return render_template('project.html')

# =====================================
# API PROJECTS
# =====================================

@app.route('/api/projects')
def api_projects():
    return jsonify(project_list)

# =====================================
# SEARCH
# =====================================

@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    results = [project for project in project_list if query.casefold() in project['title'].casefold()]
    return render_template('search.html', query=query, results=results)


# =====================================
# CONTACT
# =====================================

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        print("Nama:", name)
        print("Email:", email)
        print("Pesan:", message)

        flash("Pesan berhasil dikirim!")

        return redirect(url_for("contact"))

    return render_template("contact.html")


# ==============================
# EDUHUB CREATIVE SUITE
# ==============================

@app.route('/eduhub')
def eduhub():
    return render_template('eduhub_creative_suite_pelajar.html')


# =====================================
# EDULAB INTERACTIVE SIMULATION SUITE
# =====================================

@app.route('/edulab')
def edulab():
    return render_template('edulab_interactive_simulation_suite.html')


# =====================================
# TASKSCHOOL DASHBOARD
# =====================================

@app.route('/taskschool_dashboard')
@app.route('/taskschool-dashboard')
def taskschool_dashboard():
    return render_template('taskschool_dashboard.html')


# =====================================
# BACKWARD-COMPATIBLE ENDPOINTS
# =====================================

# Endpoint dashboard lama
app.add_url_rule(
    '/taskschool_dashboard',
    endpoint='dashboard',
    view_func=taskschool_dashboard
)

# Mengakomodasi salah ketik endpoint yang muncul
# pada error BuildError sebelumnya.
app.add_url_rule(
    '/taskschool_dashboard',
    endpoint='taskschool_dashbaasrd',
    view_func=taskschool_dashboard
)


# Route lama /todo tetap dapat digunakan
@app.route('/todo')
def todo():
    return redirect(url_for('taskschool_dashboard'))


# Skills route
@app.route('/skills')
def skills():
    skills_list = [
        {"nama": "Python", "level": "Intermediate", "percentase": 80},
        {"nama": "JavaScript", "level": "Beginner", "percentase": 60},
        {"nama": "HTML/CSS", "level": "Advanced", "percentase": 90},
        {"nama": "Flask", "level": "Intermediate", "percentase": 75},
        {"nama": "React", "level": "Beginner", "percentase": 50},
        {"nama": "SQL", "level": "Intermediate", "percentase": 70},
        {"nama": "Git", "level": "Intermediate", "percentase": 65},
        {"nama": "Django", "level": "Beginner", "percentase": 55}
    ]
    return render_template('skills.html', skills=skills_list)


# Experience route
@app.route('/experience')
def experience():
    experience_list = [
        {"perusahaan": "TechCorp", "posisi": "Software Engineer", "durasi": "2 tahun"},
        {"perusahaan": "WebSolutions", "posisi": "Frontend Developer", "durasi": "1 tahun"},
        {"perusahaan": "InnovateX", "posisi": "UI/UX Designer", "durasi": "1.5 tahun"}
    ]
    return render_template('experience.html', experiences=experience_list)


# =====================================
# RUN APPLICATION
# =====================================

if __name__ == '__main__':
    app.run(debug=True)
