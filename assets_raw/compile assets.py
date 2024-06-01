import os.path

from pygameextra import Atlas, Sheet, SheetHorizontal
import pygameextra as pe
import time

pe.init((0, 0))

SCRIPT_PATH = os.path.realpath(os.path.dirname(__file__))
DEBUG_DIRECTORY = os.path.join(SCRIPT_PATH, "atlas surfaces")
COLORS_FOR_LABELING = ["red", "blue", "pink", "darkaqua"]

os.makedirs(DEBUG_DIRECTORY, exist_ok=True)

print("Compiling atlases...", end='\t')
start = time.time()

atlases = {
    "loading_icon": Atlas.from_sheets({
        "loading_icon": Sheet(os.path.join(SCRIPT_PATH, "loading_icon.png"), SheetHorizontal(64, 64), 20, loop=True),
        "loading_icon_progress": Sheet(os.path.join(SCRIPT_PATH, "loading_icon_progress.png"), SheetHorizontal(64, 64), 0),
        "pge_icon": Sheet(os.path.join(SCRIPT_PATH, "pge_icon.png"), SheetHorizontal(96, 48), 44),
    })
}

print(f"DONE!\t[{time.time()-start:.2f}s]")

for atlas_name, atlas in atlases.items():
    atlas.save(os.path.join(SCRIPT_PATH, '..', 'pygameextra', 'assets', f'{atlas_name}.atlas'))
    atlas.surface.save_to_file(os.path.join(DEBUG_DIRECTORY, f'{atlas_name} (unlabeled).png'))
    color_index = 0

    print(f"Creating atlas labels ({atlas_name}) ...", end='\t')
    start = time.time()

    with atlas.surface:
        pe.fill.transparency(pe.colors.black, 100)
        for mapping in atlas.mappings.values():
            color = getattr(pe.colors, COLORS_FOR_LABELING[color_index])
            color_index += 1
            for i, rect in enumerate(mapping):
                pe.draw.rect(pe.colors.black, rect, 1)
                rect = pe.Rect(*rect)
                rect.scale_by_ip(.8, .8)
                pe.draw.rect(color, rect, 2, edge_rounding=5)
                pe.Text(str(i), font_size=rect.width//3, position=rect.center, colors=(pe.colors.white, pe.colors.black)).display()

        color_index = 0
        for mapping_name, mapping in atlas.mappings.items():
            color = getattr(pe.colors, COLORS_FOR_LABELING[color_index])
            color_index += 1
            rect = mapping[0]
            text = pe.Text(mapping_name, font_size=rect[3]//4, colors=(pe.colors.white, color))
            text.rect.topleft = rect[:2]
            text.rect.top += 1
            text.rect.left += 1
            text.rect.right = min(pe.display.get_width(), text.rect.right)
            text.display()
    print(f"DONE!\t[{time.time()-start:.2f}s]")

    atlas.surface.save_to_file(os.path.join(DEBUG_DIRECTORY, f'{atlas_name} (labeled).png'))
