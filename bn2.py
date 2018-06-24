from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Defining the model structure. We can define the network by just passing a list of edges.
model = BayesianModel([('D', 'R'), ('M', 'R'), ('M', 'E'), ('R', 'L')])

# Defining individual CPDs.
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.6, 0.4]])
cpd_m = TabularCPD(variable='M', variable_card=2, values=[[0.7, 0.3]])
cpd_r = TabularCPD(variable='R', variable_card=3, 
                   values=[[0.3, 0.05, 0.9,  0.5],
                           [0.4, 0.25, 0.08, 0.3],
                           [0.3, 0.7,  0.02, 0.2]],
                  evidence=['M', 'D'],
                  evidence_card=[2, 2])

cpd_l = TabularCPD(variable='L', variable_card=2, 
                   values=[[0.1, 0.4, 0.99],
                           [0.9, 0.6, 0.01]],
                   evidence=['R'],
                   evidence_card=[3])

cpd_e = TabularCPD(variable='E', variable_card=2,
                   values=[[0.95, 0.2],
                           [0.05, 0.8]],
                   evidence=['M'],
                   evidence_card=[2])

# Associating the CPDs with the network
model.add_cpds(cpd_d, cpd_m, cpd_r, cpd_l, cpd_e)

# check_model checks for the network structure and CPDs and verifies that the CPDs are correctly 
# defined and sum to 1.
model.check_model()

from pgmpy.inference.ExactInference import VariableElimination
infer = VariableElimination(model)
# Probability of getting strong recommendation letter -> 50.2%
print(infer.query(['L']) ['L'])
# weak musician -> 38.9% 
print(infer.query(['L'], evidence={'M': 0}) ['L'])