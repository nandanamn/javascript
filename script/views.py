from django.shortcuts import render

# Create your views here.
def script_large1js(request):
        return render(request,'scripts/large1js.html')  

def script_large2js(request):
        return render(request,'scripts/large2js.html') 

def script_palindrome(request):
        return render(request,'scripts/palindrome.html')  
 
def script_element1(request):
        return render(request,'scripts/element1.html')

def script_element2(request):
        return render(request,'scripts/element2.html')  

