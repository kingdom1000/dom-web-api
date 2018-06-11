
def check(key):
    domKey = open('/var/domkey/main.key', 'r').read()
    if key + '\n' == domKey:
        return True
    else:
        return False
