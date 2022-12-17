from typing import Dict
from interface import DatabaseInterface

class PostgresRepository(DatabaseInterface):
  def select_one(self) -> Dict:
    return {
      'success': True,
      'data': 'Wello World'
    }
