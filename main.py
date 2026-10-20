from pyscript import display, document

def addmember(e):
    a = document.getElementById("firstname").value
    b = document.getElementById("lastname").value 
    # retrieves the inputs of the user

    c = str.upper(a)
    d = str.upper(b)

    document.getElementById("output").innerHTML = "" 

    G7 = {'Danielle Sandoval', 'Aaliyah Pangilinan', 'Jilliane Tech', }
    G8 = {'Gavin Taguiga', 'Zeek Fernandez', 'Tyler Sales',}
    G9 = {'Zoey Ledres', 'Imee Mallari', 'Aryana Vargas'}
    G10 = {'Elise Ramos', 'Cas Santos', 'Edgar Gaston',}

    allgrades = G7 | G8 | G9 | G10 
    addedmember = (c + " " + d)
    allgrades.add(addedmember)
    members = "<br>".join(sorted(allgrades))
    numberofmembers = len(allgrades)

    e = f"ALL MEMBERS:<br><br>{members}<br><br>"
    document.getElementById("output").innerHTML = e


    f = f"TOTAL MEMBERS: {numberofmembers}"
    display(f, target = "output")