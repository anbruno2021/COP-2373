# this program reads student grades from a csv and analyzes them
# it prints stats for each exam, overall stats, and pass/fail info

import numpy as np

# constant for passing grade
PASSING_GRADE = 60

# function to load csv data
def load_data(file_name):
    
    # load only the exam columns
    grades = np.genfromtxt(file_name, delimiter=',', skip_header=1, usecols=(2, 3, 4))
    
    return grades

# function to print first few rows
def print_preview(data, num_rows=5):
    
    print("first few rows of the data:")
    print(data[:num_rows])

# function to calculate stats for each exam
def exam_statistics(data):
    
    print("\nstats for each exam:")
    
    num_exams = data.shape[1]
    
    for i in range(num_exams):
        
        print(f"exam {i+1}:")
        print(f"  mean: {np.mean(data[:, i]):.2f}")
        print(f"  median: {np.median(data[:, i]):.2f}")
        print(f"  std dev: {np.std(data[:, i]):.2f}")
        print(f"  min: {np.min(data[:, i])}")
        print(f"  max: {np.max(data[:, i])}")

# function to calculate overall stats
def overall_statistics(data):
    
    all_grades = data.flatten()
    
    print("\noverall stats for all exams:")
    print(f"  mean: {np.mean(all_grades):.2f}")
    print(f"  median: {np.median(all_grades):.2f}")
    print(f"  std dev: {np.std(all_grades):.2f}")
    print(f"  min: {np.min(all_grades)}")
    print(f"  max: {np.max(all_grades)}")

# function to calculate pass/fail counts
def pass_fail_statistics(data, passing=PASSING_GRADE):
    
    total_students, total_exams = data.shape
    total_pass = 0

    print("\npass/fail for each exam:")
    
    for i in range(total_exams):
        
        exam_pass = np.sum(data[:, i] >= passing)
        exam_fail = np.sum(data[:, i] < passing)
        total_pass += exam_pass
        print(f"exam {i+1}: {exam_pass} passed, {exam_fail} failed")

    overall_pass = (total_pass / (total_students * total_exams)) * 100
    print(f"\noverall pass percentage: {overall_pass:.2f}%")

# main function to run everything
def main():
    
    file_name = 'grades.csv'
    grades_data = load_data(file_name)
    print_preview(grades_data)
    exam_statistics(grades_data)
    overall_statistics(grades_data)
    pass_fail_statistics(grades_data)

# run main
main()
