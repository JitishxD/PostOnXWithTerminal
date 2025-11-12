import sys


def load_env_variables():
    """
    Load environment variables and validate them.

    Returns:
        tuple: (api_key, api_secret, access_token, access_secret)

    Raises:
        SystemExit: In config.py file required environment variable is not set.
    """

    # Load Environment Variables
    api_key = ""
    api_secret = ""
    access_token = ""
    access_secret = ""

    # Validate environment variables
    missing_vars = []
    if api_key == "":
        missing_vars.append("API_KEY")
    if api_secret == "":
        missing_vars.append("API_SECRET")
    if access_token == "":
        missing_vars.append("ACCESS_TOKEN")
    if access_secret == "":
        missing_vars.append("ACCESS_SECRET")

    if missing_vars:
        print(
            f"❌ Error: Missing required environment variables: {', '.join(missing_vars)}")
        print("Please check your config.py file and ensure all variables are set.")
        input("\nPress ENTER to exit...")
        sys.exit(1)

    return api_key, api_secret, access_token, access_secret
