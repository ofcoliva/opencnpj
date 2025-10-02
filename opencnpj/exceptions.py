

class OpenCNPJError(Exception):
    """Classe base para todas as exceções da biblioteca OpenCNPJ."""
    pass


# --- Erros relacionados a requisições HTTP e Rede ---

class RequestError(OpenCNPJError):
    """Classe base para erros relacionados a requisições à API."""
    pass


class NetworkError(RequestError):
    """Disparado quando ocorrem problemas de rede (ex: DNS, conexão recusada)."""
    pass


class TimeoutError(RequestError):
    """Disparado quando uma requisição excede o tempo limite de espera."""
    pass


# --- Erros baseados no status code HTTP ---

class ClientError(RequestError):
    """Disparado para erros do lado do cliente (status code 4xx)."""
    pass


class NotFoundError(ClientError):
    """Disparado quando um recurso não é encontrado (status code 404)."""
    pass


class CNPJNotFoundError(NotFoundError):
    """
    Disparado especificamente quando um CNPJ não é encontrado.
    Herda de NotFoundError para permitir captura mais genérica.
    """
    pass


class RateLimitError(ClientError):
    """Disparado quando o limite de requisições é atingido (status code 429)."""
    pass


class ServerError(RequestError):
    """Disparado para erros do lado do servidor da API (status code 5xx)."""
    pass
