from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_password_hash(password:str) -> str:
    """
    Hashes a plain text password input to be stored in the database
    
    Args:
        password (str): Plain text password

    Returns:
        str: Password hash
    """
    return pwd_context.hash(password)

def verify_password(password:str, hash:str) -> bool:
    """Compares a plain text password to the hashed password

    Args:
        password (str): Plain text password
        hash (str): Password hash

    Returns:
        bool: Do values match?
    """
    return pwd_context.verify(password, hash)

