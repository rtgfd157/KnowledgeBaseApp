from django.urls import include, path
from rest_framework.routers import DefaultRouter

from knowledge_app.api import views as kv

router = DefaultRouter()
#router.register(r"knowledge_app", kv.SubjectViewSet, basename='Subject')

router.register(r"subjects", kv.SubjectViewSet, basename='Subject')

urlpatterns = [

    path("", include(router.urls)),


    path("subjects/<slug:slug>/comments/", 
         kv.CommentCreateAPIView.as_view(),
         name="comment-create"),

    path("subjects/comment/<int:pk>/", 
         kv.CommentRUDAPIView.as_view(),
         name="comment-detail"),

    path("subjects/<slug:slug>/urlink/", 
         kv.UrlLinkCreateAPIView.as_view(),
         name="urlink-create"),

    path("subjects/urlink/<int:pk>/", 
         kv.UrlLinkRUDAPIView.as_view(),
         name="urlink-detail"),

    path("subjects/<slug:slug>/codeblock/", 
         kv.CodeBlockCreateAPIView.as_view(),
         name="codeblock-create"),

    path("subjects/codeblock/<int:pk>/", 
         kv.CodeBlockRUDAPIView.as_view(),
         name="codeblock-detail"),

    path("subjects/<slug:slug>/textapi/", 
         kv.TextAPIView.as_view(),
         name="text-api"),

        


        
]