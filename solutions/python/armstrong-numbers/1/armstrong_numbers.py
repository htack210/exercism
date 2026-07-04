def is_armstrong_number(number):
    numToStr = str(number)
    length = len(numToStr)
    runTot = 0
    
    for i in numToStr:
        runTot = runTot + int(i)**length
    return runTot == number