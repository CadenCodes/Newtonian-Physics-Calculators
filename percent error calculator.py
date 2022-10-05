print("Welcome to the Percent Error calculator")
while True:
    so = input("What was the observed value?")
    se = input("What was the expected value?")
    fo = float(so)
    fe = float(se)
    delta = abs((fo -fe)/fe)
    fin = delta * 100
    print(fin," percent")
    restart = input("Run again?")
    if restart in ('y','Y','yes','Yes','YES','YEs','yeS','yEs',' y',' Y',' yes',' Yes',' YES',' YEs',' yeS',' yEs'):
        continue
    else:
        print("Goodbye")
        break