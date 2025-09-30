# OpenCNPJ

Biblioteca **Python** para integrar de maneira descomplicada com **[OpenCNPJ API](https://opencnpj.org/).**

A base de dados usada está disponível para download no site da receita, mas caso não precise de altos limites de requisição, a solução via api pode atender sua aplicação ou suas validações de CNPJ.

# Documentação OpenCNPJ

Clique aqui para visualizar e tira dúvidas sobre os limites da api **[OpenCNPJ API](https://opencnpj.org/)**.

# Técnologias Usadas

Neste projeto foi usado requisições sincronas, futuramente devo implementar assincronas e outras funcionalidades como limitador de requisições para que não estoure os limites do **opencnpj**

## Como Instalar no seu ambinete de desenvolvimento Python:

```
pip install opencnpj
```

## Como usar

```
from opencnpj import OpenCNPJ

o = OpenCNPJ()
result = o.find_by_cnpj(cnpj="00.000.000/0001-91")
print(result)

```
