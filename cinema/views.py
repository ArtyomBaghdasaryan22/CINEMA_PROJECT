from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Showtime, Seat, Booking

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def movie_list(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    showtimes = Showtime.objects.filter(room=room)
    return render(request, 'movie_list.html', {'room': room, 'showtimes': showtimes})

def seat_list(request, showtime_id):
    showtime = get_object_or_404(Showtime, id=showtime_id)
    seats = Seat.objects.filter(room=showtime.room)
    bookings = Booking.objects.filter(showtime=showtime)
    booked_seats = [booking.seat.id for booking in bookings]

    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = get_object_or_404(Seat, id=seat_id)

        if seat.id in booked_seats:
            return render(request, 'booking_error.html', {'error_message': 'This seat is already booked.'})
        else:
            Booking.objects.create(showtime=showtime, seat=seat, booked=True)
            return redirect('seat_list', showtime_id=showtime.id)

    return render(request, 'seat_list.html', {
        'showtime': showtime,
        'seats': seats,
        'booked_seats': booked_seats,
    })
    



