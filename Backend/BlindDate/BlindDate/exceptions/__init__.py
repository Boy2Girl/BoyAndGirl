class PasswordWrongException(Exception):
    print("password wrong")


class SystemErrorException(Exception):
    print("system error")


class NotFoundException(Exception):
    print("username not found")


class AlreadyExists(Exception):
    print("user already exists")


class InsertException(Exception):
    print("user already exists")