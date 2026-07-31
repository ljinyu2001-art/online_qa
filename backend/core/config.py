from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # MySQL
    MYSQL_HOST: str = "192.168.110.118"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "123456"
    MYSQL_DATABASE: str = "online_qa"


    # Redis
    REDIS_HOST: str = "192.168.110.118"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = "123456"
    REDIS_DB: int = 0


    class Config:
        env_file = None



settings = Settings()