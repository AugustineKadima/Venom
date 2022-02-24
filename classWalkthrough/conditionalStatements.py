"""
if I get 1000 shillings I will go to Mombasa
else if I get 500 shillings I will go to Mtito Andei
else if I don't get any money I will stay at home
"""

def where_to_travel_to(income):
    if income == 1000 : return "Go to Mombasa"
    elif income == 500 : return "Go to Mtito Andei"
    else: return "Stay at home"

results = where_to_travel_to(999)
print(results)