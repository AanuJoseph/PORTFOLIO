from PIL import Image, ImageDraw, ImageFont

base_dir = r"C:\Users\USER\Desktop\Portfolio-project"
out_path = base_dir + r"\images\social-preview.jpg"
portrait_path = base_dir + r"\images\DSC_4703.jpg.jpeg"

bg = Image.new("RGB", (1200, 630), "#111827")
draw = ImageDraw.Draw(bg)

for y in range(0, 630, 3):
    alpha = y / 630
    draw.rectangle((0, y, 1200, y + 3), fill=(20 + int(alpha * 35), 24 + int(alpha * 25), 38 + int(alpha * 30)))

for x0, y0, x1, y1, color in [
    (950, 80, 1180, 260, (245, 132, 68)),
    (870, 360, 1100, 560, (247, 178, 103)),
    (1000, 500, 1170, 620, (255, 255, 255)),
]:
    draw.rectangle((x0, y0, x1, y1), fill=color)

portrait = Image.open(portrait_path).convert("RGBA")
portrait = portrait.resize((380, 430))
mask = Image.new("L", portrait.size, 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse((0, 0, portrait.size[0] - 1, portrait.size[1] - 1), fill=255)
portrait = Image.composite(portrait, Image.new("RGBA", portrait.size, (0, 0, 0, 0)), mask)

bg.paste(portrait, (80, 100), portrait)

try:
    title_font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 58)
    sub_font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 29)
    small_font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
except Exception:
    title_font = ImageFont.load_default()
    sub_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

bg_draw = ImageDraw.Draw(bg)
bg_draw.rounded_rectangle((520, 180, 1030, 350), radius=24, fill=(17, 24, 39))
bg_draw.text((540, 210), "Aanu Okusanya", font=title_font, fill="white")
bg_draw.text((540, 280), "Frontend Developer & UI Designer", font=sub_font, fill="#F7B267")
bg_draw.text((540, 330), "Building clean, responsive digital experiences.", font=small_font, fill=(221, 231, 255))
bg_draw.ellipse((540, 395, 575, 430), fill="#F7B267")
bg_draw.text((590, 390), "Available for freelance work", font=small_font, fill=(229, 231, 235))

bg.save(out_path, quality=95)
print(out_path)
print(bg.size)
