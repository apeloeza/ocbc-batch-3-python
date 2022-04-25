x = 0
y = 5

if x < y:                            # Truthy *
    print('yes 1')

if y < x:                            # Falsy
    print('yes 2')

if x:                                # Falsy
    print('yes 3')

if y:                                # Truthy *
    print('yes 4')

if 'aul' in 'grault':                # Truthy *
    print('yes 5')

if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes 6')
