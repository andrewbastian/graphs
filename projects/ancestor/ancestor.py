
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()


    for pair in ancestors:
    	# add verticies for all the values
    	graph.add_vertex(pair[0])
    	graph.add_vertex(pair[1])
    	# Connect with the edges
    	graph.add_edge(pair[1, pair[0]])

	earliest_ancestor = -1
	max_length = 1
	vertices = graph.vertices

	queue = Queue()
	queue.enqueue([starting_node])

	while queue.size() > 0:
		path = queue.dequeue()
		vertex = path[-1]

		if(len(path) > max_length) or (len(path) is max_length and vertex < earliest_ancestor):
			earliest_ancestor = vertex
			max_length = len(path)
			
		for node in vertices:[vertex]:
			new_path = list(path)
			new_path.append(node)
			queue.enqueue(new_path)

	return earliest_ancestor