class MyAppRouter(object):
    """A router to control all database operations on models in
    the myapp application"""
    def db_for_read(self, model, **hints):
        "Point all operations on myapp models to 'other'"

        if model._meta.app_label in ['account']:
            return 'default'

        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on myapp models to 'other'"

        if model._meta.app_label in ['account']:
            return 'default'

        return 'default'
