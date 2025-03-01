#Hay que añadir logica para que se conecte a postgre y use sqlite solo si no hay postgres
#hay que añadir aqui las variables de entorno en class settings
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    debug: bool = False
    db_type: str | None = "sqlite"

    class Config:
        env_file = ".env"

config = Config()