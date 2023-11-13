import zstandard

class zs_file_manager:
    def compress_zs(input_file_path, output_file_path):
        with open(input_file_path, 'rb') as input_file:
            with open(output_file_path, 'wb') as output_file:
                cctx = zstandard.ZstdCompressor()
                compressor = cctx.stream_writer(output_file)
                while True:
                    chunk = input_file.read(16384)
                    if not chunk:
                        break
                    compressor.write(chunk)
                compressor.flush(zstandard.FLUSH_FRAME)
    def decompress_zs(input_file_path,output_file_path):
        with open(input_file_path, 'rb') as compressed_file:
            with open(output_file_path, 'wb') as decompressed_file:
                dctx = zstandard.ZstdDecompressor()
                decompressor = dctx.stream_reader(compressed_file)
                while True:
                    chunk = decompressor.read(16384)
                    if not chunk:
                        break
                    decompressed_file.write(chunk)