  parser.add_argument('--boolean_flag',
                      help='This is a boolean flag.',
                      type=eval, 
                      choices=[True, False], 
                      default='True')
