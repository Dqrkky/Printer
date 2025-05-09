<<<<<<< HEAD
import Printer
import json

hpenvy6020e = Printer.HP044C0C()
scann = Printer.Scan()
print(
    json.dumps(
        obj={
            "getconfigurationconstraints": hpenvy6020e.getconfigurationconstraints(),
            "getprintmodeconfiguration": hpenvy6020e.getprintmodeconfiguration(),
            "getconfiguration": hpenvy6020e.getconfiguration()
        },
        indent=4
    )
)
=======
import printer

hpenvy6020e = printer.HP044C0C()
#scann = Printer.Scan()

print(hpenvy6020e.getconfigurationconstraints())
>>>>>>> 86a9c010a22c7ad4989a32a4e401e16f016e6e0f
