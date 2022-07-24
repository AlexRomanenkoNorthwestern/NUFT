import click

# NUFT Command Line Interface
    
# Dictionary of the list of commands available to the user
# Not used by Click CLI 
commands = {
"start" : "Start",
#Starts all websockets, does not return control flow until all websockets are open. 
"stop" : "Stop",
#Stops all websockets, keeps connection open. 
"backtest" : "Start Backtest", 
#Takes in algorithm path, historical/realtime toggle, and start/end date if historical. Executes backtest. Returns control flow during backtest, but will autoprint result.  
"systat" : "System Status",
#Prints system status, operational and non-operational status of all websockets.
"exchstat" : "Algo Status",
#Prints performance of all algorithms.
"query" : "Query memory",
#Given query for backtesting report(s), returns backtesting report(s).
"train" : "Passing Data ML Training"}
#Given ML algorithm path, data query, finds data, trains model, returns control flow during train, but will autoprint result.

# Defines the main command group
@click.group()
def CLI():
    """
    Simple CLI built for Northwestern's FinTech Club
    """
    pass

# Start Command
@CLI.command(help="Starts all websockets, does not return control flow until all websockets are open.")
def start():

    click.echo("Starting Stream")


# Stop Command
@CLI.command(help="Stops all websockets, keeps connection open.")
def stop():

    click.echo("Stopping Stream")


# backtest Command
@CLI.command(help="Takes in algorithm path, historical/realtime toggle, and start/end date if historical. Executes backtest. Returns control flow during backtest, but will autoprint result. ")
def backtest():

    click.echo("Running Backtester")


@CLI.command(help="Prints system status, operational and non-operational status of all websockets.")
def systat():

    click.echo("Displaying System Status")


@CLI.command(help="Prints performance of all algorithms.")
def excstat():

    click.echo("Displaying Exchange Status")


@CLI.command(help="Given query for backtesting report(s), returns backtesting report(s).")
def query():

    click.echo("Querying Data")


@CLI.command(help="Given ML algorithm path, data query, finds data, trains model, returns control flow during train, but will autoprint result.")
def train():

    click.echo("Training Models")

CLI()


