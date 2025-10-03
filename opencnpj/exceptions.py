class OpenCNPJError(Exception):
    """Exceção base para erros da biblioteca OpenCNPJ."""
    pass

class CNPJNotFoundError(OpenCNPJError):
    """Disparado quando um CNPJ não é encontrado na base de dados."""
    pass

class RateLimitError(OpenCNPJError):
    """Disparado quando o limite de requisições da API é atingido."""
    pass

class ServerError(OpenCNPJError):
    """Disparado quando ocorre um erro interno no servidor da API."""
    pass

class NetworkError(OpenCNPJError):
    """Disparado quando há falha de conexão ou rede."""
    pass

class TimeoutError(OpenCNPJError):
    """Disparado quando a requisição excede o tempo limite de resposta."""
    pass

class RequestError(OpenCNPJError):
    """Disparado quando ocorre um erro de requisição HTTP (ex: 400, 401, 403, 422)."""
    pass