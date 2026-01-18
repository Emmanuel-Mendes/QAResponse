import re


def validate_email(email: str) -> bool:
    """
    Args:
        email (str): Valor referente ao email do usuário

    Returns:
        Booleano: Valor do tipo booleano da validação do email, se o email estiver vazio ou com inválido, ser retornado False, caso o email contrário, será retornado True
    """
    pattern = r"^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$"

    if email and (re.match(pattern=pattern, string=email)):
        return True
    else:
        return False
