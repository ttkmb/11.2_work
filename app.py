from flask import Flask, render_template

from utils import get_all, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = get_all()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:id>/')
def get_candidate_by_id(id):
    candidate = get_candidate(id)
    return render_template('card.html', candidate=candidate)


@app.route('/search/<name>/')
def get_candidate_by_name(name):
    candidate = get_candidates_by_name(name)
    return render_template('search.html', candidates=candidate, k=len(candidate))


@app.route('/skill/<skill_name>/')
def skill_candidates(skill_name):
    candidate = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidate, k=len(candidate), skill_name=skill_name)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
