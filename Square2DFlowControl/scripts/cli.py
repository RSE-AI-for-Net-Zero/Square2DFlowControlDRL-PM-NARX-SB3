import click
from ..launch_parallel_training import main

@click.group
def Square2DFlowControl():
    pass


'''
    ap.add_argument("-n", "--number-servers", required=True, help="number of servers to spawn", type=int)
    ap.add_argument("-s", "--savedir", required=False,
                    help="Directory into which to save the NN. Defaults to 'saver_data'.", type=str,
                    default='saver_data')

'''
@Square2DFlowControl.command()
@click.option('-n', '--number-servers', 'number_servers',
              required=True,
              help="number of servers to spawn",
              type=int)
@click.option('-s', '--savedir', 'savedir',
              default='saver_data',
              help="Directory into which to save the NN. Defaults to 'saver_data'.",
              type=str)
def launch_parallel_training(number_servers, savedir):
    main(number_servers, savedir)
