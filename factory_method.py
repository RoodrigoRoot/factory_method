from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, username, email) -> None:
        self.username = username
        self.email = email



class UserMX(User):

    def __init__(self, username, email) -> None:
        self.username = username
        self.email = email
        self.country = "mx"

    def __str__(self) -> str:
        return f"{self.username} - {self.country}"


class UserCOL(User):

    def __init__(self, username, email) -> None:
        self.username = username
        self.email = email
        self.country = "col"

    def __str__(self) -> str:
        return f"{self.username} - {self.country}"

class FactoryUser(ABC):

    @abstractmethod
    def create_user() -> User:
        raise Exception


class FactoryUserMX(FactoryUser):

    def __init__(self, data) -> None:
        self.data = data

    def create_user(self) -> UserMX:
        return UserMX(**self.data)


class FactoryUserCOL(FactoryUser):

    def __init__(self, data: dict) -> None:
        self.data = data

    def create_user(self) -> UserCOL:
        return UserCOL(**self.data)


def user_factory() -> FactoryUser:


    factories = {
        "mx": FactoryUserMX(user_data),
        "col": FactoryUserCOL(user_data)
    }
    if country in factories:
        return factories[country]
    return None


def main(fac: FactoryUser) -> User:

    user = fac.create_user()
    print(user)


if __name__ == "__main__":
    email = input("Ingrese su email> ")
    username = input("Ingrese su username> ")
    country = input("Ingrese su país> ")
    user_data = {"email": email, "username": username}

    fac = user_factory()
    main(fac)
