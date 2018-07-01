st = input("Enter data: ")
sub = input("Enter letter to find positions: ")

pos = st.find(sub)
while pos >= 0:
    print(pos, end=' ')
    pos = st.find(sub, pos + 1)
