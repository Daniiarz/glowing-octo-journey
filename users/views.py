from django.shortcuts import render, get_object_or_404

# Create your views here.
from users.models import Profile


def get_real_profile(request):
    context = {
        'profile': Profile.objects.all()
    }
    return render(request, 'users/index_profile.html', context)


def get_real_profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {
        'profile': profile
    }
    return render(request, 'users/detail_profile.html', context)
