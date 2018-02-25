import sys
import datetime
import logging
from budget_management import BudgetManagement

logging.basicConfig(stream=sys.stdout, level='DEBUG')
LOGGER = logging.getLogger(__name__)

def get_budget_param():
    return {
        "account": sys.argv[2],
        "amount": sys.argv[3]
    }

def get_consumption_param():
    return {
        "account": sys.argv[2],
        "consumption": sys.argv[3],
        "desc": "" if len(sys.argv) == 4 else sys.argv[4]
    }

def get_income_param():
    return {
        "title": sys.argv[2],
        "income": sys.argv[3],
        "desc": "None" if len(sys.argv) == 4 else sys.argv[4]
    }

def get_action():
    LOGGER.debug({"argv": sys.argv})
    return sys.argv[1]

def create_budget_management():
    return BudgetManagement("balance")

def add_budget():
    def add(budget_management):
        def save(balance):
            budget_management.add_budget(balance, get_budget_param())
            balance.save()

        save(budget_management.current_balance())

    add(create_budget_management())

def add_consumption():
    def add(budget_management):
        def save(balance):
            budget_management.add_consumption(balance, \
                dict(get_consumption_param(), **{"date": datetime.datetime.now()}))
            balance.save()

        save(budget_management.current_balance())

    add(create_budget_management())

def add_income():
    def add(budget_management):
        def save(balance):
            budget_management.add_income(balance, \
                dict(get_income_param(), **{"date": datetime.datetime.now()}))
            balance.save()

        save(budget_management.current_balance())

    add(create_budget_management())

def error_cmd():
    print("error command")

def show_budget_remaining():
    import present
    def show(budget_management):
        present.showBudgetRemaining(budget_management.to_json(budget_management.current_balance()))

    show(create_budget_management())

def main():
    def process(action):
        (lambda actionDic: actionDic[(action if action in actionDic else "errorcmd").lower()]())\
        ({
            "addbudget": add_budget,
            "addconsumption": add_consumption,
            "addincome": add_income,
            "errorcmd": error_cmd,
            "showbudgetremaining": show_budget_remaining
        })

    process(get_action())

if __name__ == '__main__':
    main()
