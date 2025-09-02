from app.gui.views import BaseView


def open_table(top_view: BaseView) -> None:
    """Открыть окно отображения табеля."""
    from app.gui.views import TableView
    table = TableView(top_view)
    table.run()
