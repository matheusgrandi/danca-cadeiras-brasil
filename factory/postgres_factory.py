from useCases import UseCase
from databases import PostgresRepository

class MyPostgresFactory:
  @staticmethod
  def create() -> UseCase:
    return UseCase(PostgresRepository())