import operator
graph = {'Oradea':{'Zerind':71,'Sibiu':151},'Zerind':{'Oradea':71,'Arad':75},'Arad':{'Zerind':75,'Timisoara':118,'Sibiu':140},'Timisoara':{'Arad':118,'Lugoj':111},'Lugoj':{'Timisoara':111,'Mehadia':70},'Mehadia':{'Lugoj':70,'Dobreta':70},'Dobreta':{'Mehadia':75,'Craiova':120},'Craiova':{'Dobreta':120,'Rimnicu Vilcea':146,'Pitesti':138},'Sibiu':{'Arad':140,'Oradea':151,'Rimnicu Vilcea':80,'Fagaras':99},'Rimnicu Vilcea':{'Sibiu':80,'Craiova':146,'Pitesti':97},'Fagaras':{'Sibiu':99,'Bucharest':221},'Pitesti':{'Bucharest':101,'Rimnicu Vilcea':97,'Craiova':138},'Bucharest':{'Fagaras':211,'Pitesti':101,'Giurgiu':90,'Urziceni':85},'Giurgiu':{'Bucharest':90},'Urziceni':{'Bucharest':85,'Hirsova':98,'Vaslui':142},'Hirsova':{'Urziceni':98,'Eforie':86},'Eforie':{'Hirsova':86},'Vaslui':{'Urziceni':142,'Iasi':92},'Iasi':{'Neamt':87,'Vaslui':92},'Neamt':{'Iasi':87}}
hsld = {'Arad':366, 'Bucharest':0, 'Craiova':160, 'Dobreta':242, 'Eforie':161, 'Fagaras':176, 'Giurgiu':77, 'Hirsova':151, 'Iasi':226, 'Lugoj':244, 'Mehadia':241, 'Neamt':234, 'Oradea':380, 'Pitesti':100, 'Rimnicu Vilcea':193, 'Sibiu':253, 'Timisoara':329, 'Urziceni':80, 'Vaslui':199, 'Zerind':374}

start = 'Arad'
destination = 'Bucharest'
gn = {}
fn = {}
vis = []
route = []
shortestDistance = 0


def aStarSearch(start):
    fn[start]=0
    gn[start]=0
    vis.append(start)
    while not fn==[]:
        
        fn2 = (sorted(fn.items(), key=operator.itemgetter(1)))
        print (fn2[0][0],fn2[0][1])
        parent=fn2[0][0]
        route.append(parent)
        if parent==destination:
            shortestDistance=fn2[0][1]
            break
        vis.append(parent)
        fn.__delitem__(parent)
        for item in graph[parent]:
            if item not in vis:
                
                
                fn[item]=graph[parent][item]+hsld[item]+gn[parent]
                gn[item]=graph[parent][item]+gn[parent]
                
            
aStarSearch(start)

#print 'Shortest path : ',route
#print 'Shortest Distance = ',shortestDistance







