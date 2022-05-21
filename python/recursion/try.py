def raise_funds(amount):
    # assert amount >= 0 and int(
    #     amount) == amount, 'Only positive integers are accepted'
    if amount == 12:
      print(amount - 1)
      return
    if amount == 500:
        return amount 
    
    else:
        return raise_funds(amount + 5)


print(raise_funds(2))
