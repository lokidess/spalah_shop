from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['greet'] = "Hola"
        context['listed'] = [1, 2, 3, 4, 5, 6]
        context['some_dict'] = {'some': 1, 'test': 2}

        return context
