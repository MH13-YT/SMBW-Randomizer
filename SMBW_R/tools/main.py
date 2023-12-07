import contextlib
import os
import shutil
from . import zstandard
from . import byml

module_folder = "SMBW_R/modules"


def get_module_list():
    if not os.path.exists(module_folder):
        return []
    elements = os.listdir(module_folder)

    return [
        element
        for element in elements
        if os.path.isdir(os.path.join(module_folder, element))
        and element != "__pycache__"
        and element != "exemple_module"
    ]


def cleaner(folder):
    if os.path.isdir(folder):
        for root, dirs, files in os.walk(folder, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
            for rep in dirs:
                rep_path = os.path.join(root, rep)
                os.rmdir(rep_path)
        os.rmdir(folder)


def get_resource_metadata(resource):
    if not os.path.isdir(resource["romfs"]):
        return
    files_metadata = []
    for filename in os.listdir(resource["romfs"]):
        romfs_file_path = os.path.join(resource["romfs"], filename)
        worktable_file_path = os.path.join(resource["worktable"], filename)
        output_file_path = os.path.join(resource["output"], filename)
        if os.path.isfile(romfs_file_path):
            file_name, file_extension = os.path.splitext(filename)
            compression_extension = ""
            if file_extension == ".zs":
                compression_extension = ".zs"
                file_name = os.path.splitext(
                    os.path.splitext(os.path.basename(romfs_file_path))[0]
                )[0]
                decompressed_file_name, file_extension = os.path.splitext(
                    worktable_file_path.replace(".zs", "")
                )

            if not compression_extension:
                file_name = os.path.splitext(os.path.basename(romfs_file_path))[0]

            file_metadata = {
                "file_name": file_name,
                "romfs_file_folder": os.path.dirname(romfs_file_path),
                "output_file_folder": os.path.dirname(output_file_path),
                "worktable_file_folder": os.path.dirname(worktable_file_path),
                "compressed": compression_extension != "",
                "compression_metadata": {
                    "compression_extension": compression_extension,
                }
                if compression_extension != ""
                else None,
                "data_file_extension": file_extension,
            }

            files_metadata.append(file_metadata)
    return files_metadata


def get_resource_data(files_metadata):
    files_data = []
    for file_metadata in files_metadata:
        if not os.path.exists(f"{os.curdir}/{file_metadata['worktable_file_folder']}"):
            os.makedirs(
                f"{os.curdir}/{file_metadata['worktable_file_folder']}", exist_ok=True
            )
        if file_metadata["compressed"] == True:
            if file_metadata["compression_metadata"]["compression_extension"] == ".zs":
                zstandard.zstandard_tools.decompress(
                    f"{file_metadata['romfs_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}{file_metadata['compression_metadata']['compression_extension']}",
                    f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}",
                )
        else:
            shutil.copy(
                f"{file_metadata['romfs_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}",
                f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}",
            )
        if file_metadata["data_file_extension"] in [".byml", ".bgyml"]:
            data = byml.byml_tools.dump(
                f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}"
            )
        files_data.append(
            {
                "file_name": file_metadata["file_name"],
                "resource_type": file_metadata["worktable_file_folder"],
                "file_data": data,
            }
        )
    return files_data


def set_resource_data(files_metadata, files_data, modified_files_list, RSTB_DUMP):
    for file_metadata in files_metadata:
        for file_data in files_data:
            if (
                file_data["file_name"] == file_metadata["file_name"]
                and file_data["resource_type"] == file_metadata["worktable_file_folder"]
                and file_metadata["data_file_extension"] in [".byml", ".bgyml"]
            ):
                byml.byml_tools.restore(
                    f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}",
                    file_data["file_data"],
                )
        with contextlib.suppress(Exception):
            for name, RSTB in RSTB_DUMP.items():
                RSTB.delete_entry(
                    os.path.normpath(
                        f"{file_metadata['romfs_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}"
                    )
                    .replace(os.sep, "/")
                    .replace("romfs/", "")
                )
        if (
            f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}"
            in modified_files_list
        ):
            if not os.path.exists(f"{os.curdir}/{file_metadata['output_file_folder']}"):
                os.makedirs(
                    f"{os.curdir}/{file_metadata['output_file_folder']}", exist_ok=True
                )
            if file_metadata["compressed"] == True:
                if (
                    file_metadata["compression_metadata"]["compression_extension"]
                    == ".zs"
                ):
                    zstandard.zstandard_tools.compress(
                        f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}",
                        f"{file_metadata['output_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}{file_metadata['compression_metadata']['compression_extension']}",
                    )
            else:
                shutil.copy(
                    f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}",
                    f"{file_metadata['output_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}",
                )
    return
