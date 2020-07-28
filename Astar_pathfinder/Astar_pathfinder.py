# A* PATHFINDER

import pygame                                                                  # 1. CMD 'pip install pygame'
from queue import PriorityQueue

WIDTH = 800                                                                    # 2. Definir anchura de la ventana
WIN = pygame.display.set_mode((WIDTH, WIDTH))                                  # 3. Definir el display (cuadrado)
pygame.display.set_caption('A* Path Finding Algorithm')

RED = (255, 0, 0)                                                              # 4. Rojo: Nodo ya analizado
GREEN = (0, 255, 0)                                                            #    Verde: Nodo analizable
BLUE = (0, 0, 255)                                                             #    Azul
YELLOW = (255, 255, 0)                                                         #    Amarillo
WHITE = (255, 255, 255)                                                        #    Blanco: Punto todavia no analizado
BLACK = (0, 0, 0)                                                              #    Negro: Barrera, no se puede analizar
PURPLE = (85, 35, 100)                                                         #    Morado: Camino
ORANGE = (255, 128, 0)                                                         #    Naranja: Punto de partida
GREY = (155, 155, 155)                                                         #    Gris
TURQUOISE = (93, 193, 185)                                                     #    Turquesa: Punto final

class Spot:                                                                    # 5. Nodos
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width                                                   # 6. Coordenadas de los nodos
        self.y = col * width
        self.color = WHITE
        self. neighbors = []
        self.width = width
        self.total_rows = total_rows
    
    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):                                                       # 7. Determina si ya se ha analizado el nodo
        return self.color == RED
    
    def is_open(self):                                                         # 8. Determina si puede analizarse el nodo
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):                                                           # 9. Reinicia el display
        self.color = WHITE
    
    def make_start(self):                                                      # 10. Cambia el color de los nodos
        self.color = ORANGE
    
    def make_closed(self):
        self.color = RED
        
    def make_open(self):
        self.color = GREEN
        
    def make_barrier(self):
        self.color = BLACK
        
    def make_end(self):
        self.color = TURQUOISE
        
    def make_path(self):
        self.color = PURPLE
    
    def draw(self, win):                                                       # 11. Dibuja el nodo cuadrado. (0,0) es la esquina superior izquierda
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        
    def update_neighbors(self, grid):
        self.neighbors = []
        
        # Comprobar si la fila actual es menor que el total de filas menos una para añadir una, bajando una fila
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
            
        # Subir
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
            
        # Desplazamiento a la derecha
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
            
        # Desplazamiento a la izquierda
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])
    
    def __lt__(self, other):                                                   # 12. 'lt': "less than". Compara 2 nodos
        return False
    

def h(p1, p2):                                                                 # 13. Funcion heuristica H. Estimacion
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def algorithm(draw, grid, start, end):                                         # 22. 'draw' es una funcion, se puede utilizar como argumento porque se ha definido la funcion lambda
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))                                            # 23. Añade a la priority queue. Los argumentos son la funcion F (F=0), el numero 'count' y el nodo 'start'         
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}             # 24. Almacen de funciones G. Empieza con valor infinito
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())                         # 25. Distancia heuristica. Evita tomar como camino mas corto el nodo consigo mismo
    
    open_set_hash = {start}                                                    # 26. Trackea los items que estan y que no estan en la 'PriorityQueue'
    
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        current = open_set.get()[2]                                            # 27. Solo se desea el nodo de 'open_set', ni la funcion F, ni el 'count'
        open_set_hash.remove(current)
        
        if current == end:                                                     # 28. Crear el camino
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1                                # 29. Un nodo mas para moverse al vecino
             
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
                        
        draw()
        
        if current != start:
            current.make_closed()
            
    return False


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)                                               # 14. En 'grid' fila 'i' creada en 160, añade el objeto 'spot' creado en 164
            
    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)
    
    for row in grid:
        for spot in row:
            spot.draw(win)
    
    draw_grid(win, rows, width)
    pygame.display.update()
    
    
def get_clicked_pos(pos, rows, width):                                         # 15. Identifica la posicion del cursor
    gap = width // rows
    y, x = pos 
    
    row = y // gap
    col = x // gap
    
    return row, col


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)
    
    start = None
    end = None
    
    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False                                                    # 16. Cierra el programa si se pulsa la [X] para salir de la ventana
            
            if pygame.mouse.get_pressed()[0]:                                  # 17. Boton izquierdo
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                
                if not start and spot != end:                                  # 19. Los '!=' impiden que puedan coincidir los nodos de inicio y final
                    start = spot
                    start.make_start()
                
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                
                elif spot != end and spot != start:
                    spot.make_barrier()
            
            elif pygame.mouse.get_pressed()[2]:                                # 18. Boton derecho
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                
                if spot == start:
                    start = None
                
                elif spot == end:
                    end = None
                
            if event.type == pygame.KEYDOWN:                                   # 20. Registra si se pulsa una tecla del teclado
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                                
                    # 21. 'lambda: draw(win, grid, ROWS, width)' es una funcion anonima que llama a otra funcion como argumento
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                        
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
                       
    pygame.quit()
    
    
main(WIN, WIDTH)    
