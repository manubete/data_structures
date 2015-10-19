require_relative "l_list"

# linear structure represented by a physical stack, implements
#  push(insert item into a stack), pop (delete an item from the stack), peek

class Stack_a
  def initialize(size)
    @stack_a = Array.new(size)
    @top = 0
  end

  def empty?
    return @stack_a[0] == nil
  end

  def push(item)
    if (self.empty?)
       @stack_a[@top] = item
    else
      puts item
      @top >= @stack_a.length ? @stack_a.push(item): @stack_a[@top + 1] = item
      @top += 1
    end

    puts " after push #{@stack_a.to_s}"
    return nil
  end

  def pop
    return "ERROR" if self.empty?

    element_to_pop = @stack_a[@top]
    @stack_a[@top] = nil
    @top -= 1

    puts " after pop #{@stack_a.to_s}"
    return element_to_pop
  end

  def peek
    # return @stack_a.last
    return @stack_a[@top]
  end
end


# class drivers


nu_stack = Stack_a.new(5)
nu_stack.push("sup")
nu_stack.push("holmes")
nu_stack.push("holmes")
nu_stack.push("holmes")
nu_stack.push("sup")
nu_stack.push("holmes")
puts "pip #{nu_stack.peek()}"
nu_stack.pop()
puts "pip #{nu_stack.peek()}"
