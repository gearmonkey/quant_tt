import networkx
from copy import deepcopy

class Board(object):
    def __init__(self):
        self.board = networkx.Graph()
        self.board.add_nodes_from(range(9))
        self.players = ('X','O')
        
    def get_entanglements(self, node):
        return self.board[node].keys()
    
    def get_legal_moves(self):
        return [node_num for node_num in self.board.nodes() if node_num.has_key('label')]
        
    def _get_cycle(self):
        return networkx.cycle_basis(self.board)
        
    def find_observations(self, cycle):
        if not cycle:
            return 
        observations = []
        for i in xrange(len(self.players)):
            observation = deepcopy(self.board)
            for othernode in self.board[node].keys():
                stuff
            observations.append(observation)
        return observations
        
    def move(self, node1, node2, player):
        if self.board[node1].has_key(node2):
            outA = deepcopy(self.board)
            outB = deepcopy(self.board)
             
            outA[node1]['player'] = self.players[player]
            outA[node2]['player'] = self.players[players+1 % len(self.players)]

            outB[node1]['player'] = self.players[players+1 % len(self.players)]
            outB[node2]['player'] = self.players[player]
            return (outA, outB)
            
        if node1 == node2 or not (node1 in self.get_legal_modes() and node2 in self.get_legal_modes()):
            raise ValueError("that was a bad move")
        self.board.add_edge(node1, node2)
        self.board[node1][node2]['player']=player
        return self.find_observations(self._get_cycle())
            
    def set_resolution(self, observation):
        self.board = observation
        #check for victory
