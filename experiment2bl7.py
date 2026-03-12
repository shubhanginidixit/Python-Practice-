def file_reader(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error:", e)


# Your file path
file_path = r"C:\Users\adm\Downloads\archive (1)\student_placement_synthetic.csv"

for line in file_reader(file_path):
    print(line)