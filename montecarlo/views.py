from django.shortcuts import render
from django.views import generic
from .montecarlo import Producto, ProductoConVencimiento, ProductoSinVencimiento
from .forms import ParametersForm
# Create your views here.

class Montecarlo(generic.FormView):
    form_class = ParametersForm
    template_name = 'montecarlo/forms/montecarlo.html'

    def form_valid(self, form):
        if form.cleaned_data['pseudoaleatorio'] == 'True':
            print("algo")
            num_pseudoaleatorios = [0.94, 0.74, 0.62, 0.11, 0.17, 0.66, 0.54, 0.30, 0.69, 0.08,
           0.27, 0.13, 0.80, 0.10, 0.54, 0.60, 0.49, 0.78, 0.66, 0.44]
        else:
            num_pseudoaleatorios = []

        if form.cleaned_data['vencimiento'] is None:
            product = ProductoSinVencimiento(
                c=form.cleaned_data['costo'],
                p=form.cleaned_data['precio_venta'],
                tr=form.cleaned_data['tiempo_reposicion'],
                cr=form.cleaned_data['cant_a_reponer'],
                si=form.cleaned_data['stock_inicial'],
                r=form.cleaned_data['recupero'],
                num_pseudoaleatorios=num_pseudoaleatorios
            )
        else:
            product = ProductoConVencimiento(
                c=form.cleaned_data['costo'],
                p=form.cleaned_data['precio_venta'],
                tr=form.cleaned_data['tiempo_reposicion'],
                cr=form.cleaned_data['cant_a_reponer'],
                si=form.cleaned_data['stock_inicial'],
                # Se agrega 1 porque segun el enunciado ingresamos los dias que se vence despues de haber llegado
                # y en la libreria se consideria dias de vencimiento a partir de que llego
                v=form.cleaned_data['vencimiento'] + 1,
                num_pseudoaleatorios=num_pseudoaleatorios
            )
        ganacia = product.simular(form.cleaned_data['cant_iteraciones'])
        print(ganacia)

        return render(self.request, template_name=self.template_name, context={'ganancia': ganacia, 'form': form})