# OpenCNPJ

Biblioteca **Python** para integrar facilmente com a **[OpenCNPJ API](https://opencnpj.org/)**.

A base de dados usada está disponível para download no site da Receita Federal, mas para aplicações que não exigem altos limites de requisição, a solução via API pode ser suficiente para validações e consultas de CNPJ.

---

## Documentação da API

Consulte a documentação oficial para detalhes de uso e limites:  
**[OpenCNPJ API](https://opencnpj.org/)**

---

## Tecnologias Utilizadas

- Python 3.8+
- [requests](https://pypi.org/project/requests/)
- [pydantic](https://pydantic.dev/)
- [pip_system_certs](https://pypi.org/project/pip-system-certs/) (opcional, para ambientes corporativos)

Atualmente, as requisições são síncronas. Futuramente, poderão ser adicionadas funcionalidades assíncronas e limitador de requisições.

---

## Instalação

```bash
pip install opencnpj
```

---

## Uso Básico

```python
from opencnpj import OpenCNPJ

client = OpenCNPJ()
empresa = client.find_by_cnpj("00.000.000/0001-91")
print(empresa.razao_social)
```

---

## Exemplo Completo com Tratamento de Erros

```python
from opencnpj import OpenCNPJ
from opencnpj.exceptions import (
    CNPJNotFoundError,
    RateLimitError,
    ServerError,
    NetworkError,
    TimeoutError,
    RequestError,
    OpenCNPJError,
)
from time import sleep

if __name__ == "__main__":
    cnpj_list = [
        "00.360.305/0001-04",  # válido
        "00000000000000",      # inválido
        "06947492000130",      # válido ou pode não existir
        "12.345.678/0001-99",  # provavelmente inexistente
    ]

    client = OpenCNPJ()

    for cnpj in cnpj_list:
        try:
            empresa = client.find_by_cnpj(cnpj)
            print(f"Sucesso para {cnpj}: {empresa.razao_social}\n")

        except CNPJNotFoundError:
            print(f"AVISO: O CNPJ {cnpj} não foi encontrado ou não existe.\n")

        except RateLimitError:
            print("ERRO: Limite de requisições atingido. Pausando por um minuto...\n")
            sleep(60)

        except ServerError:
            print(f"ERRO: A API parece estar com problemas. Pulando o CNPJ {cnpj}.\n")

        except NetworkError:
            print(f"ERRO: Falha de conexão ao consultar {cnpj}.\n")

        except TimeoutError:
            print(f"ERRO: Timeout ao consultar {cnpj}.\n")

        except RequestError as e:
            print(f"ERRO: Erro de requisição ao consultar {cnpj}: {e}\n")

        except OpenCNPJError as e:
            print(f"ERRO: Erro inesperado do OpenCNPJ ao consultar {cnpj}: {e}\n")

        except Exception as e:
            print(f"ERRO: Exceção não tratada ao consultar {cnpj}: {type(e).__name__}: {e}\n")
```

---

## Retorno Esperado

```bash
Sucesso para 00.360.305/0001-04: CAIXA ECONOMICA FEDERAL
AVISO: O CNPJ 00000000000000 não foi encontrado ou não existe.
...
```

---

## Acessando os Campos do Objeto Empresa

O objeto retornado (`empresa`) possui todos os campos do cadastro do CNPJ.  
Você pode listar os campos disponíveis assim:

```python
print(empresa.campos)  # Lista os nomes dos campos disponíveis
```

Ou acessar diretamente:

```python
print(empresa.razao_social)
print(empresa.cnpj)
```

---

## Contribuição

Pull requests são bem-vindos! Para maiores informações, acesse o [repositório no GitHub](https://github.com/ofcoliva/opencnpj).

---

## Licença

[MIT License](LICENSE)