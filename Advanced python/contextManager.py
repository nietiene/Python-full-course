# contex manager is tool that maanes setip and cleanup actions automatically
# is mosttyl used in filejandling, db connections, locks..
# with handles file opening and closing automatically
with open("notext.nxt", "r") as f:
    data = f.read()
    print(data)


class myCntext:
    def __enter__(self):
        print("==> Entring block")
        return "resource"
    
    def __exit__(self, exc_type, exc_value, traceback)