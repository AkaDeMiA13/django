class Router(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "akademia_sns":
            return "default"
        elif model._meta.app_label == "ecom":
            return "db2"
 
    def db_for_write(self, model, **hints):
        if model._meta.app_label == "akademia_sns":
            return "default"
        elif model._meta.app_label == "ecom":
            return "db2"
 
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == "akademia_sns" and obj2._meta.app_label == "ecom":
            return True
        elif "akademia_sns" not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return None
 
    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == "akademia_sns":
            return db == "default"
        else:
            return db == "db2"
