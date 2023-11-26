from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSetting(BaseSettings):
    """Модель настроек для подключения к БД в контейнере"""
    NAME: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int

    model_config = SettingsConfigDict(env_file='.env.db')


class SMTPSetting(BaseSettings):
    """Модель настроек SMTP-клиента"""
    EMAIL_HOST: str
    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str
    EMAIL_PORT: int
    EMAIL_USE_TLS: bool
    EMAIL_USE_SSL: bool

    model_config = SettingsConfigDict(env_file='.env.smtp')


db_setting = DBSetting()
smtp_setting = SMTPSetting()
