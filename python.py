def justify_paragraph(paragraph, page_width):
    words = paragraph.split()
    lines = []
    current_line = []

    for word in words:
        if sum(len(w) for w in current_line) + len(current_line) + len(word) <= page_width:
            current_line.append(word)
        else:
            lines.append(current_line)
            current_line = [word]

    if current_line:
        lines.append(current_line)

    left_justified = [" ".join(line) for line in lines]

    right_justified = [" ".join(line).rjust(page_width) for line in lines]

    return left_justified, right_justified

paragraph_input = "This is a sample paragraph that we want to justify based on the given page width. Let's see how the program performs."
page_width_input = 40

left_justified, right_justified = justify_paragraph(paragraph_input, page_width_input)

print("Left Justified:")
print("\n".join(left_justified))
print("\nRight Justified:")
print("\n".join(right_justified))
