from el_pagination.views import AjaxListView
from django.db.models import Q

from mainapp.models import CarMaker


class CarMakerListView(AjaxListView):
    template_name = 'mainapp/index.html'
    page_template = 'mainapp/page.html'

    context_object_name = 'makers'

    def get_queryset(self):

        request = self.request
        key = 'pattern'
        pattern_key = request.GET.get(key, request.POST.get(key))

        if request.is_ajax() and pattern_key:
            return CarMaker.objects.filter(Q(make_id__startswith=pattern_key) |
                                           Q(make_display__startswith=pattern_key) |
                                           Q(make_country__startswith=pattern_key))
        return CarMaker.objects.all()

    def get_context_data(self, **kwargs):
        my_context = super(CarMakerListView, self).get_context_data(**kwargs)
        my_context['title'] = 'Testing Django'

        return my_context
