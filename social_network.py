"""Social_Network.py - Social Network Library.

    A social networking library for gamers to manage users, the connections
    between them, and the games they play.

"""
__author__ = 'Fernando Bonetti'
# -------------------------------- #
# Intro to CS Final Project        #
# Gaming Social Network [Option 1] #
# -------------------------------- #
#
# For students who have paid for the full course experience:
# please check submission instructions in the Instructor Note below.
# -----------------------------------------------------------------------------


example_input = "John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

example_input_alternate = """John is connected to Bryant, Debra, Walter. John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner. Bryant is connected to Olive, Ollie, Freda, Mercedes. Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man. Mercedes is connected to Walter, Robin, Bryant. Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures. Olive is connected to John, Ollie. Olive likes to play The Legend of Corgi, Starfleet Commander. Debra is connected to Walter, Levi, Jennie, Robin. Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords. Walter is connected to John, Levi, Bryant. Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man. Levi is connected to Ollie, John, Walter. Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma. Ollie is connected to Mercedes, Freda, Bryant. Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game. Jennie is connected to Levi, John, Freda, Robin. Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms. Robin is connected to Ollie. Robin likes to play Call of Arms, Dwarves and Swords. Freda is connected to Olive, John, Debra. Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."""


def create_data_structure(string_input):
    """Parse string_input and return a network.

    Args:
        string_input: input string to be parsed into network data structure.

    Returns:
        A dictionary mapping UserName keys to Dictionaries of Connections and Games for each user in the string_input.
        For example:

            network={UserName:{'Connections':[],'Games':[]}}

    doctest:
    >>> create_data_structure('Robin is connected to Ollie. Robin likes to play Call of Arms, Dwarves and Swords.')
    {'Robin': {'Connections': ['Ollie'], 'Games': ['Call of Arms', 'Dwarves and Swords']}}

"""

    input_string = [s.strip() for s in string_input.split('.') if s != '']
    # split string into list and filter empty strings
    network = {}
    for line in input_string:
        if ' is connected to ' in line:
            username, connections = line.split(' is connected to ')  # split line into username and connections
            # username = username.strip()  # remove whitespace from username
            if username not in network:
                network[username] = {'Connections': [], 'Games': []}  # add empty dictionaries if user is not in network

            network[username]['Connections'] = [s.strip() for s in connections.split(',')]
            # split connections into list and strip whitespace
        else:
            username, games = line.split(' likes to play ')  # split line into username and games
            # username = username.strip()  # remove whitespace from username
            if username not in network:
                network[username] = {'Connections': [], 'Games': []}  # add empty dictionaries if user is not in network

            network[username]['Games'] = [s.strip() for s in games.split(',')]
            # split games into list and strip whitespace

    return network


def get_connections(network, user):
    """Get connections returns list of all connections user has.

    Args:
        network: Network data structure.
        user: User to return connections for.

    Returns:
        List of all connections user has or empty list if user does not have any connections.
        If user does not exist it returns None

    doctest:
    >>> net = create_data_structure(example_input_alternate)
    >>> get_connections(net , "Debra")
    ['Walter', 'Levi', 'Jennie', 'Robin']
    >>> get_connections(net,"Joe")  # should return None

    """
    if user not in network:
        return None

    return network[user]['Connections']


def add_connection(network, user_a, user_b):
    """Adds User_B as a connection to User_B as long as both exist in network and User_A is not User_B.
       If either User_A or User_B do not exist returns False

    Args:
        network: Network data structure.
        user_a: User to add connection to.
        user_b: User to be added as a connection.

    Returns:
        Network data structure modified to contain desired connection

    doctest:
    >>> net = create_data_structure('Robin is connected to Ollie. Olive is connected to Ollie.')
    >>> add_connection(net,'Robin','Robin')
    {'Olive': {'Connections': ['Ollie'], 'Games': []}, 'Robin': {'Connections': ['Ollie'], 'Games': []}}
    >>> add_connection(net,'Robin','Olive')
    {'Olive': {'Connections': ['Ollie'], 'Games': []}, 'Robin': {'Connections': ['Ollie', 'Olive'], 'Games': []}}
    >>> add_connection(net,'Kyle','Joe')
    False
    """
    if user_b not in network or user_a not in network:  # Check if user_a and user_b are in network
        return False

    if user_a == user_b:  # Don't add connection to self.
        return network
    if user_b not in network[user_a]['Connections']:  # Check if user_b is not already a connection
        network[user_a]['Connections'].append(user_b)

    return network


def add_new_user(network, user, games):
    """Updates and returns network with user and user's games.
       If user does not exits user is created and games added.
       If user exits games are updated instead.

    Args:
        network: Network data structure.
        user: User to add or modify
        games: List of strings to use in Game dictionary for user

    Returns:
        Modified network data structure containing new user or changes to already existing user.

    doctest:
    >>> net = create_data_structure('Robin likes to play Jacks.')
    >>> net = add_new_user(net, "Robin", ['Ninja Pow'])
    >>> add_new_user(net, 'Dave', ['Ninja Hamsters'])
    {'Dave': {'Connections': [], 'Games': ['Ninja Hamsters']}, 'Robin': {'Connections': [], 'Games': ['Ninja Pow']}}
    """
    if user not in network:
        network[user] = {'Connections': [], 'Games': games}

    else:
        network[user]['Games'] = games

    return network


