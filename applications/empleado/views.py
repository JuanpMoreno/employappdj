from struct import pack
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from applications import empleado
from .models import Empleado

from .forms import EmpleadoForm

# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    model = Empleado
    context_object_name = 'lista'
    paginate_by = 2
    ordering = 'first_name'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave
        )

        print(f'Lista de resultados: {lista}')
        return lista



class ListaEmpleadosAdmin(ListView):
    template_name = 'empleado/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado



class ListByAreaEmpleado(ListView):
    template_name = 'empleado/list_by_area.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        area = self.kwargs['departamento']
        lista = Empleado.objects.filter(
        departamento__shor_name = area
        )
        return lista

class ListEmpleadoByKword(ListView):
    template_name = 'empleado/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )

        print(f'Lista de resultados: {lista}')
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'empleado/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
       empleado = Empleado.objects.get(id=2)
       return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado/detail_empleado.html'


class SuccessView(TemplateView):
    template_name = 'empleado/success.html'


class EmpleadoCreateView(CreateView):
    template_name = 'empleado/add.html'
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado_app:empleados_admin')

    def form_valid(self,form):
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = 'empleado/update.html'
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('empleado_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['first_name'])
        return super().post(request,*args,**kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado/delete.html'
    success_url = reverse_lazy('empleado_app:empleados_admin')




#DESARROLLO DEL APLICATIVO COMO PRIMER PROYECTO

class InicioView(TemplateView):
    template_name = 'inicio.html'