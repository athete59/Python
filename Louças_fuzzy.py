import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

qtdlouca = ctrl.Antecedent(np.arange(0,11,1), 'qtdlouca')
sujeira = ctrl.Antecedent(np.arange(0,11,1), 'sujeira')

pressao = ctrl.Consequent(np.arange(0,101,1),'pressao')

qtdlouca.automf(number=3, names=['pouca', 'media', 'muita'])
sujeira.automf(number=3, names=['leve', 'moderada', 'pesada'])
pressao.automf(number=3,names=['baixa', 'media', 'alta'])

#Pelo que eu entendi, seria uma boa definir até onde é considerado cada um tbm
#Da parte da quantidade, pra mim até uns 3 é pouco, ai de 4 a 6 é moderado e de 7 a 10 lotou  

qtdlouca['pouca']=fuzzy.trimf(qtdlouca.universe,[0,2,4])
qtdlouca['media']=fuzzy.trimf(qtdlouca.universe,[4,5,6])
qtdlouca['muita']=fuzzy.trimf(qtdlouca.universe,[6,8,10])


sujeira['leve']= fuzzy.trimf(sujeira.universe,[0,2,4])
sujeira['moderada']= fuzzy.trimf(sujeira.universe,[4,6,7] )
sujeira['pesada']=fuzzy.trimf(sujeira.universe,[7,8,10])

pressao['baixa']=fuzzy.trimf(pressao.universe,[0,15,30])
pressao['media']=fuzzy.trimf(pressao.universe,[30,45,60])
pressao['alta']=fuzzy.trimf(pressao.universe,[60,75,100])


#Agora é hora de mostrar o gráfico, vamos la ?
qtdlouca.view()
sujeira.view()
pressao.view()

#Hora de definir as regras, uhull

regra1=ctrl.Rule(qtdlouca['pouca'] & sujeira['leve'], pressao['baixa'])
regra2=ctrl.Rule(qtdlouca['media'] & sujeira['leve'], pressao['media'])
regra3=ctrl.Rule(qtdlouca['muita'] | sujeira['pesada'], pressao['alta'])
regra4=ctrl.Rule(qtdlouca['media'], pressao['media'])

sistema_controle= ctrl.ControlSystem([regra1,regra2,regra3,regra4])
sistema=ctrl.ControlSystemSimulation(sistema_controle)

# E agora é a hora de testar

sistema.input['qtdlouca']=2
sistema.input['sujeira']=10
sistema.compute()

print(sistema.output['pressao'])
pressao.view(sim=sistema)
plt.show()
