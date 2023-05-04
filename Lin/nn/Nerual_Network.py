from graphviz import Digraph
# the defination of the neural network
neural_net = Digraph(comment='Neural Network')
neural_net.node('X1')
neural_net.node('X2')
neural_net.node('X3')
neural_net.node('X4')
neural_net.node('H1')
neural_net.node('H2')
neural_net.node('Y')
		
# edge
neural_net.edge('X1', 'H1', label='W1')
neural_net.edge('X1', 'H2', label='W2')
neural_net.edge('X2', 'H1', label='W3')
neural_net.edge('X2', 'H2', label='W4')
neural_net.edge('X3', 'H1', label='W5')
neural_net.edge('X3', 'H2', label='W6')
neural_net.edge('X4', 'H1', label='W7')
neural_net.edge('X4', 'H2', label='W8')
neural_net.edge('H1', 'Y', label='W9')
neural_net.edge('H2', 'Y', label='W10')
# node
neural_net.attr('node', shape='circle', style='filled', color='lightblue2', fontname='Helvetica')
		
# edge
neural_net.attr('edge', fontname='Helvetica')
		
# save as pdf
neural_net.render('neural_net', view=True)

