from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from utils.utils import generate_random_token

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    id = models.CharField(primary_key=True, default=generate_random_token, editable=False, max_length=20)
    code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='text', max_length=100)

    class Meta:
        ordering = ['created']
