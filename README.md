# UnityPy_AOV

AOV Unity bundle unpack/repack tool.

The module is based on [UnityPy (1.9.24)](https://github.com/K0lb3/UnityPy/commit/ba572869925b516ee5e332699d938b9b237ba84c)
.

## Installation

```sh
pip install git+https://github.com/hexaov91/UnityPy_AOV.git
```

## Example

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
        # export texture
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

## result

You can also modify the mesh file, try it yourself :P

https://github.com/user-attachments/assets/7781f338-0198-475c-8d01-5ae4fe914ce0



## Credit & Thanks

* [UnityPy](https://github.com/K0lb3/UnityPy)
