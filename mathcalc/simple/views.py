from django.shortcuts import render


def primfacs(number):
    """Decomposes a number into prime factors.

    number -- integer.
    Returns a list of prime factors.
    Between which there is a multiplication sign, as a list item.

    """
    min_prime_factor = 2  # Minimal prime factor
    primfac = []  # Stores prime factors with multiplication signs.
    if number == 1 or number == 0:  # Already prime factor
        primfac.append(number)
        return primfac
    while min_prime_factor * min_prime_factor <= number:
        while number % min_prime_factor == 0:
            primfac.append(min_prime_factor)
            # Multiplication sign between prime factors.
            primfac.append("*")
            # Assign next branch for factorization cycle.
            number = int(number / min_prime_factor)
        # Try next factor
        min_prime_factor = min_prime_factor + 1
    # After cycles n must be prime factor.
    if number > 1:
        primfac.append(number)
        primfac.append("*")
    # Beautiful display without a sign * at the end (For ex. 2*2*2*).
    if len(primfac) > 1:
        del primfac[-1]
    return primfac


def calc(request):
    """Call base template.

    If hasn`t "number" in GET request will call page for enter number.
    Else also call answer with prime factors.

    """
    if "number" in request.GET:
        message = request.GET["number"]
        int_message = int(message)
        # For work definition primfacs(number) if number is negative.
        if int_message < 0:
            int_message *= -1
            # Calculates prime factors. Convert list to string.
            # And save negative sign for negative number.
            list_of_primes = primfacs(int_message)
            converted = map(str, list_of_primes)
            answer = "-" + "".join(converted)
        else:
            # Calculates prime factors. Convert list to string.
            list_of_primes = primfacs(int_message)
            converted = map(str, list_of_primes)
            answer = "".join(converted)
        # For avoid explicit answer like 2=2, will return only number.
        if len(list_of_primes) < 3:
            message = ""
        # Adds to prime factors equal sign.
        else:
            message = "= " + message
        context = {"answer": answer, "message": message}
        return render(request, "simple/calc.html", context)
    else:
        return render(None, "simple/calc.html")
