#! /usr/bin/env python3

import re
from functools import partial

DEFAULT_ENCODING = "utf-8"


def pre_repl(self, p, match):
    string = match.group()[2:-1] # Rule: ${var}
    
    #print("Found: {0:s}".format(string))
    
    if ":" in string:
        filename = string.split(":")[1] + ".html"
        self.create_page(filename, output=None, parent=p)

    elif string in self:
        return self[string]

    return ""
    

class SimpleTemplate(dict):

    pattern_matcher = None
    include_patter_matcher = None

    def __get_pattern_matcher(self):
        if self.pattern_matcher is None:
            self.pattern_matcher = re.compile("\$\{(?:f:)?\w+\}")
        return self.pattern_matcher
        
    def __get_include_pattern_matcher(self):
        if self.include_patter_matcher is None:
            self.include_patter_matcher = re.compile("\$\{f:\w+\}")
        return self.include_patter_matcher
        
    def __process_template_loop(self, pm, repl, t, dest):
        """Managing read/write cycles.
        
        pm: tags pattern
        repl: replacement function 
        t: input template file object
        dest: output file object
        """
        
        ipm = self.__get_include_pattern_matcher()
        do_replace = partial(pm.sub, repl)
        do_write = dest.write
        
        line = t.readline()
        while line != '':
            
            # Check include tag elements
            elems, patts = ipm.split(line), ipm.findall(line)
            
            if len(elems) > 1:
            
                # Include tags found: split and process sequentially
                # due to missing process of file tag's previous sections
            
                for x in range(0, len(elems)):
                    do_write(do_replace(elems[x]))
                    if x < len(elems) - 1:
                        do_write(do_replace(patts[x]))
                        
            else:
            
                # No file tags: process entire line
            
                dest.write(do_replace(line)) # TODO: ERROR ERROR ERROR
            
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
    
    e = SimpleTemplate(
        title="Pippo", 
        body='Pluto', 
        header='Template generator', 
        par="This is a test",
        secpar="This is a second test",
        font="tahoma",
        fontsize="11px"
        )
    
    e.create_page(input="base_template.html", output="test.html")
