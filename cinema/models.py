from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.title

class Showtime(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    showtime = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} in {self.room.name} at {self.showtime}"

class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    row = models.IntegerField()
    seat_number = models.IntegerField()

    def __str__(self):
        return f"Row {self.row}, Seat {self.seat_number} in {self.room.name}"

class Booking(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking for {self.seat} at {self.showtime}"

