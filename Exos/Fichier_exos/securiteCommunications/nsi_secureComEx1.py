def chiffrement_xor(message : str, clef : str) -> str:
    """Renvoie le message chiffré avec la clef en utilisant le xor
        octet par octet.
        La longueur de la clef est supposée au moins aussi grande
        que celle du message.
    """
    # pré-condition
    assert len(clef) >= len(message), "clef trop courte"
    # traitement
    result = ""
    for i in range(len(message)):
        result = result + chr(ord(message[i])^ord(clef[i]))
    return result

def chiffrement_xor_bis(message : str, clef : str) -> str:
    """Renvoie le message chiffré avec la clef en utilisant le xor
        octet par octet.
    """
    # traitement
    result = ""
    for i in range(len(message)):
        result = result + chr(ord(message[i])^ord(clef[i%len(clef)]))
    return result

def chiffrement_xor_ter(message : bytes, clef : bytes) -> bytes:
    """Renvoie le message chiffré avec la clef en utilisant le xor
        octet par octet.
    """
    # traitement en compréhension
    result = [message[i] ^ clef[i%len(clef)] for i in range(len(message))]
    return bytes(result)