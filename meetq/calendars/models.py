from django.db import models
from django.contrib.auth.models import User

# Calendar model
class Calendar(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                                null=True, related_name="calendars")
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    # responses (many Responses) 
    # invited (many Contacts) - to check if someone was invited, use Invited model
    color = models.CharField(max_length=7)
    duration = models.IntegerField()
    owners_available = models.CharField(null=False, blank=False)
    owners_preferred = models.CharField(null=False, blank=False)
    deadline = models.DateField()

# Contact model
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                                null=True, related_name="calendars")
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=True, blank=True)

# Invited model
class Invited(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.set_NULL,
                                    null=True, related_name="response")
    calendar = models.ForeignKey(Calendar, on_delete=models.set_NULL,
                                    null=True, related_name="response")
    
    # ensures (calendar and contact) pair is unique
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['calendar', 'contact'], name='unique_migration_host_combination'
            )
        ]

# Response model
class Response(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.set_NULL,
                                    null=True, related_name="response")
    contact = models.ForeignKey(Contact, on_delete=models.set_NULL,
                                    null=True, related_name="response")
    available = models.ArrayField(models.CharField(max_length=255))
    preferred = models.ArrayField(models.CharField(max_length=255))

    # ensures (calendar and contact) pair is unique
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['calendar', 'contact'], name='unique_migration_host_combination'
            )
        ]

class Schedule(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                                null=True, related_name="meeting")
    week = models.DateField(null=False, blank=False)

class Meeting(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                                null=True, related_name="meeting")
    contact = models.ForeignKey(Contact, on_delete=models.set_NULL,
                                    null=True, related_name="response")
    time_slot = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    # schedule this meeting is in
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL,
                                    null=True, related_name="meeting")

class SchedulePlan(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                                null=True, related_name="meeting")
    this_week = models.ForeignKey(Schedule, on_delete=models.set_NULL,
                                    null=True, related_name="response")
    next_week = models.ForeignKey(Schedule, on_delete=models.set_NULL,
                                    null=True, related_name="response")
    
