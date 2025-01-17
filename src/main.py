import dotenv
import os
import sys
from hunter import Hunter

def main() -> None:
    # check .env
    if not os.path.exists(".env"):
        print(".env file does not exists!")
        sys.exit(1)
    
    # load .env
    dotenv.load_dotenv()

    # run hunter
    Hunter(username=os.getenv('TARGET_USERNAME'))


if __name__ == "__main__":
    main()