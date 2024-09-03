from datetime import datetime

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.prices = {}

    def set_price(self, date, price):
        self.prices[date] = price

    def price(self, date):
        return self.prices.get(date, 0.0)

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock, quantity):
        self.stocks.append((stock, quantity))

    def profit(self, start_date, end_date):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        initial_value = 0.0
        final_value = 0.0

        for stock, quantity in self.stocks:
            initial_value += stock.price(start_date) * quantity
            final_value += stock.price(end_date) * quantity

        return final_value - initial_value

    def annualized_return(self, start_date, end_date):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        profit = self.profit(start_date, end_date)
        initial_value = sum(stock.price(start_date) * quantity for stock, quantity in self.stocks)

        if initial_value == 0:
            return 0.0

        years = (end_date - start_date).days / 365.25
        return ((profit / initial_value) + 1) ** (1 / years) - 1

# Ejemplo de uso
stock1 = Stock("AAPL")
stock1.set_price(datetime(2023, 1, 1), 150)
stock1.set_price(datetime(2024, 1, 1), 180)

portfolio = Portfolio()
portfolio.add_stock(stock1, 10)

print("Profit:", portfolio.profit("2023-01-01", "2024-01-01"))
print("Annualized Return:", portfolio.annualized_return("2023-01-01", "2024-01-01"))
