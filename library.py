def numberCard(value):
    return ((2 <= ord(value)-48) and (ord(value)-48 <= 6))

def faceCard(value):
    return ((value=='T') or (value=='J') or (value=='Q') or (value=='K') or (value=='A'))