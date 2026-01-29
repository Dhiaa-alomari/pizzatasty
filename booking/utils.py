from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Table, Booking

def find_available_table(date, time, guests, user, tzname):
    #  embed the date and time into a single datetime object
    selected_datetime = datetime.combine(date, time)
    
    #  determine the time range for checking existing bookings
    start_range = selected_datetime - timedelta(minutes=59)
    end_range = selected_datetime + timedelta(minutes=59)

    # check if the user has already booked a table within this time range
    # we use the filter on date and time together
    already_booked = Booking.objects.filter(
        user=user,
        date=date,
        time__range=(start_range.time(), end_range.time())
    ).exists()

    if already_booked:
        return None

    suitable_tables = Table.objects.filter(capacity__gte=guests)

    booked_tables = Booking.objects.filter(
        date=date,
        time=time
    ).values_list('table_id', flat=True)

    available_table = suitable_tables.exclude(id__in=booked_tables).first()

    return available_table