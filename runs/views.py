from django.views import generic

from .models import Run


class IndexView(generic.ListView):
    template_name = 'runs/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Run.objects.order_by('-start')[:5]
