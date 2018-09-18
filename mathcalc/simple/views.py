from django.shortcuts import render_to_response
from django.http import HttpResponse


def calc(request):
    """Function of calling a page to enter a number."""
    return render_to_response('simple/calc.html')


def primfacs(n):
    """A function that decomposes the introduced number into prime factors.
    Between factors, the multiplication sign.
    """
    i = 2
    primfac = []
    if n == 1:
        primfac.append(n)
        return primfac
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = int(n / i)
            primfac.append('*')  # Adding a sign in response for better readability of the answer
        i = i + 1
    if n > 1:
        primfac.append(n)
        primfac.append('*')
    if len(primfac) > 1:  # Instruction is needed for a beautiful display without a sign * at the end (For ex. 2*2*2*)
        del primfac[-1]
    return primfac


def search(request):
    """The function of processing the entered number and returning the response."""
    if 'q' in request.GET:
        message = request.GET['q']
    return HttpResponse(primfacs(int(message)))
