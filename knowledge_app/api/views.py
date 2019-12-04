from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from knowledge_app.api.serializers import (SubjectSerializers, CommentSerializers,
                                            Url_LinkSerializers,CodeBlockSerializers)
from knowledge_app.models import Subject, Comment, Url_Link, CodeBlock
from knowledge_app.api.permission import IsAuthorOrReadOnly, IsAuthorOrReadOnlyComment_Url_Link_Code
from rest_framework.generics import get_object_or_404
from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination

class SubjectViewSet(viewsets.ModelViewSet):
    lookup_field = "slug"
    serializer_class = SubjectSerializers
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        kwarg_pk = self.kwargs.get("pk")
        return Subject.objects.filter(author__id=self.request.user.id).order_by("-updated_at")

    #  creating record
    def perform_create(self, serializer):
        
        # if self.serializer_class.get_subject_has_subject_inheritance:
        #     subject_key_val = self.serializer_class.get_parent_pk(self, )
        #     serializer.save(author=self.request.user, subject_field=subject_key_val )
        #     return
        serializer.save(author=self.request.user)

class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for an comment instance to it's subject."""
    serializer_class = CommentSerializers
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnlyComment_Url_Link_Code]
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        kwarg_pk = self.kwargs.get("pk")
        comment = get_object_or_404(Comment, id=kwarg_pk)
        #return comment
        return Comment.objects.filter(id=kwarg_pk)

class CommentCreateAPIView(generics.CreateAPIView):
    """Allow users to add a comment instance """
    serializer_class = CommentSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_pk = self.kwargs.get("pk")
        return Comment.objects.filter(subject__id=kwarg_pk).order_by("-updated_at")
    
    def perform_create(self, serializer):
        kwarg_slug = self.kwargs.get("slug")
        subject = get_object_or_404(Subject, slug=kwarg_slug)
        serializer.save(subject_id=subject.id )


class UrlLinkRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for an comment instance to it's subject."""
    serializer_class = Url_LinkSerializers
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnlyComment_Url_Link_Code]
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        kwarg_pk = self.kwargs.get("pk")
        #url_link= get_object_or_404(Url_Link, id=kwarg_pk)
        #return comment
        return Url_Link.objects.filter(id=kwarg_pk)

class UrlLinkCreateAPIView(generics.CreateAPIView):
    """Allow users to add a comment instance """
    serializer_class = Url_LinkSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_pk = self.kwargs.get("pk")
        return Comment.objects.filter(subject__id=kwarg_pk).order_by("-updated_at")
    
    def perform_create(self, serializer):
        kwarg_slug = self.kwargs.get("slug")
        subject = get_object_or_404(Subject, slug=kwarg_slug)
        serializer.save(subject_id=subject.id )



class CodeBlockCreateAPIView(generics.CreateAPIView):
    """Allow users to add a code block instance  to subject"""
    serializer_class = CodeBlockSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_pk = self.kwargs.get("pk")
        return CodeBlock.objects.filter(subject__id=kwarg_pk).order_by("-updated_at")
    
    def perform_create(self, serializer):
        kwarg_slug = self.kwargs.get("slug")
        subject = get_object_or_404(Subject, slug=kwarg_slug)
        serializer.save(subject_id=subject.id )


class CodeBlockRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for an code block instance to it's subject."""
    serializer_class = CodeBlockSerializers
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnlyComment_Url_Link_Code]
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        kwarg_pk = self.kwargs.get("pk")
        #url_link= get_object_or_404(Url_Link, id=kwarg_pk)
        #return comment
        return CodeBlock.objects.filter(id=kwarg_pk)


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 20


class TextAPIView(ObjectMultipleModelAPIView):
    """Return list of comment,url of subject """

    sorting_fields = ['-updated_at']
    pagination_class = LimitPagination

    def get_querylist(self):

        sorting_fields = ['-updated_at']

        kwarg_slug = self.kwargs.get("slug")

        querylist = [
        {'queryset': Comment.objects.filter(subject__slug=kwarg_slug),
         'serializer_class': CommentSerializers},
         {'queryset': CodeBlock.objects.filter(subject__slug=kwarg_slug),
         'serializer_class': CodeBlockSerializers},
         {'queryset': Url_Link.objects.filter(subject__slug=kwarg_slug),
         'serializer_class': Url_LinkSerializers},
        ]

        #querylist.sort(key=lambda x: x.name)

        #querylist.sort(key=lambda x: x[1])
        #querylist.order_by("updated_at")

        return querylist




    
