"""
This file holds a class definiton for a hash validation error, which will be raised when a block that's hash doesnt meet the
proof of work standard set out by the blockchain function (e.g . not starting with "00"), attemptes to be added to the chain.
"""


class Hash_Validation_Error(Exception):
    """Called when an invalid Node (as the Hash does not meet the proof of work standard) is attempting to be added to a blockchain"""
    pass
        
    