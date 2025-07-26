# contex manager is tool that maanes setip and cleanup actions automatically
# is mosttyl used in filejandling, db connections, locks..
# with handles file opening and closing automatically
with open("notext.nxt", "r") as f:
    data = f.read()
    print(data)
