def leap_year(year):
    
    isDivByFour = year % 4 == 0
    isDivByHundred = year % 100 == 0
    isDivByFourHundred = year % 400 == 0    
    
    if isDivByFour and not isDivByHundred:
          return True
    if isDivByFour and isDivByFourHundred:
            return True
        
    return False