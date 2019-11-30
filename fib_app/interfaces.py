import abc
class FibonacciCacheInterface(abc.ABC):

    @abc.abstractmethod
    def get(self, n):
        pass
    @abc.abstractmethod
    def put(self, n, val):
        pass

    @abc.abstractmethod
    def getCachedList(self):
        pass
    @abc.abstractmethod
    def storeCachedList(self, startIndex, endIndex, sum):
        pass

    
