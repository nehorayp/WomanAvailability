class NoBitchesException(Exception):
    """This class is used to raise custom exceptions when no bitches are found."""
    def __init__(self, message : str) -> None:
        self.message = message
        super().__init__(self.message)
    
