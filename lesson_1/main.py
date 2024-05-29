from datetime import datetime,date,time
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    today = datetime.today()
    formatted_date = today.strftime("%Y-%m-%d")
    print(formatted_date)
    calculate_salary()
    get_employees()
