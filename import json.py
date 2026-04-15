import json
from pathlib import Path
import sys
filepath=Path(__file__).resolve().parent/"states_presentation.json"
effect=["BIRDS","CLOUDS","HALO","DOTS","GLOBE","NET","GLOBE","TOPOLOGY","WAVES","NET","HALO","RINGS","CLOUDS2","","","","","","","","","","",]
part=["Farewell 2026","Prayer","Band","Ramp Walk(Round1)","Speech","Talent Round(Round2)","Speech","Letters of Appreciation","Q/A(Round3)","Games","Dance","Principal's Speech","Declaration of Results","lorem ipsum","lorem ipsum","lorem ipsum","lorem ipsum","lorem ipsum","lorem ipsum","lorem ipsum","lorem ipsum","lorem ipsum","lorem ipsum",]
if len(effect)!=len(part):
    print("Check the sync")
    print(len(effect),"effect")
    print(len(part),"part")
    sys.exit
if not filepath.exists():
    data={"effects":[],"part":[]}
else:
    with open(filepath,"r") as f:
        data=json.load(f)
data["effects"] = effect
data["part"] = part
with open(filepath,"w") as f:
    json.dump(data,f,indent=4)
    
    