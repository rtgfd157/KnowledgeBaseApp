from django.apps import AppConfig


class KnowledgeAppConfig(AppConfig):
    name = 'knowledge_app'

    def ready(self):
        import knowledge_app.signals
