import mesa

class Roomba(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.counter = 0
    
    def step(self):
        if(self.model.isDirty(self.pos)):
            self.clean()
        else :
            self.move()
        self.counter+=1
        pass
    
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, 
            moore = True,
            include_center = False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        self.counter = self.counter + 1
    
    def clean(self):
        if self.model.isDirty(self.pos):
            self.model.clean(self.pos)
        pass

class CleaningModel(mesa.Model):

    def __init__(self, N, width, height, percent):
        self.num_agents = N
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.celdas_lim = int((width*height) * (1-percent)) #Calcula numero de celdas limpias
        self.celdas_suc = (width*height)-self.celdas_lim #Calcula numero de celdas sucias

        for i in range(self.num_agents):
            a = Roomba(i, self)
            self.schedule.add(a)
            x = 1
            y = 1
            self.grid.place_agent(a, (x, y))

        self.dirty_Matrix = []
        for i in range(self.celdas_suc):
            coords = (self.random.randrange(self.grid.width), self.random.randrange(self.grid.height))
            while(coords in self.dirty_Matrix):
                coords = (self.random.randrange(self.grid.width), self.random.randrange(self.grid.height))
            self.dirty_Matrix.append(coords)

    def step(self):
        self.schedule.step()

    def isDirty(self, pos):
        return (pos in self.dirty_Matrix)
    
    def clean(self, pos):
        self.dirty_Matrix.remove(pos)
            