from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.views import View
from django.shortcuts import render
from django import forms
from django.urls import path
import string
import random

# Create your views here.

# Use a dictionary to store the mapping instead of a database
url_mapping = {}

# Define a form for URL input
class UrlForm(forms.Form):
    original_url = forms.URLField(label='Enter the URL to shorten')

# Define a view for creating shortened URL
class CreateShortUrlView(View):
    def get(self, request):
        form = UrlForm()
        return render(request, 'url_form.html', {'form': form})
    
    def post(self, request):
        form = UrlForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            # Generate a unique short key
            while True:
                short_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
                if short_key not in url_mapping:
                    break
            # Save the original URL with the generated short key
            url_mapping[short_key] = original_url
            shortened_url = request.build_absolute_uri('/myapp/' + short_key)
            # Return the shortened URL to the user
            return JsonResponse({'shortened_url': shortened_url})
        return render(request, 'url_form.html', {'form': form})

# Define a view for redirecting to the original URL
class RedirectView(View):
    def get(self, request, short_key):
        original_url = url_mapping.get(short_key)
        if original_url:
            return HttpResponseRedirect(original_url)
        return HttpResponseNotFound('Shortened URL does not exist')
