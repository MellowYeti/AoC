def input_feed(file_path):
    with open(file_path) as input:
        for line in input:
            yield line
