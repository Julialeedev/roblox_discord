from django.http import HttpResponse


def google_verify(request):
    return HttpResponse(
        "google-site-verification: google1f2e1aafad15e450.html"
    )
