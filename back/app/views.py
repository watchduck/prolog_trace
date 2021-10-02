from django.http import HttpResponse
import json

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from .utils.text_to_dicts import text_to_dicts
from .utils.table import term_to_table_fancy


def home_view(request):
    html = """This is the backend.<br>
    Nothing happens here, but at <a href="/trace/">/trace/</a>
    and <a href="/tree/">/tree/</a>."""
    return HttpResponse(html)


default_error = 'Something went wrong on the server. Probably the input did not have the expected format.'


@api_view(['POST'])
@permission_classes((AllowAny, ))
def trace_view(request):
    text = request.data['text']
    try:
        data = text_to_dicts(text)
    except ValueError as e:
        data = {'error': e.args[0]}
    except:
        data = {'error': default_error}
    return HttpResponse(json.dumps(data), content_type='application/json')


@api_view(['POST'])
@permission_classes((AllowAny, ))
def tree_view(request):
    text = request.data['text']
    try:
        data = term_to_table_fancy(text)
    except ValueError as e:
        data = {'error': e.args[0]}
    except:
        data = {'error': default_error}
    return HttpResponse(json.dumps(data), content_type='application/json')


