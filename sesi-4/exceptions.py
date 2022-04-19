import sys
assert ('linux' in sys.platform), "This code runs on Linux only."
assert ('windows' in sys.platform), "This code runs on Windows only."

def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('windows' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

try:
    os_interaction()
except:
    pass

