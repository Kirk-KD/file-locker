from src.file_locker import lock_file, unlock_file

running = True
while running:
    print(' 1 - Lock file\n 2 - Unlock file\n 3 - Exit')

    op = input('Select an option: ')
    while op not in ('1', '2', '3'):
        op = input('Select an option: ')

    if op == '1':
        fp = input('Enter file path: ')
        key = lock_file(fp)
        if type(key) is int:
            print(f'File locked. Key: {key}')
        else:
            print('Failed.')

    elif op == '2':
        fp = input('Enter file path: ')
        fkey = None
        while True:
            try:
                fkey = int(input('Enter key (THE FILE WILL BE LOCKED FOREVER IF THE KEY IS WRONG): '))
                break
            except ValueError:
                print('Invalid key.')

        res = unlock_file(fp, fkey)
        if res is None:
            print('File unlocked.')
        else:
            print('Failed.')

    else:
        print('Bye!')
        running = False

input('[press ENTER to exit]')
