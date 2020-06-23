from django.db import models
from django.utils import timezone


class CoronaVirusTest(models.Model):
	name = models.CharField(max_length=250)
	phone = models.CharField(max_length=12)
	#patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
	cough = models.IntegerField(blank=True, null=True)
	cold = models.IntegerField(blank=True, null=True)
	diarrhea = models.IntegerField(blank=True, null=True)
	sore_throat = models.IntegerField(blank=True, null=True)
	body_aches = models.IntegerField(blank=True, null=True)
	headaches = models.IntegerField(blank=True, null=True)
	fever = models.IntegerField(blank=True, null=True)
	difficulty_breathing = models.IntegerField(blank=True, null=True)
	fatigue = models.IntegerField(blank=True, null=True)
	travelled_14days_ago = models.IntegerField(blank=True, null=True)
	travel_history_to_infected_area = models.IntegerField(blank=True, null=True)
	contact_with_infected = models.IntegerField(blank=True, null=True)
	result = models.IntegerField(blank=True, null=True)
	pub_date = models.DateTimeField(default=timezone.now)



	def __str__(self):
		return self.name
	
	
