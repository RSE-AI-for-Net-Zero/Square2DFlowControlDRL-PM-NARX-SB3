from click.testing import CliRunner
from Square2DFlowControl.scripts.cli import Square2DFlowControl
import sys

sys.path.append('/home/leeb/Projects/Square2DFlowControlDRL-PM-NARX-SB3/Square2DFlowControl')
sys.path.append('/home/leeb/Projects/Square2DFlowControlDRL-PM-NARX-SB3/Square2DFlowControl/simulation_base')

runner = CliRunner()
runner.invoke(Square2DFlowControl, ['launch-parallel-training', '-n', '1'])
