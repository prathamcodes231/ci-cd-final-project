from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_readme_exists():
    assert (ROOT / "README.md").is_file()


def test_dockerfile_exists():
    assert (ROOT / "Dockerfile").is_file()


def test_index_html_exists():
    assert (ROOT / "index.html").is_file()


def test_index_html_has_project_title():
    content = (ROOT / "index.html").read_text()
    assert "CI/CD Final Project" in content
