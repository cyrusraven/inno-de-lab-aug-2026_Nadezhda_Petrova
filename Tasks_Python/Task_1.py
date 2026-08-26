raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "
line = raw_user_record.split(';')  # Splitting the string into separate elements

line = [i.strip() for i in line]  # Removing all spaces from each element

line[0] = f'UID-{line[0]}'  # Attaching the particle 'UID-' to the first element

if '_' in line[1]:
    line[1] = line[1].replace('_', ' ').title()  # Replacing '_' to ' ' in the second element

line[2] = line[2].upper()  # The third element was converted to uppercase
line[3] = line[3].lower()  # The fourth element was converted to lowercase
line = ' | '.join(line)  # Joining the elements in one line
print(line)
