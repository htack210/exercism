def response(hey_bob):
    stripped = hey_bob.strip()
    lastChar = None

    if len(stripped) > 0:
        lastChar = stripped[len(stripped) - 1]
    
    if hey_bob.isupper():
        if lastChar != '?':
            return 'Whoa, chill out!'
        elif lastChar == '?':
            return 'Calm down, I know what I\'m doing!'
    else:
        if lastChar == '?':
            return 'Sure.'
        elif len(stripped) == 0:
            return 'Fine. Be that way!'
        
    return 'Whatever.'

