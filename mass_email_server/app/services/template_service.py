from jinja2 import Environment, FileSystemLoader, Template
from premailer import transform
from mjml import mjml_to_html

class TemplateService:
    def __init__(self, template_folder: str = 'templates/email_templates'):
        self.env = Environment(loader=FileSystemLoader(template_folder))

    def render(self, template_name: str, context: dict) -> str:
        template: Template = self.env.get_template(template_name)
        return template.render(**context)

    def render_mjml(self, mjml_source: str, context: dict) -> str:
        template = self.env.from_string(mjml_source)
        mjml_rendered = template.render(**context)
        result = mjml_to_html(mjml_rendered)
        return result['html']

    def inline_css(self, html: str) -> str:
        return transform(html)
