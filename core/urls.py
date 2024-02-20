from django.urls import path

from core.views import *

urlpatterns = [
    path('', pre_shift_view, name='main'),
    path('shift/', shift_main_view, name='shift_main_page'),
    path('report/', report_send, name='report_page'),
    path('reports/', reports_view, name='reports_view'),
    path('request/', request_send, name='request_send'),
    path('qr-decoder/', decode_photo, name='decode_photo'),
    path('shift/scan/', order_scan_view, name='shift_scan_page'),
    path('shift/quantity/', order_quantity_view, name='shift_qauntity_page'),
    path('shift/setup/', order_setup_view, name='shift_setup_page'),
    path('shift/processing/', order_processing_view, name='shift_processing_page'),
    path('shift/ending/', order_ending_view, name='shift_ending_page'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('backup/', backup, name='backup')
]
