import re
from traceback import format_exc as error_stack

# --------------------- Handling Code

def execute(code, verbose=True):

    """ Takes a string of foxdot code and calls toPython()
`       and exectues the returned python string in our
        global namespace """

    try:

        code = toPython( code, verbose )

        exec code in globals()

    except:
        
        print error_stack()

    return


def toPython( live_code, verbose ):

    """ Converts any FoxDot code to its equivalent in Python """

    # 1. Look for FoxDot syntax for new players

    live_code, new_player_data = new_player( live_code )

    # 2. Convert any "new" players already playing to update methods
    
    live_code = override_attempt( live_code, new_player_data )

    # 3. Convert any references to "self" to the attached player

    live_code = remove_self( live_code )

    # 4. Make sure any integer divisions are converted to floats e.g. 1/2 -> 1/2.0

    live_code = int_div_to_float( live_code )

    if not live_code: return ""

    # 4. Print out the code to the console

    if verbose:

        print stdout( live_code ) 

    # 5. Convert to python code to be executed

    raw_python = compile(live_code, '<string>', 'exec')

    return raw_python


def new_player( code ):
    """ Defining a new instrument / player is done using a double arrow
        >> followed by the name of the SynthDef as if it were a python class
        so that we can look it up and create a new player """

    # Dictionary players[code_str] = variablename, synthdef, init_args, extra methods and data

    players = {}

    # RegEx for instruments constructed using VAR >> INSTRUMENT()

    instruments = re.findall(r'\w+ >> \w+\(', code )

    # RexEx for samples constructed using VAR $ STRING

    samples = re.findall(r'\w+ \$ .*?\n', code )

    assignments = instruments + samples

    for n in range( len( assignments ) ):

        # Find out what kind of player we have

        if ">>" in assignments[n]:
            
            var, op, SynthDef = assignments[n].replace("(","").split()

        elif "$" in assignments[n]:

            SynthDef = "sample_player"

            var, op, pattern  = assignments[n].replace("\n","").split(' ', 2)


        # Find the object arguments and the index of the string at which it ends

        start = code.index(assignments[n]) + len(assignments[n]) - 1

        try:

            end = code.index(assignments[n+1])

        except:

            end = None

        data = code[start:end]
        
        # Loop through the arguments to find the enclosing brackets

        Arguments, index = enclosing_brackets( data )

        # Set the default server manager
        
        Arguments.append("server=server_")

        # See if a scale and metronome has been specified, if not, use global default

        default_scale = True
        default_metro = True

        for arg in Arguments:

            if "scale" in arg:
        
                default_scale = False
                
            if "metro" in arg:

                default_metro = False

        if default_scale:

            Arguments.append("scale=default_scale")

        if default_metro:

            Arguments.append("metro=Clock")

        # Add the sample player pattern

        if SynthDef == "sample_player":

           Arguments.append( "pat=''.join(%s)" % pattern )

        # Check for any information AFTER the init

        Methods = data[index:].rstrip()

        # Check if the player should start at the next loop (!)

        if Methods.endswith('!'):

            Arguments.append( "quantise=False" )

            Methods = Methods[:-1]

        else:

            Arguments.append( "quantise=True" )
           
        # Replace "old" code with new

        old_code = code[code.index(assignments[n]):end]

        if SynthDef == "sample_player":

            new_code = "\n%s = samples_( %s )\n%s" % (var, ",".join(Arguments), Methods)

        else:

            new_code = "\n%s = new_('%s','%s', %s )%s\n" % (var, var, SynthDef, ",".join(Arguments), Methods)

        players[new_code] = (var, SynthDef, Arguments, Methods)

        code = code.replace(old_code, new_code)

    return code, players

# Formatting and cleaning code funcrtions below

def override_attempt(code, new_players):

    """ Finds any attempt to re-assign a player while playing and reformats the arguments """

    ns = globals()

    for string, values in new_players.items(): # TODO any assignments

        name, function = string.split()[0:2]

        try:

            isplaying = ns[name].isplaying

        except:

            continue

        if name in ns and function == '=' and isplaying:

            # Rearrange code so the values are just assigned

            new_code = ""

            # 1a. Get variable name etc

            var, synth, args, methods = values

            # 1b. Check if the first argument is degree or not

            degree_stated = int("=" not in args[0] or "degree=" in args[0])

            if degree_stated:

                new_code += "\n%s.%s=%s" % (var, "degree", args[0].replace("degree=",""))

            #if synth == "sample_player":

            #    new_code += "%s.%s=%s\n" % (var, "pat", args[0])

            # 2. Iterate over the remaining arguments (except clock and servers) and format

            for a in args[degree_stated:]:

                if "metro" not in a or "server" not in a:

                    new_code += "\n%s.%s" % (var, a)

            # 3. Check any extra methods - shows users what their code is REALLY doing

            if methods:

                if methods.startswith("\n"):

                    methods = methods[1:]

                if methods.startswith(var):

                    methods = methods[len(var):]

                new_code += "\n%s%s" % (var, methods.replace("self", var))

            # Replace code and return :)

            code = code.replace( string, new_code )

    return code


def remove_self( code ):

    return code

def float_div(match):
    """ Function used in re.sub to find any integer
        divisions and replaces them so they return floats """
    sub = match.group(0)

    if "." in sub:

        return sub

    else:

        return sub + ".0"

def int_div_to_float( code ):

    return re.sub(r'\d+/\d+\.?', float_div , code)

def enclosing_brackets(string):

    open_b = 0
    
    for i in range(len(string)):
        if string[i] == "(" :
            open_b += 1
        if string[i] == ")" :
            open_b -= 1
        if open_b == 0:
            break

    bracketed_string = string[1:i]

    close = i + 1

    open_b = 0
    last_index = 0
    arguments = []

    # Separate on commas not inside brackets

    for i in range(len(bracketed_string)):

        if bracketed_string[i] in ["(","[","{"]:
            open_b += 1
        if bracketed_string[i] in [")","]","}"]:
            open_b -= 1

        # if we find a comma when we aren't in any brackets, split

        if (bracketed_string[i] == "," and open_b == 0):

            arguments.append( bracketed_string[last_index:i].strip() )

            last_index = i + 1

        elif i == len(bracketed_string) - 1:

            arguments.append( bracketed_string[last_index:i+1].strip() )

            last_index = i + 1
            
    return arguments, close


# Imitates the Python IDE output style

def stdout(code):

    console_text = code.strip().split("\n")

    return ">>> %s" % "\n>>> ".join(console_text)
