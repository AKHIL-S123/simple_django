
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('my name is akhil')

from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_groups')
    else:
        form = GroupForm()

    context = {'form': form}
    return render(request, 'create_group.html', context)

def list_groups(request):
    groups = MyGroup.objects.all()
    context = {'groups': groups}
    return render(request, 'list_groups.html', context)

# Create a model form for creating and editing groups.
class GroupForm(forms.ModelForm):
    class Meta:
        model = MyGroup
        fields = ['name']
