from app.services.template_service import TemplateService


def test_template_rendering(tmp_path):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    template_file = template_dir / "hello.html"
    template_file.write_text("Hello {{name}}!")
    service = TemplateService(template_folder=str(template_dir))
    result = service.render("hello.html", {"name": "World"})
    assert result == "Hello World!"
