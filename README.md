Full details available on the [project details page](https://pypi.org/project/python-dotenv/)

`pip install python-dotenv`

Put a `.env` file in your project.  This file is read by `load_dotenv()`.  

Adjust the arguments to `load_dotenv()` for the path to your `.env` file if it's not in the same directory as the 
module calling `load_dotenv()`

Put your variables inside the `.env` file

```
MY_SECRET=somethingSecret
```

make sure the `.env` is excluded from source control. 

[template](https://github.com/github/gitignore/blob/master/Python.gitignore)

`.gitignore`:

```
.env
__pycache__/
build/
...
```

Read in variables from the `.env` or environment variables:

```python
import os
from dotenv import load_dotenv

load_dotenv()

DOT_ENV_SECRET = os.getenv("MY_SECRET")
PATH_ENV_VAR = os.getenv("PATH")


def main():
    print(f".env Secret: '{DOT_ENV_SECRET}'")
    print(f"OS Path variable: '{PATH_ENV_VAR}'")


if __name__ == "__main__":
    main()

```

