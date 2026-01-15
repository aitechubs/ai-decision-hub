from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))

def generate_page(context):
    template = env.get_template("decision.md.jinja")
    content = template.render(context)

    filename = context["slug"] + ".md"
    path = f"public/decisions/{filename}"

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
