import json


def load_candidates_from_json():
    """
    Возвращает список всех кандидатов
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)
#print(load_candidates_from_json())

def get_all():
    return load_candidates_from_json()

def get_candidate(candidate_id):
    """
    возвращает одного кандидата по его id
    """
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate

#print(get_candidate(5))


def get_candidates_by_name(candidate_name):
    """
    Возвращает кандидатов по имени
    """
    candidates = []
    for candidate in load_candidates_from_json():
        if candidate_name.lower() in candidate['name'].lower().split():
            candidates.append(candidate)
    return candidates
#print(get_candidates_by_name('Sheri'))

def get_candidates_by_skill(skill_name):
    """
    Возвращает кандидатов по навыку
    """
    candidates_to_get = []
    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates_to_get.append(candidate)
    return candidates_to_get
#print(get_candidates_by_skill('python'))