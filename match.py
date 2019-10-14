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
        self.matches = []

class Student:
    def __init__(self, name, unique_id, ranked_companies):
        """
        Parameters
        ----------
        name : str
        unique_id : str
        ranked_companies : list of str
            In order list of the names of ranked companies 
        """
        self.name = name
        self.unique_id = unique_id
        self.ranked_companies = ranked_companies


def find_first_available_student(ranked_students, available_students):
    """
    Parameters
    ---------
    ranked_students : list of str
    available_students : list of Student

    Returns
    ------
    Student or None

    """
    for student_id in ranked_students:
        student = next((student for student in available_students if student.unique_id == student_id), None)
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
    matches = {}
    unmatched_companies = []
    unmatched_students = []
    while len(companies) > 0:
        available_companies = []
        
        for company in companies:
            student = find_first_available_student(company.ranked_students, students)
            
            if student:
                company_choice = find_first_available_company(student.ranked_companies, companies)

                if company_choice:
                    if company.name == company_choice.name:

                        # Assign student to company
                        matches[student] = company.name
                        company.matches.append(student)

                        # Remove student from matching pool
                        del students[student]

                        if len(company.matches) < company.max_matches:
                            available_companies.append(company)
                    else:   # Student's first available choice is not company
                            available_companies.append(company)
                else:   # None of student's ranked companies remain
                    print(f"Cannot match {student}")
                    unmatched_students.append(student)
                    available_companies.append(company)
            else:   # None of company's ranked students remain
                print(f'Cannot match {company.name}')
                unmatched_companies.append(company)

        companies = available_companies
                
    return matches, unmatched_companies, unmatched_students


def unilateral_match(unmatched_companies, unmatched_students):
    """Match unmatched students with companies that have ranked those students
    
    Parameters
    ----------
    unmatched_companies : list of Company
    unmatched_students : list of Student

    Returns
    -------
    dict, list of Company, list of Student
    """
    matches = {}
    for company in unmatched_companies:
        if len(company.matches) < 1:
            for student in company.ranked_students:
                if student in unmatched_students:
                    matches[student] = company.name
                    company.matches.append(student)
                    unmatched_students.remove(student)
                    unmatched_companies.remove(company)
                    break
            print(f'No unmatched students available for {company.name}')
        else: 
            print(f'{company.name} has {len(company.matches)}')
    
    return matches, unmatched_companies, unmatched_students

