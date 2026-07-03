from models import TransactionManager, Transaction
from logger import logger


class TransactionBatch:
    def __init__(self, manager: TransactionManager):
        self._manager = manager

    def __enter__(self):
        self._peding = []
        return self

    def add(self, transaction: Transaction):
        self._peding.append(transaction)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            for t in self._peding:
                self._manager.add_transaction(t)
        else:
            logger.info(f"Откат из-за  ошибки: {exc_val}")