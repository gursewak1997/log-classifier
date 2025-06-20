import re

def extract_relevant_log_sections(log: str, max_lines: int = 50) -> str:
    """
    Extracts key error-related sections from a full CI log.
    Looks for common error patterns and grabs a few surrounding lines.
    """
    lines = log.splitlines()
    keywords = ['error', 'failed', 'exception', 'timeout', '❌', 'Traceback']

    extracted = []
    context = 3  # lines before and after match

    for i, line in enumerate(lines):
        if any(k.lower() in line.lower() for k in keywords):
            start = max(i - context, 0)
            end = min(i + context + 1, len(lines))
            extracted.extend(lines[start:end])
            extracted.append("")  # separate blocks

    # Remove duplicates and trim if needed
    seen = set()
    final = []
    for l in extracted:
        if l not in seen:
            seen.add(l)
            final.append(l)
    
    return "\n".join(final[:max_lines]) or "No relevant log sections found."

