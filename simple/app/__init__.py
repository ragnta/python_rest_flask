from .madcontroller import MadController
from .maddao import MadDao
from .csvreader import Reader


madController = MadController(MadDao(Reader()))