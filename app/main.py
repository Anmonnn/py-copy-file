def copy_file(command: str) -> None:
    comm = command.split(" ")

    if len(comm) < 3 or comm[0] != "cp" or comm[1] == comm[2]:
        return

    try:
        with open(comm[1], "r") as file_in, open(comm[2], "w") as file_out:
            for line in file_in:
                file_out.write(line)
    except Exception:
        return
