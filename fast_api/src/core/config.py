import os
from pydantic import BaseSettings, BaseModel
from dotenv import load_dotenv

IS_DOCKER = os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False)

if not IS_DOCKER:
    load_dotenv()   # take environment variables from .env.


class JWTSettings(BaseModel):
    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM')


class KafkaPromSettings(BaseModel):
    KAFKA_HOST: str = os.getenv('KAFKA_HOST')
    KAFKA_PORT: str = os.getenv('KAFKA_PORT')


class KafkaDevSettings(BaseModel):
    KAFKA_HOST: str = os.getenv('KAFKA_HOST_DEBUG')
    KAFKA_PORT: str = os.getenv('KAFKA_PORT_DEBUG')


class Settings(BaseSettings):

    PROJECT_NAME: str = os.getenv('PROJECT_NAME')

    TOPIC: str = os.getenv('TOPIC')

    jwt_settings: JWTSettings = JWTSettings()

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'


class PromSettings(Settings):
    kafka_settings: KafkaPromSettings = KafkaPromSettings()


class DevSettings(Settings):
    kafka_settings: KafkaDevSettings = KafkaDevSettings()


def get_settings():
    environment = os.getenv('ENVIRONMENT')
    if environment == 'prom':
        return PromSettings()
    else:
        return DevSettings()


settings = get_settings()
