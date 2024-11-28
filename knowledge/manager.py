import atexit
from functools import wraps
from .rag_setup import UCExpertRAG


class RAGManager:
    """Singleton manager for RAG system"""
    _instance = None
    
    @classmethod
    def get_instance(cls):
        """Get or create RAG instance"""
        if cls._instance is None:
            cls._instance = UCExpertRAG()
        return cls._instance
    
    @classmethod
    def cleanup(cls):
        """Clean up RAG resources"""
        if cls._instance:
            cls._instance.cleanup()
            cls._instance = None

# Register cleanup for Django shutdown
atexit.register(RAGManager.cleanup)

def with_rag(func):
    """Decorator to handle RAG instance management"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            rag = RAGManager.get_instance()
            return func(*args, **kwargs, rag=rag)
        except Exception as e:
            print(f"RAG error: {str(e)}")
            raise
    return wrapper