from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import PaidChoices, Tada
from .forms import TadaForm


class TadaListView(ListView):
    """ List of all TADA as history page """
    template_name = 'tada_list.html'
    context_object_name = 'tada'
    queryset = Tada.objects.all().order_by('-date') 


class CreateTadaView(CreateView):
    """ Creating new TADA """    
    template_name = 'tada_create.html'
    form_class = TadaForm
    queryset = Tada.objects.all() 
    success_url = '/'


def approve_paid(request, pk):
    """ Function will update unpaid to paid and no reverse. """
    payment = Tada.objects.get(pk=pk)
    payment.paid = PaidChoices.PAID
    payment.save()
    return redirect('tada-list')


def tada_pdf_view(request, *args, **kwargs):
    """Generating pdf for every tada as report receipt"""

    pk = kwargs.get('pk')
    tada = get_object_or_404(Tada, pk=pk)

    template_path = 'tada_pdf.html'
    context = {'tada': tada}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Receipt_{tada.id}_{tada.date}.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response