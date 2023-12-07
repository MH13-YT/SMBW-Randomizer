import os
import shutil
import zstandard


class zstandard_tools:
    def get_signature(file_path):
        with open(file_path, "rb") as file:
            magic = file.read(4)
            return magic

    def verify_zs(file_path):
        with open(file_path, "rb") as file:
            magic = file.read(4)
            return magic == b"\xfd\x2f\xb5\x28" or magic == b"\x28\xb5\x2f\xfd"

    def decompress(input_file_path, output_file_path):
        if not zstandard_tools.verify_zs(input_file_path):
            print("Not a ZSTD compressed file.")
            return

        with open(input_file_path, "rb") as compressed_file:
            with open(output_file_path, "wb") as decompressed_file:
                dctx = zstandard.ZstdDecompressor()
                decompressor = dctx.stream_reader(compressed_file)
                shutil.copyfileobj(decompressor, decompressed_file)

    def compress(input_file_path, output_file_path, compression_level=19):
        with open(input_file_path, "rb") as input_file:
            with open(output_file_path, "wb") as output_file:
                cctx = zstandard.ZstdCompressor(level=compression_level)
                output_file.write(cctx.compress(input_file.read()))

        if not zstandard_tools.verify_zs(output_file_path):
            raise ValueError(
                f"Échec de la vérification du fichier compressé : {output_file_path}"
            )
        else:
            return True
