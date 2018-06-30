from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.sampling import BayesianModelSampling

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

# Forward_sample then iterate and count strong musician/ good letter/both
inference = BayesianModelSampling(model)
numSamples = 10000
samples = inference.forward_sample(size=numSamples, return_type='recarray')

part1 = 0
strongLetter = 0
weakMusician = 0
strongLetterWeakMuscician = 0

# Samples have structure (M E D R L)
for sample in samples:
    # P(m = strong)P(d = low)P(r = ∗ ∗ |m = strong, d = low)P(e = high|m = strong)P(letter = weak| ∗ ∗)
    if sample[0] and not sample[2] and sample[3] == 2 and sample[1] and not sample[4]:
        part1 += 1
    # P(letter = strong)
    if sample[4]:
        strongLetter += 1
    if not sample[0]:
        weakMusician += 1
    # P(m = strong)P(letter = strong)
    if not sample[0] and sample[4]:
        strongLetterWeakMuscician += 1

print("Part 1: ", part1 / numSamples)
print("Strong letter: ", strongLetter / numSamples)
print("Strong letter given weak musician:", strongLetterWeakMuscician / weakMusician)


