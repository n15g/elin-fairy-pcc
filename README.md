# Elin Fairies

----
![Version Badge](https://img.shields.io/badge/version-1.0.0-blue)
![GitHub License](https://img.shields.io/github/license/n15g/elin-fairies)

### Fairy PCC mod for [Elin](https://store.steampowered.com/app/2135150/Elin/)
Adds new, smaller portraits and sprites for fairy characters.

![Layer Comps](site/comparison.gif)

![Layer Comps](site/sprite_showcase.gif)


### Dev Tools

* **Photoshop** - Portrait source files are in `.psd` format.
* **[Aseprite](https://www.aseprite.org/)** - PCC sprites are in `*.ase` format.
* **Python** - Build scripts and various tooling.

### Portrait Layer Comps

Photoshop Layer Comps are used to output the overlay images for portraits.
Unfortunately the output options don't work well with Elin's naming convention, so there's
a small python script to rename the default filenames.

To export a portrait:

1. In Photoshop, `Window -> Layer Comps`
   ![Layer Comps](site/layer_comps1.png)
   You'll want two comps for a portrait:
   1. `base` - All visible layers on, this is your base portrait.
   2. `overlay` - Only the hair overlay layers enabled.
2. In Photoshop, `File -> Export -> Layer Comps to Files...`
   ![Layer Comps](site/layer_comps2.png)
   1. Set the `Destination` to the `Portrait` folder.
   2. Set the `File Name Prefix` to the portrait name.
   3. Un-check the `File Name Prefix` checkbox.
   4. Set the `File Type` to `PNG-24.
   5. Hit `Run`.
3. Run the Python script `dev/rename_layer_comps.py`
   ```python dev/rename_layer_comps.py```
