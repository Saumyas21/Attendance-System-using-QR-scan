from MyQR import myqr 
import os 

# create and read
with open('students.txt', 'r') as f:
    lines = f.read().split("\n")
    print(lines)

# specify the folder for saving QR codes
save_dir = os.path.join(os.getcwd(), 'QR_codes')

# create the folder if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for line in lines:
    # Skip empty lines
    if not line.strip():
        continue

    version, level, qr_name = myqr.run(
        line,
        level='H',
        version=1,
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name=f"{line.replace(' ', '_')}.bmp",
        save_dir=save_dir
    )


