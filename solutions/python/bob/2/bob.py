def response(hey_bob):
    stripped = hey_bob.strip()
    last_char = None

    if len(stripped) > 0:
        last_char = stripped[len(stripped) - 1]

    if hey_bob.isupper():
        if last_char != '?':
            return 'Whoa, chill out!'
        if last_char == '?':
            return 'Calm down, I know what I\'m doing!'
    else:
        if last_char == '?':
            return 'Sure.'
        if len(stripped) == 0:
            return 'Fine. Be that way!'
        
    return 'Whatever.'