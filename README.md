# Elin Fairies

----
![Version Badge](https://img.shields.io/badge/version-1.0.0-blue)
![GitHub License](https://img.shields.io/github/license/n15g/elin-fairies)

### A Fairy PCC mod for [Elin](https://store.steampowered.com/app/2135150/Elin/)
I love that Elin lets you play as a fairy character, but was disappointed that the base
game doesn't really offer any way to visually differentiate a fairy character from the other
races.

![Layer Comps](site/comparison.gif)

This mod adds new portraits and sprites for fairy characters that are much smaller than the default sprites, including
a bunch of pretty fairy wings. The smaller stature of the PCC can cause some visual glitches, noted below, but for the 
most part it works well.

![Layer Comps](site/sprite_showcase.gif)

Fairy portraits are all full-body to reflect the smaller stature of the fae.

![Layer Comps](site/portraits.png)

### Character Creation

Since the game cannot differentiate fairy sprites from default sprites, you'll often find that the initial random
character will be confusing a mix of the two. Fairy sprites are all prefixed with `fairy` to make it easier to
find compatible sprites.

#### Wings and Imports
Since the back slot is not available during the initial character creator you will need to either
use an import file with wings already set, or find a mirror in-game to adjust the back slot after creation.

Included in the mod directory is a set of templates for fairy characters with wings and outfits pre-applied.

You can find the mod folder by using the `Mod Viewer` on the title screen. Click the mod name and then `Open in Explorer`.
Use the files in the `Template` folder with the `Import` function during character creation.

## Github
https://github.com/n15g/elin-fairies

## Known Issues

### Items
![Beeg](site/beeg.png)

Game items that appear on the character, like tools or some headpieces are not scaled down, so they appear comically
large. For tools and weapons it's mostly amusing and stylistic, but clothing items look jarring.

### Zoom Aliasing
![Zoom](site/zoom.png)

At the default zoom level the player sprites are slightly larger than the original sprite sheets. This causes some of
the rows and columns to be duplicated, causing a wonky look. This happens with normal PCC sprites as well, but it's a lot
more pronounced with the smaller sprites that rely on single-pixel details. This can be fixed by adjusting the default
zoom using the map tools button next to the minimap to adjust the zoom level.

# Development

## Requirements

* **Photoshop** - For portrait source files in `.psd` format.
* **[Aseprite](https://www.aseprite.org/)** - For PCC sprites in `*.ase` format.
* **Python** - Build scripts and various tooling.

## Portrait Layer Comps

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

### Aseprite

Included in the `dev/aseprite` folder are `.pal` palette files and `.lua` script extensions for Aseprite.

Both can be installed by running the `dev/aseprite/install-aseprite-extensions.py` python file, or manually copying
into the appropriate folders by using the `File -> Scripts -> Open Scripts Folder` and the `Open Folder` button
from the Palette list.

### PCC sprites

The `elin-pcc.lua` script is an export script that will compile layers and tags in an Aseprite document
into the appropriate sprite sheets for Elin. See one of the existing `.ase` files for an example of how to set
up a document for export.

```
-- Elin sprite export script.
-- The script will look for a layer/group named `base_` as the basis for export and if not found,
-- default to the whole sprite.
-- For PCC files, the sprite sheet is split using tags to separate the 4 cardinal directions, 4 frames each:
--
-- [  front   ][   left   ][    right    ][     back     ]
-- [1][2][3][4][5][6][7][8][9][10][11][12][13][14][15][16]
--
-- Special layer types:
--
-- Back sprites:
-- Some attachments have two sprites, one layered in front and one behind the player character.
-- During export, the script will look for a layer group named `_back` and if found use this layer group as the
-- basis for the `<type>bk` sprite.
```

