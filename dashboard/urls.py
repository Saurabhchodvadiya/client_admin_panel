from django.urls import path
from dashboard import views as FT_view

from dashboard.views import find_record, home_page,surfaceProduct,throughproducts,add_data,otherproducts
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [

     path('', home_page, name='pages/home_page'),
     path('suraface/', surfaceProduct, name='surfaceProduct'),
     path('through/', throughproducts, name='throughProduct'),
      path('other/', otherproducts, name='otherProduct'),
     path('find_record/',find_record,name="find_record"),
     path('edit-surface',FT_view.edit_surface_data,name="edit_surface"),
     path('edit-through',FT_view.edit_through_data,name="edit_through"),
     path('add-data',FT_view.add_data,name="add_data"),
     path('update-surface-profiles',FT_view.update_surface,name="update_surface"),
     path('get-surface-data',FT_view.get_surface_unique_data,name="get_surface_unique_data"),
     path('update-through-profiles',FT_view.update_through,name="update_through"),
     path('get-through-data',FT_view.get_through_unique_data,name="get_through_unique_data"),
     path('update-other-profiles',FT_view.update_other,name="update_other"),
     path('add-manufacture-data',FT_view.add_menu_data,name="add_manufacture_data"),
     path('get-other-data',FT_view.get_other_unique_data,name="get_other_unique_data"),
      path('edit-other',FT_view.edit_other_data,name="edit_other"),
        # path('search_record/',search_record,name="search_record")
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  