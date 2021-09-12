from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, \
    cache_control, never_cache
from django.views.decorators.vary import vary_on_headers
from django.core.cache import cache
import datetime
import json
from messaging.models import Publisher

from django.http import HttpResponse


class PublisherListView(ListView):
    model = Publisher
    # template_name = 'publisher_list.html'
    context_object_name = 'publisher_list_data'

    @method_decorator(never_cache)
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cached_publishers = cache.get('publishers')
        if cached_publishers is None:
            publishers = Publisher.objects.all()
            cache.set('publishers', publishers)

        # Add in a QuerySet of all the books
        context['publisher_list'] = cached_publishers
        return context


# Create your views here.
@cache_control(max_age=400, private=True)
@vary_on_headers('user-agent')
@cache_page(40 * 7, cache='default')
async def home(request):
    now = datetime.datetime.now()
    cache.set('key', 'Initial Value')
    html = '<html><body>It is now %s.</body><html>' % now
    return HttpResponse(html)


async def list_products(request):
    items = [('name', 'keyboard'), ('size', '12x4'), ('rate', '2.5')]
    products = dict(items)
    cache_products = lambda d: cache.set('products', d)
    data = cache.get('products', cache_products(products))
    return HttpResponse(json.dumps(data), content_type='application/json')
