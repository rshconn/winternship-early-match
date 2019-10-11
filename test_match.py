from match import Company, Student, mutual_match, unilateral_match

def test_mutual_match():
    companies = {
        Company('A', 1, ['0', '1']),
        Company('B', 1, ['1', '0'])
    }
    
    students = [
        Student('0', '0', 0, ['A', 'B']),
        Student('1', '1', 1, ['B', 'A'])
    ]
    
    matches = mutual_match(companies, students)

    assert matches == {'0': 'A', '1': 'B'}
    print('passed test_simple_match')

def test_mutual_match_two_rounds():
    companies = {
        Company('A', 1, ['0', '1']),
        Company('B', 1, ['0', '1'])
    }
    
    students = [
        Student('0', '0', 0, ['A', 'B']),
        Student('1', '1', 1, ['B', 'A'])
    ]

    matches = mutual_match(companies, students)
    assert matches == {'0': 'A', '1': 'B'}
    print('passed test_match_two_rounds')

def test_no_mutual_match():
    companies = {
        Company('A', 1, ['0', '1']),
        Company('B', 1, ['0', '1']),
        Company('C', 1, ['0', '1'])
    }
    
    students = [
        Student('0', '0', 0, ['A', 'B']),
        Student('1', '1', 1, ['B', 'A'])
    ]
    
    matches = mutual_match(companies, students)
    assert matches == {'0': 'A', '1': 'B'}
    print('passed test_no_match')

def test_more_than_one_mutual_match():
    companies = {
        Company('A', 2, ['0', '1', '2', '3']),
        Company('B', 1, ['0', '1']),
    }
    
    students = [
        Student('0', '0', 0, ['A', 'B']),
        Student('1', '1', 1, ['B', 'A']),
        Student('2', '2', 2, ['A']),
        Student('3', '3', 3, ['A'])
    ]

    
    matches = mutual_match(companies, students)
    assert matches == {'0': 'A', '1': 'B', '2': 'A'}
    print('passed test_more_than_one_match')

if __name__ == "__main__":
	test_mutual_match()
	test_mutual_match_two_rounds()
	test_no_mutual_match()
	test_more_than_one_mutual_match()