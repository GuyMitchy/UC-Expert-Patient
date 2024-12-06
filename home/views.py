from django.views.generic import TemplateView
from django.utils import timezone
from datetime import timedelta
from symptoms.models import Symptom
from medications.models import Medication
from foods.models import Food


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Get data from last 7 days
            week_ago = timezone.now() - timedelta(days=7)

            context['dashboard'] = {
                'recent_symptoms': Symptom.objects.filter(
                    user=self.request.user,
                    date__gte=week_ago
                ).order_by('-date')[:3],

                'active_medications': Medication.objects.filter(
                    user=self.request.user,
                    active=True
                ).order_by('-start_date')[:3],

                'recent_foods': Food.objects.filter(
                    user=self.request.user,
                    date__gte=week_ago
                ).order_by('-date')[:3]
            }
        return context
