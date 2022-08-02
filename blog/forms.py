from django.forms import ModelForm
from.models import post,comment

class renew(ModelForm):
    class Meta:
        model=post
        fields=['title','content','image']


class reply(ModelForm):
    class Meta:
        model=comment
        fields=['comment','image']