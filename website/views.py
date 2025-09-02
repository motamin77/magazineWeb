from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from website.forms import contactForm , newsletterForm
from django.contrib import messages

def home_page(request):
    return render(request, 'website/index.html')

def about_page(request):
    return render(request, 'website/about.html')

def contact_page(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
          
        else:
            messages.error(request, 'There was an error in your submission. Please correct the errors below.')
    form = contactForm()                        
    return render(request, 'website/contact.html', {'form': form})
    

def newsletter_page(request):
    if request.method == 'POST':
        form = newsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
        
    
    
# def faq_page(request):
#     return render(request, 'faq.html')

# def portfolio_page(request):
#     return render(request, 'portfolio.html')

# def team_page(request):
#     return render(request, 'team.html')

# def pricing_page(request):
#     return render(request, 'pricing.html')

# def testimonials_page(request):
#     return render(request, 'testimonials.html')

# def blog_overview_page(request):
#     return render(request, 'blog_overview.html')

def test(request):
    return render(request, 'website/test.html', {})

