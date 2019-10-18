import csv
from collections import Counter
from match import Company, Student 


def format_string(string):
    """
    Parameters
    ----------
    string : str
    
    Returns
    -------
    str
    """
    return string.replace(" ", "")
    

def load_max_matches(filepath):
    """
    Parameters
    ----------
    filepath : str
        csv with the fields company, max_matches
    
    Returns
    ------
    dict {str : int}
    """
    max_matches = {}
    with open(filepath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            max_matches[format_string(row['company'])] = int(row['max_matches'])
    return max_matches
        
        
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
    max_matches = load_max_matches('data/max_matches.csv')
    with open(filepath) as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        # Skip first 2 non-header rows
        for i in range(2, len(data)):
            name = format_string(data[i][name_field])
            ranked_students = []
            for field in student_fields:
                student = data[i][field]
                if student:
                    ranked_students.append(format_string(student))
            companies.append(Company(name, max_matches[name], ranked_students))
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
            name = format_string(data[i][name_field])
            for field in company_fields:
                if data[i][field]:
                    ranked_companies = format_string(data[i][field].strip('"')).split(',')
                    break
            students.append(Student(name, ranked_companies))
    return students
    
    
def parse_student_name(name):
    """
    Parameters
    ----------
    name : str
    """
    return name.split(',')


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
        f.write('first,last,company\n')
        for student in matches:
            first, last = parse_student_name(student.name)
            company = matches[student].name
            f.write(f'{first},{last},{company}\n')


def write_unmatched_companies(unmatched_companies, matches, output_prefix):
    """
    Parameters
    ----------
    unmatched_companies : list of Company
    output_prefix : str
    """
    print('Writing unmatched companies')
    with open(f'{output_prefix}_unmatched_companies.csv', 'w') as f:
        f.write('company,num_matches,num_open_matches\n')
        num_matches = Counter(matches.values())
        for company in unmatched_companies:
            name = company.name
            num_matches = num_matches[company]
            num_open_matches = company.max_matches - num_matches
            f.write(f'{name},{num_matches},{num_open_matches}\n')


def write_unmatched_students(unmatched_students, output_prefix):
    """
    Parameters
    ----------
    unmatched_students : list of Student
    output_prefix : str
    """
    print('Writing unmatched students')
    with open(f'{output_prefix}_unmatched_students.csv', 'w') as f:
        f.write('first,last\n')
        for student in unmatched_students:
            first, last = parse_student_name(student.name)
            f.write(f'{first},{last}\n')