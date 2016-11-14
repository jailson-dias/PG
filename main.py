import _thread as thread

from hermite_bezier import main_hermite
from ui import start

try:
    thread.start_new_thread(main_hermite, ())
    start()
    # Inicio do programa e das threads para rodar o grafico e a curva
    # thread.start_new_thread(start, ())
except KeyboardInterrupt:
    thread.exit()
while 1:
    pass