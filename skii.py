from textx import metamodel_from_file

class SKIIInterpreter:
    def __init__(self):
        self.variables = {}
        self.lists = {}
        self.dictionaries = {}

    def evaluate(self, expr):
        if isinstance(expr, int):  # Already a raw integer
            return expr
        elif isinstance(expr, str):  # Variable name or string literal
            if expr.startswith('"') and expr.endswith('"'):  # String literal
                return expr[1:-1]  # Remove the quotes
            elif expr.startswith("'") and expr.endswith("'"):  # Single-quoted string literal
                return expr[1:-1]  # Remove the quotes
            elif expr in self.variables:
                return self.variables[expr]
            else:
                raise ValueError(f"Undefined variable: {expr}")
        elif hasattr(expr, "left") and hasattr(expr, "right"):
            # Handle operations
            if expr.__class__.__name__ == "AdditionOperation":  # 'traverse'
                left = self.evaluate(expr.left)
                right = self.evaluate(expr.right)
                return left + right
            elif expr.__class__.__name__ == "SubtractionOperation":  # 'descend'
                left = self.evaluate(expr.left)
                right = self.evaluate(expr.right)
                return left - right
            elif expr.__class__.__name__ == "MultiplicationOperation":  # 'lift'
                left = self.evaluate(expr.left)
                right = self.evaluate(expr.right)
                return left * right
            elif expr.__class__.__name__ == "DivisionOperation":  # 'carve'
                left = self.evaluate(expr.left)
                right = self.evaluate(expr.right)
                return left // right

        raise ValueError(f"Invalid expression: {expr}")

    def execute_command(self, command):
        # execute a single command based on its type.
        if command.__class__.__name__ == "VariableDeclaration":
            self.variables[command.name] = self.evaluate(command.value)
        elif command.__class__.__name__ == "PrintStatement":
            print(self.evaluate(command.expression))
        elif command.__class__.__name__ == "AdditionOperation":
            self.variables[command.left] += self.evaluate(command.right)
        elif command.__class__.__name__ == "SubtractionOperation":
            self.variables[command.left] -= self.evaluate(command.right)
        elif command.__class__.__name__ == "MultiplicationOperation":
            self.variables[command.left] *= self.evaluate(command.right)
        elif command.__class__.__name__ == "DivisionOperation":
            self.variables[command.left] //= self.evaluate(command.right)

    def execute(self, model):
        # execute the entire program by iterating through blocks.
        for block in model.blocks:
            block_type = block.__class__.__name__
            if block_type == "GreenBlock":
                self.execute_green_block(block)
            elif block_type == "BlueBlock":
                self.execute_blue_block(block)
            elif block_type == "BlackDiamondBlock":
                self.execute_black_diamond_block(block)

    def execute_green_block(self, block):
        # execute commands in a green block.
        for stmt in block.commands:
            self.execute_command(stmt)

    def execute_blue_block(self, block):
        #execute commands in a blue block with more complex control structures.
        for stmt in block.commands:
            stmt_type = stmt.__class__.__name__
            
            if stmt_type == "WhileLoop":
                while self.evaluate_condition(stmt.condition):
                    for command in stmt.body:
                        self.execute_command(command)
            
            elif stmt_type == "ForLoop":
                start = self.evaluate(stmt.start)
                end = self.evaluate(stmt.end)
                step = self.evaluate(stmt.step)
                for i in range(start, end, step):
                    self.variables[stmt.name] = i
                    for command in stmt.body:
                        self.execute_command(command)
            
            elif stmt_type == "IfStatement":
                body = stmt.primary_body if self.evaluate_condition(stmt.condition) else stmt.alternative_body
                for command in body:
                    self.execute_command(command)
            
            elif stmt_type == "ListDeclaration":
                self.lists[stmt.name] = [self.evaluate(elem) for elem in stmt.elements]
            
            elif stmt_type == "DictionaryDeclaration":
                self.dictionaries[stmt.name] = {
                    self.evaluate(entry.key): self.evaluate(entry.value)
                    for entry in stmt.entries
                }
            
            else:
                self.execute_command(stmt)#

    def evaluate_condition(self, condition):
        left = self.evaluate(condition.left)
        right = self.evaluate(condition.right)
        op = condition.op
        if op == "->":
            return left < right
        elif op == "<-":
            return left > right
        elif op == "||":
            return left == right
        elif op == "X=":
            return left != right
        elif op == "->>":
            return left <= right
        elif op == "<<-":
            return left >= right
        else:
            raise ValueError(f"Invalid condition operator: {op}")

    def execute_black_diamond_block(self, block):
        # execute commands in a black diamond block.
        for stmt in block.commands:
            stmt_type = stmt.__class__.__name__
            
            if stmt_type == "ClassDefinition":
                self.execute_class_definition(stmt)
            
            elif stmt_type == "RecursiveFunction":
                self.execute_recursive_function(stmt)
            
            elif stmt_type == "ErrorHandling":
                self.execute_error_handling(stmt)
            
            else:
                self.execute_command(stmt)

    def execute_method(self, method):
        # execute a method's body
        for stmt in method.body:
            self.execute_command(stmt)

    def execute_class_definition(self, class_def):
        # execute a class definition
        print(f"Executing class {class_def.name}.")
        methods = {m.name: m for m in class_def.members if hasattr(m, 'name')}
        
        if 'init' in methods:
            print(f"Executing method: init")
            self.execute_method(methods['init'])

    def execute_recursive_function(self, function):
        # execute a recursive function with limit
        def recurse(depth=0):
            if depth > 100:  # prevents stack overflow
                return
            for command in function.body:
                self.execute_command(command)
            recurse(depth + 1)

        recurse()

    def execute_error_handling(self, stmt):
        # execute error handling block.
        try:
            for command in stmt.try_body:
                self.execute_command(command)
        except Exception as e:
            if stmt.exception and stmt.exception in self.variables:
                self.variables[stmt.exception] = str(e)
            for command in stmt.catch_body:
                self.execute_command(command)

# run the interpreter
skii_mm = metamodel_from_file('skii.tx')
#skii_model = skii_mm.model_from_file('green.skii')
#skii_model = skii_mm.model_from_file('while.skii')
skii_model = skii_mm.model_from_file('`program.sk¡¡')
interpreter = SKIIInterpreter()
interpreter.execute(skii_model)
