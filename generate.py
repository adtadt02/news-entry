from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('/output', exist_ok=True)

width, height = 1024, 1024
image = Image.new('RGB', (width, height), color='#0f172a')
draw = ImageDraw.Draw(image)

try:
    title_font = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 42)
    heading_font = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 24)
    body_font = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 18)
    small_font = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 14)
except:
    title_font = ImageFont.load_default()
    heading_font = ImageFont.load_default()
    body_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# Header
draw.rectangle([0, 0, width, 90], fill='#1e293b')
draw.text((40, 24), "WORLD NEWS IN ONE IMAGE — NOV 23, 2026", fill='#f8fafc', font=title_font)

# Columns/Cards
cards = [
    ("COP31 Climate Summit Collapses", [
        "• Climate talks in Turkey collapse without fossil fuel phase-out deal.",
        "• Draft text omits coal, oil, and gas references entirely.",
        "• Saudi Arabia & Russia led push; US absent after Paris withdrawal."
    ], "#334155", 40, 120),
    ("Nvidia Reinstates Jensen Huang as CEO", [
        "• Nvidia board unanimously votes to reinstate Jensen Huang as CEO.",
        "• Stock rallies; Trump endorses move as essential for economy.",
        "• US intelligence scrutinized over contacts in tech sector."
    ], "#334155", 530, 120),
    ("Student Protests & Regional Unrest", [
        "• Nationwide strikes across Europe over cost of living & rearmament.",
        "• 3 more ships struck in Strait of Hormuz amid record attacks.",
        "• Ukraine reports strike on Russian warship in Mediterranean port."
    ], "#334155", 40, 560),
    ("Global Headlines & Politics", [
        "• Democrats secure largest House majority since 1992.",
        "• Spain's right set to win majority despite Socialist gains.",
        "• Jim Beam flagship distillery pauses production indefinitely."
    ], "#334155", 530, 560)
]

for title, bullets, bg_color, x, y in cards:
    draw.rounded_rectangle([x, y, x + 454, y + 400], radius=16, fill=bg_color, outline='#475569', width=2)
    draw.text((x + 24, y + 24), title, fill='#38bdf8', font=heading_font)
    
    cy = y + 80
    for bullet in bullets:
        # Simple word wrap or multi-line printing
        draw.text((x + 24, cy), bullet, fill='#e2e8f0', font=body_font)
        cy += 45

# Footer
draw.rectangle([0, height - 50, width, height], fill='#1e293b')
draw.text((40, height - 35), "Source: Associated Press, Reuters, Democracy Now, Euronews | Compiled for make.fun", fill='#94a3b8', font=small_font)

image.save('/output/entry.png', 'PNG')
print("Successfully generated /output/entry.png")
