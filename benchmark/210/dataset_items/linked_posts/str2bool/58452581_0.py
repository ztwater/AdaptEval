parser.add_argument("mybool", default=True,type=lambda x: bool(int(x)))
myargs=parser.parse_args()
print(myargs.mybool)
