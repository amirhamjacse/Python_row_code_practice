def markdown_to_html(markdown_text):
    html_output = []
    lines = markdown_text.split('\n')

    for line in lines:
        line = line.strip()

        # Headings
        if line.startswith('#'):
            level = len(line.split(' ')[0])
            content = line[level+1:] if len(line) > level else ''
            html_output.append(f"<h{level}>{content.strip()}</h{level}>")
        
        # Unordered list
        elif line.startswith('- '):
            if not html_output or not html_output[-1].startswith("<ul>"):
                html_output.append("<ul>")
            html_output.append(f"<li>{line[2:].strip()}</li>")
        else:
            # Handle end of <ul> block
            if html_output and html_output[-1].startswith("<li>") and not line.startswith("- "):
                html_output.append("</ul>")

            # Bold and Italic replacement
            line = line.replace("**", "<b>").replace("<b>", "</b>", 1)  # first ** is closed by next **
            line = line.replace("*", "<i>").replace("<i>", "</i>", 1)   # similar for *

            # Paragraph
            if line:
                html_output.append(f"<p>{line}</p>")

    # If list was open but not closed
    if html_output and html_output[-1].startswith("<li>"):
        html_output.append("</ul>")

    return '\n'.join(html_output)


# Example usage:
markdown_text = """
# My Title

This is a paragraph with **bold text** and *italic text*.

## Subheading

- Item 1
- Item 2
- Item 3

Another paragraph.
"""

html = markdown_to_html(markdown_text)
print(html)
