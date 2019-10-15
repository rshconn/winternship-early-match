import csv
from match import Company, Student 

 # TODO: Handle spaces

def load_company_responses(filepath, name_field, student_fields):
    """
    Parameters
    ----------
    filename : str
    name_field : str
    student_fields : list of str
        In order list of student ranking fields
    
    Returns
    -------
    list of Company
    """
    print('Loading company responses')
    companies = []
    with open(filepath) as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        # Skip first 2 non-header rows
        for i in range(2, len(data)):
            name = data[i][name_field]
            ranked_students = []
            for field in student_fields:
                student = data[i][field]
                if student:
                    ranked_students.append(student)
            # TODO: max_matches
            companies.append(Company(name, 2, ranked_students))
    return companies

def load_student_responses(filepath, name_field, company_fields):
    """
    Parameters
    ----------
    filepath : str
    name_field : str
    company_fields : list of str
    
    Returns
    -------
    list of Student
    """
    # Note: Should already have students who do not want to be matched & Natures Plus matches filtered out
    print('Loading student responses')
    students = []
    with open(filepath) as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        # Skip first 2 non-header rows
        for i in range(2, len(data)):
            name = data[i][name_field]
            for field in company_fields:
                if data[i][field]:
                    ranked_companies = data[i][field].strip('"').split(',')
                    break
            students.append(Student(name, ranked_companies))
    return students
    

def format_student_name(name):
    """
    Parameters
    ----------
    name : str
    """
    # TODO
    pass
    
    
def write_matches(matches, output_prefix):
    """"
    Parameters
    ----------
    matches : dict
        {Student: Company}
    output_prefix : str
    """
    print('Writing matches')
    with open(f'{output_prefix}_matches.csv', 'w') as f:
        f.write('student,company\n')
        for student in matches:
            f.write(f'{student.name}, {matches[student].name}\n')

def write_unmatched_companies(unmatched_companies, output_prefix):
    """
    Parameters
    ----------
    unmatched_companies : list of Company
    output_prefix : str
    """
    print('Writing unmatched companies')
    with open(f'{output_prefix}_unmatched_companies.csv', 'w') as f:
        f.write('company,num_matches\n')
        for company in unmatched_company:
            f.write(f'{company.name}, {matches[student].name}\n')

def write_unmatched_students(unmatched_students, output_prefix):
     """
    Parameters
    ----------
    unmatched_students : list of Company
    output_prefix : str
    """
    pass