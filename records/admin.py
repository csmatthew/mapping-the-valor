from django.contrib import admin
from .models.valor_record import ValorRecord
from .models.hierarchy import Province, Diocese

# Register the model with the admin site
admin.site.register(Province)
admin.site.register(ValorRecord)
admin.site.register(Diocese)
