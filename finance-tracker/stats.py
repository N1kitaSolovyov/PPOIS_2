from models import Transaction, TransactionManager, TransactionType
from typing import Dict
from dataclasses import dataclass

@dataclass
class StatsResult:
    balance: float
    total_income: float = 0.0
    total_expens: float
    total_count: int
    average_income: float
    average_expens: float
    count_income: int
    count_expens: int
    max_income: float
    max_expens: float
    category_expense: dict[str, float]

class TransactionStats(StatsResult):
    
    def calculate(self, transactions: list[Transaction]) -> StatsResult:
        for t in transactions:
            if t.transaction_type == TransactionType.INCOME:
                total_income += t.amount
