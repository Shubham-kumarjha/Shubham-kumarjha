import sys
import cv2
import numpy as np

def img_to_ascii_svg(image_path, output_svg_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        img = np.zeros((100, 100), dtype=np.uint8)
        cv2.putText(img, "AI DATA", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2)

    width = 90
    height = int(img.shape[0] * (width / img.shape[1]) * 0.5)
    img_resized = cv2.resize(img, (width, height))

    chars = " .`:-=+*cs#%@"
    num_chars = len(chars)

    svg_lines = []
    svg_header = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width * 9} {height * 11}" width="100%" height="auto" style="background-color: #0d1117; border-radius: 8px;">\n'
    svg_header += '<style>\n'
    svg_header += '  .ascii { font-family: "Fira Code", monospace; font-size: 9px; fill: #00ff66; white-space: pre; font-weight: bold; }\n'
    svg_header += '</style>\n'
    svg_lines.append(svg_header)

    for y in range(height):
        line_str = ""
        for x in range(width):
            pixel_val = img_resized[y, x]
            char_idx = int((pixel_val / 255.0) * (num_chars - 1))
            line_str += chars[char_idx]
        
        line_str = line_str.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        svg_lines.append(f'<text x="10" y="{(y + 1) * 11}" class="ascii">{line_str}</text>\n')

    svg_lines.append('</svg>')

    with open(output_svg_path, "w", encoding="utf-8") as f:
        f.writelines(svg_lines)

    print(f"ASCII SVG generated: {output_svg_path}")

if __name__ == "__main__":
    inp = sys.argv[1] if len(sys.argv) > 1 else "prepared_photo.png"
    out = sys.argv[2] if len(sys.argv) > 2 else "ascii-portrait.svg"
    img_to_ascii_svg(inp, out)
