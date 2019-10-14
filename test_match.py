from match import (Company, Student, find_first_available_company, find_first_available_student,
                   mutual_match, unilateral_match)

def test_find_first_available_company():
    ranked_companies = ['A', 'B', 'C']
    company_to_find = Company('C', 1, ['0', '1'])
    available_companies = [company_to_find]
    company = find_first_available_company(ranked_companies, available_companies)
    assert company == company_to_find
    
    
def test_find_first_available_student():
    ranked_students = ['000', '111']
    student_to_find = Student('111', '111', ['B', 'A'])
    available_students = [
        Student('222', '222', ['A', 'B']),
        student_to_find
    ]
    student = find_first_available_student(ranked_students, available_students)
    assert student ==  student_to_find


def test_mutual_match():
    companies = [
        Company('A', 1, ['0', '1']),
        Company('B', 1, ['1', '0'])
    ]
    
    students = [
        Student('0', '0', ['A', 'B']),
        Student('1', '1', ['B', 'A'])
    ]
    
    matches, unmatched_companies, unmatched_students = mutual_match(companies, students)

    assert matches == {'0': 'A', '1': 'B'}
    assert unmatched_companies == []
    assert unmatched_students == []

def test_mutual_match_two_rounds():
    companies = [
        Company('A', 1, ['0', '1']),
        Company('B', 1, ['0', '1'])
    ]
    
    students = [
        Student('0', '0', ['A', 'B']),
        Student('1', '1', ['B', 'A'])
    ]

    matches = mutual_match(companies, students)
    assert matches == {'0': 'A', '1': 'B'}

def test_no_mutual_match():
    companies = [
        Company('A', 1, ['0', '1']),
        Company('B', 1, ['0', '1']),
        Company('C', 1, ['0', '1'])
    ]
    
    students = [
        Student('0', '0', ['A', 'B']),
        Student('1', '1', ['B', 'A'])
    ]
    
    matches = mutual_match(companies, students)
    assert matches == {'0': 'A', '1': 'B'}

def test_more_than_one_mutual_match():
    companies = [
        Company('A', 2, ['0', '1', '2', '3']),
        Company('B', 1, ['0', '1']),
    ]
    
    students = [
        Student('0', '0', ['A', 'B']),
        Student('1', '1', ['B', 'A']),
        Student('2', '2', ['A']),
        Student('3', '3', ['A'])
    ]

    matches = mutual_match(companies, students)
    assert matches == {'0': 'A', '1': 'B', '2': 'A'}

def test_unilateral_match():
    unmatched_companies = [
        Company('AA', 1, ['0', '1']),
    ]
    
    unmatched_students = [
        Student('0', '0', ['A', 'B']),
        Student('1', '1', ['B', 'A'])
    ]
    
    matches, unmatched_companies, unmatched_students = unilateral_match(
        unmatched_companies, unmatched_students)
        
    assert matches == {}
    assert unmatched_companies == []
    assert unmatched_students == []


def test_unilateral_match_unmatched_company():
    unmatched_companies = [
        Company('AA', 1, ['0', '1']),
    ]
    
    unmatched_students = []
    
    matches, unmatched_companies, unmatched_students = unilateral_match(
        unmatched_companies, unmatched_students)
        
    assert matches == {}
    assert unmatched_companies == [ Company('AA', 1, ['0', '1'])]
    assert unmatched_students == []


def test_unilateral_match_unmatched_student():
    unmatched_companies = []
    
    unmatched_students = [Student('0', '0', ['A', 'B'])]
    
    matches, unmatched_companies, unmatched_students = unilateral_match(
        unmatched_companies, unmatched_students)
        
    assert matches == {}
    assert unmatched_companies == []
    assert unmatched_students == [Student('0', '0', ['A', 'B'])]