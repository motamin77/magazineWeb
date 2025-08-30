from django.shortcuts import render

def home_page(request):
    return render(request, 'website/index.html')

def about_page(request):
    return render(request, 'website/about.html')

def contact_page(request):
    return render(request, 'website/contact.html')

# def services_page(request):
#     return render(request, 'services.html')

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

