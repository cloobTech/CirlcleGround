from decimal import Decimal
from datetime import datetime




def calculate_booking_price(price_per_hour: Decimal, start_time: datetime, end_time: datetime) -> Decimal:
    if end_time <= start_time:
        raise ValueError("End time must be after start time")
    
    duration_hours = Decimal((end_time - start_time).total_seconds()) / Decimal(3600)
    return (price_per_hour * duration_hours).quantize(Decimal("0.01"))