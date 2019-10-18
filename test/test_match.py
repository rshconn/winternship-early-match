from match import (Company, Student, find_first_available_company, find_first_available_student,
                   company_can_be_matched, company_has_open_spots, mutual_match, unilateral_match)

def test_find_first_available_company():
    ranked_companies = ['A', 'B', 'C']
    company_to_find = Company('C', 1, ['0', '1'])
    available_companies = [company_to_find]
    company = find_first_available_company(ranked_companies, available_companies)
    assert company == company_to_find
    
def test_find_first_available_student():
    ranked_students = ['000', '111']
    student_to_find = Student('111', ['B', 'A'])
    available_students = [
        Student('222', ['A', 'B']),
        student_to_find
    ]
    student = find_first_available_student(ranked_students, available_students)
    assert student ==  student_to_find

def test_company_can_be_matched_true():
    company = Company('A', 1, ['0', '1'])
    available_students = [Student('0', ['C', 'B', 'A'])]
    assert company_can_be_matched(company, available_students)
    
def test_company_can_be_matched_false():
    company = Company('A', 1, ['0', '1'])
    available_students = [Student('0', ['C', 'B'])]
    assert not company_can_be_matched(company, available_students)

def test_company_has_open_spots_false():
    company = Company('A', 1, ['0', '1'])
    matches = {Student('0', []): company}
    assert not company_has_open_spots(company, matches)

def test_company_has_open_spots_true():
    company = Company('A', 1, ['0', '1'])
    matches = {Student('0', []): Company('B', 1, ['0', '1'])}
    assert company_has_open_spots(company, matches)
    
def test_mutual_match():
    co_A = Company('A', 1, ['0', '1'])
    co_B = Company('B', 1, ['1', '0'])
    companies = [co_A, co_B]
    
    student_0 = Student('0', ['A', 'B'])
    student_1 = Student('1', ['B', 'A'])
    students = [student_0, student_1]
    
    matches, unmatched_companies, unmatched_students = mutual_match(companies, students)

    assert matches == {student_0: co_A, student_1: co_B}
    assert unmatched_companies == []
    assert unmatched_students == []

def test_mutual_match_two_rounds():
    co_A = Company('A', 1, ['0', '1'])
    co_B = Company('B', 1, ['0', '1'])
    companies = [co_A, co_B]
 
    student_0 = Student('0', ['A', 'B'])
    student_1 = Student('1', ['B', 'A'])
    students = [student_0, student_1]    

    matches, unmatched_companies, unmatched_students = mutual_match(companies, students)
    assert matches == {student_0: co_A, student_1: co_B}
    assert unmatched_companies == []
    assert unmatched_students == []

def test_no_mutual_match():
    co_A = Company('A', 1, ['0', '1'])
    co_B = Company('B', 1, ['0', '1'])
    co_C = Company('C', 1, ['0', '1'])
    companies = [co_A, co_B, co_C]
 
    student_0 = Student('0', ['A', 'B'])
    student_1 = Student('1', ['B', 'A'])
    students = [student_0, student_1]   
    
    matches, unmatched_companies, unmatched_students = mutual_match(companies, students)
    assert matches == {student_0: co_A, student_1: co_B}
    assert unmatched_companies == [co_C]
    assert unmatched_students == []

def test_more_than_one_mutual_match():
    co_A = Company('A', 2, ['0', '1', '2', '3'])
    co_B = Company('B', 1, ['0', '1'])
    companies = [co_A, co_B]
    
    student_0 = Student('0', ['A', 'B'])
    student_1 = Student('1', ['B', 'A'])
    student_2 = Student('2', ['A'])
    student_3 = Student('3', ['A'])
    students = [student_0, student_1, student_2, student_3]

    matches, unmatched_companies, unmatched_students = mutual_match(companies, students)
    assert matches == {student_0: co_A, student_1: co_B, student_2: co_A}
    assert unmatched_companies == []
    assert unmatched_students == [student_3]

def test_unilateral_match():
    co_AA = Company('AA', 1, ['0', '1'])
    companies = [co_AA]
    
    student_0 = Student('0', ['A', 'B'])
    student_1 = Student('1', ['B', 'A'])
    students = [student_0, student_1]   
    
    matches = {Student('test', []): Company('other', 1, ['00', '11'])}
    
    matches, unmatched_companies, unmatched_students = unilateral_match(
        companies, students, matches)
        
    assert matches == {student_0: co_AA}
    assert unmatched_companies == []
    assert unmatched_students == [student_1]


def test_unilateral_match_unmatched_company():
    co_AA = Company('AA', 1, ['0', '1'])
    companies = [co_AA]
 
    students = []
    num_matches = {co_AA: 0}
    
    matches, unmatched_companies, unmatched_students = unilateral_match(
        companies, students, num_matches)
        
    assert matches == {}
    assert unmatched_companies == [co_AA]
    assert unmatched_students == []


def test_unilateral_match_unmatched_student():
    companies = []
    
    student_0 = Student('0', ['A', 'B'])
    students = [student_0]
    
    co_AA = Company('AA', 1, ['0', '1'])
    num_matches = {co_AA: 0}
    
    matches, unmatched_companies, unmatched_students = unilateral_match(
        companies, students, num_matches)
    assert matches == {}
    assert unmatched_companies == []
    assert unmatched_students == [student_0]