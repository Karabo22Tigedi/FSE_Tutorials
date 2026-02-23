from decimal import Decimal, InvalidOperation
from typing import List

# Constants
CURRENCY_SYMBOL = "R"


class Transaction:
    def __init__(self, date, description, amount, category):
        self.date = date
        self.description = description
        try:
            self.amount = Decimal(amount)
        except InvalidOperation:
            raise ValueError(f"Invalid amount: {amount}")
        self.category = category

    def __repr__(self):
        return f"Transaction(date='{self.date}', description='{self.description}', amount={self.amount}, category='{self.category}')"


# TODO: Implement this function to sum all transactions with negative amounts
def calculate_total_expenses(transactions: List[Transaction]) -> Decimal:
    """Calculates the total expenses from a list of transactions.

    Args:
        transactions: A list of Transaction objects.

    Returns:
        The total expenses as a Decimal (should be negative).
    Example:
        >>> transactions = [Transaction('2024-01-01', 'Groceries', '-500.00', 'Food'),
        ...                 Transaction('2024-01-02', 'Rent', '-1500.00', 'Housing')]
        >>> calculate_total_expenses(transactions)
        Decimal('-2000.00')
    """
    total_expense = Decimal(0)
    for trans in transactions:
        trans_amount = Decimal(trans.amount)
        if trans_amount < 0:
            total_expense += trans_amount
    return total_expense


# TODO: Implement this function to sum all transactions with positive amounts
def calculate_total_income(transactions: List[Transaction]) -> Decimal:
    """Calculates the total income from a list of transactions.

    Args:
        transactions: A list of Transaction objects.

    Returns:
        The total income as a Decimal (should be positive).
    """
    total_income = Decimal(0)
    for trans in transactions:
        trans_amount = Decimal(trans.amount)
        if trans_amount > 0:
            total_income += trans_amount
    return total_income


# NOTE: This function is already complete - no changes needed here!
def format_currency(amount: Decimal) -> str:
    """
    Format a numeric amount as South African Rand currency.

    Args:
        amount: The amount to format as a float or Decimal.

    Returns:
        A formatted string with the Rand symbol and two decimal places.

    Example:
        >>> format_currency(Decimal("1234.56"))
        'R 1234.56'
    """
    return f"{CURRENCY_SYMBOL} {amount:,.2f}"


# TODO: Update this function to work with Transaction objects instead of dicts.
# Change List[dict] to List[Transaction], use dot notation (t.amount), and update docstring.
# Hint: With Transaction objects, simply sum all amounts (expenses are negative, income is positive)!
def calculate_balance(transactions: List[Transaction]) -> Decimal:
    """
    Calculate the current balance from a list of transactions.

    Income transactions add to the balance; expense transactions subtract.

    Args:
        transactions: A list of Transaction objects.

    Returns:
        The calculated balance as a Decimal.

    Example:
        >>> transactions = [
        ...     Transaction('2024-01-01', 'Salary', '5000.00', 'Income'),
        ...     Transaction('2024-01-02', 'Rent', '-1000.00', 'Housing')
        ... ]
        >>> calculate_balance(transactions)
        Decimal('4000')
    """
    balance = Decimal(
        calculate_total_income(transactions) + calculate_total_expenses(transactions)
    )
    return balance
