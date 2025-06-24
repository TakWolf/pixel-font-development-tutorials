from pathlib import Path

from pixel_font_builder import FontBuilder, Glyph

project_root_dir = Path(__file__).parent
build_dir = project_root_dir.joinpath('build')
build_dir.mkdir(exist_ok=True)


def main():
    builder = FontBuilder()
    builder.font_metric.font_size = 11
    builder.font_metric.horizontal_layout.ascent = 11
    builder.font_metric.horizontal_layout.descent = -4

    builder.meta_info.version = '1.0.0'
    builder.meta_info.family_name = 'My Font'

    builder.glyphs.append(Glyph(
        name='.notdef',
        horizontal_offset=(0, -4),
        advance_width=6,
        bitmap=[
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ],
    ))
    builder.glyphs.append(Glyph(
        name='CAP_LETTER_A',
        horizontal_offset=(0, -4),
        advance_width=6,
        bitmap=[
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ],
    ))

    builder.character_mapping[65] = 'CAP_LETTER_A'

    builder.save_otf(build_dir.joinpath('my-font.otf'))
    builder.save_ttf(build_dir.joinpath('my-font.ttf'))


if __name__ == '__main__':
    main()
