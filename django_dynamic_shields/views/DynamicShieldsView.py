from django.views import View
from django.http import JsonResponse
from django_dynamic_shields.data import ShieldsData


class DynamicShieldsView(View):
    shields_data: ShieldsData

    def create_shields_data(self):
        pass

    def get(self):
        create_shields_data()
        return JsonResponse(self.shields_data.dict)
