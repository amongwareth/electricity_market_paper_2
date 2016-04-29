import logging
import importlib

logger = logging.getLogger(__name__)


class LoaderClass(object):

    def __init__(self):
        self._loaded_module = {}
        self._loaded_class = {}

    def get_module(self, module_name):
        '''	This method returns the module '''
        if module_name in self._loaded_module:
            logger.debug("Saved imported module '%s'", module_name)
            module = self._loaded_module[module_name]
        else:
            module = self._import_module(module_name)
            self._loaded_module[module_name] = module
        return module

    def _import_module(self, module_name):
        logger.debug("Importing module '%s'", module_name)
        try:
            module = importlib.import_module(module_name)
        except ImportError as error:
            logger.error("Error importing module '%s'", module_name)
            raise
        return module

    def _import_class(self, module, classname):
        logger.debug("Loading class '%s' from module '%s'", classname, module)
        module = self.get_module(module)
        if hasattr(module, classname):
            retclass = getattr(module, classname)
        else:
            logger.error("Error importing class '%s' from module '%s'", classname, module)
            raise ImportError('%s.%s' % (module, classname))
        return retclass

    def get_class(self, classname):
        if classname in self._loaded_class:
            logger.debug("Saved imported class '%s'", classname)
            retclass = self._loaded_class[classname]
        else:
            module_name, class_name = classname.rsplit('.', 1)
            retclass = self._import_class(module_name, class_name)
            self._loaded_class[classname] = retclass
        return retclass

    def get_instance(self, classname, *args, **kwargs):
        logger.debug(
            "Return new instance of class '%s', args = %s, kwargs = %s", classname, args, kwargs)
        requested_class = self.get_class(classname)
        instance = requested_class(*args, **kwargs)
        instance._aliased_class = classname
        return instance
