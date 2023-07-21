try:
    # avinash
    avinash=12
except Exception as a:
    print(a)
except EOFError as a:
    print(a)
except IOError as a:
    print(a)
else:
    print('run until except are not run')
finally:
    print(' it is run any codition')