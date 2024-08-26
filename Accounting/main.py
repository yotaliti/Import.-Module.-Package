from application.salary import get_employees
from application.db.people import calculate_salary
from datetime import datetime
from smile.smile import smile


dt_now = datetime.now()

if __name__ == '__main__':
    print(dt_now.date())
    get_employees()
    calculate_salary()
    smile()
