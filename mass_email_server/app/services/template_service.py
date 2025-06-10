from jinja2 import Environment, FileSystemLoader, Template

class TemplateService:
    def __init__(self, template_folder: str = 'templates/email_templates'):
        self.env = Environment(loader=FileSystemLoader(template_folder))

    def render(self, template_name: str, context: dict) -> str:
        template: Template = self.env.get_template(template_name)
        return template.render(**context)
