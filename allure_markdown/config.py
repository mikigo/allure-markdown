import pathlib
class _Config:
    templates_path = pathlib.Path(__file__).parent / "templates"

    title = 'Allure Markdown Report'
    description = "This is a markdown report generated from Allure metadata."
    results_dir = "allure-results"
    output = "allure_markdown_report.md"

config = _Config()
