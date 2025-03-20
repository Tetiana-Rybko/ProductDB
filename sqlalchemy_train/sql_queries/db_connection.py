from sqlalchemy.orm import sessionmaker


class DBConnection:
    def __init__(self, engine) -> None:
        self.engine = engine
        self.session_fabric = sessionmaker(
            bind=self.engine
        )

    def __enter__(self):
        self.session = self.session_fabric()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
