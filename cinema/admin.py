from django.contrib import admin
from django import forms
from django.forms import widgets
from .models import Room, Movie, Showtime, Seat, Booking


class ShowtimeAdminForm(forms.ModelForm):
    class Meta:
        model = Showtime
        fields = '__all__'
        widgets = {
            'showtime': widgets.SplitDateTimeWidget(date_attrs={'type':'date'}, time_attrs={'type': 'time'}),
        }

class ShowtimeAdmin(admin.ModelAdmin):
    form = ShowtimeAdminForm

admin.site.register(Room)
admin.site.register(Movie)
admin.site.register(Showtime, ShowtimeAdmin)
admin.site.register(Seat)
admin.site.register(Booking)


