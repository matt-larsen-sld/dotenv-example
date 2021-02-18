import os
from dotenv import load_dotenv

load_dotenv()

DOT_ENV_SECRET = os.getenv("DEV_VARIABLE")
PATH_ENV_VAR = os.getenv("PATH")


def main():
    print(f".env Secret: '{DOT_ENV_SECRET}'")
    print(f"OS Path variable: '{PATH_ENV_VAR}'")


if __name__ == "__main__":
    main()
