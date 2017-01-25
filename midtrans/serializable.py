class Serializable:
    def __init__(self):
        pass

    def serialize(self):
        results = {}
        for key in self.__dict__:
            val = getattr(self, key)

            if hasattr(val, 'serialize'):
                results[key] = val.serialize()
            else:
                if val is not None:
                    if type(val) is list:
                        results[key] = []
                        for val in getattr(self, key):
                            if hasattr(val, 'serialize'):
                                results[key].append(val.serialize())
                            elif val is not None:
                                results[key].append(val)
                    else:
                        results[key] = val

        return results
