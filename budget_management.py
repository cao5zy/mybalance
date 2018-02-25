import logging
from pipe import *
# schema defintion



LOGGER = logging.getLogger(__name__)

class BudgetManagement:
    def __init__(self, dbname="testdb"):
        from pymodm import connect, MongoModel, fields
        connect('mongodb://localhost:27017/%s' % dbname)

        class Income(MongoModel):
            income = fields.FloatField()
            desc = fields.CharField(min_length=0, max_length=255)
            date = fields.DateTimeField()
            title = fields.CharField(min_length=1, max_length=50)

        class Consumption(MongoModel):
            consumption = fields.FloatField()
            account = fields.CharField(min_length=1, max_length=125)
            date = fields.DateTimeField()
            desc = fields.CharField(min_length=0, max_length=125)

        class Budget(MongoModel):
            account = fields.CharField(min_length=1, max_length=125)
            amount = fields.FloatField()

        class Balance(MongoModel):
            incomes = fields.EmbeddedDocumentListField(Income)
            consumptions = fields.EmbeddedDocumentListField(Consumption)
            budgets = fields.EmbeddedDocumentListField(Budget)
            key = fields.CharField(min_length=1, max_length=50, primary_key=True, required=True)

        class Key(MongoModel):
            name = fields.CharField(min_length=1, \
                max_length=20, primary_key=True, verbose_name="name")
            order = fields.IntegerField()
        # schema definition

        def current_key(name="default"):
            return {
                "name": name,
                "order": (lambda result: 0 if result.count() == 0 else result[0].order)(Key.objects.raw({"_id": name}))
            }

        def set_current_key(keyObj):
            Key(name = keyObj["name"], order = keyObj["order"]).save()

            return current_key(keyObj["name"])

        def increase_key(keyObj):
            return {
                "name": keyObj["name"],
                "order": keyObj["order"] + 1
            }
        
        def decodeKey(keyObj):
            return "{name}-{order}".format(name = keyObj["name"], order = keyObj["order"])

        def new_balance(name="default"):
            import datetime
            def new(balance):
                balance.save()
                return balance

            return new(Balance(incomes=[Income(income=0, \
                    desc='default', \
                    date=datetime.datetime.now(), \
                    title="income")], \
                consumptions=[Consumption(consumption=0, \
                    account="None", \
                    date=datetime.datetime.now(), \
                    desc="NA")], \
                budgets=[Budget(account="None", \
                    amount=0)], \
                key=decodeKey(set_current_key(increase_key(current_key(name))))\
                ))


        def current_balance(name="default"):
            return (lambda result:new_balance(name) if result.count() == 0 else result[0])\
                (Balance.objects.raw({"_id": decodeKey(current_key(name))}))

                
        def add_income(balance, incomeDict):
            LOGGER.debug({"add_income": incomeDict})
            balance.incomes.append(Income(income=incomeDict["income"], \
                desc=incomeDict["desc"], \
                date=incomeDict["date"], \
                title=incomeDict["title"]))

        def add_consumption(balance, consumptionDict):
            balance.consumptions.append(Consumption(\
                consumption=consumptionDict["consumption"], \
                account=consumptionDict["account"], \
                date=consumptionDict["date"], \
                desc=consumptionDict["desc"]))

        def add_budget(balance, budgetDict):
            LOGGER.debug({"add_budget": budgetDict})
            balance.budgets.append(Budget(\
                account=budgetDict["account"], \
                amount=budgetDict["amount"]))

        def to_json(balance):
            return {
            "incomes": balance.incomes | \
                select(lambda n:{"income": n.income, "desc": n.desc, "date": n.date, "title": n.title}) | \
                as_list(),
            "consumptions": balance.consumptions | \
                select(lambda n: {"consumption": n.consumption, "account": n.account, "date": n.date, "desc": n.desc}) | \
                as_list(),
            "budgets": balance.budgets | \
                select(lambda n: {"account": n.account, "amount": n.amount}) | \
                as_list()
            }

        self.new_balance=new_balance
        self.current_balance=current_balance
        self.current_key=current_key
        self.set_current_key=set_current_key
        self.increase_key=increase_key
        self.add_income=add_income
        self.add_consumption=add_consumption
        self.add_budget=add_budget
        self.to_json=to_json