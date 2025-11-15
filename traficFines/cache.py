# Ivonne Mendoza
# ivonne@imendoza.io

from pathlib import Path
class Cache:
    """
    Implementacion de la clase Cache
    """
    def __init__(self, app_name:str, obsolescence:int, cache_dir:str=None)->None:
        self.__app_name = app_name
        self.__cache_dir = cache_dir or str(Path.home() / ".my_cache" / app_name)
        self.__obsolescence = obsolescence

    #@property is used to get the value of a private attribute without using any getter methods. \
    #We have to put a line @property in front of the method where we return the private variable.

    @property
    def app_name(self)->str:
        return self.__app_name

    @property
    def cache_dir(self)->str:
        return self.__cache_dir

    @property
    def obsolescence(self)->int:
        return self.__obsolescence