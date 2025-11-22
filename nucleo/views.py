from django.http import HttpResponse

def hola_mundo(request):
    """
    Una vista simple que retorna un saludo en HTML.
    """
    html_content = """
    <div style='font-family: sans-serif; text-align: center; padding-top: 50px;'>
        <h1>Bienvenidos a Incognita <br>>:)</h1>
    </div>
    """
    return HttpResponse(html_content)