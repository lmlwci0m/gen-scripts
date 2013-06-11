#! /usr/bin/env python3

import re


class SimpleTemplate(dict):

    def get_pattern_matcher(self):
        return re.compile("\$\{(?:f:)?\w+\}")

    def create_page(self, input="base_template.html", output="test.html", parent=None):
        """Make transformation from input to output.
    
    
        """
    
        pm = self.get_pattern_matcher()
    
        if parent == None:
            with open(output, "w", encoding="utf-8") as f:
                with open(input, "r", encoding="utf-8") as t:
            
                    def repl(match):
                        string = match.group()[2:-1] # Rule: ${var}
                        
                        print("Found: {0:s}".format(string))
                        
                        if ":" in string:
                            filename = string.split(":")[1] + ".html"
                            self.create_page(filename, output=None, parent=f)
        
                        elif string in self:
                            return self[string]
            
                        return ""
            
                    line = t.readline()
                    while line != '':
                        #elems = [x[2:-1] for x in pm.findall(line)]
                        subline = pm.sub(repl, line)
                        if (subline != ""):
                            f.write(subline)
                        line = t.readline()
            
        else:
        
            with open(input, "r", encoding="utf-8") as t:
            
                def repl(match):
                    string = match.group()[2:-1] # Rule: ${var}
                    
                    print("Found: {0:s}".format(string))
                    
                    if ":" in string:
                        filename = string.split(":")[1] + ".html"
                        self.create_page(filename, output=None, parent=parent)
        
                    elif string in self:
                        return self[string]
            
                    return ""
            
                line = t.readline()
                while line != '':
                    #elems = [x[2:-1] for x in pm.findall(line)]
                    subline = pm.sub(repl, line)
                    if (subline != ""):
                        parent.write(subline)
                    line = t.readline()


if __name__ == '__main__':
    
    e = SimpleTemplate(title="Pippo", body='Pluto', header='Header', par="Ti si ma")
    
    e.create_page()
