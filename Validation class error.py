class Error():
    pass

class Hash_Validation_Error(Error):
    """Called when an invalid Node (as the Hash does not meet the proof of work standard) is attempting to be added to a blockchain"""