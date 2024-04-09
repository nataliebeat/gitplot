from .cli import parser

args = parser.parse_args()
print(args.echo)

