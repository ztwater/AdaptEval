        except AttributeError:
            cls = meth.__globals__.get(class_name)
