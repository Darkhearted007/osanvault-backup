from pathlib import Path
from datetime import datetime, timezone
import json

# Resolve all paths from the repository root rather than the process working directory.
ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "site"
DATA_DIR = ROOT / "data"
TEMPLATES_DIR = ROOT / "templates"

SITE_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------
# Load NET token data
# ------------------------------
with (DATA_DIR / "net-data.json").open(encoding="utf-8") as f:
    net = json.load(f)

# ------------------------------
# Load properties data
# ------------------------------
with (DATA_DIR / "properties.json").open(encoding="utf-8") as f:
    props = json.load(f)

# ------------------------------
# Generate index.html
# ------------------------------
with (TEMPLATES_DIR / "index-template.html").open(encoding="utf-8") as f:
    index_template = f.read()

index_html = index_template.replace(
    "{{TIMESTAMP}}",
    datetime.now(timezone.utc).strftime("%B %d, %Y %H:%M UTC"),
)
for key in ["total_investors", "total_tokenized_properties", "last_property_added"]:
    index_html = index_html.replace(f"{{{{{key}}}}}", str(net.get(key, "N/A")))

(SITE_DIR / "index.html").write_text(index_html, encoding="utf-8")

# ------------------------------
# Generate net.html
# ------------------------------
with (TEMPLATES_DIR / "net-template.html").open(encoding="utf-8") as f:
    net_template = f.read()

for key, value in net.items():
    net_template = net_template.replace(f"{{{{{key}}}}}", str(value))

(SITE_DIR / "net.html").write_text(net_template, encoding="utf-8")

# ------------------------------
# Generate properties.html
# ------------------------------
with (TEMPLATES_DIR / "properties-template.html").open(encoding="utf-8") as f:
    prop_template = f.read()

prop_html = ""
snippet = """<div class=\"property\">\n<img src=\"assets/images/{image}\" alt=\"{name}\">\n<h2>{name}</h2>\n<p>Location: {location}</p>\n<p>Price: {price}</p>\n<p>Tokenized: {tokenized}</p>\n</div>"""

for p in props:
    prop_html += snippet.format(**p)

prop_template = prop_template.replace("{{PROPERTIES_LIST}}", prop_html)
(SITE_DIR / "properties.html").write_text(prop_template, encoding="utf-8")

# ------------------------------
# Copy static pages
# ------------------------------
for page in ["about.html", "roadmap.html", "tokenomics.html", "contact.html", "styles.css"]:
    src = ROOT / page
    if src.exists():
        (SITE_DIR / src.name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
