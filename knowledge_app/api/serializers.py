from rest_framework import serializers
from knowledge_app.models import Url_Link, Subject, Comment, CodeBlock
from drf_multiple_model.views import ObjectMultipleModelAPIView


class SubjectSerializers(serializers.ModelSerializer):

    #subject = serializers.StringRelatedField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    subject_field = None
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        exclude = [ "subject_field"]

    def get_subject_has_subject_inheritance(self, instance):
        request = self.context.get("request")
        instance = instance.subject.filter(author=request.user.pk, pk=self.id)
        if instance.subject_field.exists():
            #print("exists-------")
            return True
        #print("not exists-------")
        return False

    def get_subject_inheritance(self, instance):
        request = self.context.get("request")
        instance = instance.subject.filter(pk = request.user.pk)
        if instance.subject_field.exists():
            #print("exists----1---")

            return True
        #print("not exists----1---")
        return False

    def get_parent_pk(self, instance):
        request = self.context.get("request")
        #instance = instance.id.
        return  instance.id

    def get_updated_at(self, instance):
        return instance.updated_at.strftime("%B %d, %Y")


class CommentSerializers(serializers.ModelSerializer):

    subject = serializers.StringRelatedField(read_only=True)
    updated_at = serializers.SerializerMethodField()
    subject_slug = serializers.SerializerMethodField()


    class Meta:
        model = Comment
        #exclude = ["updated_at"]
        fields = "__all__"

    def get_updated_at(self, instance):
        return instance.updated_at.strftime("%B %d, %Y")

    def get_subject_slug(self, instance):
        return instance.subject.slug


class Url_LinkSerializers(serializers.ModelSerializer):

    subject = serializers.StringRelatedField(read_only=True)
    updated_at = serializers.SerializerMethodField()
    subject_slug = serializers.SerializerMethodField()

    class Meta:
        model = Url_Link
        #exclude = ["updated_at"]
        fields = "__all__"

    def get_subject_slug(self, instance):
        return instance.subject.slug

    def get_updated_at(self, instance):
        return instance.updated_at.strftime("%B %d, %Y")



class CodeBlockSerializers(serializers.ModelSerializer):

    subject = serializers.StringRelatedField(read_only=True)
    updated_at = serializers.SerializerMethodField()
    subject_slug = serializers.SerializerMethodField()

    class Meta:
        model = CodeBlock
        #exclude = ["updated_at"]
        fields = "__all__"


    def get_subject_slug(self, instance):
        return instance.subject.slug

    def get_updated_at(self, instance):
        return instance.updated_at.strftime("%B %d, %Y")
