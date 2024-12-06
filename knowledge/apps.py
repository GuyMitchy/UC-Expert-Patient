from django.apps import AppConfig
import atexit


class KnowledgeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'knowledge'

    def ready(self):
        from .manager import RAGManager
        atexit.register(RAGManager.cleanup)
