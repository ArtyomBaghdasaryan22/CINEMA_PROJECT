import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema_project.settings')
django.setup()

from cinema.models import Room, Seat

def create_seats():
    red_room = Room.objects.get(name='Red Room')
    red_seat_count = 0
    for row in range(1, 11):
        for seat_number in range(1, 9):
            Seat.objects.create(room=red_room, row=row, seat_number=seat_number)
            red_seat_count += 1

    blue_room = Room.objects.get(name='Blue Room')
    blue_seat_count = 0
    for row in range(1, 9):
        for seat_number in range(1, 7):
            Seat.objects.create(room=blue_room, row=row, seat_number=seat_number)
            blue_seat_count += 1

    green_room = Room.objects.get(name='Green Room')
    green_seat_count = 0
    for row in range(1, 13):
        for seat_number in range(1, 11):
            Seat.objects.create(room=green_room, row=row, seat_number=seat_number)
            green_seat_count += 1

    print(f"Created {red_seat_count} seats in Red Room.")
    print(f"Created {blue_seat_count} seats in Blue Room.")
    print(f"Created {green_seat_count} seats in Green Room.")

if __name__ == "__main__":
    create_seats()




