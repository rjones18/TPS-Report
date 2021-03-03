import csv

# Employees is a list of dictionaries.
# The keys in these dictionaries will be the header fields of your spreadsheet.
employees = [
  {
    'first_name': 'Bill',
    'last_name': 'Lumbergh',
    'job_title': 'Vice President',
    'hire_date': 1985,
    'performance_review': 'poor',
    'review_finished': 'yes'
  },
  {
    'first_name': 'Michael',
    'last_name': 'Bolton',
    'job_title': 'Programmer',
    'hire_date': 1995,
    'performance_review': 'excellent',
    'review_finished': 'yes'
  },
  {
    'first_name': 'Peter',
    'last_name': 'Gibbons',
    'job_title': 'Programmer',
    'hire_date': 1989,
    'performance_review': 'excellent',
    'review_finished': 'yes'
  },
  {
    'first_name': 'Samir',
    'last_name': 'Nagheenanajar',
    'job_title': 'Programmer',
    'hire_date': 1974,
    'performance_review': 'excellent',
    'review_finished': 'yes'
  },
  {
    'first_name': 'Milton',
    'last_name': 'Waddams',
    'job_title': 'Collator',
    'hire_date': 1974,
    'performance_review': 'excellent',
    'review_finished': 'yes'
  },
  {
    'first_name': 'Bob',
    'last_name': 'Porter',
    'job_title': 'Consultant',
    'hire_date': 1999,
    'performance_review': 'poor',
    'review_finished': 'yes'
  },
  {
    'first_name': 'Bob',
    'last_name': 'Slydell',
    'job_title': 'Consultant',
    'hire_date': 1999,
    'performance_review': 'poor',
    'review_finished': 'yes'
  }
]


def main():

  with open('tps_report.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'job_title', 'hire_date', 'performance_review', 'review_finished']
    
    
   
    writer = csv.DictWriter(csvfile, fieldnames)
    writer.writeheader()
    
    
    for employee in employees:
      writer.writerow(employee)


main()
