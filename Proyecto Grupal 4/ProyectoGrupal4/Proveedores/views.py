# debemos import render de django shortcuts
from django.shortcuts import render, redirect

# debemos impotar desde forms la clase creada con antelacion ProveedoresForm
from .forms import ProveedoresForm
from .models import Proveedores


# debemos crear una metodo para guardar el formulario con la informacion que proviene de forms

def crear_proveedores(request):
    # verificar que el metodo utilizado por el formulario es POST
    if request.method == 'POST':
        # genero una variable donde le asigno toda la data proveniente de el formulario ProveedoresForm
        form = ProveedoresForm(request.POST)
        # verifico si la informacion del formulario es valida con la funcion is_valid()
        if form.is_valid():
            # si esto la informacion es valida procedo a guardar la informacion en la base de datos de django
            form.save()
            # en caso de exito, redirigimos a la pagina principal donde se visualizaran todos los proveedores
            return redirect('pagina_principal')
    else:
        # si la peticion enviada no es de tipo POST se devuelve un formulario vacio
        form = ProveedoresForm()

    # est retorno pemmitira al usuario ver el formulario y poder completarlo en el archivo form proveedores
    return render(request, 'form_proveedores.html', {'form': form})


def proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'pagina_principal.html', {'proveedores': proveedores})
