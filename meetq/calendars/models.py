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
    # responses (many Responses) - check responses model
    # invited (many Contacts) - to check if someone was invited, use Invited model
    color = models.CharField(max_length=7)
    duration = models.IntegerField()
    owners_available = models.CharField(max_length=200, null=False, blank=False)
    owners_preferred = models.CharField(max_length=200, null=False, blank=False)
    deadline = models.DateField()

# Contact model
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                                null=True, related_name="contact")
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=True, blank=True)

# # Invited model
# class Invited(models.Model):
#     contact = models.ForeignKey(Contact, on_delete=models.SET_NULL,
#                                     null=True, related_name="invited")
#     calendar = models.ForeignKey(Calendar, on_delete=models.SET_NULL,
#                                     null=True, related_name="invited")
    
#     # ensures (calendar and contact) pair is unique
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['calendar', 'contact'], name='unique_migration_host_combination'
#             )
#         ]

# Response model
class Response(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.SET_NULL,
                                    null=True, related_name="response")
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL,
                                    null=True, related_name="response")
    responded = models.BooleanField(default=False)
    available = models.JSONField()
    preferred = models.JSONField()

    # ensures (calendar and contact) pair is unique
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['calendar', 'contact'], name='unique_migration_host_combination'
            )
        ]

class Schedule(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                                null=True, related_name="schedule")
    week = models.DateField(null=False, blank=False)

class Meeting(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                                null=True, related_name="meeting")
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL,
                                    null=True, related_name="meeting")
    time_slot = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    # schedule this meeting is in
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL,
                                    null=True, related_name="meeting")

class SchedulePlan(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                                null=True, related_name="scheduleplan")
    this_week = models.ForeignKey(Schedule, on_delete=models.SET_NULL,
                                    null=True, related_name="scheduleplanthisweek")
    next_week = models.ForeignKey(Schedule, on_delete=models.SET_NULL,
                                    null=True, related_name="scheduleplannextweek")
    
