import random

def get_command(message: str) -> str:
    p_command = message.lower()

    if p_command == '$hello':
        return 'Hey there!'
    
    if p_command == '$roll':
        return str(random.randint(1, 9))

    if p_command == '!help':
        return '`It looks like you need help!  This function is currently a work in progress.`'


    
