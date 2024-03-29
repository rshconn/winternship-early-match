from collections import Counter

class Company:
    def __init__(self, name, max_matches, ranked_students):
        """
        Parameters
        ----------
        name : str
        max_matches : int
        ranked_students : list of str

        """
        self.name = name
        self.max_matches = max_matches
        self.ranked_students = ranked_students


class Student:
    def __init__(self, name, ranked_companies):
        """
        Parameters
        ----------
        name : str
        ranked_companies : list of str
            In order list of the names of ranked companies 
        """
        self.name = name
        self.ranked_companies = ranked_companies
    
    
def find_first_available_student(ranked_students, available_students, mutual=False, company_name=''):
    """
    Parameters
    ---------
    ranked_students : list of str
    available_students : list of Student
    mutual : bool
    company_name

    Returns
    ------
    Student or None

    """
    for student_name in ranked_students:
        if mutual:
            student = next((student for student in available_students if 
                            student.name == student_name and company_name in student.ranked_companies), None)
        else: 
            student = next((student for student in available_students if student.name == student_name), None)
        if student:
            return student
    return None


def find_first_available_company(ranked_companies, available_companies):
    """
    Parameters
    ---------
    ranked_companies : list of str
    available_companies : list of Company

    Returns
    ------
    Company or None
    """
    for company_name in ranked_companies:
         company = next((company for company in available_companies if company.name == company_name), None)
         if company: 
             return company
    return None


def company_can_be_matched(company, available_students):
    """
    Parameters
    ----------
    company : Company 
    available_students : list of Student
    
    Returns
    -------
    bool
    """
    for student in available_students:
        if company.name in student.ranked_companies:
            return True
    return False


def company_has_open_spots(company, matches):
    """
    Parameters
    ----------
    company : Company
    matches : dict
    
    Returns
    -------
    bool 
    """
    num_matches = Counter(matches.values())
    return num_matches[company] < company.max_matches
    
    
def mutual_match(companies, students):
    """
    Parameters
    ---------
    companies : list of Company
    students : list of Student
    
    Returns
    -------
    dict, list of Company, list of Student
    """
    print('Matching')
    matches = {}    # {Student : Company}
    unmatched_companies = []
    unmatched_students = []
    while len(companies) > 0:   # Round
        print(f'Number of matches: {len(matches)}')
        available_companies = []
        
        for company in companies:
            if company_can_be_matched(company, students):
                student = find_first_available_student(company.ranked_students,
                                                       students,
                                                       mutual=True,
                                                       company_name=company.name)
                
                if student:
                    company_choice = find_first_available_company(student.ranked_companies, companies)
    
                    if company_choice:
                        # print(f'{student.name} wants {company_choice.name}')
                        if company.name in student.ranked_companies:
                            # Assign student to company
                            matches[student] = company
    
                            # Remove student from matching pool
                            students.remove(student)
    
                    else:   # None of student's ranked companies remain
                        print(f"Cannot match {student}")
                        # Remove student from matching pool
                        students.remove(student)
                        unmatched_students.append(student)
                        available_companies.append(company)
    
                else:   # None of company's ranked students remain
                    print(f'Cannot match {company.name}')
                    unmatched_companies.append(company)
                
                if company_has_open_spots(company, matches):
                    available_companies.append(company)
    
            else:   # None of company's remaining ranked students have ranked them
                print(f'Cannot match {company.name}')
                unmatched_companies.append(company)
                
        companies = available_companies
   
    # Add any remaining students
    unmatched_students = unmatched_students + students
    return matches, unmatched_companies, unmatched_students


def unilateral_match(companies, students, matches):
    """Match unmatched students with companies that have ranked those students
    
    Parameters
    ----------
    companies : list of Company
    students : list of Student
    matches : dict
        {Student : Company}

    Returns
    -------
    dict, list of Company, list of Student
    """
    print('Assigning unilateral matches')
    new_matches = {}    # {Student: Company}
    unmatched_companies = []
    while len(companies) > 0 and len(students) > 0:
        for company in companies:
            student = find_first_available_student(company.ranked_students, students)
            if student: # Unilateral match 
                matches[student] = company
                students.remove(student)
                
                if not company_has_open_spots(company, {**matches, **new_matches}):
                    companies.remove(company)
                
            else:
                print(f'No unmatched students available for {company.name}')
                companies.remove(company)
                unmatched_companies.append(company)
    return new_matches, unmatched_companies, students

