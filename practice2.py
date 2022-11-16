def dollars():
  amount = int(input("Amount in Dollars:"))
  return amount

def usd_to_eur(x):
  new = x*0.90
  return f"Amount in euros:{new}"