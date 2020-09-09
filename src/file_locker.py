from random import randint


def read_from_file(path):
    try:
        with open(path) as f:
            return f.read()
    except IOError as err:
        print(err)
        return err


def get_locked_text(orig):
    ori = ''
    temp = randint(17, 23)
    key_ord = randint(-temp, temp)

    for char in orig:
        c_ord = ord(char)

        if 0 <= c_ord + key_ord <= 11141111:
            ori += str(chr(c_ord - key_ord))
        else:
            ori += char

    return key_ord, str(ori)


def get_unlocked_text(orig, key):
    ori = ''
    for char in orig:
        c_ord = ord(char)
        if 0 <= c_ord + key <= 11141111:
            ori += str(chr(c_ord + key))
        else:
            ori += char
    return ori


def lock_file(path):
    read = read_from_file(path)
    locked_key, locked_text = get_locked_text(read)
    try:
        with open(path, 'w') as f:
            f.write(locked_text)
    except IOError as err:
        print(err)
        return err
    finally:
        f.close()
    return locked_key


def unlock_file(path, key):
    read = read_from_file(path)
    unlocked_text = get_unlocked_text(read, key)
    try:
        with open(path, 'w') as f:
            f.write(unlocked_text)
    except IOError as err:
        print(err)
        return err
    finally:
        f.close()
