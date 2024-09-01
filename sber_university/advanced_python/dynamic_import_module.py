import importlib


def dynamic_import(module):
    return importlib.import_module(module)

print(__name__)
if __name__ == '__main__':
    module = dynamic_import('foo')
    module.main()
