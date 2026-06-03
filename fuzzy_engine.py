import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def build_system():

    gpa = ctrl.Antecedent(np.arange(0, 4.1, 0.1), 'gpa')
    exp = ctrl.Antecedent(np.arange(0, 11, 1), 'experience')
    proj = ctrl.Antecedent(np.arange(0, 21, 1), 'projects')
    test = ctrl.Antecedent(np.arange(0, 101, 1), 'test_score')
    comm = ctrl.Antecedent(np.arange(0, 101, 1), 'communication')

    score = ctrl.Consequent(np.arange(0, 101, 1), 'suitability')

    # MEMBERSHIP FUNCTIONS
    gpa['low'] = fuzz.trapmf(gpa.universe, [0, 0, 2, 2.5])
    gpa['medium'] = fuzz.trimf(gpa.universe, [2, 3, 3.5])
    gpa['high'] = fuzz.trapmf(gpa.universe, [3, 3.5, 4, 4])

    exp['low'] = fuzz.trimf(exp.universe, [0, 1, 3])
    exp['high'] = fuzz.trimf(exp.universe, [3, 6, 10])

    proj['few'] = fuzz.trimf(proj.universe, [0, 2, 5])
    proj['many'] = fuzz.trimf(proj.universe, [10, 15, 20])

    test['low'] = fuzz.trapmf(test.universe, [0, 0, 40, 60])
    test['high'] = fuzz.trapmf(test.universe, [80, 90, 100, 100])

    comm['weak'] = fuzz.trimf(comm.universe, [0, 0, 40])
    comm['strong'] = fuzz.trimf(comm.universe, [70, 85, 100])

    score['reject'] = fuzz.trimf(score.universe, [0, 0, 40])
    score['good'] = fuzz.trimf(score.universe, [50, 70, 85])
    score['excellent'] = fuzz.trimf(score.universe, [80, 100, 100])

    # RULES
    rules = [

    # EXCELLENT
    ctrl.Rule(gpa['high'] & test['high'] & comm['strong'], score['excellent']),
    ctrl.Rule(exp['high'] & proj['many'], score['excellent']),

    # GOOD
    ctrl.Rule(gpa['medium'] & test['high'], score['good']),
    ctrl.Rule(gpa['high'] & comm['strong'], score['good']),
    ctrl.Rule(exp['high'] & comm['strong'], score['good']),

    # REJECT
    ctrl.Rule(test['low'], score['reject']),
    ctrl.Rule(gpa['low'] & exp['low'], score['reject']),
    ctrl.Rule(comm['weak'], score['reject']),

    # DEFAULT SAFE RULES
    ctrl.Rule(gpa['medium'], score['good']),
    ctrl.Rule(test['high'], score['good']),
]

    system = ctrl.ControlSystem(rules)
    return ctrl.ControlSystemSimulation(system)