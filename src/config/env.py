import os

def get_env(env_name: str, deafult: str):
    if env_name in os.environ:
        return os.environ[env_name]
    return deafult

HOST_DB = get_env("HOST_DB", "localhost")
PORT_DB = get_env("PORT_DB", "3306")
USER_DB = get_env("USER_DB", "root")
PASSWORD_DB = get_env("PASSWORD_DB", "postgres")
DB_NAME = get_env("DB_NAME", "postgres")
APP_PORT = get_env("APP_PORT", "9621")

