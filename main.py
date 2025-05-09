import printer
import json

hpenvy6020e = printer.HP044C0C()
scann = printer.Scan()
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