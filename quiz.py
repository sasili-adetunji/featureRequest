from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb6gOJV6d4z5WttyazIx3PCY5mbEJASdc-CdUgQ9UttK6WDio1uTxb_h6VlpZc0cNO7kn5k67LLHHVuS6HKkmsChMV_ukabFO9OU0ePY0HCeigtDYxn8RJnyD0ta8WEqFoW577Zw0y0Uvbf8ZaWCS3sShryWJVizIqEBu3saFi2kocrd5jjnqQ9-CZb05SwGrgEnWP'


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
