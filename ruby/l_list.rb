class Node
  def initialize(data = nil, next_node = nil)
    @next_node = next_node
    @data = data
  end

  def appendToTail(node)
    node_to_append = node
    tail_node = self

    until tail_node.get_next_node == nil
      tail_node = tail_node.get_next_node
    end

    tail_node.set_next_node(node_to_append)
  end

  def get_next_node
    return @next_node
  end

  def set_next_node(new_node)
    @next_node = new_node
  end

  def get_data
    return @data
  end

  def printNodes
    current_node = self

    until current_node == nil
      current_node.get_next_node == nil ? print("Node: #{current_node.get_data} \n") : print("Node: #{current_node.get_data} ->")
      current_node = current_node.get_next_node
    end

  end

end

# das_list = Node.new("sup")
# das_list.printNodes()
#
# yo = Node.new("yo")
# das_list.appendToTail(yo)
#
# das_list.printNodes()
