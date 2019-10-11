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
        self.ranked_students = ranked_students  #
        self.matches = []

class Student:
    def __init__(self, first_name, last_name, unique_id, ranked_companies):
        """
        Parameters
        ----------
        first_name : str
        last_name : str
        unique_id : int
        ranked_companies : list of str
            In order list of the names of ranked companies 
        """
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.ranked_companies = ranked_companies
        self.match = None


def find_first_available(rankings, available):
    """
    Parameters
    ---------
    rankings : list of str
        In order list o
    available : list of str

    Returns
    ------

    """
    for item in rankings:
        if item in available:
            return item
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
            student = find_first_available(company.ranked_students, students)
            
            if student:
                company_choice = find_first_available(student.ranked_companies, [company.name for company in companies])
            
                if company_choice:
                    if company.name == company_choice:

                        # Assign student to company
                        matches[student] = company.name
                        company.matches.append(student)

                        # Remove student from matching pool
                        del students[student]

                        if len(company.matches) < company.max_matches:
                            available_companies.append(company)
                    else:
                            available_companies.append(company)
                else:
                    print(f'Cannot match {student}')
                    unmatched_students.append(student)
                    available_companies.append(company)
            else:
                print(f'Cannot match {company.name}')
                unmatched_companies.append(company)

        companies = available_companies
                
    return matches, unmatched_companies, unmatched_students

# TODO: Companies should get at least 1 student
def unilateral_match(unmatched_students, unmatched_companies):
    """
    Parameters
    ----------
    unmatched_students : list of Student
    unmatched_companies : list of Company 

    Returns
    -------
    dict
    """
    matches = {}
    for company in unmatched_companies:
        if len(company.matches) < 1:
            for student in company.ranked_students:
                if student in unmatched_students:
                    matches[student] = company.name
                    company.matches.append(student)
                    break
            print()
        else: 
            print(f'{company.name} ')

