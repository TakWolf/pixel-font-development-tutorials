import shutil
from pathlib import Path

from pixel_font_knife.mono_bitmap import MonoBitmap

project_root_dir = Path(__file__).parent
glyphs_dir = project_root_dir.joinpath('assets', 'glyphs')
build_dir = project_root_dir.joinpath('build')
move_right_and_overlap_bolding_dir = build_dir.joinpath('move_right_and_overlap_bolding')
move_left_and_overlap_bolding_dir = build_dir.joinpath('move_left_and_overlap_bolding')
inflation_bolding_dir = build_dir.joinpath('inflation_bolding')


def move_right_and_overlap_bolding(bitmap: MonoBitmap) -> MonoBitmap:
    solid_bitmap = bitmap.resize(left=1).plus(bitmap)
    shadow_bitmap = solid_bitmap.minus(bitmap).resize(left=1)
    result_bitmap = solid_bitmap.minus(shadow_bitmap)
    return result_bitmap


def move_left_and_overlap_bolding(bitmap: MonoBitmap) -> MonoBitmap:
    solid_bitmap = bitmap.resize(right=1).plus(bitmap, x=1)
    shadow_bitmap = solid_bitmap.minus(bitmap, x=1).resize(left=-1)
    result_bitmap = solid_bitmap.minus(shadow_bitmap)
    return result_bitmap


def inflation_bolding(bitmap: MonoBitmap) -> MonoBitmap:
    result_bitmap = bitmap.scale(scale_x=4, scale_y=4).resize(left=1, right=1, top=1, bottom=1).stroke(1)
    result_bitmap = result_bitmap.scale(scale_x=0.5, scale_y=0.5)
    return result_bitmap


def main():
    if build_dir.exists():
        shutil.rmtree(build_dir)
    move_right_and_overlap_bolding_dir.mkdir(parents=True)
    move_left_and_overlap_bolding_dir.mkdir(parents=True)
    inflation_bolding_dir.mkdir(parents=True)

    for file_path in glyphs_dir.iterdir():
        if file_path.suffix != '.png':
            continue

        bitmap = MonoBitmap.load_png(file_path)
        move_right_and_overlap_bolding(bitmap).save_png(move_right_and_overlap_bolding_dir.joinpath(file_path.name))
        move_left_and_overlap_bolding(bitmap).save_png(move_left_and_overlap_bolding_dir.joinpath(file_path.name))
        inflation_bolding(bitmap).save_png(inflation_bolding_dir.joinpath(file_path.name))


if __name__ == '__main__':
    main()
