from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.sites.requests import RequestSite

from .models import Person, Education, ProjectOrJob, ProfessionalSkills, Academics, AreaOfInterest
from .forms import PersonForm, EducationForm, ProjectOrJobForm, ProfessionalSkillsForm, AcademicsForm, AreaOfInterestForm


def resumeFill(request):
    if request.method == 'POST':
        personform = PersonForm(request.POST)
        educationform = EducationForm(request.POST)
        projectOrJobform = ProjectOrJobForm(request.POST)
        professionalSkillsform = ProfessionalSkillsForm(request.POST)
        academicsform = AcademicsForm(request.POST)
        areaOfInterestform = AreaOfInterestForm(request.POST)

        if personform.is_valid():
            personform.save()

        if educationform.is_valid():
            educationform.save()

        if projectOrJobform.is_valid():
            projectOrJobform.save()

        if professionalSkillsform.is_valid():
            professionalSkillsform.save()

        if academicsform.is_valid():
            academicsform.save()

        if areaOfInterestform.is_valid():
            areaOfInterestform.save()

    return render(request, 'resume/resume_fill.html', {

        'personform': PersonForm(),
        'educationform': EducationForm(),
        'projectOrJobform': ProjectOrJob(),
        'professionalSkillsform': ProfessionalSkillsForm(),
        'academicsform': AcademicsForm(),
        'areaOfInterestform': AreaOfInterestForm(),
    })


def resumeView(request):
    site_name = RequestSite(request).domain
    person = Person.objects.all()[:1]
    education = Education.objects.all()
    projectOrJob = ProjectOrJob.objects.all()[:5]
    professionalSkills = ProfessionalSkills.objects.all()[:5]
    academics = Academics.objects.all()[:5]
    areaOfInterest = AreaOfInterest.objects.all()

    return render_to_response('resume/resume_view.html', {
        'site_name': site_name,
        'person': person,
        'education': education,
        'projectOrJob': projectOrJob,
        'professionalSkills': professionalSkills,
        'academics': academics,
        'areaOfInterest': areaOfInterest,
    }
    )  # , context_instance=RequestContext(request))
