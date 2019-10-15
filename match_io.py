import csv
from match import Company, Student 


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
            companies.append(Company(name, 0, ranked_students))
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
    
    
def write_matches(matches):
    """"
    Parameters
    ----------
    matches : dict
        {Student: Company}
    """
    with open('matches.csv', 'w') as f:
        f.write('student,company\n')
        for student in matches:
            f.write(f'{student.name}, {matches[student].name}\n')