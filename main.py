import click
from collections import Counter

from match_io import (load_company_responses, load_student_responses, write_matches,
                      write_unmatched_companies, write_unmatched_students)
from match import mutual_match, unilateral_match

@click.command()
@click.argument('companies_filepath', required=True)
@click.argument('students_filepath', required=True)
@click.option('--company_name_field', default='Q1')
@click.option('--company_ranking_fields', default='Q35,Q47,Q48,Q49,Q50,Q51,Q52,Q53,Q54,Q55,Q136,Q137,Q138,Q139,Q140,Q141,Q142,Q143,Q144,Q145,Q146,Q147,Q148,Q149,Q150,Q151,Q152,Q153,Q154,Q155')
@click.option('--student_name_field', default='Q7')
@click.option('--student_ranking_fields', default='Q20_0_GROUP,Q8_0_GROUP')
@click.option('--output_prefix', default='')
def main(companies_filepath, students_filepath, company_name_field,
         company_ranking_fields, student_name_field, student_ranking_fields,
         output_prefix):
    companies = load_company_responses(companies_filepath, company_name_field,
                                       company_ranking_fields.split(','))
    students  = load_student_responses(students_filepath, student_name_field,
                                       student_ranking_fields.split(','))
    
    
    mutual_matches, unmatched_companies, unmatched_students = mutual_match(companies, students)
    
    num_matches = Counter(mutual_matches.values())
    unilateral_matches, unmatched_companies, unmatched_students = unilateral_match(
        companies, students, num_matches)
        
    all_matches = {**mutual_matches, **unilateral_matches}
    write_matches(all_matches, output_prefix)
    write_unmatched_students(unmatched_students, output_prefix)
    write_unmatched_companies(unmatched_companies, all_matches, output_prefix)
    
if __name__ == "__main__":
    main()