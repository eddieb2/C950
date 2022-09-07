from enum import Enum

# Enum for determining the status of a package
class StatusLocation(Enum):
    HUB = 0
    ENROUTE = 1
    DELIVERED = 2