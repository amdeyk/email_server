from app.services.template_service import TemplateService


def test_template_rendering(tmp_path):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    template_file = template_dir / "hello.html"
    template_file.write_text("Hello {{name}}!")
    service = TemplateService(template_folder=str(template_dir))
    result = service.render("hello.html", {"name": "World"})
    assert result == "Hello World!"


def test_render_mjml(tmp_path):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    service = TemplateService(template_folder=str(template_dir))
    mjml_source = "<mjml><mj-body><mj-section><mj-column><mj-text>Hello {{name}}!</mj-text></mj-column></mj-section></mj-body></mjml>"
    html = service.render_mjml(mjml_source, {"name": "Alice"})
    assert "Hello Alice!" in html


def test_inline_css():
    service = TemplateService()
    html = "<style>h1{color:red;}</style><h1>Hello</h1>"
    inlined = service.inline_css(html)
    assert "style=\"color:red" in inlined
