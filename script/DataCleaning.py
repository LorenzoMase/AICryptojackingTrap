import re
def process_file(file_input, file_output):
    date_pattern = re.compile(r'^\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}')
    mid_line_pattern = re.compile(r'(?<!^)(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})')
    special_chars_pattern = re.compile(r'[^a-zA-Z0-9\s/:]')
    prev_line = ""

    with open(file_input, 'r') as f_in:
        with open(file_output, 'w') as f_out:
            for line in f_in:
                if not line.strip():
                    continue
                line = special_chars_pattern.sub('', line)

                if not date_pattern.match(line):
                    prev_line = prev_line.rstrip('\n') + line
                else:
                    if prev_line:
                        f_out.write(prev_line)
                    prev_line = line
                    
                prev_line = mid_line_pattern.sub(r'\n\1', prev_line)
            if prev_line:
                f_out.write(prev_line)

if __name__ == "__main__":    
    file_input = "Path_OfLog"
    file_output = "Path_OfPreprocessedLog"
    process_file(file_input, file_output)
