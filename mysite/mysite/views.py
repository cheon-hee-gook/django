from typing import Any
from django.views.generic.base import TemplateView

# -- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['app_list'] = ['polls', 'books']
        return context