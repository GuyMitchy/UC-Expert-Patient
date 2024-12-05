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

# manager.py
def with_rag(func):
    """Decorator to handle RAG instance management"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            rag = RAGManager.get_instance()
            response = func(*args, **kwargs, rag=rag)
            return response
        except Exception as e:
            print(f"RAG error: {str(e)}")
            raise
        finally:
            # Always run cleanup after the function completes
            try:
                RAGManager.cleanup()
                print("RAG cleanup completed")  # Add this for debugging
            except Exception as e:
                print(f"Cleanup error: {str(e)}")
    return wrapper