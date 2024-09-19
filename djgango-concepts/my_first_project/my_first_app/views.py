from django.shortcuts import render

def my_view(request):
  car_list = [
    {"marca":"BMW"},
    {"marca":"chevrolet"},
]
  context = {
    "car_list":car_list
  }
  return  render(request,"my_first_app/car_list.html",context)
