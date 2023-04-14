
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Subscribers

from django.contrib import messages

from shopkeeper.models import Profile, pruduct

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

# Create your views here.
def Subscribe(request):
    content=request.POST.get('subEmail')
    e=False
    for s in Subscribers.objects.all():
        if content == s.email:
            e=True
    if  e:
        message="You have already been registered"
        m_type='error'
    else:
        message="Thank you for subscribing to our newsletters."
        Subscribers.objects.create(email=content)
        m_type='success'
   
    data = {
        'subEmail':content,
        'message':message,
        'type': m_type
        
    }
    return JsonResponse(data, safe=False)



def mail_letter(request):
    profile=Profile.objects.all()[0]
    products=pruduct.objects.all()
    emails = Subscribers.objects.all()
    mail_list= []
    for m in emails:
        mail_list.append(m.email)
    if request.method == 'POST':
        subject='shoptune '+ request.POST.get("subject")
        prods_ids=request.POST.get('prods').split(',')
        prods=[]
        
        for i in prods_ids:
            if i != '':
                if pruduct.objects.filter(id=i).exists():
                    prods.append(pruduct.objects.get(id=i)) 
        p=request.POST.get("p")
        h2=request.POST.get("h2")
     

 
       
  
        html_content = render_to_string('admin_pages/notfication.html', {'SUBJECT':subject,'h2':h2,'p':p,'prods':prods, "profile": profile }) # render with dynamic value
        text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

        # create the email, and attach the HTML version as well.
        try:
            msg = EmailMultiAlternatives(subject, text_content,  profile.email, mail_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, "I've then sent the notification to subscribers successfully")
            return redirect('admin-page')
        except:
            messages.error(request, "There's a problem! Please check your Gmail settings")
    return render(request, "admin_pages/send_notifications.html", {"products": products})





   
    
