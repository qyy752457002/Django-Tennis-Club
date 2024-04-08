from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

# Create your views here.
def members(request):
    # load template from templates folder
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())

    # Get all the records and fields of the Member model
    mymembers = Member.objects.all().values() 

    print("here")
    # load template from templates folder
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

# Gets the slug as an argument
def details(request, slug):
    # Uses the slug to locate the correct record in the Member table
    mymember = Member.objects.get(slug=slug)
    # Loads the details.html template
    template = loader.get_template('details.html')
    # Creates an object containing the member.
    context = {
        'mymember': mymember,
    }
    # Sends the object to the template.
    # Outputs the HTML that is rendered by the template.
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    # Get all the records and fields of the Member model
    # mymembers = Member.objects.all().values()

    # Return only the records where firstname is 'Emil'
    # mydata = Member.objects.filter(firstname='Emil').values()

    # 获取 templates 中的 template.html
    template = loader.get_template('template.html')
    
    # context = {
    #     'mymembers' : mydata,
    # }

    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    
    return HttpResponse(template.render(context, request))  
