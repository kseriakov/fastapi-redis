from enum import Enum


class StreamKey(Enum):
    ORDER_CREATED = 'order_created'
    ORDER_REFUNDED = 'order_refunded'
    
    
class StreamGroup(Enum):
    INVENTORY = 'inventory'
    PAYMENT = 'payment'