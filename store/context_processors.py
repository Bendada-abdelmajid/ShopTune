from shopkeeper.models import pruduct,mainCat, subCat, categorys, Profile
import json
from django.http import JsonResponse
def categories(request):
    categ={}
    

    for x in mainCat.objects.all():
        cats={}
        for s in subCat.objects.filter(main_cat= x):
            catslist=categorys.objects.filter(sub_cat= s)
            vidlist=[]
            for c in catslist:
                vidlist.append({"name": c.name, "id": c.id, "link":  "/products/"+ str(x.slug) + "/" + str(s.slug) +"/"+str(c.slug)})

            cats[s.name]= {"link": "/products/"+ str(x.slug) + "/" + str(s.slug) , "list":vidlist}
        categ[x.name]= {"slug":x.slug, "list":cats}

    
    return {"categories": categ}
       
    
def profile(request):
    profile=Profile.objects.all()[0]
    return {
        'profile': profile,
    }

