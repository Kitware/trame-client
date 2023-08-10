class BgColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


COLOR_PALETTE = [
    BgColors.OKBLUE,
    BgColors.WARNING,
    BgColors.OKCYAN,
    BgColors.FAIL,
    BgColors.OKGREEN,
]


def compute_indent(line: str, increment=2) -> str:
    if line.startswith("</"):
        return -increment
    if line.endswith("/>"):
        return 0
    if line.startswith("<"):
        return increment
    return 0


def to_pretty_html(html_content: str) -> str:
    indent_step = 2
    output_lines = []
    indent = 0
    for line in html_content.splitlines():
        delta = compute_indent(line, indent_step)
        if delta < 0:
            indent += compute_indent(line)

        color = COLOR_PALETTE[int(indent / indent_step) % len(COLOR_PALETTE)]

        output_lines.append(
            f"{color}{' '*indent}{line.replace(' >', '>')}{BgColors.ENDC}"
        )
        if delta > 0:
            indent += compute_indent(line)

    return "\n".join(output_lines)
