'''
Base classes for optimisers

'''
from os import error
import numpy as np
from freelunch import darwin
from freelunch.adaptable import adaptable_set


class optimiser:
    '''
    Base class for all optimisers
    '''
    name = 'optimiser'
    tags = []
    hyper_definitions = {}
    hyper_defaults = {}
    can_run_quick = False

    def __init__(self, obj=None, hypers={}, bounds=None):
        '''
        Unlikely to instance the base class but idk what else goes here
        '''
        self.hypers = dict(self.hyper_defaults, **hypers) # Hyperparamters/ methods (dictionary of )
        self.obj = obj # Objective function
        self.bounds = bounds # Bounds / constraints
        self.nfe = 0 # TODO: wrap obj so that these are counted automatically

    def __call__(self, nruns=1, return_m=1, full_output=False):
        '''
        API for running the optimisation
        '''
        if self.obj is None:
            raise NotImplementedError('No optimiser selected')
        if nruns == 1 and return_m == 1 and not full_output and self.can_run_quick:
            return self.run_quick()
        if nruns > 1:
            sols = np.concatenate([self.run() for i in range(nruns)])
        else: 
            sols = self.run()
        sols = sorted(sols, key=lambda x: x.fitness)
        if not full_output:
            return np.array([sol.dna for sol in sols[:return_m]])
        else:
            out = {
                'optimiser':self.name,
                'hypers':self.hypers,
                'bounds':self.bounds,
                'nruns':nruns,
                'nfe':self.nfe,
                'solutions':[sol.dna for sol in sols],
                'scores':[sol.fitness for sol in sols]
            }
            return out

    def __repr__(self):
        return self.name + ' optimisation object'    

    def run(self):
        if self.obj is None:
            raise NotImplementedError('No objective function selected')

    def run_quick(self):
        if self.obj is None:
            raise NotImplementedError('No objective function selected')

    def parse_hyper(self, op):
        if isinstance(op, list): # top 10 recursive gamer moments
            strats = [self.parse_hyper(strat) for strat in op]
            return adaptable_set(strats)
        elif isinstance(op, darwin.genetic_operation):
            return op()
        elif isinstance(op, str):
            try:
                op = getattr(darwin,op)
                return op()
            except AttributeError:
                raise AttributeError # TODO handle this properly


# Subclasses for granularity

class continuous_space_optimiser(optimiser):
    '''
    Base class for continuous space optimisers i.e DE, PSO, SA etc.
    '''

class discrete_space_optimiser(optimiser):
    '''
    Base class for discrete space optimisers i.e GA, GP etc.
    '''

