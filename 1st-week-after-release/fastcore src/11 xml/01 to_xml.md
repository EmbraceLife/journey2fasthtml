
```python
def to_xml(elm, lvl=0):
    "Convert `ft` element tree into an XML string"
    if elm is None: return ''
    if isinstance(elm, tuple): return '\n'.join(to_xml(o) for o in elm)
    if hasattr(elm, '__ft__'): elm = elm.__ft__()
    sp = ' ' * lvl
    if not isinstance(elm, list): return f'{_escape(elm)}\n'

    tag,cs,attrs = elm
    stag = tag
    if attrs:
        sattrs = (_to_attr(k,v) for k,v in attrs.items())
        stag += ' ' + ' '.join(sattrs)

    isvoid = getattr(elm, 'void_', False)
    cltag = '' if isvoid else f'</{tag}>'
    if not cs: return f'{sp}<{stag}>{cltag}\n'
    if len(cs)==1 and not isinstance(cs[0],(list,tuple)) and not hasattr(cs[0],'__ft__'):
        return f'{sp}<{stag}>{_escape(cs[0])}{cltag}\n'
    res = f'{sp}<{stag}>\n'
    res += ''.join(to_xml(c, lvl=lvl+2) for c in cs)
    if not isvoid: res += f'{sp}{cltag}\n'
    return res
```

---

### purpose
Convert a FastHTML element tree into a well-formatted XML string. XML, or eXtensible Markup Language, is a way of formatting and structuring data using tags. It is similar to HTML but is designed to store and transport data rather than display it.

### inputs
A single element (elm) that could be a FastHTML component, a tuple of components, or a simple text element.
An optional level of indentation (lvl) for formatting nested elements.

### High-Level actions

1. **Start Function Definition**
   - Define the `to_xml` function, which will convert an element tree into an XML string representation.

2. **Handle `None` Input**
   - Check if the element (`elm`) is `None`, and return an empty string if true. This ensures the function doesn't process null elements.

3. **Process Tuples**
   - If the element is a tuple, recursively convert each item within the tuple to an XML string and join them with new lines. This handles multiple elements grouped together.

4. **Convert Custom Objects**
   - Check if the element has a `__ft__` method, which transforms custom objects into a format that can be converted to XML. Call this method to get a compatible representation.

5. **Prepare Indentation**
   - Set up indentation (`sp`) based on the current level (`lvl`) to ensure nested elements are formatted correctly in the output.

6. **Handle Non-List Elements**
   - If the element is not a list, escape and return it as a string. This covers plain text or non-structured data within the element.

7. **Extract Tag, Children, and Attributes**
   - Decompose the list into its `tag`, `children` (`cs`), and `attributes` (`attrs`). These components are essential for constructing the XML representation.

8. **Construct Start Tag with Attributes**
   - Begin forming the start tag (`stag`). If attributes exist, convert them to a string format and append them to the start tag.

9. **Identify Void Elements**
   - Check if the element is a void (self-closing) tag using a `void_` attribute. Set the closing tag (`cltag`) appropriately.

10. **Handle Elements Without Children**
    - If there are no children, return the start tag and closing tag (if needed) with proper indentation. This handles simple elements.

11. **Handle Elements with a Single Simple Child**
    - If there's a single child that isn't a complex structure, escape it and include it between the opening and closing tags. This is for elements containing simple content.

12. **Begin Nested Elements Construction**
    - Start the nested elements by adding a newline and indentation before processing the children. This sets up for recursive processing.

13. **Recursively Process Children**
    - Convert each child element recursively into XML, increasing the indentation level to maintain hierarchical structure.

14. **Close Nested Elements**
    - After processing all children, append the closing tag if the element is not void. This finalizes the nested element structure.

15. **Return Final XML String**
    - Return the complete XML string for the element, ready for rendering or further use.

---

### Large Picture of the `to_xml` Function

The `to_xml` function is designed to take a structured representation of HTML or XML components and transform them into a well-formatted XML string. It recursively handles complex nested structures, attributes, and special void elements to ensure the resulting XML is valid and accurately represents the original structure. This functionality is crucial for rendering HTML/XML in environments like web applications or data exchange formats.

