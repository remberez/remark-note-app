from fastapi_users.authentication import BearerTransport

# TODO: Изменить ссылку
bearer_transport = BearerTransport(
    tokenUrl="auth/jwt/login",
)
