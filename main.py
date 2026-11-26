#!/usr/bin/env python3
"""Render one newspaper-style image summing up Thursday 26 November 2026.

Writes entry.png (1024x1024 PNG) to MAKEFUN_OUTPUT_DIR, or /output when
that variable is not set. No network access. Deterministic: repeated runs
produce identical bytes.
"""

import os

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1024
HEIGHT = 1024
MARGIN = 36

PAPER = (247, 243, 234)
INK = (26, 26, 26)
RED = (163, 30, 34)
NAVY = (31, 58, 95)
PANEL_BG = (255, 255, 255)
PANEL_LINE = (180, 175, 165)
MUTED = (90, 86, 78)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Split text into lines that fit max_width pixels."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


STORIES = [
    {
        "num": "1",
        "head": "UKRAINE HITS RUSSIAN AIR BASE",
        "desc": "Five planes damaged and two oil refineries struck in Samara.",
        "tag": "REUTERS",
    },
    {
        "num": "2",
        "head": "ASIAN MARKETS BOUNCE BACK",
        "desc": "Nikkei +1.6%, Kospi +1.9%, Taiwan +3% as Wall Street recovers.",
        "tag": "REUTERS",
    },
    {
        "num": "3",
        "head": "JUDGES URGE DROPPING NETANYAHU CHARGES",
        "desc": "Israeli judges urge dropping the most serious corruption charges.",
        "tag": "JERUSALEM",
    },
    {
        "num": "4",
        "head": "CAIRO TANKER FIRE KILLS 30",
        "desc": "A fuel tanker fire on the Giza Ring Road kills at least 30 people.",
        "tag": "CAIRO",
    },
    {
        "num": "5",
        "head": "HOUTHIS CLAIM STRIKE ON SAUDI REFINERY",
        "desc": "Iran says tankers hit mines near Hormuz; Brent oil jumps near $95.",
        "tag": "GULF",
    },
    {
        "num": "6",
        "head": "ANTHROPIC CLOSES BELOW IPO PRICE",
        "desc": "Shares end at $82.79 as the AI sell-off deepens; Nvidia falls 3.9%.",
        "tag": "NEW YORK",
    },
]


def draw_panel(draw, x, y, w, h, story):
    draw.rectangle([x, y, x + w, y + h], fill=PANEL_BG, outline=PANEL_LINE, width=2)
    # Number badge in the top-left corner.
    badge = 44
    draw.rectangle([x, y, x + badge, y + badge], fill=RED)
    num_font = font(SANS_BOLD, 26)
    num_w = draw.textlength(story["num"], font=num_font)
    draw.text((x + (badge - num_w) / 2, y + 8), story["num"], font=num_font, fill=(255, 255, 255))
    # Headline, wrapped to at most two lines.
    head_font = font(SANS_BOLD, 27)
    text_x = x + 18
    text_w = w - 36
    head_lines = wrap(draw, story["head"], head_font, text_w)
    cy = y + badge + 14
    for line in head_lines[:2]:
        draw.text((text_x, cy), line, font=head_font, fill=INK)
        cy += 34
    # Thin rule under the headline.
    draw.line([text_x, cy + 4, x + w - 18, cy + 4], fill=PANEL_LINE, width=2)
    # Description, wrapped to at most two lines so it never reaches the tag.
    desc_font = font(SANS, 21)
    desc_lines = wrap(draw, story["desc"], desc_font, text_w)
    cy += 18
    for line in desc_lines[:2]:
        draw.text((text_x, cy), line, font=desc_font, fill=INK)
        cy += 28
    # Source tag below the description, or pinned near the bottom when the
    # description is short; never overlapping the description text.
    tag_font = font(SANS_BOLD, 17)
    tag_y = max(y + h - 32, cy + 12)
    draw.text((text_x, tag_y), story["tag"], font=tag_font, fill=NAVY)


def main():
    img = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
    draw = ImageDraw.Draw(img)

    # Masthead.
    title_font = font(SERIF_BOLD, 58)
    title = "THE WORLD IN ONE IMAGE"
    title_w = draw.textlength(title, font=title_font)
    draw.text(((WIDTH - title_w) / 2, 30), title, font=title_font, fill=INK)
    date_font = font(SANS_BOLD, 25)
    date = "THURSDAY, 26 NOVEMBER 2026"
    date_w = draw.textlength(date, font=date_font)
    draw.text(((WIDTH - date_w) / 2, 108), date, font=date_font, fill=RED)
    draw.line([MARGIN, 152, WIDTH - MARGIN, 152], fill=RED, width=4)
    draw.line([MARGIN, 160, WIDTH - MARGIN, 160], fill=INK, width=2)

    # Six story panels in a 2 by 3 grid.
    grid_top = 180
    grid_bottom = 956
    gutter = 24
    col_w = (WIDTH - 2 * MARGIN - gutter) // 2
    row_h = (grid_bottom - grid_top - 2 * 20) // 3
    for i, story in enumerate(STORIES):
        col = i % 2
        row = i // 2
        px = MARGIN + col * (col_w + gutter)
        py = grid_top + row * (row_h + 20)
        draw_panel(draw, px, py, col_w, row_h, story)

    # Footer.
    foot_font = font(SANS, 18)
    footer = "A summary of Thursday's reporting - sources as noted in each panel."
    foot_w = draw.textlength(footer, font=foot_font)
    draw.text(((WIDTH - foot_w) / 2, 972), footer, font=foot_font, fill=MUTED)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    img.save(os.path.join(out_dir, "entry.png"), format="PNG")


if __name__ == "__main__":
    main()
