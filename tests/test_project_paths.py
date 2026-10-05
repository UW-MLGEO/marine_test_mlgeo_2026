from marine_test_mlgeo_2026 import project_layout


def test_project_layout_includes_required_directories() -> None:
    assert project_layout() == ("data", "src", "outputs")
