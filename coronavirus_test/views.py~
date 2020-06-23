from django.shortcuts import render
from .models import CoronaVirusTest
#from blog.models import Post
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Create your views here.
		
def CoronaVirusTestView(request):
	if request.method == "POST":
		name = request.POST.get("name")
		phone = request.POST.get("phone")
		cough = request.POST.get("cough")
		cold = request.POST.get("cold")
		diarrhea = request.POST.get("diarrhea")
		sore_throat = request.POST.get("sore_throat")
		body_aches = request.POST.get("body_aches")
		headaches = request.POST.get("headaches")
		fever = request.POST.get("fever")
		difficulty_breathing = request.POST.get("difficulty_breathing")
		fatigue = request.POST.get("fatigue")
		travelled_14days_ago = request.POST.get("travelled_14days_ago")
		travel_history_to_infected_area = request.POST.get("travel_history_to_infected_area")
		contact_with_infected = request.POST.get("contact_with_infected")
		pub_date = timezone.now()
		
		result_a = int(cough) + int(cold) + int(diarrhea)  + int(body_aches) + int(headaches) + int(fever) + int(difficulty_breathing) +int(fatigue) + int(travelled_14days_ago) + int(travel_history_to_infected_area) + int(contact_with_infected)
		result = result_a / 2.75
		precautions = []
		if 2*2.75 >= result < 5*2.75:
			info = "You are just fine!, your symthoms may be stress related."
			precautions.append("With children, keep calm, carry on and get the flu shot.")
			precautions.append("Don’t stockpile masks. ")
			precautions.append("But do stock up on medicine and resources.")
			precautions.append("Avoid eating raw or undercooked meat or animal organs.")
			precautions.append("If you're visiting live markets in areas that have recently had new coronavirus cases, avoid contact with live animals and surfaces they may have touched.")
			precautions.append("Keep up with the vitamin C")
			precautions.append("Avoid touching your eyes, nose and mouth if your hands aren't clean.")
			precautions.append("Wash your hands often with soap and water for at least 20 seconds, or use an alcohol-based hand sanitizer that contains at least 60% alcohol.")
			precautions.append("Stay home if you can.")
			precautions.append("Eat more fruits")
			precautions.append("Always use face mask and hand gloves if you must go out.")
			precautions.append("Wash your hands. With soap. Then wash them again. ")
			precautions.append("Stay informed by visiting blogsmond.com")
			precautions.append("If you find any one around your vacinity that may have the virus please contact medical help or call NCDC on 08009700000010")
			
		elif 5*2.75 >= result < 12*2.75:
			info = "You are not too well!, but you do not have the corona virus, your symthoms may be stress related."
			precautions.append("Stay home if you can.")
			precautions.append("Eat more fruits")
			precautions.append("Always use face mask and hand gloves if you must go out.")
			precautions.append("Wash your hands. With soap. Then wash them again. ")
			precautions.append("Stay informed by visiting blogsmond.com")
			precautions.append("With children, keep calm, carry on and get the flu shot.")
			precautions.append("Don’t stockpile masks. ")
			precautions.append("But do stock up on medicine and resources.")
			precautions.append("Avoid eating raw or undercooked meat or animal organs.")
			precautions.append("If you're visiting live markets in areas that have recently had new coronavirus cases, avoid contact with live animals and surfaces they may have touched.")
			precautions.append("Keep up with the vitamin C")
			precautions.append("Avoid touching your eyes, nose and mouth if your hands aren't clean.")
			precautions.append("Wash your hands often with soap and water for at least 20 seconds, or use an alcohol-based hand sanitizer that contains at least 60% alcohol.")
			precautions.append("If you find any one around your vacinity that may have the virus please contact medical help or call NCDC on 08009700000010")
			#0-5 5-10 10-15 15-20
		elif 12*2.75 >= result < 24*2.75:
			info = "Unfortunately, there is a sllight chance that you may have contracted the corona virus."
			precautions.append("Contact medical help call NCDC on 08009700000010")
			precautions.append("Please stay isolated and not touch things others may touch")
			precautions.append("Please stay indoor and stay updated by visiting blogsmond.com")
			precautions.append("If you find any one around your vacinity that may have the virus please contact medical help call NCDC on 08009700000010")
			precautions.append("Contact medical help call NCDC on 08009700000010")
			
		#elif result >= 24*2.75:
		else:
			info = "Unfortunately, you may have the corona virus."
			precautions.append("Contact medical help call NCDC on 08009700000010")
			precautions.append("Please stay isolated and not touch things others may touch")
			precautions.append("Please stay indoor and stay updated by visiting blogsmond.com")
			precautions.append("If you find any one around your vacinity that may have the virus please contact medical help call NCDC on 08009700000010")
			precautions.append("Contact medical help call NCDC on 08009700000010")
			
		
		#all_posts = Post.objects.order_by("-pub_date")[:16]
		result = int((result / 36) * 100)
		context = {"result": result, "info": info, "precautions": precautions, "name": name}
			
		coronavirustest = CoronaVirusTest.objects.create(name=name, phone=phone, result=result, cough=cough, cold=cold, diarrhea=diarrhea, sore_throat =sore_throat , body_aches=body_aches, headaches=headaches, fever=fever, difficulty_breathing=difficulty_breathing, fatigue=fatigue, travelled_14days_ago=travelled_14days_ago,  contact_with_infected=contact_with_infected, travel_history_to_infected_area=travel_history_to_infected_area, pub_date=pub_date)
		coronavirustest.save()
		
		
		return render(request, 'coronavirus_test/test_result.html', context)
		
	else:
		return render(request, 'coronavirus_test/coronavirus_test.html')
		
		

		
		
		
		
		
		
		
		
