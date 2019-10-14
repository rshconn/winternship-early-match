from collections import Counter

from match import mutual_match, unilateral_match

def main():
    # TODO: IO
    companies = []
    students  = []
    
    mutual_matches, unmatched_companies, unmatched_students = mutual_match(companies, students)
    num_matches = Counter(mutual_matches.values())
    unilateral_matches, unmatched_companies, unmatched_students = unilateral_match(
        companies, students, num_matches)
        
    all_matches = {**mutual_matches, **unilateral_matches}
    # TODO: IO
    
if __name__ == "__main__":
    main()