def get_secondary_connections(network, user, unique=True):
    """Return list of users secondary connections

    Args:
        network: Network data structure
        user: User who we get secondary connections for
        unique: Boolean flag to tell whether to remove duplicates from returned list. Defaults to True

    Returns:
        List containing secondary connections for user or an empty list if no secondary connections found.
        If user is not in network it returns None

    doctest:
    >>> net = create_data_structure(example_input_alternate)
    >>> get_secondary_connections(net, 'Robin')
    ['Mercedes', 'Freda', 'Bryant']
    >>> get_secondary_connections(net,'Joe')  # should return None
    """
    if user not in network:
        return None

    secondary_connections = []
    for connection in network[user]['Connections']:  # Loop through users connections
        secondary_connections.extend(network[connection]['Connections'])  # add connections of connections to result

    if unique:
        return list(set(secondary_connections))  # Use set to make each entry unique are return secondary connections

    return secondary_connections


def connections_in_common(network, user_a, user_b):
    """Find and return connections in common with user_a and user_b.

    Args:
        network: Network data structure.
        user_a: first user to compare
        user_b: second user to compare

    Returns:
        An integer with number of connections in common.
        If user_a or user_b is not in network returns False

    doctest:
    >>> net = create_data_structure(example_input)
    >>> connections_in_common(net, "Mercedes", "John")
    2
    >>> connections_in_common(net, "Robin", "John")
    0
    >>> connections_in_common(net, "Joe", "Bob")
    False
    """
    if user_a not in network and user_b not in network:
        return False

    count = 0
    for entry in network[user_a]['Connections']:  # iterate over all connections for user_A
        if entry in network[user_b]['Connections']:  # check if User_A and User_B share a connection
            count += 1  # Increase count by 1 if connection is shared

    return count


def path_to_friend(network, user_a, user_b, path=None):
    """Finds a path through connections between users.
    Shows how users are connected

    Args:
        network: Network data structure.
        user_a: User to start path with.
        user_b: User to end path with.
        path: List with partial path between Users. Defaults to None.

    Returns:
        A list containing the nodes in the  path. Returns None if no path was found or either user is not in network:

    doctest:
    >>> net = create_data_structure(example_input)
    >>> path_to_friend(net, 'John', 'Ollie')
    ['John', 'Bryant', 'Ollie']
    >>> path_to_friend(net, 'John', 'John')
    ['John']
    >>> path_to_friend(net, 'John', 'Joe')     # Return None

    >>> net = add_new_user(net, "Guy", [])
    >>> path_to_friend(net, 'John', 'Guy')     # Return None

    """
    if not path:  # Define path if not defined in passed arguments.
        path = []

    path += [user_a]
    if user_a == user_b:  # if User_A is User_B return
        return path

    if user_b in network[user_a]['Connections']:  # if User_B is a connection return
        return path + [user_b]
    if not user_a in network or not user_b in network:  # return None if User_A or User_B not in network
        return None
    for user in network[user_a]['Connections']:  # Iterate through connections of user
        if user not in path:
            new_path = path_to_friend(network, user, user_b, path)
            if new_path:  # Filter any results that return None
                return new_path

    return None


def suggest_friends(network, user):
    """Suggests Friends for a particular user

    Args:
        network: Network data structure.
        user: String containing user to suggest friends for.

    Returns:
        Returns list of lists containing Username and  number of your connections that have this user as a friend
        Example:
            [[Username,#of mutual friends you share]]
        Returns False if User is not in network
        Returns empty list if it can't a user that is the connection of 2 or more of the user's connections
        that is not already a connection of the user

    doctest:
    >>> net = create_data_structure(example_input)
    >>> suggest_friends(net,'Bryant')
    [['John', 2]]
    >>> suggest_friends(net,'Joe')
    False

    """
    if user not in network:
        return False  # return False if user is not in network

    connections = get_connections(network, user)
    secondary_connections = get_secondary_connections(network, user, False)
    shared = {s: 0 for s in secondary_connections}  # fill dictionary with secondary connections
    for entry in secondary_connections:  # iterate over secondary connections
        count = 0  # initialise count
        for users in secondary_connections:  # iterate over secondary connections
            if users == entry:  # if entry == users update count by 1 for mutual friend
                count += 1

        shared[entry] = count  # store count in dictionary of secondary connections

    # use a list comprehension to return a list of users who are friends of your friends
    # but not your friend along with count of mutual friends
    return [[u, shared[u]] for u in shared if shared[u] > 1 and u not in connections and u != user]


# net = create_data_structure(example_input_alternate)
# print net
# print path_to_friend(net, 'John', 'Ollie')
# print get_connections(net, "Debra")
# print add_new_user(net, "Debra", [])
# print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"])  # True
# print get_connections(net, "Mercedes")
# print add_connection(net, "John", "Freda")
# print get_secondary_connections(net, "Mercedes")
# print connections_in_common(net, "Mercedes", "John")
# print suggest_friends(net, 'Bryant')
