from django.shortcuts import render

# Create your views here.
# products/views.py
from django.shortcuts import render
from django.contrib import messages
from .forms import FileUploadForm
from .services import import_products_from_file

def upload_file_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            result = import_products_from_file(request.FILES['file'])
            
            # Display messages based on the result
            if result["status"] == "success":
                messages.success(request, result["message"])
            else:
                messages.error(request, result["message"])
    else:
        form = FileUploadForm()
    
    return render(request, 'upload.html', {'form': form})



# products/views.py

# ... (keep your existing upload_file_view function) ...

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('-added_on')
    serializer_class = ProductSerializer
    lookup_field = 'sku' # Use SKU for lookups instead of ID