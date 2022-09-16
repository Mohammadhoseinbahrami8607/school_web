from django.urls import path

from . import views

urlpatterns = [
    path('sign_up/', views.Sign_up.as_view(), name='sign_up'),
    path('panel/<str:username>', views.panel_list_view, name='panel_list_view'),
    path('panel/<str:username>/exam_panel/', views.exam_panel, name='exam_list'),
    path('panel/<str:username>/exam_panel/<int:pk>/', views.exam_detail_view, name='opinion_exam'),
    path('panel/<str:username>/exam_panel/<int:pk>/<int:pk2>', views.exam_quastion, name='quastions')
]
