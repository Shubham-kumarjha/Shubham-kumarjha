import sys

def generate_info_card_svg(output_path):
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 260" width="100%" height="auto" style="background-color: #0d1117; border-radius: 8px; border: 1px solid #30363d;">
  <style>
    .header { font-family: 'Fira Code', monospace; font-size: 14px; fill: #00ff66; font-weight: bold; }
    .label { font-family: 'Fira Code', monospace; font-size: 12px; fill: #58a6ff; font-weight: bold; }
    .value { font-family: 'Fira Code', monospace; font-size: 12px; fill: #c9d1d9; }
    .accent { font-family: 'Fira Code', monospace; font-size: 12px; fill: #bc8cff; }
  </style>
  
  <!-- Terminal Top Bar -->
  <rect x="0" y="0" width="450" height="30" fill="#161b22" rx="8" />
  <circle cx="18" cy="15" r="5" fill="#ff5f56" />
  <circle cx="34" cy="15" r="5" fill="#ffbd2e" />
  <circle cx="50" cy="15" r="5" fill="#27c93f" />
  <text x="225" y="20" text-anchor="middle" font-family="Fira Code, monospace" font-size="11" fill="#8b949e">shubham@neofetch:~</text>

  <!-- Content -->
  <text x="20" y="55" class="header">shubham@data-ai-engine</text>
  <text x="20" y="70" fill="#30363d">-----------------------------------</text>
  
  <text x="20" y="95" class="label">OS:</text><text x="120" y="95" class="value">Data &amp; AI Stack (Linux/Ubuntu)</text>
  <text x="20" y="120" class="label">Host:</text><text x="120" y="120" class="value">SLIET Punjab (ECE '25)</text>
  <text x="20" y="145" class="label">Kernel:</text><text x="120" y="145" class="value">Python 3.11 / PyTorch / SQL</text>
  <text x="20" y="170" class="label">Uptime:</text><text x="120" y="170" class="value">Building ML Models &amp; Pipelines</text>
  <text x="20" y="195" class="label">Shell:</text><text x="120" y="195" class="accent">zsh (AI/ML Enthusiast)</text>
  <text x="20" y="220" class="label">Portfolio:</text><text x="120" y="220" class="value">shubham-kumarjha.vercel.app</text>
</svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Info Card SVG generated!")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "info-card.svg"
    generate_info_card_svg(out)
