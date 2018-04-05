from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from .models import Person


def add_person(request):
    context = RequestContext(request)

    if request.method == 'Post':
        form = Person(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.usern = request.user
            task.save()

            return redirect('/')
        else:
            print form.errors

    else:
        form = Person()

    return render_to_response('resume/resume.html', {'form': form}, context)
