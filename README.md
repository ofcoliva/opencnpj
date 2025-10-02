# OpenCNPJ

Biblioteca **Python** para integrar de maneira descomplicada com **[OpenCNPJ API](https://opencnpj.org/).**

A base de dados usada está disponível para download no site da receita, mas caso não precise de altos limites de requisição, a solução via api pode atender sua aplicação ou suas validações de CNPJ.

# Documentação OpenCNPJ

Clique aqui para visualizar e tira dúvidas sobre os limites da api **[OpenCNPJ API](https://opencnpj.org/)**.

# Técnologias Usadas

Neste projeto foi usado requisições sincronas, futuramente devo implementar assincronas e outras funcionalidades como limitador de requisições para que não estoure os limites do **opencnpj**

## Como Instalar no seu ambinete de desenvolvimento Python:


```bash
pip install pencnpj  
```

## Como usar

```python
from opencnpj import OpenCNPJ

o = OpenCNPJ()
result = o.find_by_cnpj(cnpj="00.000.000/0001-91")
print(result)

```

### Caso queira algo mais refinado

```python
from opencnpj import OpenCNPJ
from opencnpj.exceptions import *
from time import sleep

if __name__ == "__main__":
    
    cnpj_list = ["00.360.305/0001-04", "00000000000000", "06947492000130"]

    client = OpenCNPJ()

    for cnpj in cnpj_list:
        try:
            empresa = client.find_by_cnpj(cnpj)
            print(f"Sucesso para {cnpj}: {empresa}\n")

        except CNPJNotFoundError:
            print(f"AVISO: O CNPJ {cnpj} não foi encontrado.\n")

        except RateLimitError:
            print("ERRO: Limite de requisições atingido. Pausando por um minuto...\n")
            sleep(60)

        except ServerError:
            print(f"ERRO: A API parece estar com problemas. Pulando o CNPJ {cnpj}.\n")

        except OpenCNPJError as e:
            print(f"Ocorreu um erro inesperado ao processar {cnpj}: {e}\n")
```