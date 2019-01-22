import networkx as nx
import matplotlib.pyplot as plt

ws = nx.watts_strogatz_graph(8,4,0)
wsb = nx.watts_strogatz_graph(8,4,0.5)
wsr = nx.watts_strogatz_graph(8,4,1)

nx.draw_networkx(ws,pos=nx.circular_layout(ws))
plt.show()

wsbig = nx.watts_strogatz_graph(30,6,0)
wsbigsw = nx.watts_strogatz_graph(30,6,0.7)
wsbigrand = nx.watts_strogatz_graph(30,6,1)

nx.draw_networkx(wsbigsw,pos=nx.circular_layout(wsbigsw))
#nx.draw_networkx(wsbigsw,pos=nx.spectral_layout(wsbigsw))
plt.show()

def graph_to_txt(G, filename):
    f = open(filename,'w+')
    for e in G.edges():
        u,v = e
        f.write("\'"+str(u)+"\' \'"+str(v)+"\'\n")
    f.close()
