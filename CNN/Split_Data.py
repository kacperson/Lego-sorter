import os

_, dirs, _ = os.walk('Data/train').__next__()
for label in dirs:
    _, _, files = os.walk(f'Data/train/{label}').__next__()
    i = 0
    os.mkdir(f'Data/test/{label}')
    os.mkdir(f'Data/validation/{label}')
    for file in files:
        if i < 3000:
            os.rename(f'Data/train/{label}/{file}', f'Data/test/{label}/{file}')
        elif i < 3250:
            os.rename(f'Data/train/{label}/{file}', f'Data/validation/{label}/{file}')
        else:
            break
        i += 1
