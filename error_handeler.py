

class Handler:

    def check_if_none(value):
        if value is not None: return {"passed": True}
        else: return {"passed": False}