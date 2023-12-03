import byml

class byml_tools:
    def dump(file_path):
        with open(file_path, "rb") as fichier_byml:
            parser = byml.Byml(fichier_byml.read())
            document = parser.parse()
            return document

    def restore(file_path,data):
        with open(file_path, 'wb') as fichier:
            writer = byml.Writer(data, be=False, version=4)
            writer.write(fichier)