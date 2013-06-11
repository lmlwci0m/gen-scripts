#! /usr/bin/env python3

import re
from functools import partial

DEFAULT_ENCODING = "utf-8"


def pre_repl(self, p, match):
    string = match.group()[2:-1] # Rule: ${var}
    
    print("Found: {0:s}".format(string))
    
    if ":" in string:
        filename = string.split(":")[1] + ".html"
        self.create_page(filename, output=None, parent=p)

    elif string in self:
        return self[string]

    return ""
    

class SimpleTemplate(dict):

    def __get_pattern_matcher(self):
        return re.compile("\$\{(?:f:)?\w+\}")
        
    def __process_template_loop(self, pm, repl, t, dest):
        """Managing read/write cycles."""
        
        line = t.readline()
        while line != '':
        
            subline = pm.sub(repl, line) # Possible recursion here
            
            if (subline != ""):
                
                # Here no recursion, variable value found in dictionary 
                
                dest.write(subline)
                
            line = t.readline()
            
    def __process_template(self, input, pm, p):
        """Template reading and transformation initialization."""
    
        with open(input, "r", encoding=DEFAULT_ENCODING) as t:
            repl = partial(pre_repl, self, p)
            self.__process_template_loop(pm, repl, t, p)
            
    def create_page(self, input="base_template.html", output="test.html", parent=None):
        """Make transformation from input to output.
    
        Using recursion in order to write template transformations.
        
        input: tamplate fila name
        output: output of tree tranformation. Used only on root
        parent: file object reference for no-root nodes
        """
    
        pm = self.__get_pattern_matcher()
    
        if parent == None:
        
            # Start of template tree: new file creation
        
            with open(output, "w", encoding=DEFAULT_ENCODING) as f:
                self.__process_template(input, pm, f)
            
        else:
        
            # Go deep into the tree: use existing open file
        
            self.__process_template(input, pm, parent)
            


if __name__ == '__main__':
    
    e = SimpleTemplate(title="Pippo", body='Pluto', header='Header', par="Auuuuu")
    
    e.create_page(input="base_template.html", output="test.html")
