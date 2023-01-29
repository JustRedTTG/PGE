import pickle, os
import pgerom as pe

def save(file,*args):
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'wb') as f:
        pickle.dump(args, f)


def load(file):
    args = []
    if os.path.exists(file):
        with open(file,"rb") as f:
            args = pickle.load(f)
        return args

    else:
        raise Exception("Save file does not exist")


def savePGE(file,*args):
    i = 0
    data = ""
    for x in args:
        try:
            Vtype = x.PGE
        except:
            raise Exception("Variable "+str(i+1)+" is either not supported or not a PGE variable ;)")
        # go
        data += Vtype+":"
        if Vtype == "text":
            data += str(x.text)+",,"
            data += str(x.font)+",,"
            data += str(x.fontsize)+",,"
            data += str(x.original_pos)+",,"
            data += str(x.color)+",,"
            data += str(x.background)+",,"
            data += str(x.layer)
        data += "\n"
        i += 1
    if os.path.exists(file):
        os.remove(file)
    f = open(file, "a+")
    f.seek(0)
    f.write(data)
    f.close()