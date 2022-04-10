D1 = {
    "CAD" : "Solidworks",
    "CAM" : "MasterCam",
    "CAE" : "Ansys"
    }

print("Initial Dictionary : ",D1)
D1.clear()
print("Cleared Dictionary : ",D1)
D1 = {
    "CAD" : "Solidworks",
    "CAM" : "MasterCam",
    "CAE" : "Ansys"
    }
print("Copy of Dictionary : ",D1.copy())
D2 = {
    "FEA" : "Numerical",
    "Draft" : "AutoCAD"
    }
print("Another Dictionary : ",D2)
D3 = D1.fromkeys(D1,D2)
print("Fromkeys Dictionary = ",D3)
print("CAD Software : ",D1.get("CAD"))
print("List containing a tuple for each : ",D1.items())
print("List containing dictionary's keys : ",D1.keys())
D1.pop("CAE")
print("Dicitonary after popping CAE : ",D1)
D1 = {
    "CAD" : "Solidworks",
    "CAM" : "MasterCam",
    "CAE" : "Ansys"
    }
print("\nDICTIONARY RESTORED TO ORIGINAL KEY-VALUE PAIRS AFTER POP OPERATION\n")
D1.popitem()
print("Dictionary after removing last added item : ",D1)
D1.update({"CAM":"CNC"})
print("Dicitonary after updating : ",D1)
D1 = {
    "CAD" : "Solidworks",
    "CAM" : "MasterCam",
    "CAE" : "Ansys"
    }
print("\nDICITONARY RESTORED TO ORIGINAL KEY-VALUE PAIRS AFTER UPDATE\n")
print("List containing dictionary's values : ",D1.values())

