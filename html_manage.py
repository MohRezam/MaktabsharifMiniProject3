from pathlib import Path
import re

old_path = "images/"
new_path = "Icons/"

all_html_path = Path.cwd().joinpath("front")

htmls = [html.name for html in all_html_path.glob("*.html")]

for html_file in htmls:
    html_path = f"{all_html_path}/{html_file}"

    html_data = Path(html_path).read_text()

    pattern = re.compile(r'(?<=")' + re.escape(old_path) + r'(?=.*[-]icon[-]?1?)([^"]*)')

    new_html_content = re.sub(pattern, new_path + r'\1', html_data)

    # Path(html_path).write_text(new_html_content)
