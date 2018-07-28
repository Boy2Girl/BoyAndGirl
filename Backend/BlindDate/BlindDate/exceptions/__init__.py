class PasswordWrongException(Exception):
    print("password wrong")


class SystemErrorException(Exception):
    print("system error")


class NotFoundException(Exception):
    print("username not found")


class UserAlreadyExists(Exception):
    print("user already exists")