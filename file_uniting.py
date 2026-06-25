import os

path_to_files = os.getcwd()
files_in_dir = os.listdir(path_to_files)
final_file = 'finalfile.txt'
data = dict()
final_file_path = os.path.join(path_to_files, final_file)

with open(final_file_path, 'w') as f:
    f.write('')

for file in files_in_dir:
    if 'txt' in file:
        path_to_file = os.path.join(path_to_files, file)
        with open(path_to_file) as f:
            file_text = f.read().strip()
            if not file_text:
                continue
            data[file] = {'length_of_text':len(file_text), 'file_text': file_text}
    sorted_data = sorted(data, key = lambda k: data[k]['length_of_text'])

print(sorted_data)
print(data)

with open(final_file, 'w') as f:
    for file in sorted_data:
        f.write(f'{file}\n{data[file]['length_of_text']}\n{data[file]['file_text']}\n')