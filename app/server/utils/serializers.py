"""
Entidade responsável para serialização de objetos em JSON para insert em banco de dados
"""


def sa_obj_to_dict(obj):
    """
    Converte qualquer objeto do SQLAlchemy em um dicionário simples.
    Remove metadados internos que causam erro no JSONB.
    """
    if obj is None:
        return None

    # Extrai as colunas e valores
    data = {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

    # Se houver campos de data/uuid, converte para string para evitar erros no JSON
    for key, value in data.items():
        if hasattr(value, "isoformat"):  # Para datetime e date
            data[key] = value.isoformat()
        elif hasattr(value, "hex"):  # Para UUIDs
            data[key] = str(value)

    return data
