import bcrypt



def hash_password(password: str) -> str:
    
    hashed_password =  bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed_password

def encode_to_bytes(plain_password: str):
    plain_bytes = plain_password.encode('utf-8')
    return(plain_bytes)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """function to verify password"""
    encoded_password = encode_to_bytes(plain_password)
    return bcrypt.checkpw(encoded_password, hashed_password)
