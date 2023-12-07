import byml


class byml_tools:
    def dump(file_path):
        with open(file_path, "rb") as byml_file:
            parser = byml.Byml(byml_file.read())
            document = parser.parse()
            return document

    def restore(file_path, data):
        with open(file_path, "wb") as byml_file:
            writer = byml.Writer(data, be=False, version=4)
            writer.write(byml_file)
