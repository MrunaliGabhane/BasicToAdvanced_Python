def average_age_of_employees_with_s_job_title(employees):
   s_employees = [employee['age'] for employee in employees.values() if employee['job_title'].startswith('S')]

   if not s_employees:
      return 0

   return sum(s_employees) / len(s_employees)

company = {
    'employees': {
        'John': {'age': 35, 'job_title': 'Manager'},
        'Emma': {'age': 28, 'job_title': 'Software Engineer'},
        'Kelly': {'age': 41, 'job_title': 'Senior Developer'},
        'Sam': {'age': 30, 'job_title': 'Software Engineer'},
        'Mark': {'age': 37, 'job_title': 'Senior Manager'},
        'Sara': {'age': 32, 'job_title': 'Software Engineer'},
    }
}

print(average_age_of_employees_with_s_job_title(company)) 
