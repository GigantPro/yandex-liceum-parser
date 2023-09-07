BUISNESS_LOGO = """██╗░░░██╗░█████╗░███╗░░██╗██████╗░███████╗██╗░░██╗  ██╗░░░░░██╗░█████╗░███████╗██╗░░░██╗███╗░░░███╗
╚██╗░██╔╝██╔══██╗████╗░██║██╔══██╗██╔════╝╚██╗██╔╝  ██║░░░░░██║██╔══██╗██╔════╝██║░░░██║████╗░████║
░╚████╔╝░███████║██╔██╗██║██║░░██║█████╗░░░╚███╔╝░  ██║░░░░░██║██║░░╚═╝█████╗░░██║░░░██║██╔████╔██║
░░╚██╔╝░░██╔══██║██║╚████║██║░░██║██╔══╝░░░██╔██╗░  ██║░░░░░██║██║░░██╗██╔══╝░░██║░░░██║██║╚██╔╝██║
░░░██║░░░██║░░██║██║░╚███║██████╔╝███████╗██╔╝╚██╗  ███████╗██║╚█████╔╝███████╗╚██████╔╝██║░╚═╝░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝  ╚══════╝╚═╝░╚════╝░╚══════╝░╚═════╝░╚═╝░░░░░╚═╝

██████╗░░█████╗░██████╗░░██████╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
██████╔╝███████║██████╔╝╚█████╗░█████╗░░██████╔╝
██╔═══╝░██╔══██║██╔══██╗░╚═══██╗██╔══╝░░██╔══██╗
██║░░░░░██║░░██║██║░░██║██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝"""


# Colors commands
COLOR_START_COMMAND = '\033['
COLOR_RESET_COMMAND = '\033[0m'

# Text colors
COLOR_RED_CODE = '31m'
COLOR_GREEN_CODE = '32m'
COLOR_YELLOW_CODE = '33m'
COLOR_BLUE_CODE = '34m'

# Background colors
BACKGROUND_COLOR_RED_CODE = '41m'

# Ready text styles
RED_TEXT    = COLOR_START_COMMAND + COLOR_RED_CODE    + '{text}' + COLOR_RESET_COMMAND
GREEN_TEXT  = COLOR_START_COMMAND + COLOR_GREEN_CODE  + '{text}' + COLOR_RESET_COMMAND
YELLOW_TEXT = COLOR_START_COMMAND + COLOR_YELLOW_CODE + '{text}' + COLOR_RESET_COMMAND
BLUE_TEXT   = COLOR_START_COMMAND + COLOR_BLUE_CODE   + '{text}' + COLOR_RESET_COMMAND

# Unicode symbols
UNICODE_CIRCLE_NUMBS = '⓿❶❷❸❹❺❻❼❽❾❿⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴'


EULA_TEXT = RED_TEXT.format(text=f'\n{UNICODE_CIRCLE_NUMBS[1]} The author refuses liability for unforeseen outcome (for example, an account blocking)\n')
EULA_TEXT += RED_TEXT.format(text=f'{UNICODE_CIRCLE_NUMBS[2]} Use this utility only at your own peril and risk!\n')
EULA_TEXT += RED_TEXT.format(text=f'{UNICODE_CIRCLE_NUMBS[3]} The utility was created only in introductory!\n')
