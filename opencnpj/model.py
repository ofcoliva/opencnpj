from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import date

class Telefone(BaseModel):
    """
    Representa um telefone de contato da empresa.
    """
    ddd: str
    numero: str
    is_fax: bool = False

class Socio(BaseModel):
    """
    Representa um sócio ou administrador no Quadro de Sócios e Administradores (QSA).
    """
    nome_socio: str = Field(..., alias='nome_socio')
    cnpj_cpf_socio: str = Field(..., alias='cnpj_cpf_socio')
    qualificacao_socio: str = Field(..., alias='qualificacao_socio')
    data_entrada_sociedade: date = Field(..., alias='data_entrada_sociedade')
    identificador_socio: str = Field(..., alias='identificador_socio')
    faixa_etaria: str = Field(..., alias='faixa_etaria')

class CNPJ(BaseModel):
    """
    Modelo principal que representa os dados cadastrais de uma empresa (CNPJ).
    """
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str] = None
    situacao_cadastral: str
    data_situacao_cadastral: date
    matriz_filial: str
    data_inicio_atividade: date
    cnae_principal: str
    cnaes_secundarios: List[str]
    natureza_juridica: str
    logradouro: str
    numero: str
    complemento: Optional[str] = None
    bairro: str
    cep: str
    uf: str
    municipio: str
    email: Optional[str] = None
    telefones: List[Telefone]
    capital_social: str  # Mantido como string devido ao formato "120000000000,00"
    porte_empresa: str
    opcao_simples: str
    data_opcao_simples: Optional[date] = None
    opcao_mei: str
    data_opcao_mei: Optional[date] = None
    qsa: List[Socio] = Field(..., alias='QSA')

    @field_validator('data_opcao_mei', mode='before')
    @classmethod
    def handle_invalid_dates(cls, valor_recebido):
        if isinstance(valor_recebido, str) and valor_recebido in ('0000-00-00', '0'):
            return None
        
        return valor_recebido