from dotenv import load_dotenv
import os

class Config:
    @classmethod
    def load_config(cls, env_path = ".env"):
        print(os.path.abspath(env_path))
        load_dotenv(env_path)

    @classmethod
    def get(cls, key, default = None):
        return os.getenv(key, default)