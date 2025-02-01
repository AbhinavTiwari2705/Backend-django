from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faq_list_{lang}'
        cached_data = cache.get(cache_key)

        if cached_data is None:
            response = super().list(request, *args, **kwargs)
            cache.set(cache_key, response.data, timeout=3600)  # Cache for 1 hour
            return response

        return Response(cached_data)

