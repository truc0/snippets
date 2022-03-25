from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from .models import Snippet
from .models import LANGUAGE_CHOICES


def index(request):
    if request.method == 'POST':
        errors = []
        try:
            code = request.POST.get('code')
            language = request.POST.get('language')
            # check language
            if code == '':
                errors.append('code should not be empty')
            if language not in (item[0] for item in LANGUAGE_CHOICES):
                errors.append('unsupport language')
            # check if language exists
            if len(errors) != 0:
                return render(request, 'index.html', context={
                    'errors': errors,
                    'languages': LANGUAGE_CHOICES
                })
            # create model
            snippet = Snippet.objects.create(code=code, language=language)
            return redirect(reverse('detail', args=[snippet.id]))
        except:
            errors.append('Please make sure code and language is provided')
            return render(request, 'index.html', context={
                'errors': errors,
                'languages': LANGUAGE_CHOICES
            }, status=400)
    else:
        context = {
            'languages': LANGUAGE_CHOICES
        }
        return render(request, 'index.html', context=context)


def detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    lexer = get_lexer_by_name(snippet.language, stripall=True)
    formatter = HtmlFormatter(cssclass='highlight w-full px-2 py-2 overflow-auto')
    html = highlight(snippet.code, lexer, formatter)
    css = formatter.get_style_defs('.highlight')
    context = {
        'snippet': snippet,
        'highlighted': html,
        'styles': css,
        'link': request.build_absolute_uri(
            reverse('detail', args=[snippet.id])
        )
    }
    return render(request, 'detail.html', context=context)


def raw(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return snippet.code
    
