import re
import base58
from rest_framework.exceptions import ValidationError, ErrorDetail


def get_and_validate_hash(request):
    '''
    Extracts and validates the hash and blockchain from the request.
    '''
    hash = request.data.get('hash', None)
    blockchain = request.data.get('blockchain', None)

    if not hash or not blockchain:
        raise ValidationError('Hash and blockchain are required objects')

    if validate_hash(hash, blockchain):
        return hash, blockchain
    else:
        raise ValidationError('Hash is not correct')

def validate_hash(tx_hash, blockchain):
    '''
    Validates the transaction hash against the specified blockchain.
    '''
    validators = {
        "bitcoin": is_valid_bitcoin_hash,
        "ethereum": is_valid_eth_hash,
        "tron": is_valid_eth_hash,
        "polygon": is_valid_eth_hash,
        "solana": is_valid_solana_hash,
        "ton": is_valid_ton_hash,
    }
    validator = validators.get(blockchain.lower())
    if validator:
        return validator(tx_hash)
    return False

def is_valid_bitcoin_hash(tx_hash):
    return bool(re.fullmatch(r"[0-9a-f]{64}", tx_hash))

def is_valid_eth_hash(tx_hash):
    return bool(re.fullmatch(r"[0-9a-f]{64}", tx_hash))

def is_valid_solana_hash(tx_hash):
    try:
        decoded = base58.b58decode(tx_hash)
        return 43 <= len(decoded) <= 88
    except ValueError:
        return False

def is_valid_ton_hash(tx_hash):
    if re.fullmatch(r"[0-9a-f]{64}", tx_hash):
        return True
    if re.fullmatch(r"[0-9a-zA-Z+/]{43}={0,2}", tx_hash):
        return True
    return False
