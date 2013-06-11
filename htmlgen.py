#! /usr/bin/env python3

import re


def get_pattern_matcher():
    return re.compile("\$\{\w+\}")


def create_html5_page(body="Test body", title="Page test title", output="test.html"):
    """Generate base html 5 page.
    
    
    """
    
    with open("base_template.html", "r", encoding="utf-8") as t:
    
        with open(output, "w", encoding="utf-8") as f:
            
            pm = get_pattern_matcher()
            
            line = t.readline()
            while line != '':
            
                #elems = [x[2:-1] for x in pm.findall(line)]
            
                
            
                f.write(pm.sub(repl, line))
            
                #if 'title' in elems:
                #    f.write(line.format(title))
                    
                #elif 'body' in elems:
                #    f.write(line.format(None, body))
                    
                #else:
                #    f.write(line)
                    
                line = t.readline()
                
def repl(match):
    if match.group() == '${title}':
        return "Page test title"
    elif match.group() == '${title2}':
        return "Test body 2"
    elif match.group() == '${body}':
        return "Test body"
        
    return ""


if __name__ == '__main__':
    
    create_html5_page()
    
    #pattern = "\$\{\w+\}"
    #c = re.compile(pattern)
    #elems = []
    #with open("base_template.html", "r", encoding="utf-8") as t:
    #    line = t.readline()
    #    while line != '':
    #        elems += c.findall(line)
    #        line = t.readline()
    #print(elems)