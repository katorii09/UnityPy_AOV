# UnityPy_AOV

AOV Unity bundle unpack/repack tool.

The module is based on [UnityPy (1.9.24)](https://github.com/K0lb3/UnityPy/commit/ba572869925b516ee5e332699d938b9b237ba84c)
.

## Installation

```sh
pip install git+https://github.com/hexaov91/UnityPy_AOV.git
```

## Example

The usage is same as UnityPy

#### Extract Texture2D

```python
import os
import UnityPy_AOV

env = UnityPy_AOV.load("test.assetbundle")

os.makedirs("Texture2D",exist_ok=True)

for obj in env.objects:
    if obj.type.name == "Texture2D":
        data = obj.read()
        dest = os.path.join("Texture2D", f'{data.m_Name}')
        img = data.image
        img.save(dest+ ".png")

```

#### Import Texture2D

```python
import os
import UnityPy_AOV
from PIL import Image

env = UnityPy_AOV.load("test.assetbundle")

for obj in env.objects:
    if obj.type.name == "Texture2D":
        data = obj.read()
        # edit texture
        fp = os.path.join("Texture2D", f"{data.m_Name}.png")
        pil_img = Image.open(fp)
        data.image = pil_img
        data.save()

with open("test_moded.assetbundle", "wb") as f:
    f.write(env.file.save("lz4"))

```

More examples can be found [here](https://github.com/K0lb3/UnityPy#example).

#### About Mesh

Due to slight changes in the mesh structure, even if you build and export the raw data of the mesh using the same version of the Unity engine, you cannot use it directly.  
*(Hint: Set the value of `m_IsInUse` to the number of bones.)*

Once you’ve processed it, use `obj.set_raw_data(YourMeshData)` to complete the mesh replacement.  

If the structure is incorrect, UnityPy (or others tool) may throw an error when attempting to parse this object next time.

## Credit & Thanks

* [K0lb3 - UnityPy](https://github.com/K0lb3/UnityPy)
